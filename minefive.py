import sys
import os
import hashlib

#def equal(sizes):                          
#    equal_list = []
#    for i in range(0, len(sizes) - 1):
#        for y in range(0, len(sizes) - 1):
#            if sizes[i][1] == sizes[y][1]:
#                equal_list.append((sizes[i], sizes[y]))
#    return equal_list


def lsizes():                                    #сделать для любого пути принимая на вход дирректорию
    mine_dir = os.getcwd()
    ur_dir = os.listdir()
    sizes = []
    for i in ur_dir:                            
        statinfo = os.stat(i)
        sizes.append((i, statinfo.st_size))
    return sizes


def equal(sizes):                              
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
    duplicates = check_for_duplicates(equal(lsizes()))
    for i in duplicates:
        print(i)
    print("This is duplicates: ", duplicates)
    sys.exit("Have a good day")


if __name__ == '__main__':
    main()

