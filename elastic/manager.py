from elasticsearch_dsl import Document as ElasticDocument
from elasticsearch_dsl import Q, Search

from cars.models import Car

from .documents.cars import CarDocument


class ElasticManager:
    documents = [CarDocument]

    @classmethod
    def index(cls, documents: list[ElasticDocument] = None):
        documents = documents or cls.documents

        for Document in documents:
            if Document._index.exists():
                print(f"{Document.__name__} already exists")
                continue

            print(f"Index document: {Document.__name__}")
            Document.init()

    @classmethod
    def populate(cls):
        qs = Car.objects.select_related("domain", "brand", "model")

        for car in qs:
            print(f"Populate document: {car.id}")
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

    @classmethod
    def delete(cls, ids_to_delete: list, documents: list[ElasticDocument] = None):
        documents = documents or cls.documents

        for Document in documents:
            search = Search(index=Document._index._name)
            query = Q("terms", _id=ids_to_delete)
            search = search.query(query)

            response = search.delete()
            print(f"Deleted {response['deleted']} documents from {Document._index._name}")
