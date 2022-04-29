import re


def human_key(key):
    if not isinstance(key, str):
        key = key.__str__()
    parts = re.split("(\d*\.\d+|\d+)", key)
    return tuple(
        (e.swapcase() if i % 2 == 0 else float(e)) for i, e in enumerate(parts)
    )
