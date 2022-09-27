import time
from pages.Y import SearchHelper
from pages.Y import YandexSeacrhLocators



def test_img(browser):
    yandex_main_page = SearchHelper(browser)
    yandex_main_page.go_to_site("https://ya.ru/")
    yandex_main_page.click_on_element(YandexSeacrhLocators.LOCATOR_ALL_SERVICES)
    assert yandex_main_page.check_exists_element(YandexSeacrhLocators.LOCATOR_IMAGE) == True, "IMAGE don't exist"
    yandex_main_page.click_on_element(YandexSeacrhLocators.LOCATOR_IMAGE)
    names_of_windows = browser.window_handles
    browser.switch_to.window(names_of_windows[1])
    assert browser.current_url == "https://yandex.ru/images/", "It isn't yandex images"
    yandex_main_page.click_on_element(YandexSeacrhLocators.LOCATOR_RESULTS_IMAGE_SEARCH)
    assert len(yandex_main_page.get_words()) > 0, "The category name is not displayed in the search field"
    yandex_main_page.click_on_element(YandexSeacrhLocators.LOCATOR_FIRST_RESULTS_OF_IMAGE_SEARCH)
    assert yandex_main_page.find_element(YandexSeacrhLocators.LOCATOR_OPEN_IMAGE).is_displayed() == True, "Image isn't visible"
    src_of_first_image = yandex_main_page.find_element(YandexSeacrhLocators.LOCATOR_OPEN_IMAGE).get_attribute("src")
    yandex_main_page.click_on_element(YandexSeacrhLocators.LOCATOR_BUTTON_NEXT_IMAGE)
    time.sleep(1)
    src_of_second_image = yandex_main_page.find_element(YandexSeacrhLocators.LOCATOR_OPEN_IMAGE).get_attribute("src")
    assert src_of_first_image != src_of_second_image, "The first and second images is same."
    yandex_main_page.click_on_element(YandexSeacrhLocators.LOCATOR_BUTTON_BACK_IMAGE)
    src_of_third_image = yandex_main_page.find_element(YandexSeacrhLocators.LOCATOR_OPEN_IMAGE).get_attribute("src")
    assert src_of_third_image == src_of_first_image, "The third image is different from the second. "
    time.sleep(3)