import sys
import os
import hashlib
from builtins import print
import time


def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.
    """
    def wrapper(*args, **kwargs):
        t = time.process_time()
        res = func(*args, **kwargs)
        print(func.__name__, time.process_time() - t)
        return res
    return wrapper

def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов
    декорируемой функции.
    """
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        print("{0} была вызвана: {1}x".format(func.__name__, wrapper.count))
        return res
    wrapper.count = 0
    return wrapper










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
              # создание вложенных словарей где ключ - хэш,  значение - путь
            old_dict2[i][y] = {str(md5(old_dict2[i][y])): [str(old_dict2[i][y])]}
    return old_dict2



@counter
def md5(fname):                                  # возвращаем хэш файла
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()




@benchmark
def last_action(last_dict):                                                    #FOURTH ACTION
  for key_size in last_dict:                             #ищем в словарь файлы с одинаковыс хэшом и помещаем их под один ключ
    laik = last_dict[key_size]
    for list_numb in range(len(laik)):                      #для каждого элемента
      for y in laik[list_numb]:                             #
        if laik[list_numb][y] != '':                        #
          for j in range(list_numb + 1, len(laik)):         #
            for s in laik[j]:
              if y == s:
                laik[list_numb][y].append(laik[j][s][0])
                laik[j][s] = ''

  result = {}                                        #создаём новый словарь и помещаем в него словари где хэш ключ, а значение - дубликаты
  for key_size in last_dict:
    laik = last_dict[key_size]
    for list_numb in range(len(laik)):
        for y in laik[list_numb]:
            if len(laik[list_numb][y]) > 1:
                result.setdefault(y, laik[list_numb][y])

  return result




@benchmark
def main():
    dir_name = input("Pls enter name of directory with slash like '/': ")

    duplicates = last_action((hash_and_path2(sorted_dict(lsizes_final(dir_name)))))
    for hash_key in duplicates:
        print(hash_key, duplicates[hash_key])

    input("Pls enter any symbol for end")
    sys.exit("Have a good day")


if __name__ == '__main__':
    main()

