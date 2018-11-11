
def count_bytes(binary_data):
    """Return the length of a string a string of bytes.

    Should raise TypeError if binary_data is not a bytes string.
    """
    # Hints:
    # - Use the `len()` to measure the length of a bytes sequence;
    # - Use `isinstance(binary_data, bytes)` to check if `binary_data` is
    #   actually an instance of the `bytes` type;
    # - Use `raise TypeError("some message")` to raise a `TypeError` exception.

    # TODO: replace the following by the answer:
    return 0


def text_in_bytes(text, binary_data, encoding="utf-8"):
    """Return True of the text can be found in the decoded binary data"""
    # Hints:
    # - Use `binary_data.decode(encoding)` to decode the text content of
    #   `binary_data`.
    # - `text_a in text_b` returns `True` if `text_b` contains at least one
    #   occurence of the `text_a` sequence of characters.

    # TODO: replace the following by the answer:
    return False


def count_bytes_in_file(filepath):
    """Count the number of bytes in a file

    To do so: open the file in binary mode, read the content in memory and
    return the length of the resulting bytes string.

    Note that there are more efficient ways to do this but this is just to
    illustrate that you can read the raw bytes of a file in Python and
    therefore compute the file size this way, even for text files.
    """
    # Hints:
    # - Use the `f = open(filepath)` function to open filepath
    # - Call `open` with mode `mode='rb'` for "read" and "binary"
    # - Calling `f.read()` returns the content of the file f
    # - Use the `len()` to measure the lenght of a bytes sequence

    # TODO: replace the following by the answer:
    return 0


def text_in_file(text, filepath, encoding="utf-8"):
    """Return True of the text can be found in the content of the file

    To do so: open the file in read and text mode with the right encoding, read
    the content of the file and check whether the `text` sequence is a
    sub-sequence of the text content of the file.
    """
    # Hints:
    # - Call `open` with mode `mode='r'` for "read" and "text" mode
    # - When calling `open` in text mode, it is required to pass the correct
    #  `encoding` parameter, for instance:
    #      f = open(filepath, mode='r', encoding='utf-8')

    # TODO: replace the following by the answer:
    return False
