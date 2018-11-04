import unicodedata


def code_points(text, normalize=None):
    """Return the sequence of unicode code points as intergers

    If normalize is not None, first apply one of the unicode normalization
    schemes: NFC, NFD, NFKC, NFKD.

    https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize
    """

    if normalize is not None:
        text = unicodedata.normalize(normalize, text)
    return [ord(c) for c in text]


def remove_accents(text):
    text = unicodedata.normalize('NFKD', text)
    return ''.join([c for c in text if not unicodedata.combining(c)])


def tokenize_western_language(text):
    return ""


def tokenize_japanese(text):
    return ""
