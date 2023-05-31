nbNombres = int(input())
set1 = {}
liste = []
num1 = 0
memoir1 = 0
add = 0
sub = 0
emergency = 0
emergency2 = 0
for i in range(nbNombres):
    liste.append(int(input()))
i = 0
while not i == nbNombres - 1:
    if liste[i] == liste[i+1]:
        i += 1
        memoir1 += 1
        if i == nbNombres - 1:
            emergency = 1
        if not i == 1:
            num1 = liste[i-2]
        if emergency == 0:
            while liste[i] == liste[i+1]:
                memoir1 += 1
                i += 1
                if i == nbNombres - 1:
                    emergency = 1
                    break
        add += memoir1
        if emergency == 0:
            if liste[i + 1] == num1:
                memoir1 -= 1
        if liste[i] in set1:
            set1.update({liste[i]: set1[liste[i]] + memoir1})
        else:    
            set1.update({liste[i]: memoir1})
    memoir1 = 0
    if i == nbNombres - 1:
                break
    if not i == 0:
        if liste[i - 1] == liste[i + 1]:
            if liste[i] in set1:
                set1.update({liste[i]: set1[liste[i]] - 1})
            else: 
                set1.update({liste[i]: -1})
    i += 1
list1 = []
list2 = []
for i in set1:
    list1.append(i)
for i in range(len(list1)):
    list2.append(set1[list1[i]])
list2.sort()
k = add - list2[len(list2) - 1]
print(k)

