def extract_bookname(book_card):
    for tag in book_card.find_elements_by_tag_name("a"):
        if "/product/" not in tag.get_attribute("href"):
            # Not the link to the book page
            continue
        if tag.text:
            return tag.text
    # Could not find a link to the book with some title...
    return ""

extract_bookname(first_card)