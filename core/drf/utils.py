def serialize_choice_field(choices: list[tuple[str, str]]) -> list[dict]:
    """
    TODO: test
    """
    try:
        return [{"id": str(item.value), "name": item.label} for item in choices]
    except (AttributeError, ValueError):
        return [{"id": str(value), "name": label} for value, label in choices.items()]
