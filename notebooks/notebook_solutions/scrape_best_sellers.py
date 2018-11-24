import pandas as pd
from selenium import webdriver


def find_bestsellers_carousel(driver):
    driver.get("https://www.amazon.com")
    driver.find_element_by_link_text("Departments").click()
    driver.find_element_by_link_text("Books").click()
    carousels = driver.find_elements_by_class_name("acswidget-carousel")
    bestsellers_carousels = [carousel for carousel in carousels
                             if "Books Bestsellers" in carousel.text]
    assert len(bestsellers_carousels) == 1
    return next(iter(bestsellers_carousels))


def extract_bookname(book_card):
    link_tags = [tag for tag in book_card.find_elements_by_tag_name("a")
                 if "/product/" in tag.get_attribute("href")
                 and not tag.find_elements_by_tag_name("img")]
    assert len(link_tags) == 1
    return next(iter(link_tags)).text


def extract_price(book_card):
    price_element = book_card.find_element_by_class_name("acs_product-price")
    price_text = price_element.text.strip()
    assert price_text.startswith("$")
    return float(price_text[1:])


def extract_product_id(book_card):
    link_urls = [tag.get_attribute("href")
                 for tag in book_card.find_elements_by_tag_name("a")]
    product_urls = set(url for url in link_urls if "/product/" in url)
    assert len(product_urls) == 1
    url = next(iter(product_urls))
    components = url.split("/")
    return int(components[components.index("product") + 1])


def extract_bestseller_data(n_books=30):
    driver = webdriver.Firefox()
    try:
        carousel = find_bestsellers_carousel(driver)
        next_page = carousel.find_element_by_class_name(
            "a-carousel-goto-nextpage")
        collected_data = []
        for i in range(n_books)
            cards = carousel.find_elements_by_class_name(
                "a-carousel-card")
            for card in cards:
                info = {}
                info["name"] = extract_bookname(card)
                info["price"] = extract_price(card)
                info["produce_id"] = extract_product_id(card)
                collected_data.append(info)
                if len(collected_data) >= n_books:
                    return pd.DataFrame(collected_data)

            # nextpage_button.click() might raise an error if
            # the button is not ready. The following javascript
            # will not click on the button as long as the page
            # is not fully ready.
            driver.execute_script("arguments[0].click();",
                                  nextpage_button)

    finally:
        driver.close()
    raise ValueError(f"Could not collect {n_books} after"
                     f" scanning {n_books} carousel pages")


print(extract_bestseller_data(n_books=30))
