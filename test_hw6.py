from datetime import time


def dark_theme_by_time(current_time):
    if time(hour=6) <= current_time < time(hour=22):
        return False
    else:
        return True

def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)
    # TODO переключите темную тему в зависимости от времени суток (с 22 до 6 часов утра - ночь)
    is_dark_theme = dark_theme_by_time(current_time)

    assert is_dark_theme is True

def dark_theme_by_time_and_user_choice(current_time, dark_theme_enabled_by_user):
    if dark_theme_enabled_by_user is True:
        return True
    elif dark_theme_enabled_by_user is False:
        return False
    else:
        return dark_theme_by_time(current_time)


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True
    # TODO переключите темную тему в зависимости от времени суток,
    #  но учтите что темная тема может быть включена вручную

    is_dark_theme = dark_theme_by_time_and_user_choice(current_time, dark_theme_enabled_by_user)
    assert is_dark_theme is True

def find_suitable_user_by_name(name, users):
    for user in users:
        if user["name"] == name:
            return user

def find_suitable_user_by_age(age, users):
    list_users = []
    for user in users:
        if user["age"] < age:
            list_users.append(user)
    return list_users


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    # TODO найдите пользователя с именем "Olga"
    name = "Olga"
    suitable_users = find_suitable_user_by_name(name, users)
    assert suitable_users == {"name": "Olga", "age": 45}

    # TODO найдите всех пользователей младше 20 лет
    age = 20
    suitable_users = find_suitable_user_by_age(age, users)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"

def read_func_data(func, *args):
    func_name = func.__name__.replace('_', ' ').title()
    args = ', '.join([*args])
    print(f"{func_name} [{args}]")
    return f"{func_name} [{args}]"


def test_readable_function():
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    actual_result = read_func_data(open_browser, browser_name)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    actual_result = read_func_data(go_to_companyname_homepage, page_url)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    actual_result = read_func_data(find_registration_button_on_login_page, page_url, button_text)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"