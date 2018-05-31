def string(text):
    return sum(_numbers(text))

def _numbers(text, delimiter="\n"):
    return [_number(x) for x in text.split(delimiter)]

def _number(text):
    if not text:
        return 0
    return float(text)
