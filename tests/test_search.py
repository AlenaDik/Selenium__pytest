from pages.Y import SearchHelper
from pages.Y import YandexSeacrhLocators


def test_yandex_search(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site("https://ya.ru/")
    assert yandex_main_page.check_exists_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD) > 0, "Search don'texist"
    yandex_main_page.enter_word("тензор")
    assert yandex_main_page.check_exists_elements(YandexSeacrhLocators.LOCATOR_SEARCH_SUGGEST) > 0, "Suggests don't exist" #== True, "Search don'texist"
    yandex_main_page.click_ENTER()
    assert yandex_main_page.get_link_of_first_result_of_search() == "https://tensor.ru/", "First result of search isn't true"
