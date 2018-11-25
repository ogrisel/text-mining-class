def extract_price(book_card):
    price_element = book_card.find_element_by_class_name("acs_product-price")
    price_text = price_element.text.strip()
    if not price_text.startswith("$"):
        return None
    return float(price_text[1:])


extract_price(first_card)
