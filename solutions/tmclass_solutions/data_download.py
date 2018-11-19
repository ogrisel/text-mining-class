import tarfile
from urllib.request import urlretrieve
from tmclass_solutions import DATA_FOLDER_PATH


WPS_URL = ("https://github.com/ogrisel/text-mining-class/releases/download/"
           "wikipedia_scraping/wikipedia_scraping.tar.xz")

WPL_URL = ("https://github.com/ogrisel/text-mining-class/releases/download/"
           "wikipedia_language/wikipedia_language.parquet")


def download(url, folder_path, verbose=False):
    filepath = folder_path / url.rsplit("/", 1)[1]
    if not filepath.exists():
        if verbose:
            print(f"Downloading {url} to {str(filepath)}...")
        tmp_filepath = folder_path / (filepath.name + ".part")
        urlretrieve(url, tmp_filepath)
        tmp_filepath.rename(filepath)
    else:
        print(f"{str(filepath)} already exists.")
    return filepath


def download_wikipedia_scraping_result(output_folder=DATA_FOLDER_PATH,
                                       verbose=False):
    archive_filepath = download(WPS_URL, output_folder, verbose=verbose)

    scraping_folder = output_folder / "wikipedia_scraping"
    if scraping_folder.exists():
        if verbose:
            print(f"{str(scraping_folder)} already exists.")
        return

    print(f"Extracting {str(archive_filepath)} to {str(output_folder)}...")
    with tarfile.open(archive_filepath) as f:
        f.extractall(output_folder)


def download_wikipedia_language_dataset(output_folder=DATA_FOLDER_PATH,
                                        verbose=False):
    download(WPL_URL, output_folder, verbose=verbose)


if __name__ == "__main__":
    download_wikipedia_scraping_result(verbose=True)
    download_wikipedia_language_dataset(verbose=True)
