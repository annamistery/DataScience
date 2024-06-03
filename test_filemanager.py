from file_manager import creator, system

name = creator()
assert name == 'Создатель программы: Anna Myshlyakova, student of AI University, Course of DataSciense', "нет такого имени"


system = system ()
assert system == 'Windows', 'Другая система'


from unittest.mock import MagicMock
external_system = MagicMock()
def create_patch (external_system):
    falder = 'content'
    path = os.path.join(os.getcwd(),falder)
    if not os.path.exists(path):
        os.mkdir(path)
        print("Папка успешно создана!")
    else:
        print(f'Папка {falder} уже существует')
    return 
external_system.create_patch()
assert create_patch, "папка не создана"

import unittest
from unittest.mock import patch
import random

# здесь должна быть ваша функция victorina()
import random

def get_random_person(FAMOUS_PEOPLE):
    return random.choice(list(FAMOUS_PEOPLE.items()))

def get_user_input(name):
    return input(f'Когда родился {name}? ')

def print_message(message):
    print(message)

def victorina():
    FAMOUS_PEOPLE = {'A.C.Пушкин': '26.06.1799', 'М.Ю.Лермонтов': '15.10.1814', 'С.А. Есенин':'03.10.1895',
                    'В.С. Высоцкий': '25.01.1938', 'С.П. Королёв': '12.01.1907', 'В.П. Глушков': '20.08.1908',
                    'А.Н. Туполев': '29.10.1888', 'Ю.А.Гагарин': '09.03.1934'}
    rounds = int(get_user_input('Сколько раз вы хотите играть?'))
    for _ in range(rounds):
        name, date = get_random_person(FAMOUS_PEOPLE)
        answer = get_user_input(name)
        if answer == date:
            print_message('Верно')
        else:
            print_message('Неверно')
    print_message('Пока!')


import unittest
from unittest.mock import patch

# здесь ваш обновленный код victorina() и вспомогательные функции...

class TestVictorina(unittest.TestCase):
    @patch('__main__.get_user_input', side_effect=['1', '26.06.1799'])  # Предоставляем ожидаемые ответы
    @patch('__main__.print_message')  # Подменяем print_message
    @patch('__main__.get_random_person', return_value=('A.C.Пушкин', '26.06.1799'))  # Подменяем выбор случайной персоны
    def test_victorina_correct_answer(self, mock_get_random_person, mock_print_message, mock_get_user_input):
        victorina()
        mock_print_message.assert_any_call('Верно'), 'функция работает некорректно'

    # аналогично можно добавить тест для неверного ответа

print('Тест успешно пройден')
