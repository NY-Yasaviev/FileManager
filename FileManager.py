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
Если оно свободно, просит ввести путь до файла.
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
bad_msg = "Что-то пошло не так"
print(help_text)

work = True

COMMAND = 0
PATH = 1
KEY = 2

while work:
    request = input(os.path.abspath(os.curdir) + ">>").split()
    if request[COMMAND] == "cat":
        try:
            file = open(request[PATH], 'r')
            data = file.readlines()
            for row in data:
                print(row)
            file.close()
        except:
            print("Файл не найден.")
    elif request[COMMAND] == "cd":
        try:
            if request[PATH] == "..":
                os.chdir(os.path.abspath(os.pardir))
            else:
                os.chdir(request[PATH])
        except:
            print("Директория не найдена.")
    elif request[COMMAND] == "dir" or request[COMMAND] == "ls":
        try:
            for file in os.listdir("."):
                print(file)
        except:
            print(bad_msg)
    elif request[COMMAND] == "exit":
        try:
            print("Goodbye!")
            work = False
        except:
            print(bad_msg)
    elif request[COMMAND] == "help":
        try:
            print(help_text)
        except:
            print(bad_msg)
    elif request[COMMAND] == "mk":
        try:
            open(request[PATH],'w').close()
        except:
            print(bad_msg)
    elif request[COMMAND] == "mkdir":
        try:
            os.mkdir(os.path.join(os.curdir, request[PATH]))
        except:
            print(bad_msg)
    elif request[COMMAND] == "open":
        os.startfile(request[PATH], 'open')
    elif request[COMMAND] == "rm":
        try:
            os.remove(os.curdir,request[PATH])
        except:
            print("Файл не найден")
    elif request[COMMAND] == "rmdir":
        try:
            shutil.rmtree()
    else:
        print("Command not found")
