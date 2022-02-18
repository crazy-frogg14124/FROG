for a in range(1,10001):
    arm=0
    s=a
    i=str(a)
    while a>0:
        arm=arm+(a%10)**len(i)
        a=a//10
    if s==arm:
        print(s)
