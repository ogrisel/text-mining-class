def extract_product_id(book_card):
    link_urls = [tag.get_attribute("href")
                 for tag in book_card.find_elements_by_tag_name("a")]
    product_urls = set(url for url in link_urls if "/product/" in url)
    assert len(product_urls) == 1
    url = next(iter(product_urls))
    components = url.split("/")
    return components[components.index("product") + 1]


extract_product_id(first_card)
