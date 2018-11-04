import json


def load_encoding_metadata(metada_filepath):
    """Helper function to load the metadata of text files

    Parse the content of the metadata.json file to retrieve the name of the
    encoding for each of the text file in the same folder.
    """
    with open(metada_filepath) as f:
        metadata = json.load(f)
    return {entry['filename']: entry['encoding']
            for entry in metadata}
