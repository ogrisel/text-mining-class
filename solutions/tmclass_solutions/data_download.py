import tarfile
from urllib.request import urlretrieve
from tmclass_solutions import DATA_FOLDER_PATH
from tmclass_solutions import MODEL_FOLDER_PATH


WPS_URL = ("https://github.com/ogrisel/text-mining-class/releases/download/"
           "wikipedia_scraping/wikipedia_scraping.tar.xz")

WPL_URL = ("https://github.com/ogrisel/text-mining-class/releases/download/"
           "wikipedia_language/wikipedia_language.parquet")

LC_URL = ("https://github.com/ogrisel/text-mining-class/releases/download/"
          "language_classifier/language_classifier.pkl.gz")


def download(url, folder_path, verbose=False):
    filepath = folder_path / url.rsplit("/", 1)[1]
    if not filepath.exists():
        if verbose:
            print(f"Downloading {url} to {filepath}...")
        tmp_filepath = folder_path / (filepath.name + ".part")
        urlretrieve(url, tmp_filepath)
        tmp_filepath.rename(filepath)
    else:
        print(f"{filepath} already exists.")
    return filepath


def download_wikipedia_scraping_result(output_folder=DATA_FOLDER_PATH,
                                       verbose=False):
    archive_filepath = download(WPS_URL, output_folder, verbose=verbose)

    scraping_folder = output_folder / "wikipedia_scraping"
    if scraping_folder.exists():
        if verbose:
            print(f"{scraping_folder} already exists.")
        return

    print(f"Extracting {archive_filepath} to {output_folder}...")
    with tarfile.open(archive_filepath) as f:
        f.extractall(output_folder)

    return output_folder


def download_wikipedia_language_dataset(output_folder=DATA_FOLDER_PATH,
                                        verbose=False):
    return download(WPL_URL, output_folder, verbose=verbose)


def download_language_classifier(output_folder=MODEL_FOLDER_PATH,
                                 verbose=False):
    return download(LC_URL, output_folder, verbose=verbose)


if __name__ == "__main__":
    download_wikipedia_scraping_result(verbose=True)
    download_wikipedia_language_dataset(verbose=True)
    download_language_classifier(verbose=True)
