from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from pages.base import BasePage


class YandexSeacrhLocators:

    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, "text")
    LOCATOR_YANDEX_SEARCH = (By.XPATH, "/html/body/main/div[2]/form/div")
    LOCATOR_SEARCH_SUGGEST = (By.CSS_SELECTOR, "body > div.mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile > ul > li")
    LOCATOR_FIRST_RESULTS_OF_SEARCH = (By.CSS_SELECTOR, "#search-result > li:nth-child(3) > div > div.Organic.organic.Typo.Typo_text_m.Typo_line_s.i-bem > div.Organic-Subtitle.Organic-Subtitle_noWrap.Typo.Typo_type_greenurl.organic__subtitle > div > a")  #search-result > li:nth-child(3) > div > div.Organic.organic.Typo.Typo_text_m.Typo_line_s.i-bem > div.VanillaReact.OrganicTitle.OrganicTitle_multiline.Typo.Typo_text_l.Typo_line_m.organic__title-wrapper > a#search-result > li:nth-child(3)
    LOCATOR_IMAGE = (By.CSS_SELECTOR, "body > div.services-pinned__popup.services-pinned__popup_more.services-pinned__popup_visible_yes > div > div > div.scrollbar__scrollable > div > div > div.services-pinned__more-popup-list > a:nth-child(12) > div.services-pinned__more-popup-item-title")
    LOCATOR_ALL_SERVICES = (By.CSS_SELECTOR, "body > main > div.services-pinned.services-pinned_more_yes.i-bem.services-pinned_js_inited > div > a")
    LOCATOR_RESULTS_IMAGE_SEARCH = (By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div[1]')
    LOCATOR_CHECK = (By.XPATH, "/html/body/header/div/div[1]/div[2]/form/div[1]/span/span/input")# uniq1663910297442698977
    LOCATOR_FIRST_RESULTS_OF_IMAGE_SEARCH = (By.XPATH, "/html/body/div[3]/div[2]/div[1]/div[1]/div/div[2]/div/a")
    LOCATOR_OPEN_IMAGE = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[3]/div/div[5]/img")
    LOCATOR_BUTTON_NEXT_IMAGE = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[4]")
    LOCATOR_BUTTON_BACK_IMAGE = (By.XPATH, "/html/body/div[12]/div[2]/div/div/div/div[3]/div/div[2]/div[1]/div[1]")



class SearchHelper(BasePage):

    def get_words(self):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_CHECK)
        return search_field.get_attribute("value")

    def enter_word(self, word):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_ENTER(self):
        search_field = self.find_element(YandexSeacrhLocators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.send_keys(Keys.ENTER)

    def click_on_element(self, locator):
        all_services = self.find_element(locator)
        all_services.click()

    def check_exists_element(self, locator): # for element
        try:
            self.find_element(locator)
        except NoSuchElementException:
            return False
        return True

    def check_exists_elements(self, locator): # for elementS
        elements = self.find_elements(locator)
        return len(elements)

    def get_link_of_first_result_of_search(self):
        results_of_search = self.find_elements(YandexSeacrhLocators.LOCATOR_FIRST_RESULTS_OF_SEARCH)
        link = [elem.get_attribute("href") for elem in results_of_search]
        return link[0]