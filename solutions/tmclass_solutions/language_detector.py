"""Tools to train a language classification model

This modules contains functions to extract multi-lingual text documents from
Wikipedia articles to be able to train a machine learning model to classify the
language of a piece of text.

"""
from tmclass_solutions.scraping import WikipediaArticle
from tmclass_colutions.scraping import WebScaper


BASE_URL_EN = "https://en.wikipedia.org/wiki/"


def scrape_wikipedia_texts(output_folder_path, english_seed_articles,
                           follow_lang_links=False):
    english_folder = output_folder_path / "en"
    if not english_folder.exists():
        english_folder.mkdir()

    to_scrape = []
    scraper = WebScaper()
    for article_name in english_seed_articles:
        article_path = english_folder / article_name
        if article_name.exists():
            raw_content = article_path.read_bytes()
        else:
            article_url = BASE_URL_EN + article_name
            if scraper.can_fetch(article_url):
                headers, raw_content = scraper.fetch(article_url)
                # TODO: we could check the headers to check that it's UTF-8
                # and if not decode and re-encode the HTML payload in UTF-8.
                article_path.write_bytes(raw_content)

        article = WikipediaArticle(raw_content, encoding="utf-8")
        for language, new_article_url in article.get_language_links().items():
            to_scrape.append(new_article_url)

    # TODO: scrape the collected urls
