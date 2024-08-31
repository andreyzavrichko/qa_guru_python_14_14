import allure
from allure_commons.types import Severity

from pages.search_page import search_page


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Доставка")
@allure.story("Проверка экспресс-доставки")
def test_express(setup_browser):
    search_page.open()
    search_page.click_express()
    search_page.check_express_img()
