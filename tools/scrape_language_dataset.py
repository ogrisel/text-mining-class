from pathlib import Path
from urllib.parse import urlparse

from tmclass_solutions.scraping import SimpleWebScraper
from tmclass_solutions.scraping import WikipediaArticle


EN_BASE_URL = "https://en.wikipedia.org/wiki/"
english_articles = [
    "Agriculture", "Architecture", "Art", "Biology", "Business",
    "Cinematography", "Culture", "Economy", "Literature", "Music",
    "Politics", "Religion", "Sport", "Science", "Technology", "Trade"
]

# Most represented languages for those seed articles in text size
# (number of unicode symbols):
hostnames = [
    "fr.wikipedia.org",
    "en.wikipedia.org",
    "ar.wikipedia.org",
    "ru.wikipedia.org",
    "uk.wikipedia.org",
    "fa.wikipedia.org",
    "ca.wikipedia.org",
    "sr.wikipedia.org",
    "es.wikipedia.org",
    "zh.wikipedia.org",
    "it.wikipedia.org",
    "de.wikipedia.org",
    "gl.wikipedia.org",
    "pt.wikipedia.org",
    "vi.wikipedia.org",
    "ta.wikipedia.org",
    "ja.wikipedia.org",
    "bg.wikipedia.org",
    "kn.wikipedia.org",
    "azb.wikipedia.or",
    "id.wikipedia.org",
    "el.wikipedia.org",
    "eo.wikipedia.org",
    "hy.wikipedia.org",
    "hi.wikipedia.org",
    "sv.wikipedia.org",
    "he.wikipedia.org",
    "tr.wikipedia.org",
    "th.wikipedia.org",
    "bn.wikipedia.org",
]

output_folder = Path("/tmp/wikipedia_scraping")
output_folder.mkdir(exist_ok=True, parents=True)

scraper = SimpleWebScraper(output_folder)
whitelist = set(hostnames)
for article_name in english_articles:
    article_url = EN_BASE_URL + article_name
    folder = scraper.fetch_and_save(article_url)
    print(f"Fetched {folder}")
    article = WikipediaArticle((folder / "body").read_bytes())
    language_links = article.get_language_links()
    for language_link in language_links:
        if urlparse(language_link).hostname not in whitelist:
            continue
        folder = scraper.fetch_and_save(language_link)
        print(f"Fetched {folder}")
