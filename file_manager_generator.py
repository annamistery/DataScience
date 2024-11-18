import  os
import random
import shutil
os.getcwd()

"""
Пишем в файл название вызываемых фукнций
"""


def save_call_to_file(func):
    def inner(*args, **kwargs):
        # пишем название фукнции в файл
        function_name = func.__name__
        with open('log_func.txt', 'a', encoding='utf-8') as f:
            f.write(f'{function_name}\n')

        result = func(*args, **kwargs)
        return result

    return inner


def add_decor(f):
    # inner - итоговая функция с новым поведение
    def inner(*args, **kwargs):
        # поведение до вызова
        print('-' * 10)
        result = f(*args, **kwargs)
        # поведение после вызова
        print('-' * 10)
        return result

    # возвращается функция inner с новым поведением
    return inner

import os

@save_call_to_file
def create_patch(folder):
    folder = input("Введите название папки:")
    path = os.path.join(os.getcwd(), folder)
    os.mkdir(path) if not os.path.exists(path) else None
    print("Папка успешно создана!" if not os.path.exists(path) else f'Папка {folder} уже существует')


@save_call_to_file    
def remove_patch():
    folder = input("Введите название папки:")
    path = os.path.join(os.getcwd(),folder)
    shutil.rmtree(path) if os.path.exists(path) else None
    print("Папка успешно удалена!" if os.path.exists(path) else f'Папки {folder} не существует')

    
@save_call_to_file
def copy_file ():
    path_file = input('Введите путь к файлу')
    new_path = input("Введите новую директорию")
    new_file = input("Введите имя нового файла:")
    new_path = os.path.join(new_path, new_file)
    
    if not os.path.exists(path_file):
      print('Исходная директория не существует. Проверьте путь!')
      
    else:
        shutil.copy(path_file, new_path) if not os.path.exists(new_path) else None
        
        print('Файл успешно скопирован!' if not os.path.exists(new_path) else f'Файл c именем {new_path} уже существует!')
      
    return

@save_call_to_file 
def content ():
    dir = input('Введите название директории')
    print(os.listdir(dir))

import pathlib
@save_call_to_file
def files_dir():
    dir = input('Введите название директории')
    dir = pathlib.Path(dir)
    files = [file.name for file in dir.iterdir() if file.is_file()]
    print(files)    
    
    
@save_call_to_file
def patch_dir():
    dir = input('Введите название директории:')
    dir = pathlib.Path(dir)
    files = [file.name for file in dir.iterdir() if file.is_dir()]
    print(files)


import platform

@add_decor
@save_call_to_file
def system ():
    print(platform.system())

@add_decor
@save_call_to_file
def creator ():
  print('Создатель программы: Anna Myshlyakova, student of AI University, Course of Data Sciense')

@save_call_to_file
def victorina():
    def get_answer():
        FAMOUS_PEOPLE = {'A.C.Пушкин': '26.06.1799', 'М.Ю.Лермонтов': '15.10.1814', 'С.А. Есенин':'03.10.1895',
                          'В.С. Высоцкий': '25.01.1938', 'С.П. Королёв': '12.01.1907', 'В.П. Глушков': '20.08.1908',
                          'А.Н. Туполев': '29.10.1888', 'Ю.А.Гагарин': '09.03.1934'}
        name, data = random.choice (list(FAMOUS_PEOPLE.items()))

        answer = input(f'Когда родился {name}')
        
        print('Верно' if answer == data else 'Неверно')


    rounds = int(input('Сколько раз вы хотите играть?'))
    for i in range(rounds):
        get_answer()
    print('Пока!')

@save_call_to_file
def bank_accaunt():
    bill_sum = 0
    history = []
    while True:
      print('1.пополнение счёта')
      print('2.покупка')
      print('3.история покупок')
      print('4.выход')
      choice = input("Выберите пункт меню:")
      if choice == '1':
        sum = int(input('Пополните счёт:'))
        bill_sum += sum
      elif choice == '2':
        cost = int(input('Введите сумму покупки:'))
        name = input('Введите наименование покупки:')
        if cost < bill_sum:
          bill_sum-=cost
          history.append((name, cost))
        else:
            print('Недостаточно средств')
      elif choice == '3':
        print(history)
      elif choice == '4':
        print(bill_sum)
        break
      else:
        print("Неверный пункт меню")

import os

@save_call_to_file
def change_directory():
    path = input('Введите название новой директории')

    try:
        os.chdir(path)
        print("Текущая директория: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Такая директория: {0} не существует".format(path))   
        
