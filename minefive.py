import sys
import os
import hashlib
from builtins import print


def md5(fname):                                  # возвращаем хэш файла
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()





def hash_and_path2(old_dict2):          #THIRD ACTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in old_dict2:
        for y in range(len(old_dict2[i])):
              # абслоютный путь к которому мы будем присваивать хэш файла указанного в нём
            old_dict2[i][y] = {str(md5(old_dict2[i][y])): str(old_dict2[i][y])}
    return old_dict2



def lsizes_final(dir_name):          #FIRST ACTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!     # выводит список полных путей и размера
    paths = dir_name
    new_path = []
    ways_list = []
    sizes = []                      #список содержащий в себе кортежи из полного пути и размера файла
    for i in os.walk(paths):                                # создаём список с адресом самой папки, файлами которые в ней лежат, и вложенными в ней папками
        new_path.append(i)
    for address, dirs, files in new_path:                   # создаём список только адресов файлов
        for file in files:
                 ways_list.append(address+'/'+file)
    for i in ways_list:                                     # создаём список с размером и адресом файлов (объед с пред)
        statinfo = os.stat(i)
        sizes.append((i, str(statinfo.st_size)))
    return sizes

def sorted_dict(just): #SECOND ACTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    new_dict = {}
    old_dict = {}
    for i in just:
        new_dict[i[1]] = []
    for i in just:
        new_dict[i[1]].append(i[0]) #массив где количество памяти - ключ, ячейки - значения
    for i in new_dict:
        if len(new_dict[i]) > 1:
            old_dict[i] = new_dict[i] # количество файлы которые весят одинаково
    return old_dict

def hash_and_path2(old_dict2):          #THIRD ACTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in old_dict2:
        for y in range(len(old_dict2[i])):
              # абслоютный путь к которому мы будем присваивать хэш файла указанного в нём
            old_dict2[i][y] = {str(md5(old_dict2[i][y])): [str(old_dict2[i][y])]}
    return old_dict2




def md5(fname):                                  # возвращаем хэш файла
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()





def last_action(last_dict):                                                    #FOURTH ACTION
  for key in last_dict:                             #ищем в словарь файлы с одинаковыс хэшом и помещаем их под один ключ
    laik = last_dict[key]
    for i in range(len(laik)):                                                               #i каждый словарь листа
      for y in laik[i]:                                                                 #y ключ каждого словаря
        if laik[i][y] != '':
          for j in range(i + 1, len(laik)):                                     #j каждый словарь л
            for s in laik[j]:
              if y == s:
                laik[i][y].append(laik[j][s][0])
                laik[j][s] = ''
                s = ''
  result = {}                                                                       #создаём новый словарь и помещаем в него отсортированный
  for key in last_dict:
    laik = last_dict[key]
    for i in range(len(laik)):
        for y in laik[i]:
            if len(laik[i][y]) > 1:
                result.setdefault(y, laik[i][y])

  return result





def main():
    dir_name = input("Pls enter name of directory with slash like '/': ")

    duplicates = last_action((hash_and_path2(sorted_dict(lsizes_final(dir_name)))))
    for hash_key in duplicates:
        print(hash_key, duplicates[hash_key])

    input("Pls enter any symbol for end")
    sys.exit("Have a good day")


if __name__ == '__main__':
    main()

