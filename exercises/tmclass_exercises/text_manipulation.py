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
    results = [ord(i) for i in list(text)]
    return results


def character_categories(text, normalize=None):
    """Return the list of unicode categories for each character in text

    If normalize is not None, apply the specified normalization before
    extracting the categories.
    """
    # HINTS:
    # - `unicodedata.category(c)` returns the categoriy of character `c`

    categories = []
    if normalize is not None:
        text = unicodedata.normalize(normalize, text)      
    for i in text:
        categories.append(unicodedata.category(i))

    return categories


def remove_accents(text):
    """Replace accentuated characters by their non-accentuated counterparts

    A simple way to do this would be to decompose accentuated characters in the
    sequence using one of the unicode decomposition schemes and then filter the
    resulting sequence to remove combining characters (also known as
    diacritical marks).
    """
    # HINTS:
    # - Using a decomposition normalization makes it possible to treat accents
    #   as individual characters
    # - `unicodedata.combining(c)` returns whether `c` is a combining character
    #   (in particular accents and other diacritical marks).
    # - It is possible to assemble characters into (unicode) strings using the
    #   `+` operator: `"abc" + "123" == "abc123"`

    norma = unicodedata.normalize('NFD', text)
    if norma == text:
        return text
    else:
        return ''.join([i for i in norma if not unicodedata.combining(i)])


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

    from janome.tokenizer import Tokenizer
    t = Tokenizer()
    return t.tokenize(text, wakati=True)
