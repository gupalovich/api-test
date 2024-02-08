from elasticsearch_dsl import Document, InnerDoc, Keyword, Nested


class CarDocument(Document):
    class Index:
        name = "car"
        settings = {
            "number_of_shards": 1,
            "number_of_replicas": 0,
        }

    class Domain(InnerDoc):
        name = Keyword()

    class Brand(InnerDoc):
        name = Keyword()

    class Model(InnerDoc):
        name = Keyword()

    domain = Nested(Domain)
    brand = Nested(Brand)
    model = Nested(Model)
    vin = Keyword()
    color = Keyword()
    transmission = Keyword()
