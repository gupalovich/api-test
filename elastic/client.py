from elasticsearch_dsl.connections import connections


def setup_elasticsearch_connection(settings: dict, verbose: bool = True):
    connections.configure(**settings)
    if verbose:
        print(connections.get_connection().info())
    return connections.get_connection()
