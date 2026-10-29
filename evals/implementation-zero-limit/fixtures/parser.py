def parse_limit(value):
    result = int(value) if value else 20
    if result < 0:
        raise ValueError("negative limit")
    return result
