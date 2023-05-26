dictionary ={}
nbnombres = int(input())
new = int(input())
lowscore = nbnombres - 1
for i in range(nbnombres-1):
    if not new in dictionary:
        dictionary.update({new:i})
    elif new in dictionary:
        if i - dictionary[new] <= lowscore:
            lowscore = i - dictionary[new]
            dictionary[new] = i
        else:
            dictionary[new] = i
    new = int(input())
print(lowscore)