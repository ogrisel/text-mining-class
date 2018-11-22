
def count_bytes(binary_data):
    """Return the length of a string a string of bytes.

    Should raise TypeError if binary_data is not a bytes string.
    """
    if not isinstance(binary_data, bytes):
        raise TypeError("expected bytes, got %s" % type(binary_data))
    return len(binary_data)


def text_in_bytes(text, binary_data, encoding="utf-8"):
    """Return True of the text can be found in the decoded binary data"""
    return text in binary_data.decode(encoding)


def count_bytes_in_file(filepath):
    """Count the number of bytes in a file

    To do so: open the file in read and binary mode, read the content in memory
    and return the length of the resulting bytes string.

    Note that there are more efficient ways to do this but this is just to
    illustrate that you can read the raw bytes of a file in Python and
    therefore compute the file size this way, even for text files.
    """
    with open(filepath, mode='rb') as f:
        binary_content = f.read()
    return len(binary_content)


def text_in_file(text, filepath, encoding="utf-8"):
    """Return True of the text can be found in the content of the file

    To do so: open the file in read and text mode with the right encoding, read
    the content of the file and check whether the `text` sequence is a
    sub-sequence of the text content of the file.
    """
    with open(filepath, mode="r", encoding=encoding) as f:
        text_content = f.read()
    return text in text_content


def convert_text_file(source_filepath, source_encoding, target_filepath,
                      target_encoding='utf-8'):
    """Copy the text content of a file to a specified target encoding

    To do so:
        - open the source file in read, text mode using the source encoding;
        - read the text content;
        - open the target file in write, text mode using the target encoding;
        - write the text content.
    """
    with open(source_filepath, mode="r", encoding=source_encoding) as f:
        text_content = f.read()
    with open(target_filepath, mode="w", encoding=target_encoding) as f:
        f.write(text_content)
