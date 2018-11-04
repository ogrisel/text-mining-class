from pathlib import Path


def list_text_files(folder):
    """List text files in folder.

    Return a list of pathlib.Path object for each file in folder. Only return
    paths of files that ends in '.txt' and sort the results by alphatebical
    order to produce a deterministic outcome.
    """
    return sorted(Path(folder).glob('*.txt'))
