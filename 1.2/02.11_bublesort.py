def bubble_sort(mn):
    length=len(mn)
    for i in range(length):
        for j in range(length-i-1):
            if mn[j]>mn[j+1]:
                d=mn[j]
                mn[j]=mn[j+1]
                mn[j+1]=d
s=[34,56,14,84]
bubble_sort(s)
print(s)
         
