def sort(file_sort = ""):
    with open(file_sort, "r") as file:
        massiv = []
        for line in file:
            l = line.split("\n")[0]
            l = l.split( )
            massiv2=[]
            for i in l:
                i = int(i)
                massiv2.append(i)
            massiv.append(massiv2)
    return massiv

def add(a, b, massiv, m):
    elements = massiv[a][b]
    massiv[a][b] = 0
    m.append(elements)
    try:
        if massiv[a][b + 1] == elements:
            if not massiv[a][b + 1] == massiv[a][0]:
                x = add(a, b + 1, massiv, m)
    except IndexError:
        x = 0
    try:
        if massiv[a + 1][b] == elements:
            if not massiv[a + 1][b] == massiv[0][b]:
                x = add(a + 1, b, massiv, m)
    except IndexError:
        x = 0
    try:
        if massiv[a - 1][b] == elements:
            if not massiv[a - 1][b] == massiv[0][b]:
                x = add(a - 1, b, massiv, m)
    except IndexError:
        x = 0
    try:
        if massiv[a][b - 1] == elements:
            if not massiv[a][b - 1] == massiv[a][0]:
                x = add(a, b - 1, massiv, m)
    except IndexError:
        x = 0
    return m

massiv = []
file_sort = "mas.txt"
massiv = sort(file_sort)
i = 0
for a in range(len(massiv)):
     for b in range(len(massiv[a])):
         print(massiv[a][b], end = " ")
     print()
for a in range(len(massiv)):
     for b in range(len(massiv[a])):
         if massiv[a][b] == 0:
             continue
         else:
             m = []
             f = add(a, b, massiv, m)
             i = i + 1
print("Количество островов в массиве:", i)
