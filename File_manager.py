import os

dict = {}
if os.path.isfile('memory.txt'):
    memory = open('memory.txt', 'r')
    for line in memory:
        num = line.find(' ')
        rline = line[num+1:]
        rline = rline.strip()
        line = line.split()[0]
        dict[line] = rline
    memory.close()


str = ''

while str != 'exit':
    str = input()

    if str in dict:
        os.startfile(dict[str], 'open')
    else:
        print('Введите путь к файлу:')
        str1 = input()
        memory = open('memory.txt', 'a')
        memory.write('\n' + str + ' ' + str1)
        dict[str] = str1
        os.startfile(dict[str], 'open')
        memory.close()