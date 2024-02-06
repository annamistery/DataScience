import  os
import random
import shutil
os.getcwd()

def create_patch ():
    falder = input("Введите название папки:")
    path = os.path.join(os.getcwd(),falder)
    if not os.path.exists(path):
       os.mkdir(path)
       print("Папка успешно создана!")
    else:
      print(f'Папка {falder} уже  ужесуществует')

def remove_patch():
    falder = input("Введите название папки:")
    path = os.path.join(os.getcwd(),falder)
    if os.path.exists(path):
       shutil.rmtree(path)
       print("Папка успешно удалена!")
    else:
      print("Такой папки не существует")

def copy_file ():
    path_file = input('Введите путь к файлу')
    new_path = input("Введите новую директорию")
    new_file = input("Введите имя нового файла:")
    new_path = os.path.join(new_path, new_file)
    if not os.path.exists(path_file):
       print('Исходная директория не существует. Проверьте путь!')
       return
    else:
      if not os.path.exists(new_path):
       shutil.copy(path_file, new_path)
       print('Файл успешно скопирован!')
      else:
       print("Файл с таким именем уже существует!")

def content ():
    dir = input('Введите название директории')
    print(os.listdir(dir))

import pathlib
def files_dir():
    dir = input('Введите название директории')
    dir = pathlib.Path(dir)
    files = [file.name for file in dir.iterdir() if file.is_file()]
    print(files)    

def patch_dir():
    dir = input('Введите название директории:')
    dir = pathlib.Path(dir)
    files = [file.name for file in dir.iterdir() if file.is_dir()]
    print(files)

import platform
def system ():
    return platform.system()


def creator ():
  print('Создатель программы: Anna Myshlyakova, student of AI University, Course of DataSciense')


def victorina():
    def get_answer():
        FAMOUS_PEOPLE = {'A.C.Пушкин': '26.06.1799', 'М.Ю.Лермонтов': '15.10.1814', 'С.А. Есенин':'03.10.1895',
                          'В.С. Высоцкий': '25.01.1938', 'С.П. Королёв': '12.01.1907', 'В.П. Глушков': '20.08.1908',
                          'А.Н. Туполев': '29.10.1888', 'Ю.А.Гагарин': '09.03.1934'}
        name, data = random.choice (list(FAMOUS_PEOPLE.items()))

        answer = input(f'Когда родился {name}')
        if answer == data:
            print('Верно')
        else:
          print ('Неверно')

    rounds = int(input('Сколько раз вы хотите играть?'))
    for i in range(rounds):
        get_answer()
    print('Пока!')


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

def change_directory():
    path = input('Введите название новой директории')

    try:
        os.chdir(path)
        print("Текущая директория: {0}".format(os.getcwd()))
    except FileNotFoundError:
        print("Такая директория: {0} не существует".format(path))   

def function_menu ():
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
      print('12.Выйти из программы')
      choice = input("Выберите пункт меню:")
      if choice == '1':
        create_patch ()
      elif choice == '2':
        remove_patch()
      elif choice == '3':
        copy_file ()
      elif choice == '4':
        content ()
      elif choice == '5':
        files_dir()
      elif choice == '6':
        patch_dir()
      elif choice == '7':
        system ()
      elif choice == '8':
        creator ()
      elif choice == '9':
        victorina()
      elif choice == '10':
        bank_accaunt()
      elif choice == '11':
        change_directory()
      elif choice == '12':
        print("Выход из программы")
        break
      else:
        print("Неверный пункт меню")

if __name__ == "__main__":
     main()
