from tmclass_solutions.scraping import WikipediaArticle
from tmclass_solutions.scraping import WebScraper

from tmclass_solutions import DATA_FOLDER_PATH


def test_extract_text_from_html_page():
    culture_path = DATA_FOLDER_PATH / "wikipedia_text" / "en" / "Culture"
    culture_page = WikipediaArticle(culture_path.read_text(encoding="utf-8"))
    main_text = culture_page.get_main_text()
    assert main_text.startswith("Culture")
    assert main_text.endswith(".")

    paragraphs = main_text.split("\n\n")
    assert len(paragraphs) == 35
