from lxml.html import document_fromstring
from lxml.etree import strip_elements
from urllib.parse import urlparse, unquote
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen, Request
from time import time, sleep
from pathlib import Path
import json


class DisallowedFetchError(Exception):
    pass


class WikipediaArticle:
    """Structured reprenstentation of an Wikipedia page

    Parse the raw HTML content of a wikipedia page to extract:

    - the list of links to pages describing the same content in differnt
      languages

    - the clean text content of all the paragraphs in the main text content
      section of the page.
    """

    def __init__(self, html_content, encoding="utf-8"):
        if isinstance(html_content, bytes):
            html_content = html_content.decode(encoding)
        self.document = document_fromstring(html_content)
        strip_elements(self.document, "style")

    def get_language_links(self):
        link_tags = self.document.cssselect("a.interlanguage-link-target")
        return sorted([tag.attrib['href'] for tag in link_tags])

    def get_main_text(self):
        elements = self.document.cssselect(".mw-parser-output > p")
        stripped_paragraphs = [e.text_content().strip() for e in elements]
        return "\n\n".join(p for p in stripped_paragraphs if len(p) > 0)


class SimpleWebScraper:
    user_agent = "Text Mining Class / WebScraper"
    fetch_interval = 0.1  # 10 requests / second max

    def __init__(self, output_folder=None):
        self.robot_file_parsers = {}
        self.last_fetch_time = 0
        if output_folder is not None:
            self.output_folder = Path(output_folder)

    def get_robot_url(self, url):
        parsed_url = urlparse(url)
        return f"{parsed_url.scheme}://{parsed_url.hostname}/robots.txt"

    def can_fetch(self, url):
        parsed_url = urlparse(url)
        # Fetching and parsing the robots.txt file can be expensive in it-self.
        # Let's cache the RobotFileParser instances, one per host, on the
        # scraper itself to reuse them for consecutive queries.
        rfp = self.robot_file_parsers.get(parsed_url.hostname)
        if rfp is None:
            rfp = RobotFileParser(self.get_robot_url(url))
            rfp.read()
            self.robot_file_parsers[parsed_url.hostname] = rfp
        return rfp.can_fetch(self.user_agent, parsed_url.path)

    def fetch(self, url):
        if not self.can_fetch(url):
            raise DisallowedFetchError(
                f"robots.txt does not allow fetching {url}")
        since_last_fetch = time() - self.last_fetch_time
        if since_last_fetch < self.fetch_interval:
            # Avoid hammering Wikipedia too frequently
            sleep(self.fetch_interval - since_last_fetch)

        self.last_fetch_time = time()
        request = Request(url, headers={'User-Agent': self.user_agent})
        response = urlopen(request)
        return dict(response.headers), response.read()

    def fetch_and_save(self, url):
        parsed_url = urlparse(url)

        final_path = unquote(parsed_url.path[1:])
        folder = self.output_folder / parsed_url.hostname / final_path
        if not folder.exists():
            # Create the folder and store the result of the call to the fetch
            # method there.
            folder.mkdir(parents=True)
            headers, body = self.fetch(url)

            body_path = folder / "body"
            body_path.write_bytes(body)

            headers_path = folder / "headers.json"
            with open(headers_path, mode='w') as f:
                json.dump(headers, f)

        return folder
