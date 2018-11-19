import json
from urllib.parse import quote
from tmclass_solutions.scraping import SimpleWebScraper
from tmclass_solutions.scraping import WikipediaArticle
from tmclass_solutions.data_download import download_wikipedia_scraping_result

from tmclass_solutions import DATA_FOLDER_PATH as ROOT

EN_WIKIPEDIA_PATH = ROOT / "wikipedia_scraping" / "en.wikipedia.org" / "wiki"


def test_extract_text_from_html_wikipedia_page():
    download_wikipedia_scraping_result()

    culture_path = EN_WIKIPEDIA_PATH / "Culture" / "body"
    culture_page = WikipediaArticle(culture_path.read_text(encoding="utf-8"))
    main_text = culture_page.get_main_text()
    assert main_text.startswith("Culture")
    assert main_text.endswith("tradition of textual theory.")

    paragraphs = main_text.split("\n\n")
    assert len(paragraphs) == 35


def test_extract_language_links_from_html_wikipedia_page():
    download_wikipedia_scraping_result()

    culture_path = EN_WIKIPEDIA_PATH / "Culture" / "body"
    culture_page = WikipediaArticle(culture_path.read_text(encoding="utf-8"))
    language_links = culture_page.get_language_links()
    assert len(language_links) == 171

    expected_link = "https://af.wikipedia.org/wiki/Kultuur"
    assert language_links[0] == expected_link

    expected_link = "https://zh.wikipedia.org/wiki/" + quote("文化")
    assert language_links[-1] == expected_link


def test_robot_file_url():
    scraper = SimpleWebScraper()
    url = "https://en.wikipedia.org/wiki/Tomato"
    assert scraper.get_robot_url(url) == "https://en.wikipedia.org/robots.txt"

    url = "https://scikit-learn.org/stable/documentation.html"
    assert scraper.get_robot_url(url) == "https://scikit-learn.org/robots.txt"


def test_web_scraper_robots_file_handling():
    scraper = SimpleWebScraper()
    assert scraper.can_fetch("https://en.wikipedia.org/wiki/Tomato")
    assert not scraper.can_fetch("https://en.wikipedia.org/api/")
    assert not scraper.can_fetch("https://en.wikipedia.org/wiki/Special:")


def test_web_scraper_fetch():
    scraper = SimpleWebScraper()
    headers, body = scraper.fetch("https://fr.wikipedia.org/wiki/Tomate")
    assert isinstance(headers, dict)
    assert isinstance(body, bytes)
    assert headers['Content-Type'] == "text/html; charset=UTF-8"

    article = WikipediaArticle(body, encoding="utf-8")
    expected_link = "https://en.wikipedia.org/wiki/Tomato"
    assert expected_link in article.get_language_links()

    main_text = article.get_main_text()
    assert main_text.startswith("Solanum lycopersicum\n\nLe plant de tomates")


def test_web_scraper_fetch_and_save(tmpdir):
    scraper = SimpleWebScraper(output_folder=tmpdir)
    result_folder = scraper.fetch_and_save(
        "https://fr.wikipedia.org/wiki/Pomme_de_terre")

    result_folder == tmpdir / "fr.wikipedia.org" / "wiki" / "Pomme_de_terre"
    with open(result_folder / "headers.json") as f:
        headers = json.load(f)
    assert headers['Content-Type'] == "text/html; charset=UTF-8"

    body = (result_folder / "body").read_bytes()
    article = WikipediaArticle(body)
    expected_link = "https://en.wikipedia.org/wiki/Potato"
    assert expected_link in article.get_language_links()
    assert article.get_main_text().startswith(
        "Solanum tuberosum\n\nLa pomme de terre, ou patate[1]")
