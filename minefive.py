import sys
import os
import hashlib

#paths = 'D:/WORKWORKWORK/test'                                показывает все файлы на пка
#for path in paths:
#    for dirpath, dirnames, filenames in os.walk(path):
#        for filename in filenames:
#            print(filename)
#for i in os.walk



#for i in os.walk(paths):
#    new_path.append(i)
#for address, dirs, files in new_path:
#    for file in files:
#             print(address+'/'+file)

#def lsizes(dir_name):                                    #принимает на вход дирректорию првоеряет все файлы внутри
#    filenames = os.listdir(dir_name)
#    sizes = []
#    for filename in filenames:                           #создаём лист из имён файлов находящийся в данной дирректории , и их размера (lambda)
#        real_way = str(os.path.abspath(os.path.join(dir_name, filename)))
#        if os.path.isfile(real_way):
#            statinfo = os.stat(real_way)
#            sizes.append((real_way, statinfo.st_size))
#    return sizes

def lsizes(dir_name):                                     # выводит список полных путей и размера
    paths = dir_name
    new_path = []
    ways_list = []
    sizes = []
    for i in os.walk(paths):                                # создаём список с адресом самой папки, файлами которые в ней лежат, и вложенными в ней папками
        new_path.append(i)
    for address, dirs, files in new_path:                   # создаём список только адресов файлов
        for file in files:
                 ways_list.append(address+'/'+file)
    for i in ways_list:                                     # создаём список с размером и адресом файлов (объед с пред)
        statinfo = os.stat(i)
        sizes.append((i, statinfo.st_size))
    return sizes


def equal(sizes):                               #возвращаем пары одинаковых документов (lambda)
    equal_list = []
    for i in range(0, len(sizes)):
        for y in range(i + 1, len(sizes)):
            if sizes[i][1] == sizes[y][1]:
                equal_list.append((sizes[i], sizes[y]))
    return equal_list

def md5(fname):                                  # возвращаем хэш файла
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()


def check_for_duplicates(equal_list):                           #сравниваем по хэшу выыводим попарно, сделать вывод всех одинаковых вместе
    result = []
    for i in equal_list:
        if md5(i[0][0]) == md5(i[0][0]):

            result.append((i[0][0], i[1][0]))
    return result


def main():
    dir_name = input("Pls enter name of directory with slash like '/': ")
    duplicates = check_for_duplicates(equal(lsizes(dir_name)))
    for i in duplicates:
        print(i)
    print("This is duplicates: ", duplicates)
    input("Pls enter any symbol for end")
    sys.exit("Have a good day")


if __name__ == '__main__':
    main()

