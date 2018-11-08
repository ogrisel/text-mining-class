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


def character_categories(text, normalize=None):
    """Return the list of unicode categories for each character in text

    If normalize is not None, apply the specified normalization before
    extracting the categories.
    """
    if normalize is not None:
        text = unicodedata.normalize(normalize, text)
    return [unicodedata.category(c) for c in text]


def remove_accents(text):
    """Replace accentuated characters by their non-accentuated counterparts

    A simple way to do this would be to decompose accentuated characters in the
    sequence using one of the unicode decomposition schemes and then filter the
    resulting sequence to remove combining characters (also known as
    diacritical marks).

    Comments: the following solution is a very naive implementation of that
    only uses basic operations on the sequence of unicode characters.

    A more efficient approach that works only for languages that use the
    latin alphabet would use batch conversion to ASCII characters as done in:

        sklearn.feature_extraction.text.strip_accents_ascii

    """
    text = unicodedata.normalize('NFKD', text)
    return "".join([c for c in text if not unicodedata.combining(c)])


def tokenize_western_language(text):
    r"""Split a text document as a sequence of word-level tokens

    Words are separated by any spacing or punctuation. The resulting sequence
    of tokens is therefore devoid of any punctuation information from the
    original text.

    Comments: the following solution is a very naive (and slow) implementation
    of a western language tokenizer that only uses basic operations on the
    sequence of unicode characters.

    A more efficient way to implement this would be to use the regular
    expression module of Python. For instance look at the source code of the
    following code extracted from scikit-learn:

        tokens = re.compile(r'(?u)\b\w+\b').findall(text)
    """
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
    """Tokenize a string of Japanese text as a sequence of "word" tokens

    Japanese text needs to be segmented using a language aware strategy
    (morphological analysis): it is not possible to use spaces and punctuation
    only to itentify words.
    """
    from janome.tokenizer import Tokenizer
    return Tokenizer().tokenize(text, wakati=True)
