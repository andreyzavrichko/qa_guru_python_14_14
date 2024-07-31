from selene import browser, have, be


class SearchPage:
    def open(self):
        browser.open('/')

    def type_search_input(self, value):
        browser.element('.input__field').click().type(value).press_enter()

    def check_result(self):
        browser.element(".layout__content").should(be.visible)

    def check_result_count(self, value):
        browser.element(".layout__content").should(have.text(value))

    def click_search_link(self):
        browser.element("(//a[@href='https://www.mvideo.ru/mmaster?from=widget']//div)[2]").click()

    def click_express(self):
        browser.element("(//div[@class='text ng-star-inserted'])[3]").click()

    def click_auth(self):
        browser.element("//div[text()='Авторизуйтесь, чтобы применить Бонусные рубли']").click()

    def check_result_dropdown(self, value):
        browser.element(".dropdown__title").should(have.text(value))

    def check_hit_sales(self):
        browser.element("//h2[text()='Хиты продаж']").should(be.visible)

    def check_sales_day(self):
        browser.element("//span[text()='Товары дня']").should(be.visible)

    def check_auth_form(self):
        browser.element("//h2[text()=' Вход или регистрация ']").should(be.visible)

    def check_result_empty(self, value):
        browser.element(".empty-products__header").should(have.text(value))

    def check_result_image(self):
        browser.element(".empty-products__image").should(be.visible)

    def check_result_layout(self, value):
        browser.element(".layout__content").should(have.text(value))

    def check_express_img(self):
        browser.element(
            "//li[text()='Экспресс-доставка: быстра доставка за 2 часа техники и электроники от М.Видео - Москва']").should(
            be.visible)
