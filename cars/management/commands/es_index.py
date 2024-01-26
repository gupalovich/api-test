from django.core.management.base import BaseCommand
from elasticsearch_dsl import connections

from cars.documents import CarDocument


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.es_conn = connections.get_connection()
        self.es_documents = [CarDocument]

    def handle(self, *args, **options):
        for Document in self.es_documents:
            self.stdout.write("Index document:", Document.__name__)
            Document.init()
