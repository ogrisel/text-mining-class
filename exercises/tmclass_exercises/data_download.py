import tarfile
from urllib.request import urlretrieve
from tmclass_exercises import DATA_FOLDER_PATH


WPS_URL = ("https://github.com/ogrisel/text-mining-class/releases/download/"
           "wikipedia_scraping/wikipedia_scraping.tar.xz")

WPL_URL = ("https://github.com/ogrisel/text-mining-class/releases/download/"
           "wikipedia_language/wikipedia_language.parquet")


def download_wikipedia_scraping_result(output_folder=DATA_FOLDER_PATH):
    archive_filepath = output_folder / WPS_URL.rsplit("/", 1)[1]
    if not archive_filepath.exists():
        print(f"Downloading {WPS_URL} to {str(archive_filepath)}...")
        urlretrieve(WPS_URL, archive_filepath)

    scraping_folder = output_folder / "wikipedia_scraping"
    if scraping_folder.exists():
        print(f"{str(scraping_folder)} already exists.")
        return

    print(f"Extracting {str(archive_filepath)} to {str(output_folder)}...")
    with tarfile.open(archive_filepath) as tf:
        tf.extractall(output_folder)


def download_wikipedia_language_dataset(output_folder=DATA_FOLDER_PATH):
    dataset_path = output_folder / "wikipedia_language.parquet"
    if dataset_path.exists():
        print(f"{str(dataset_path)} already exists.")
        return

    print(f"Downloading {WPL_URL} to {str(dataset_path)}...")
    urlretrieve(WPL_URL, dataset_path)
    print("done.")


if __name__ == "__main__":
    download_wikipedia_scraping_result()
    download_wikipedia_language_dataset()
