def string(text):
    if not text:
        return 0
    if float(text) < 0:
        raise ValueError("negative")
    return float(text)
