from pages.main_page import MainPage


def test_switch_to_sauces_tab(driver):
    main = MainPage(driver)
    main.open_main()
    main.open_sauces_tab()
    assert main.is_tab_active("Соусы")


def test_switch_to_buns_tab(driver):
    main = MainPage(driver)
    main.open_main()
    main.open_buns_tab()
    assert main.is_tab_active("Булки")


def test_switch_to_fillings_tab(driver):
    main = MainPage(driver)
    main.open_main()
    main.open_fillings_tab()
    assert main.is_tab_active("Начинки")