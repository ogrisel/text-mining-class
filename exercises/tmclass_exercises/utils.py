import tarfile
from urllib.request import urlretrieve
from pathlib import Path
from tmclass_exercises import DATA_FOLDER_PATH


WPS_URL = ("https://github.com/ogrisel/text-mining-class/releases/download/"
           "wikipedia_scraping/wikipedia_scraping.tar.xz")


def download_wikipedia_scraping_result(output_folder=DATA_FOLDER_PATH):
    scraping_folder = output_folder / "wikipedia_scraping"
    if scraping_folder.exists():
        print(f"{str(scraping_folder)} already exists.")
        return

    archive_filepath = Path(WPS_URL.rsplit("/", 1)[1])
    if not archive_filepath.exists():
        print(f"Downloading {WPS_URL} to {str(archive_filepath)}...")
        urlretrieve(WPS_URL, archive_filepath)

    print(f"Extracting {str(archive_filepath)} to {str(output_folder)}...")
    with tarfile.open(archive_filepath) as tf:
        tf.extractall(output_folder)

    print(f"Deleting {str(archive_filepath)}")
    archive_filepath.unlink()


if __name__ == "__main__":
    download_wikipedia_scraping_result()
