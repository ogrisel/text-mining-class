import unicodedata


def code_points(text, normalize=None):
    """Return the sequence of unicode code points as integers

    If normalize is not None, first apply one of the unicode normalization
    schemes: NFC, NFD, NFKC, NFKD.

    More details on normalization schemes in:

    https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize
    """
    # HINTS:
    # - `ord("a")` returns the integer code point of "a"
    # - `list("abc")` returns a list of characters: ["a", "b", "c"]
    # - use `text = unicodedata.normalize("NFC", text)` to normalize some text
    #   using the NFC scheme.

    if normalize is not None:
        text = unicodedata.normalize(normalize, text)
    return[ord(symbol) for symbol in text]


def character_categories(text, normalize=None):
    """Return the list of unicode categories for each character in text

    If normalize is not None, apply the specified normalization before
    extracting the categories.
    """
    if normalize is not None:
        text = unicodedata.normalize(normalize, text)
    return [unicodedata.category(c) for c in text]


def remove_accents(text):
    text = unicodedata.normalize('NFKD', text)
    return "".join([c for c in text if not unicodedata.combining(c)])


def tokenize_generic(text):
    """Split a text document as a sequence of word-level tokens

    Words are separated by any spacing or punctuation. The resulting sequence
    of tokens is therefore devoid of any punctuation information from the
    original text.
    """
    # HINTS:
    # - `unicodedata.category(c)` returns the categoriy of character `c`
    # - The list of categories is available at:
    # http://www.unicode.org/reports/tr44/tr44-6.html#General_Category_Values

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
    if current_token != "":
        collected_tokens.append(current_token)
    return collected_tokens


def tokenize_japanese(text):
    """Tokenize a string of Japanese text as a sequence of "word" tokens

    Japanese text needs to be segmented using a language aware strategy
    (morphological analysis): it is not possible to use spaces and punctuation
    only to itentify words.
    """
    # HINTS:
    # - Use the `janome.tokenizer.Tokenizer` class tokenize the text
    # - Read the online documentation of the janome package to only return
    #   the surface form for each token.

    # TODO: write me!
    return []
