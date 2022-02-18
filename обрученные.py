l=[]
for a in range(1,10001):
    b=0
    c=0
    f=0
    for i in range(1,a):
        if a%i==0:
            b=b+i
            f=b-1
    for j in range(1,f):
        if f%i==0:
            c=c+i
    if (a==c-1) and (a!=b):
        if a<f:
            l.append((a,f))
        else:
            l.append((f,a))
l=sorted(set(l))
for obr in l:
    print(obr)
