import allure
from allure_commons.types import Severity

from pages.search_page import SearchPage

search_page = SearchPage()


@allure.tag("web")
@allure.severity(Severity.MINOR)
@allure.feature("Поиск")
@allure.story("Проверка отображения страницы поиска")
def test_search_visible(setup_browser):
    with allure.step("Открыть сайт"):
        search_page.open()
    with allure.step("Ввести в поиске значение"):
        search_page.type_search_input("ролики")
    with allure.step("Проверка отображения страницы поиска"):
        search_page.check_result()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск")
@allure.story("Проверка отображения количества товаров")
def test_search_count(setup_browser):
    with allure.step("Открыть сайт"):
        search_page.open()
    with allure.step("Ввести в поиске значение"):
        search_page.type_search_input("ролики")
    with allure.step("Проверка отображения страницы поиска"):
        search_page.check_result_count("Найдено 33 товара")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск")
@allure.story("Проверка наличия фильтра")
def test_filter(setup_browser):
    with allure.step("Открыть сайт"):
        search_page.open()
    with allure.step("Ввести в поиске значение"):
        search_page.type_search_input("телевизор")
    with allure.step("Проверка отображения страницы поиска"):
        search_page.check_result_dropdown("Сначала популярные")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск")
@allure.story("Проверка невалидного запроса")
def test_empty_search(setup_browser):
    with allure.step("Открыть сайт"):
        search_page.open()
    with allure.step("Ввести в поиске значение"):
        search_page.type_search_input("авпвапавпвапавп")
    with allure.step("Проверка невалидного запроса"):
        search_page.check_result_empty("По вашему запросу ничего не найдено")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск")
@allure.story("Проверка поиска большого значения")
def test_image_error(setup_browser):
    with allure.step("Открыть сайт"):
        search_page.open()
    with allure.step("Ввести в поиске значение"):
        search_page.type_search_input("5555555555555555555555555555555555555555555555"
                                      "555555555555555555555555555555555555")
    with allure.step("Проверка отображения картинки"):
        search_page.check_result_image()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Поиск")
@allure.story("Проверка смешанного запроса")
def test_mixed_search(setup_browser):
    with allure.step("Открыть сайт"):
        search_page.open()
    with allure.step("Ввести в поиске значение"):
        search_page.type_search_input("мвидео-топ")
    with allure.step("Проверка количества найденного товара"):
        search_page.check_result_layout("Найдено 2000 товаров")


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Хит продаж")
@allure.story("Проверка отображения раздела Хиты продаж")
def test_hit_sales(setup_browser):
    with allure.step("Открыть сайт"):
        search_page.open()
    with allure.step("Проверка количества найденного товара"):
        search_page.check_hit_sales()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Доставка")
@allure.story("Проверка экспресс-доставки")
def test_express(setup_browser):
    with allure.step("Открыть сайт"):
        search_page.open()
    with allure.step("Нажать на доставку"):
        search_page.click_express()
    with allure.step("Проверка картинки экспресс-доставки"):
        search_page.check_express_img()


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.feature("Товар-дня")
@allure.story("Проверка товаров дня")
def test_express(setup_browser):
    with allure.step("Открыть сайт"):
        search_page.open()
    with allure.step("Проверка отображения товара дня"):
        search_page.check_sales_day()


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.feature("Авторизация")
@allure.story("Проверка окна авторизации")
def test_express(setup_browser):
    with allure.step("Открыть сайт"):
        search_page.open()
    with allure.step("Нажать на авторизацию"):
        search_page.click_auth()
    with allure.step("Проверка окна авторизации"):
        search_page.check_auth_form()
