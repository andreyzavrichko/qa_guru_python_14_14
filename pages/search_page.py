import allure
from selene import browser, have, be, by


class SearchPage:
    def open(self):
        with allure.step("Открыть сайт"):
            browser.open('/')

    def type_search_input(self, value):
        with allure.step("Ввести в поиске значение"):
            browser.element("//input[@class='input__field input__field--indent-from-icon']").click().type(value).press_enter()

    def check_result(self):
        with allure.step("Проверка отображения страницы поиска"):
            browser.element("//main[@class='layout__content']").should(be.visible)

    def check_result_count(self, value):
        with allure.step("Проверка отображения страницы поиска"):
            browser.element("//main[@class='layout__content']").should(have.text(value))

    def click_express(self):
        with allure.step("Нажать на доставку"):
            browser.element(by.text('Экспресс-доставка от 2 часов')).click()

    def click_auth(self):
        with allure.step("Нажать на авторизацию"):
            browser.element(by.text('Авторизуйтесь, чтобы применить Бонусные рубли')).click()

    def check_result_dropdown(self, value):
        with allure.step("Проверка отображения страницы поиска"):
            browser.element("//div[@class='dropdown__title']").should(have.text(value))

    def check_hit_sales(self):
        with allure.step("Проверка количества найденного товара"):
            browser.element(by.text('Хиты продаж')).should(be.visible)

    def check_sales_day(self):
        with allure.step("Проверка отображения товара дня"):
            browser.element(by.text('Товары дня')).should(be.visible)

    def check_auth_form(self):
        with allure.step("Проверка окна авторизации"):
            browser.element("//form[@class='login-form ng-untouched ng-pristine ng-valid']").should(be.visible)

    def check_result_empty(self, value):
        with allure.step("Проверка невалидного запроса"):
            browser.element("//p[@class='empty-products__header']").should(have.text(value))

    def check_result_image(self):
        with allure.step("Проверка отображения картинки"):
            browser.element("//img[@class='empty-products__image']").should(be.visible)

    def check_result_layout(self, value):
        with allure.step("Проверка количества найденного товара"):
            browser.element("//main[@class='layout__content']").should(have.text(value))

    def check_express_img(self):
        with allure.step("Проверка картинки экспресс-доставки"):
            browser.element(by.text('Экспресс-доставка: быстра доставка за 2 часа техники'
                                    ' и электроники от М.Видео - Москва')).should(be.visible)
