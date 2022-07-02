def get_or_default(data, field_name: str, default=None):
    if field_name in data:
        return data[field_name]
    else:
        return default
