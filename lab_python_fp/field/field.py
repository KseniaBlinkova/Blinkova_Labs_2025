def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        key = args[0]
        for item in items:
            if key in item and item[key] is not None:
                yield item[key]
    else:
        for item in items:
            result = {}
            has_valid_fields = False
            for key in args:
                if key in item and item[key] is not None:
                    result[key] = item[key]
                    has_valid_fields = True
            if has_valid_fields:
                yield result
