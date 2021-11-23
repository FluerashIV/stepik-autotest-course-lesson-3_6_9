# pytest -s --language=es test_items.py
# pytest -s --language=ru test_items.py
# pytest -s --language=fr test_items.py

from selenium.webdriver.common.by import By

def test_add_to_basket_button_is_present_on_goods_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.implicitly_wait(10)
    assert browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket"), "'add to basket' button is not present" #elements просто для того, чтобы дойти до assert, иначе падает на NoSuchElementException

