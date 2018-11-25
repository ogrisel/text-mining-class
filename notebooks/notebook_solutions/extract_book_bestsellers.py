import pandas as pd


def extract_book_bestsellers_data(driver, n_books=10):
    bestsellers = None
    carousels = driver.find_elements_by_class_name("acswidget-carousel")
    for carousel in carousels:
        if "bestsellers" in carousel.text.lower():
            bestsellers = carousel
            break
    if not bestsellers:
        raise ValueError("Could not find best sellers on page")

    collected_data = []
    for i in range(n_books):
        cards = bestsellers.find_elements_by_class_name(
            "a-carousel-card")
        for card in cards:
            info = {}
            info["name"] = extract_bookname(card)
            if not info["name"]:
                # Invalid card
                continue
            info["price"] = extract_price(card)
            info["product_id"] = extract_product_id(card)
            collected_data.append(info)
            if len(collected_data) >= n_books:
                return pd.DataFrame(collected_data)

        next_page = carousel.find_element_by_class_name(
            "a-carousel-goto-nextpage")
        next_page.click()
#         driver.execute_script("arguments[0].click();", next_page)


extract_book_bestsellers_data(driver, n_books=10)