def make_filter_config(data: list) -> dict:
    """
    :param data:
    [
        {
            field: brand
            name: Бренд
            type: checkbox
            contains_field: True
            opened: True
            relation: model
            relation_messages: text
            columns: 1
            fields_map_db: brand__name
            fields_id_map_db: brand__id
            placeholders: Все бренды
            postfix: km
            interval: 1
            limit: 5
            limit_button: показать еще
        }
    ]
    :return:
    """
    return {
        "limited": {
            item.get("field"): {
                "count": item.get("limit"),
                "button": item.get("button"),
            }
            for item in data
            if item.get("limit") and item.get("button")
        },
        "names": {item.get("field"): item.get("name") for item in data},
        "placeholders": {item.get("field"): item.get("placeholders") for item in data},
        "opened": [item.get("field") for item in data if item.get("opened")],
        "fields": {item.get("field"): item.get("type") for item in data},
        "contains_field": [item.get("field") for item in data if item.get("contains_field")],
        "relations": {item.get("field"): item.get("relation") for item in data if item.get("relation")},
        "relation_messages": {
            item.get("field"): item.get("relation_messages") for item in data if item.get("relation_messages")
        },
        "columns": {item.get("field"): item.get("columns", 2) for item in data},
        "fields_map_db": {item.get("field"): item.get("fields_map_db", item.get("field")) for item in data},
        "fields_id_map_db": {item.get("field"): item.get("fields_id_map_db", "id") for item in data},
        "sorting_translate": {
            "price": [
                "Сначала дешевле",
                "Сначала дороже",
            ]
        },
        "sorting_group_names": {"price_created": "Сортировать"},
        "sorting_group": {
            "price_created": {
                "price": "Возрастанию цены",
                "-price": "Убыванию цены",
                "-created": "Дата появления (сначала новые)",
                "created": "Дата появления (сначала старые)",
            }
        },
        "range_params": {
            item.get("field"): {"postfix": item.get("postfix"), "interval": item.get("interval")}
            for item in data
            if item.get("type") == "range"
        },
    }
