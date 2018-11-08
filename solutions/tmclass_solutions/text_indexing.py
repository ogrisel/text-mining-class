
def build_index(folder_path):
    """Index all text files in folder and return an in-memory text index

    The return value is a Python dictionary that maps text token to the the
    filenames and line numbers that contains that token.

    The text files can be stored in different encodings, in which case it is
    important to decode with the correct encoding prior to tokenization.

    Futhermore, in addition to text encoding, the language of the document is
    also important to do language-specific normalization (e.g. converting to
    lower case, removing accents) and tokenization.
    """
    # TODO
    return {}
