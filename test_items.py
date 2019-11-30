import time


def test_lang_link(browser, ch_lang):
    link = f"http://selenium1py.pythonanywhere.com/{ch_lang}/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)

    browser.find_element_by_css_selector("#add_to_basket_form > button")
    assert True
