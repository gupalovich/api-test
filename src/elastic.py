from django.conf import settings

from elastic.client import setup_elasticsearch_connection

# Elastic search connection
elastic_conn = setup_elasticsearch_connection(settings=settings.ELASTICSEARCH_DSL, verbose=True)
