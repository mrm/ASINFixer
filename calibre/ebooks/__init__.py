def normalize(x):
    if isinstance(x, unicode):
        import unicodedata
        x = unicodedata.normalize('NFC', x)
    return x