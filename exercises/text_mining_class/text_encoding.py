
def list_text_files(folder):
    """List text files in folder.

    Return a list of pathlib.Path object for each file in folder. Only return
    paths of files that ends in '.txt' and sort the results by alphatebical
    order to produce a deterministic outcome.
    """
    # Hints:
    # - Add `from pathlib import Path` at the top of this source file.
    # - `folder_path = Path(folder)` converts a name to a pathlib.Path object
    # - `folder_path.glob('*.ext')` can find all files that end in '.ext'
    # - Python lists have `.sort()` method to be sorted in-place. You can
    #   alternatively use the `sorted(my_list)` function to create a new list.

    # TODO: replace the following by the answer:
    return []


def count_bytes(filepath):
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
