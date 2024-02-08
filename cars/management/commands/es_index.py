from django.core.management.base import BaseCommand
from elasticsearch_dsl import Q, Search, connections

from cars.documents import CarDocument
from cars.models import Car


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.es_conn = connections.get_connection()
        self.es_documents = [CarDocument]

    def _index(self):
        for Document in self.es_documents:
            if Document._index.exists():
                self.stdout.write(f"{Document.__name__} already exists")
                continue

            self.stdout.write(f"Index document: {Document.__name__}")
            Document.init()

    def _populate(self):
        qs = Car.objects.select_related("domain", "brand", "model")

        for car in qs:
            self.stdout.write(f"Populate document: {car.id}")
            car_document = CarDocument(
                meta={"id": car.id},
                domain=CarDocument.Domain(name=car.domain.name),
                brand=CarDocument.Brand(name=car.brand.name),
                model=CarDocument.Model(name=car.model.name),
                vin=car.vin,
                color=car.color,
                transmission=car.transmission,
            )
            car_document.save()

    def _delete(self, ids_to_delete: list):
        for Document in self.es_documents:
            search = Search(index=Document._index._name)
            query = Q("terms", _id=ids_to_delete)
            search = search.query(query)

            response = search.delete()
            self.stdout.write(f"Deleted {response['deleted']} documents from {Document._index._name}")

    def handle(self, *args, **options):
        self._index()
        self._populate()

        # Example: Delete documents with IDs 1 and 2
        # ids_to_delete = [1, 2]
        # self._delete(ids_to_delete)
