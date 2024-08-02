import allure
from allure_commons.types import Severity

from pages.search_page import SearchPage

search_page = SearchPage()


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.feature("Поиск")
@allure.story("Проверка отображения страницы поиска")
def test_search_visible(setup_browser):
    search_page.open()
    search_page.type_search_input("ролики")
    search_page.check_result()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск")
@allure.story("Проверка отображения количества товаров")
def test_search_count(setup_browser):
    search_page.open()
    search_page.type_search_input("ролики")
    search_page.check_result_count("Найдено 33 товара")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск")
@allure.story("Проверка наличия фильтра")
def test_filter(setup_browser):
    search_page.open()
    search_page.type_search_input("телевизор")
    search_page.check_result_dropdown("Сначала популярные")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск")
@allure.story("Проверка невалидного запроса")
def test_empty_search(setup_browser):
    search_page.open()
    search_page.type_search_input("авпвапавпвапавп")
    search_page.check_result_empty("По вашему запросу ничего не найдено")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск")
@allure.story("Проверка поиска большого значения")
def test_image_error(setup_browser):
    search_page.open()
    search_page.type_search_input("5555555555555555555555555555555555555555555555"
                                  "555555555555555555555555555555555555")
    search_page.check_result_image()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск")
@allure.story("Проверка смешанного запроса")
def test_mixed_search(setup_browser):
    search_page.open()
    search_page.type_search_input("мвидео-топ")
    search_page.check_result_layout("Найдено 2000 товаров")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Хит продаж")
@allure.story("Проверка отображения раздела Хиты продаж")
def test_hit_sales(setup_browser):
    search_page.open()
    search_page.check_hit_sales()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Доставка")
@allure.story("Проверка экспресс-доставки")
def test_express(setup_browser):
    search_page.open()
    search_page.click_express()
    search_page.check_express_img()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Товар-дня")
@allure.story("Проверка товаров дня")
def test_day(setup_browser):
    search_page.open()
    search_page.check_sales_day()


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.feature("Авторизация")
@allure.story("Проверка окна авторизации")
def test_auth(setup_browser):
    search_page.open()
    search_page.click_auth()
    search_page.check_auth_form()
