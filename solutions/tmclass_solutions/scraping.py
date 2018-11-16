from lxml.html import document_fromstring
from urllib.parse import urlparse
from urllib.robotparser import RobotFileParser
from urllib.request import urlopen, Request
from time import time, sleep


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

    def get_language_links(self):
        link_tags = self.document.cssselect("a.interlanguage-link-target")
        link_tags.sort(key=lambda t: t.attrib['lang'])
        return {tag.attrib['lang']: tag.attrib['href'] for tag in link_tags}

    def get_main_text(self):
        p_tags = self.document.cssselect("#mw-content-text p")
        return "\n".join(tag.text_content() for tag in p_tags).strip()


class WebScraper:
    user_agent = "Text Mining Class / WebScraper"
    fetch_interval = 0.1  # 10 requests / second max

    def __init__(self):
        self.robot_file_parsers = {}
        self.last_fetch_time = 0

    def can_fetch(self, url):
        u = urlparse(url)
        rfp = self.robot_file_parsers.get(u.hostname)
        if rfp is None:
            robots_url = f"{u.scheme}://{u.hostname}/robots.txt"
            rfp = RobotFileParser(robots_url)
            rfp.read()
            self.robot_file_parsers[u.hostname] = rfp
        return rfp.can_fetch(self.user_agent, u.path)

    def fetch(self, url):
        if not self.can_fetch(url):
            return None
        since_last_fetch = time() - self.last_fetch_time
        if since_last_fetch < self.fetch_interval:
            # Avoid hammering Wikipedia too much
            sleep(self.fetch_interval - since_last_fetch)

        self.last_fetch_time = time()
        request = Request(url, headers={'User-Agent': self.user_agent})
        response = urlopen(request)
        return dict(response.headers), response.read()
