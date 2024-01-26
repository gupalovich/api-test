from elasticsearch_dsl import (
    Boolean,
    Completion,
    Date,
    Document,
    InnerDoc,
    Keyword,
    Nested,
    Text,
)


class CarDocument(Document):
    class Index:
        name = "car"
