def test_bascket_button(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    button = browser.find_elements_by_css_selector('.btn-add-to-66666basket')

    assert len(button) > 0, 'такой кнопки не существует'
    print("Тест завершен")
