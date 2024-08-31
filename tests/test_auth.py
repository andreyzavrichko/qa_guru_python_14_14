import allure
from allure_commons.types import Severity

from pages.search_page import search_page


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.feature("Авторизация")
@allure.story("Проверка окна авторизации")
def test_auth(setup_browser):
    search_page.open()
    search_page.click_auth()
    search_page.check_auth_form()
