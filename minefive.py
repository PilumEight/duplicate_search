import sys
import os
import hashlib



def lsizes(dir_name):                                    #принимает на вход дирректорию првоеряет все файлы внутри
    filenames = os.listdir(dir_name)
    sizes = []
    for filename in filenames:                           #создаём лист из имён файлов находящийся в данной дирректории , и их размера (lambda)
        real_way = str(os.path.abspath(os.path.join(dir_name, filename)))
        if os.path.isfile(real_way):
            statinfo = os.stat(real_way)
            sizes.append((real_way, statinfo.st_size))
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
    dir_name = input("Pls enter name of directory: ")
    duplicates = check_for_duplicates(equal(lsizes(dir_name)))
    for i in duplicates:
        print(i)
    print("This is duplicates: ", duplicates)
    input("Pls enter any symbol for end")
    sys.exit("Have a good day")


if __name__ == '__main__':
    main()

