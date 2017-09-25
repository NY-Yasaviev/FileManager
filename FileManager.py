# coding: utf-8

import os
import shutil

print("""Добро пожаловать!
Это примитивный файловый менеджер, который обладает некоторыми надстройками. Подробнее будет в разделе "Помощь".""")
help_text = """"Помощь:
$ cat _path to file_ - Выводит содержимое файла в консоль.
Примеры:
cat FileManager.py (файл находится в этой же директории);
cat C:\\Users\\User\App\Manage.py (прописан абсолютный путь до файла).
$ cd _path_ - Изменение текущей директории.
Примеры:
cd .. (Переход в родительскую директорию)
cd C:\\Users\\User\App (Переход по абсолютному пути)
cd MyDir (Переход по локальному пути)
$ dir - Выводит файлы из текущей директории. ( Кроме скрытых).
$ exit - Выход из консоли файлового менеджера.
$ help - Вывод в консоль всех команд с их подробным описанием.
$ ls - Смотреть dir.
$ mk _filename_ - Создает файл с названием _filename_ .
Пример:
mk MyTXTFile.txt 
$ mkdir _dirname_ - Создает директорию с названием _dirname_ .
Пример:
mkdir MyDir 
$ open _path to file_ - Открывает (двойной клик по файлу) файл.
Пример:
open MyTXTFile.txt 
Надстройки:
$$ open add _keyword_ - Добавление возможности открытия по ключевому слову. Сначала проверяет, что такое ключевое слово не занято.
Если оно свободно, просит ввести путь до файла. Кдючевыми словами не могут быть команды настроек. Ключи не чувствительны к регистру.
Пример:
open add english
Введите путь(абсолютный) до файла: C:\\Users\\User\Documents\English\Book.pdf
open english 
$$ open edit _keyword_ - Изменение пути до файла, который открывается по этому ключевому слову. Сначала проверяет, что такое ключевое слово есть.
Если оно есть, то просит ввести новый путь до файла. 
Пример:
open edit english
Введите новый путь(абсолютный) до файла: C:\\Users\\User\Documents\English\Workbook.pdf
open english 
$$ open keys - Выводит все ключевые слова.
$$ open rm _keyword_ - Удаляет ключ и путь, привязанный к этому ключу, из памяти.Сначала проверяет наличие такого ключа.
Пример:
open rm english 
$ rm _filename_ - Удаляет файл с названием _filename_ .
Пример:
rm MyTXTFile.txt 
$ rmdir _dirname_ - Удаляет всю директорию (т.е. вложенные директории тоже) с названием _dirname_ .
Пример:
rmdir MyDir
"""

print(help_text)

bad_msg = """Что-то пошло не так...
Мне страшно."""

try:
    keywords_dict = {}
    if os.path.isfile(os.path.join(os.curdir, "DataBase.txt")):
        database = open('DataBase.txt', 'r')
        for line in database:
            num = line.find(' ')
            rline = line[num + 1:]
            rline = rline.strip()
            lline = line[:num]
            keywords_dict[lline] = rline
        database.close()
except:
    print(bad_msg)

dir_of_script = os.getcwd()

work = True

while work:
    request = input(os.path.abspath(os.curdir) + ">>")
    num_of_first_space = request.find(' ')
    if num_of_first_space == -1:
        num_of_first_space = len(request)

    num_of_last_space = request.rfind(' ')

    command = request[:num_of_first_space]

    if command == "cat":
        try:
            path = request[num_of_first_space + 1:]
            file = open(os.path.join(os.curdir, path), 'r')
            data = file.readlines()
            for row in data:
                print(row)
            file.close()
        except:
            print("Файл не найден.")

    elif command == "cd":
        try:
            path = request[num_of_first_space + 1:]
            if path == "..":
                os.chdir(os.path.abspath(os.pardir))
            else:
                os.chdir(path)
        except:
            print("Директория не найдена.")

    elif command == "dir" or command == "ls":
        try:
            for file in os.listdir("."):
                print(file)
        except:
            print(bad_msg)

    elif command == "exit":
        try:
            os.chdir(dir_of_script)
            database = open('DataBase.txt', 'w')
            for key, value in keywords_dict.items():
                database.write(key + ' ' + value + '\n')
            database.close()

            print("Goodbye!")
            work = False
        except:
            print(bad_msg)

    elif command == "help":
        try:
            print(help_text)
        except:
            print(bad_msg)

    elif command == "mk":
        try:
            path = request[num_of_first_space + 1:]
            open(os.path.join(os.curdir, path), 'w').close()
        except:
            print(bad_msg)

    elif command == "mkdir":
        try:
            path = request[num_of_first_space + 1:]
            os.mkdir(os.path.join(os.curdir, path))
        except:
            print(bad_msg)

    elif command == "open":
        try:
            rcmd = request[num_of_first_space + 1:]
            num_of_first_space = rcmd.find(' ')

            if num_of_first_space == -1:
                num_of_first_space = len(rcmd)

            if rcmd[:num_of_first_space] in ['add', 'edit', 'keys', 'rm']:
                command = rcmd[:num_of_first_space]
                key = rcmd[num_of_first_space + 1:]

                if command == "add":
                    if key in keywords_dict.keys():
                        print("Ключ уже занят. Придумайте новый ключ и повторите попытку.")
                    else:
                        path_to_file = input("Введите путь(абсолютный) до файла:")
                        keywords_dict[key] = path_to_file

                elif command == "edit":
                    if key not in keywords_dict.keys():
                        print("Ключ не найден. Проверьте ключ и попробуйте снова.")
                    else:
                        keywords_dict[key] = input("Введите новый путь (абсолютный) до файла:")

                elif command == "keys":
                    for key in keywords_dict.keys():
                        print(key)

                elif command == "rm":
                    if key not in keywords_dict.keys():
                        print("Ключ не найден. Проверьте ключ и попробуйте снова.")
                    else:
                        keywords_dict.pop(key)

            else:
                key_or_path = rcmd[:num_of_first_space]
                is_key = False
                for key, value in keywords_dict.items():
                    if key_or_path == key:
                        os.startfile(value, 'open')
                        is_key = True
                        continue
                if not is_key:
                    print()
                    os.startfile(os.path.join(os.curdir, key_or_path), 'open')
        except:
            print('Файл или ключевое слово не найдены')

    elif command == "rm":
        try:
            name_of_file = request[num_of_first_space + 1:]
            os.remove(os.path.join(os.curdir, name_of_file))
        except:
            print("Файл не найден.")

    elif command == "rmdir":
        try:
            name_of_dir = request[num_of_first_space + 1:]
            shutil.rmtree(os.path.join(os.curdir, name_of_dir))
        except:
            print("Директория не найдена.")

    else:
        print("Команда не найдена.")
