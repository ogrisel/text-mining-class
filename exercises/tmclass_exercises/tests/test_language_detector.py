from tmclass_exercises.language_detector import split_paragraphs
from tmclass_exercises.language_detector import WikipediaDataset
from tmclass_exercises.language_detector import scrape_wikipedia_texts
from tmclass_exercises import DATA_FOLDER_PATH


def test_scrape_language_dataset():
    output_folder = DATA_FOLDER_PATH / "wikipedia_scraping_output"
    if output_folder.exists():
        # Delete the output of a previous run. We do not delete the folder
        # at the end of the test to make it easy to do manual introspection
        # of the results of the test for pedagogical purpose.
        output_folder.rmdir()

    english_seed_articles = [
        "Agriculture", "Architecture", "Art", "Biology", "Business",
        "Cinematography", "Culture", "Economy", "Literature", "Music", "Politics",
        "Religion", "Sport", "Science", "Technology", "Trade"
    ]
    scrape_wikipedia_dataset(output_folder, english_seed_articles,
                             follow_lang_links=False)

    assert output_folder.ls() == ['en']

    scrape_wikipedia_dataset(output_folder, english_seed_articles,
                             follow_lang_links=True)


MULTI_PARAGRAPH_DOCUMENT = """\

This is the first paragraph. Is it not very interesting but it is the first
paragraph in the document.

And here is the second paragraph. It is much more interesting. This is the
second paragraph. This paragraph is very repetitive. This paragraph is very
repetitive. This paragraph is very repetitive. This paragraph is very
repetitive.

To short a paragraph.

This the third valid paragraph. It's boring but at least it's the final
paragraph.

"""

SHORT_DOCUMENT = "This is a very short document. It has only one line."


def test_split_paragraph_30():
    paragraphs = split_paragraphs(SHORT_DOCUMENT, minimum_length=30)
    assert len(paragraphs) == 1
    assert paragraphs[0] == SHORT_DOCUMENT

    paragraphs = split_paragraphs(MULTI_PARAGRAPH_DOCUMENT, minimum_length=30)
    assert len(paragraphs) == 3
    assert paragraphs[0].startswith("This is the first paragraph.")
    assert paragraphs[0].endswith("very\nrepetitive.")
    assert paragraphs[1].startswith("And here is the second paragraph.")
    assert paragraphs[1].endswith("first\nparagraph in the document.")
    assert paragraphs[2].startswith("This the third valid paragraph.")
    assert paragraphs[2].endswith("final\nparagraph.")
    assert all(len(p) > 30 for p in paragraphs)


def test_split_paragraph_100():
    paragraphs = split_paragraphs(SHORT_DOCUMENT, minimum_length=100)
    assert len(paragraphs) == 0

    paragraphs = split_paragraphs(MULTI_PARAGRAPH_DOCUMENT, minimum_length=100)
    assert len(paragraphs) == 1
    assert paragraphs[0].startswith("And here is the second paragraph.")
    assert paragraphs[0].endswith("first\nparagraph in the document.")


def test_prepare_dataset():
    dataset = WikipediaDataset(DATA_FOLDER_PATH / "wikipedia_text")

    dataset.text_and_labels(min_paragraph,
                             min_samples_per_class=100)


