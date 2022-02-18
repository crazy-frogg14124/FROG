print("armstrong numbers: ")
armstrong = [x for x in range(10000) if sum(list(map(lambda y: y ** len(str(x)), list(map(int, str(x)))))) == x]
print(armstrong)
