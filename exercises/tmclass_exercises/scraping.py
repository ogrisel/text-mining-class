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
        """Return the list of URLs of related pages"""
        # HINTS:
        # - `cssselect` makes it possible to get a list of DOM elements using
        #   a CSS selection expression:
        #     elements = self.document.cssselect("#identifier tag")
        # - `element.attrib` is a dictionary of the tag attributes.
        # - The URL of a link "a" tag is stored as the value of the `href`
        #   attribute.
        # - Use the "Inspect Element" function of Firefox to explore the DOM
        #   and find identifiers or class names to precisely craft a CSS
        #   selection expression for the language navigation links.

        # TODO: implement me!
        return []

    def get_main_text(self):
        r"""Return the text of the paragraphs of the main content area

        Paragraphs are separated by "\n\n".
        """
        # HINTS:
        # - `cssselect` makes it possible to get a list of DOM elements using
        #   a CSS selection expression:
        #     elements = self.document.cssselect("parent_tag#identifier tag")
        # - For a given element, the `text_content` method retrieves the
        #   cleaned up text content of that element and all its descendants:
        #     elements[0].text_content()
        # - Here we want to only select the paragraphs of the main content
        #   area, without the info box or navigation elements.
        # - Use the "Inspect Element" function of Firefox to explore the DOM
        #   and find identifiers or class names to precisely craft a CSS
        #   selection expression for the paragraphs of the main content area.

        # TODO: implement me!
        return ""


class SimpleWebScraper:
    user_agent = "Text Mining Class / WebScraper"

    def __init__(self, output_folder=None):
        if output_folder is not None:
            self.output_folder = Path(output_folder)

    def get_robot_url(self, url):
        """Parse url to retrieve https://hostname/robots.txt"""
        # Hint: use urllib.parse.urlparse to extract the "scheme" ("http"
        #       or "https") and the "hostname" of the URL.

        # TODO:
        return "https://implement.me"

    def can_fetch(self, url):
        """Check if it is allowed to scrape the resource hosted at url

        This is done by parsing the robots.txt of the host.
        """
        # Hint:
        #   Use `urllib.robotparser.RobotFileParser` to check if scraping
        #   "url" is allowed or not for our user agent.

        # TODO: implement me!
        return False

    def fetch(self, url):
        """Fetch the content of url

        Return the dict of response headers and the bytes of the response
        body.
        """
        # Hint:
        #   Use `urllib.request.urlopen` to retrieve "URL"
        #   Return both the dictionnary of headers and the bytes of the body
        #   of the Response object returned by `urlopen`.
        #   Bonus: set the User-Agent header in the Request passed to
        #   `urlopen`.

        # TODO: implement me!
        return {}, b""

    def fetch_and_save(self, url):
        """Fetch the content of URL

        Parse URL to find the hostname and the path. Create a mirror folder
        structure on the file system to store the results.

        The bytes of the body of the response are save as a file named "body"
        in that folder while the dict of response headers are saved as a JSON
        file named "headers.json" in the same folder.
        """
        # Hint: use "urllib.parse.unquote" on the "path" component of URL
        #       to build the folder name where to save the results.
        # TODO: implement me!
        return self.output_folder / "path/to/folder"
