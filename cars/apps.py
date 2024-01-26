from django.apps import AppConfig
from django.conf import settings
from elasticsearch_dsl.connections import connections


class CarsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "cars"

    def ready(self) -> None:
        # self.module.autodiscover()
        connections.configure(**settings.ELASTICSEARCH_DSL)

        print(connections.get_connection())