@save_call_to_file        
def save_directory ():
    victorina = '''def victorina():
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
    print_message('Пока!')'''


    bill = '''import os
import pickle
import json

FILE_NAME = 'orders_obj.json'

# Инициализация переменных
orders = {}
cost = 0

if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
    with open(FILE_NAME, 'r') as f:
        loaded_data = json.load(f)
        # Проверка на корректность загруженных данных
        if isinstance(loaded_data, list) and len(loaded_data) == 2 and isinstance(loaded_data[0], dict) and isinstance(loaded_data[1], int):
            orders = loaded_data[0]
            cost = loaded_data[1]
        else:
            print("Ошибка: данные в файле повреждены. Инициализация пустыми значениями.")
            orders = {}
            cost = 0
# Основной цикл программы
while True:
    print('1. Добавить покупку')
    print('2. История покупок')
    print('3. Выход')
    choice = input('Введите номер: ')

    if choice == '1':
        name = input('Введите название: ')
        price = int(input('Введите цену: '))
        orders[name] = price
        cost += price

    elif choice == '2':
        if orders:
            print("История покупок:")
            for name, price in orders.items():
                print(f"{name}: {price}")
            print(f"Общая стоимость покупок: {cost}")
        else:
            print("История заказов пуста.")

    elif choice == '3':
       # Сохранение данных в файл перед выходом
        with open(FILE_NAME, 'wb') as f:
            json_str = json.dumps((orders, cost))
            json_bytes = json_str.encode('utf-8')
            f.write(json_bytes)
        break

    else:
        print('Неправильно введены данные')
        continue

    ''' 

    def create_directory():
        import os
        directory = os.getcwd()
        folder = 'content'
        path = os.path.join(directory, folder)
        
        os.mkdir(path) if not os.path.exists(path) else None
        
        print("Папка успешно создана!" if not os.path.exists(path) else f'Папка {folder} уже существует')
        
        return path

    path = create_directory()



    def create_patch():
          
        modules = os.path.join(path, 'modules')
        packages = os.path.join(path, 'packages')

        if os.path.exists(path):
        
            if not os.path.exists(os.path.join(path, 'victory.py')) and not os.path.exists(os.path.join(path, 'bill.py')):
                with open(os.path.join(path, 'victory.py'), 'w') as f:
                    f.write(victorina)
                with open(os.path.join(path, 'bill.py'), 'w') as f:
                    f.write(bill)
            if not os.path.exists(modules) and not os.path.exists(packages):
            
                os.mkdir(modules)
                os.mkdir(packages)
            
                print("Файлы victory.py, bill.py успешно созданы!")
                print("Папки 'modules' и 'packages' успешно созданы!")
            
            else:
                print("Файл victory.py уже существует")
                print("Файл bill.py уже существует")
                print(f"Папка {modules} уже существует")
                print(f"Fапка {packages} уже существует")

        return 

    patсh = create_patch()

    print(f"Путь: {patсh}")
    print(f"Путь к папке 'модуль': {os.path.join(patсh, 'modules')}")
    print(f"Путь к папке 'пакеты': {os.path.join(path, 'packages')}")
    
    assert os.path.exists(path), "директория не создана"   
    assert os.path.exists(os.path.join(path, 'modules')), "папка 'modules' не создана"
    assert os.path.exists(os.path.join(path, 'packages')), "папка 'packages' не создана"

    assert 'victory.py' in os.listdir(path), "файл 'victory.py' не создан"
    assert 'bill.py' in os.listdir(path), "файл 'bill.py' не создан"


    path_dir = str(os.listdir(path))

    import json
    if not os.path.exists(os.path.join(path,'listdir.txt')):
        with open(os.path.join(path,'listdir.txt'), 'w') as f:
            json.dump(path_dir, f) 
    
    assert 'listdir.txt' in os.listdir(path), "файл 'listdir.txt' не создан"


def function_menu():
    while True:
      print('1.Создать папку')
      print('2.Удалить папку')
      print('3.Копировать файл')
      print('4.Просмотр содержимого рабочей директории')
      print('5.Вывести только список папок')
      print('6.Вывести только список файлов')
      print('7.Вывести информацию об операционной системе')
      print('8.Вывести информацию о создателе программы')
      print('9.Сыграть в викторину')
      print('10.Мой банковский счёт')
      print('11.Сменить рабочую директорию')
      print('12.Сохранить содержимое рабочей директории в файл')
      print('13.Выйти из программы')
      choice = input("Выберите пункт меню:")
      if choice == '1':
        create_patch()
      elif choice == '2':
        remove_patch()
      elif choice == '3':
        copy_file()
      elif choice == '4':
        content()
      elif choice == '5':
        files_dir()
      elif choice == '6':
        patch_dir()
      elif choice == '7':
        system()
      elif choice == '8':
        creator()
      elif choice == '9':
        victorina()
      elif choice == '10':
        bank_accaunt()
      elif choice == '11':
        change_directory()
        print("Рабочей директория изменена")
      elif choice == '12':
        save_directory()
        print("Содержимое директории сохранено") 
      elif choice == '13':
        print("Выход из программы")
        break
      else:
        print("Неверный пункт меню")

if __name__ == "__main__":
     function_menu ()
