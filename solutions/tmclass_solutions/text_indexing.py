from tmclass_solutions.text_manipulation import tokenize_generic
from tmclass_solutions.text_manipulation import tokenize_japanese
from tmclass_solutions.text_manipulation import remove_accents


class TextIndex:

    def __init__(self):
        # Initialize an empty Python dictionary to map text token to the the
        # document names and line numbers that contains that token.
        self._token_to_doc = {}

    def lookup_token(self, token):
        return sorted(self._token_to_doc.get(token, {}).items())

    def preprocess(self, text, language=None):
        if language in ('fr', 'en'):
            return remove_accents(text.lower())
        else:
            return text

    def tokenize(self, text, language=None):
        if language == "ja":
            return tokenize_japanese(text)
        else:
            return tokenize_generic(text)

    def index_text(self, doc_name, text_content, language=None):
        for i, line in enumerate(text_content.split("\n")):
            line_number = i + 1  # enumerate starts at 0
            line = self.preprocess(line, language=language)
            tokens = self.tokenize(line, language=language)
            for token in tokens:
                entry = self._token_to_doc.setdefault(token, {})
                line_numbers = entry.setdefault(doc_name, [])
                line_numbers.append(line_number)

    def index_text_file(self, filepath, language, encoding="utf-8"):
        text_content = filepath.read_text(encoding=encoding)
        self.index_text(filepath.name, text_content, language=language)

    def query(self, query_text, language=None):
        query_text = self.preprocess(query_text, language=language)
        query_tokens = self.tokenize(query_text, language=language)
        result_set = None
        for token in query_tokens:
            document_set = set(self._token_to_doc.get(token, {}).keys())
            if result_set is None:
                result_set = document_set
            else:
                result_set.intersection_update(document_set)
            if len(result_set) == 0:
                return []
        return sorted(result_set)
