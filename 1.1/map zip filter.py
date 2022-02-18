l1 = [1,2,3,4,5,6,7,8,9,10]
def double(num):
    return num*2
end_l = list(map(double, l1))
print('(1)', end_l)

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [1,2,3,4,5,6,7,8,9,10]
l3 = [1,2,3,4,5,6,7,8,9,10]
def umnogenie(num):
    return num[0]*num[1]*num[2]
all_l = list(zip(l1, l2, l3))
end_l = list(map(umnogenie, all_l))
print('(2)', end_l)

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [1,2,3,4,5,6,7,8,9,10]
l3 = [1,2,3,4,5,6,7,8,9,10]
def len1(num):
    return len(num)
all_l = list(zip(l1, l2, l3))
end_l = list(map(len, all_l))
print('(3)', end_l)

l1 = [1,2,3,4,5,6,7,8,9,10]
def chet(num):
    if num%2 == 0:
        return num
    else:
        return 0
end_l = list(filter(chet, l1))
print('(4)', end_l)

l1 = [1,2,3,4,5,6,7,8,9,10]
def krat(num):
    if num % 3 == 0:
        return num
    else:
        return 0
all_l = list(map(krat, l1))
end_l = list(filter(None, all_l))
print('(5)',end_l)

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [1,2,3,4,5,6,7,8,9,10]
l3 = [1,2,3,4,5,6,7,8,9,10]
all_l = list(zip(l1, l2, l3))
print('(6)', all_l)

l1 = [1,2,3,4,5,6,7,8,9,10]
l2 = [1,2,3,4,5,6,7,8,9,10]
double_l2 = list((map(lambda x: x*2, l2)))
all_l = list(zip(l1, double_l2))
print('(7)', all_l)
