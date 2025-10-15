def test_constructor_tabs_switch(driver, pages):
    pages["main"].open("/")
    pages["main"].open_sauces_tab()
    assert pages["constructor"].is_sauces_visible()
    pages["main"].open_fillings_tab()
    assert pages["constructor"].is_fillings_visible()
    pages["main"].open_buns_tab()
    assert pages["constructor"].is_buns_visible()