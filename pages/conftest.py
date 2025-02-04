import pytest
from selenium import webdriver


# Определяем функцию pytest_addoption на уровне модуля (обычно этот код выносится в conftest.py)
def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Выбор языка интерфейса для браузера (например, en, ru)"
    )

@pytest.fixture(scope="class")
def browser(request):
    # Получаем значение опции с именем "language"
    lang = request.config.getoption("language")
    print(f"\nstart browser for test with lang: {lang}")

    options = webdriver.ChromeOptions()
    options.add_argument(f"--lang={lang}")
    
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()