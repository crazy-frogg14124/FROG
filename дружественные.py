l=[]
for a in range(1,10001):
    b=0
    c=0
    for i in range(1,a):
        if a%i==0:
            b=b+i
    for i in range(1,b):
        if b%i==0:
            c=c+i
    if (a==c) and (a!=b):
        if a<b:
            l.append((a,b))
        else:
            l.append((b,a))
l=sorted(set(l))
for druj in l:
    print(druj)
