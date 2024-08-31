import allure
from allure_commons.types import Severity

from pages.search_page import search_page


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Хит продаж")
@allure.story("Проверка отображения раздела Хиты продаж")
def test_hit_sales(setup_browser):
    search_page.open()
    search_page.check_hit_sales()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Товар-дня")
@allure.story("Проверка товаров дня")
def test_day(setup_browser):
    search_page.open()
    search_page.check_sales_day()
