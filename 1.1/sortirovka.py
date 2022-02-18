def f_sort(a):
    if len(a) <= 1:
        return a
    number = a[0]
    left = ([i for i in a if i < number])
    middle = ([i for i in a if i == number])
    right = ([i for i in a if i > number])

    return f_sort(left) + middle + f_sort(right)
try:
    file_input = input('Введите имя входного файла: ')
    file_output = input('Введите имя выходного файла: ')
    chisla = []
    with open("number.txt") as f:
        for line in f:
            number.append([int(x) for x in line.split()])

    f_sort(number)
    print(f_sort(number))
    number = open(file_output, "a")
    save = number_end.write(str(f_sort(number)))
    
except FileNotFoundError:
    print('Файл не найден')
except FileExistsError:
    print("Файл уже существует")

print('Выполнила Панова Софья 14124')
print('быстрая сортировка')
print('алгоритм быстрой сортировки включает в себя два основных этапа: разбиение массива относительно опорного элемента;'
      'рекурсивная сортировка каждой части массива. Программа сортирует иделит числа на'
      '1)элементы меньше определенного значения'
      '2)само значение'
      '3)элементы больше или равные этому значению' ')

