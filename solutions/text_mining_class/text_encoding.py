from pathlib import Path


def list_text_files(folder):
    """List text files in folder.

    Return a list of pathlib.Path object for each file in folder. Only return
    paths of files that ends in '.txt' and sort the results by alphatebical
    order to produce a deterministic outcome.
    """
    # Hints:
    # - `folder_path = Path(folder)` converts a name to a pathlib.Path object
    # - `folder_path.glob('*.ext')` can find all files that end in '.ext'
    # - Python lists have `.sort()` method to be sorted in-place. You can
    #   alternatively use the `sorted(my_list)` function to create a new list.
    return sorted(Path(folder).glob('*.txt'))
