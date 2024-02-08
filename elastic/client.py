from elasticsearch import Elasticsearch

client = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", "WoqiRk7*wzJFICpWmpBC"),
    # ca_certs="http_ca.crt",
    verify_certs=False,
    ssl_show_warn=False,
)
print(client.info())
