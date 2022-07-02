from collections import defaultdict


def filter_or_not(model_list, query, *field_names):
    if query:
        args = {name: query for name in field_names}
        return model_list.filter(**args)
    else:
        return model_list
