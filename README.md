# Проект по автоматизации тестирования МВидео

## :cherry_blossom:	Содержание

> ➠ [Покрытый функционал](#earth_africa-покрытый-функционал)
>
> ➠ [Технологический стек](#classical_building-технологический-стек)
>
> ➠ [Запуск тестов из терминала](#запуск-тестов-из-терминала)
>
> ➠ [Запуск тестов в Jenkins](#robot-удаленный-запуск-тестов)
>
> ➠ [Отчет о результатах тестирования в Allure Report](#skier-главная-страница-allure-отчета)
>
> ➠ [Уведомления в Telegram с использованием бота](#-уведомления-в-telegram-с-использованием-бота)
>
> ➠ [Пример запуска теста в Selenoid](#-пример-запуска-теста-в-selenoid)


## :earth_africa: Покрытый функционал

> Разработаны автотесты на <code>UI</code>.
### UI

- [x] Проверка отображения страницы поиска
- [x] Проверка отображения количества товаров
- [x] Проверка наличия фильтра
- [x] Проверка невалидного запроса
- [x] Проверка поиска большого значения
- [x] Проверка смешанного запроса
- [x] Проверка отображения раздела Хиты продаж
- [x] Проверка экспресс-доставки
- [x] Проверка товаров дня
- [x] Проверка окна авторизации

## :classical_building: Технологический стек

<p align="center">
<img width="6%" title="PyCharm" src="images/logo/pycharm.svg">
<img width="6%" title="Python" src="images/logo/python.svg">
<img width="6%" title="Selenium" src="images/logo/selenium.svg">
<img width="6%" title="Selenoid" src="images/logo/Selenoid.svg">
<img width="6%" title="Allure Report" src="images/logo/Allure_Report.svg">
<img width="6%" title="Pytest" src="images/logo/pytest.svg">
<img width="6%" title="GitHub" src="images/logo/GitHub.svg">
<img width="6%" title="Jenkins" src="images/logo/Jenkins.svg">
<img width="6%" title="Telegram" src="images/logo/Telegram.svg">
</p>

 В данном проекте автотесты написаны на <code>Python</code> с использованием <code>Selene</code> для UI-тестов.
>
> <code>Selenoid</code> выполняет запуск браузеров в контейнерах <code>Docker</code>.
>
> <code>Allure Report</code> формирует отчет о запуске тестов.
>
> В качестве библиотеки для модульного тестирования используется <code>Pytest</code>.
>
> <code>Jenkins</code> выполняет запуск тестов.
> После завершения прогона отправляются уведомления с помощью бота в <code>Telegram</code>.


## Запуск тестов из терминала

### :robot: Локальный запуск тестов

```
pytest
```

### :robot: Удаленный запуск тестов 

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```

### :skier: Главная страница Allure-отчета

<p align="center">
<img title="Allure Overview" src="images/screens/allure_suites.png">
</p>

### :eye_speech_bubble: Детализация шагов

<p align="center">
<img title="Allure Behaviors" src="images/screens/allure_details.png">
</p>


### :frog: Основной дашборд

<p align="center">
<img title="Allure Overview Dashboard" src="images/screens/allure_overview_dashboard.png">
</p>


## <img width="4%" title="Telegram" src="images/logo/Telegram.svg"> Уведомления в Telegram с использованием бота

> После завершения сборки специальный бот, созданный в <code>Telegram</code>, автоматически обрабатывает и отправляет сообщение с отчетом о прогоне.

<p align="center">
<img title="Telegram Notifications" src="images/screens/telegram_notifications.png">
</p>

## <img width="4%" title="Selenoid" src="images/logo/Selenoid.svg"> Пример запуска теста в Selenoid

> К каждому тесту в отчете прилагается видео. Одно из таких видео представлено ниже.
<p align="center">
  <img title="Selenoid Video" src="images/gif/selenoid_video.gif">
</p>


