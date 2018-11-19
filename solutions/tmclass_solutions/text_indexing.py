from tmclass_solutions.text_manipulation import tokenize_generic
from tmclass_solutions.text_manipulation import tokenize_japanese
from tmclass_solutions.text_manipulation import remove_accents
from tmclass_solutions.language_detector import LanguageDetector


class TextIndex:
    """Simplistic in-memory full-text index

    The internal data-structure of the index is built on top of nested Python
    dicts and sets: for each token, store a set with the names of the documents
    holding that token:

        {
            "token_1": {"doc_3", "doc_5"},
            "token_2": {"doc_1"},
            ...
        }

    The methods named `index_text` and `index_text_file` can process text
    documents to index them into that data-structure.

    The method `lookup_token` retrieves the set of the names of documents
    containing that token.

    The method `query` implements document retrieval for text queries that can
    contain several words at once.
    """

    def __init__(self):
        # Initialize an empty Python dictionary to map text token to the the
        # names of document that contains that token.
        self._token_to_doc = {}
        self._language_detector = LanguageDetector()

    def __len__(self):
        """Return the total number of indexed documents

        Empty document (without any tokens) are ignored.
        """
        all_documents = set()
        for document_set in self._token_to_doc.values():
            all_documents.update(document_set)
        return len(all_documents)

    def lookup_token(self, token):
        """Retrieve the list of names of documents containing a give token

        The list of names is sorted by alphabetical order to get deterministic
        outputs so as to ease testing.
        """
        return sorted(self._token_to_doc.get(token, set()))

    def preprocess(self, text, language=None):
        """Apply language specific preprocessing

        For western / latin language, convert all the letters to lower case and
        replace accentuated characters by their non-accentuated counterparts.

        This preprocessing is applied both on the text content of a document to
        index and to any text query prior to tokenization.
        """
        if language is None:
            language = self._language_detector(text)
        if language in ("de", "en", "fr", "es", "ca"):
            # The above list of language codes is incompilete for real use but
            # enough as a demo demo.
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
        if language is None:
            language = self._language_detector(text)
        if language == "ja":
            return tokenize_japanese(text)
        else:
            return tokenize_generic(text)

    def index_text(self, document_name, text_content, language=None):
        """Add a text document to the index

        First the text of the document is preprocessed and then tokenized
        assuming a specific language.

        Then for each token, the name of the document where that token occurs
        in the document are inserted in the index.
        """
        if language is None:
            language = self._language_detector(text_content)
        text_content = self.preprocess(text_content, language=language)
        tokens = self.tokenize(text_content, language=language)
        for token in tokens:
            document_set = self._token_to_doc.setdefault(token, set())
            document_set.add(document_name)

    def index_text_file(self, filepath, language=None, encoding="utf-8"):
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

        The list of names is sorted by alphabetical order to get deterministic
        outputs so as to ease testing.
        """
        if language is None:
            language = self._language_detector(query_text)
        query_text = self.preprocess(query_text, language=language)
        query_tokens = self.tokenize(query_text, language=language)
        result_set = None
        for token in query_tokens:
            document_set = self._token_to_doc.get(token, set())
            if result_set is None:
                result_set = document_set
            else:
                result_set.intersection_update(document_set)
        if result_set is None:
            # Query only holds tokens that are not present in indexed
            # documents.
            return []
        return sorted(result_set)
