import unicodedata


def code_points(text, normalize=None):
    """Return the sequence of unicode code points as integers

    If normalize is not None, first apply one of the unicode normalization
    schemes: NFC, NFD, NFKC, NFKD.

    More details on normalization schemes in:

    https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize
    """
    if normalize is not None:
        text = unicodedata.normalize(normalize, text)
    return [ord(c) for c in text]


def remove_accents(text):
    text = unicodedata.normalize('NFKD', text)
    return "".join([c for c in text if not unicodedata.combining(c)])


def tokenize_western_language(text):
    # Note: the following is a very naive implementation of a western language
    # tokenizer that only uses basic operations on the sequence of unicode
    # characters.
    #
    # A more efficient way to implement this would be to use the regular
    # expression module of Python. For instance look at the source code of the
    # following code extracted from scikit-learn:
    #     re.compile(r'(?u)\b\w+\b').findall(text)
    collected_tokens = []
    current_token = ""
    for character in text:
        if unicodedata.category(character)[0] in ('L', 'N'):
            # Append the character (Letter or Number) to the current token:
            current_token += character
        else:
            # This is not a character we are interested in: If the current
            # token is not empty: finalize it and start a new token.
            if current_token != "":
                collected_tokens.append(current_token)
            current_token = ""
    return collected_tokens


def tokenize_japanese(text):
    from janome.tokenizer import Tokenizer
    return Tokenizer().tokenize(text, wakati=True)
