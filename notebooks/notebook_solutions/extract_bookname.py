def extract_bookname(book_card):
    link_tags = [tag for tag in book_card.find_elements_by_tag_name("a")
                 if "/product/" in tag.get_attribute("href")
                 and not tag.find_elements_by_tag_name("img")]
    assert len(link_tags) == 1
    return next(iter(link_tags)).text


extract_bookname(first_card)
