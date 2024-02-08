class ElasticsearchDslError(Exception):
    pass


class VariableLookupError(ElasticsearchDslError):
    pass


class RedeclaredFieldError(ElasticsearchDslError):
    pass


class ModelFieldNotMappedError(ElasticsearchDslError):
    pass
