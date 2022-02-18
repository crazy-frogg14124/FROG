number = 0
p = { }
replicas = []
roles = []

with open("roles.txt", "r",encoding='utf-8') as file:
    for line in file:
        line = line.rstrip()
        if line != "roles:":
            if line != "textLines:":
                roles.append(line)
            else:
                break
    roles.append("Слова автора")
    roles.sort()

    for i in range(len(roles)):
        replicas.append([])
    for line in file:
        number += 1
        line = line.rstrip()
        if ":" in line:
            if "(" in line:
                value = line.partition("(")[2]
                for i in range(len(roles)):
                    if "Слова автора" == roles[i]:
                        replicas[i].append(value.replace(')', ''))
                line = line.partition("(")[0]
            if line.partition(":")[0] in roles:
                k = line.partition(":")[0]
                value = line.partition(":")[2]
                p[k] = value
                for i in range(len(roles)):
                    if k == roles[i]:
                        result = str(number) + str(")") + str(p[k])
                        replicas[i].append(result)
                last_k = k
        else:
            if "(" in line:
                value = line.partition("(")[2]
                for i in range(len(roles)):
                    if "Слова автора" == roles[i]:
                        replicas[i].append(value.replace(')', ''))
            else:
                value = line
                p[last_k] = value
                for i in range(len(roles)):
                    if last_k == roles[i]:
                        replicas[i].append(p[last_k])
                        
for i in range(len(roles)):
    print(str(roles[i]) + str(": "))
    for j in range(len(replicas[i])):
        print(replicas[i][j])
    print()
print(replicas)
