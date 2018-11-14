from tmclass_solutions.text_manipulation import tokenize_generic
from tmclass_solutions.text_manipulation import tokenize_japanese
from tmclass_solutions.text_manipulation import remove_accents


class TextIndex:
    """Simplistic in-memory full-text index

    The internal data-structure of the index is built on top of nested Python
    dicts and lists: for each token, store a dictionary with document names as
    keys a list of line numbers as values:

        {
            "token_1": {"doc_3": [12, 42], "doc_5": [1]},
            "token_2": {"doc_1": [17, 21]},
            ...
        }

    The methods named `index_text` and `index_text_file` can process text
    documents to index them into that data-stracture.

    The method `look_token` retrieves the list documents and line numbers that
    contain a specific token.

    The method `query` implements document retrieval for text queries that can
    contain several words at once.
    """

    def __init__(self):
        # Initialize an empty Python dictionary to map text token to the the
        # document names and line numbers that contains that token.
        self._token_to_doc = {}

    def lookup_token(self, token):
        """Retrieve the list of documents and line numbers for a give token

        The list is sorted by document names to get deterministic outputs.
        """
        return sorted(self._token_to_doc.get(token, {}).items())

    def preprocess(self, text, language=None):
        """Apply language specific preprocessing

        For western / latin language, convert all the letters to lower case.

        For French language, replace accentuated characters by their
        non-accentuated counterparts.

        This preprocessing is applied both on the text content of a document to
        index and to any text query prior to tokenization.
        """
        if language in ('fr', 'en'):
            return remove_accents(text.lower())
        else:
            return text

    def tokenize(self, text, language=None):
        """Tokenize text assuming a specific language

        Japanese texts are tokenized with a language specific tokenization
        model. All other language use the generic tokenization schemes that
        splits words on spaces and punctuation characters.

        Tokenization is applied both on the text content of a document to index
        and to any text query.
        """
        if language == "ja":
            return tokenize_japanese(text)
        else:
            return tokenize_generic(text)

    def index_text(self, doc_name, text_content, language=None):
        """Add a text document to the index

        First the text of the document is preprocessed and then tokenized
        assuming a specific language.

        Then for each token, the name of the document and the list of all the
        line numbers where that token occurs in the document are inserted in
        the index.
        """
        for i, line in enumerate(text_content.split("\n")):
            line_number = i + 1  # enumerate starts at 0
            line = self.preprocess(line, language=language)
            tokens = self.tokenize(line, language=language)
            for token in tokens:
                doc_entry = self._token_to_doc.setdefault(token, {})
                line_numbers = doc_entry.setdefault(doc_name, [])
                line_numbers.append(line_number)

    def index_text_file(self, filepath, language, encoding="utf-8"):
        """Index a text document stored as a file

        Read the text by decoding the file content with the provided encoding.
        Then call the `index_text` method to index the content.

        The filename is used as the document name in the index.
        """
        text_content = filepath.read_text(encoding=encoding)
        self.index_text(filepath.name, text_content, language=language)

    def query(self, query_text, language=None):
        """Find all the documents matching a given text query

        First preprocess and tokenize the query (depending on the language of
        the query). Then for each document retrieve all the documents that
        contain each token.

        In the end return the list of document names for documents that contain
        all the tokens of the query at the same time (implicit conjunctive
        query with "and" operators).
        """
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
