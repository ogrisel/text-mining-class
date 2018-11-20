"""Simplistic in-memory indexing of text documents."""


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
        # Hints:
        # - feel free to import and call functions from the
        #   `tmclass_exercises.text_manipulation` module.
        # - String objects have `.lower()` method:
        #   `"Some content with ABC".lower() == "some content with abc"`

        #  TODO: replace the following by the answer:
        return text

    def tokenize(self, text, language=None):
        """Tokenize text assuming a specific language

        Japanese texts are tokenized with a language specific tokenization
        model. All other language use the generic tokenization schemes that
        splits words on spaces and punctuation characters.

        Tokenization is applied both on the text content of a document to index
        and to any text query.
        """
        # Hints: feel free to import and call functions from the
        # `tmclass_exercises.text_manipulation` module.

        #  TODO: replace the following by the answer:
        return []

    def index_text(self, document_name, text_content, language=None):
        """Add a text document to the index

        First the text of the document is preprocessed and then tokenized
        assuming a specific language.

        Then for each token, the name of the document where that token occurs
        in the document are inserted in the index.
        """
        # Hints:
        # - You can reuse the the `self.preprocess(...)` and'
        #   `self.tokenize(...)` methods here.
        # - For each token in text_content, add the `document_name` in
        #   `self._token_to_doc`
        # - The `setdefault` method of Python dicts can be handy:
        #       >>> d = {"a": {"doc1"})
        #       >>> d.setdefault("a", set()).add("doc2")
        #       >>> d
        #       {"a": {"doc1", "doc2"})
        #       >>> d.setdefault("b", set()).add("doc3")
        #       >>> d
        #       {"a": {"doc1", "doc2"}, "b": {"doc3"})

        #  TODO: replace the following by the answer:
        pass

    def index_text_file(self, filepath, language, encoding="utf-8"):
        """Index a text document stored as a file

        Read the text by decoding the file content with the provided encoding.
        Then call the `index_text` method to index the content.

        The filename is used as the document name in the index.
        """
        #  TODO: replace the following by the answer:
        pass

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
        # Hints:
        # - You can reuse the the `self.preprocess(...)` and'
        #   `self.tokenize(...)` methods here.
        # - Python sets have an intersection method to compute common elements:
        #     {'a', 'b'}.intersection({'b', 'c'}) == {'b'}

        #  TODO: replace the following by the answer:
        return []
