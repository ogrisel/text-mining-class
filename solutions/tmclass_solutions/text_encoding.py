from pathlib import Path
import unicodedata


def list_text_files(folder):
    """List text files in folder

    Return a list of pathlib.Path object for each file in folder. Only return
    paths of files that ends in '.txt' and sort the results by alphatebical
    order to produce a deterministic outcome.
    """
    return sorted(Path(folder).glob('*.txt'))


def count_bytes(filepath):
    """Count the number of bytes in a file

    To do so: open the file in binary mode, read the content in memory and
    return the length of the resulting bytes string.

    Note that there are more efficient ways to do this but this is just to
    illustrate that you can read the raw bytes of a file in Python and
    therefore compute the file size this way, even for text files.
    """
    with open(filepath, mode='rb') as f:
        return len(f.read())
