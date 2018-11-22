from lxml.html import document_fromstring
from lxml.etree import strip_elements
from pathlib import Path
# from urllib.parse import urlparse, unquote
# from urllib.robotparser import RobotFileParser
# from urllib.request import urlopen, Request
# import json


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
        # TODO: implement me!
        return []

    def get_main_text(self):
        # TODO: implement me!
        return ""


class SimpleWebScraper:
    user_agent = "Text Mining Class / WebScraper"

    def __init__(self, output_folder=None):
        if output_folder is not None:
            self.output_folder = Path(output_folder)

    def get_robot_url(self, url):
        # TODO: implement me!
        return "https://implement.me"

    def can_fetch(self, url):
        # TODO: implement me!
        return False

    def fetch(self, url):
        # TODO: implement me!
        return {}, b""

    def fetch_and_save(self, url):
        # TODO: implement me!
        return self.output_folder / "path/to/folder"
