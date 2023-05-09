longueurSegment = int(input())
nbNombres = int(input())
timesdone = 0
liste = [int(input()) for i in range(nbNombres)]
somme1 = liste[0]
for i in range(longueurSegment - 1):
    somme1 += liste[i+1]
previous, new = somme1, somme1
for count in range(nbNombres - longueurSegment):
    new = (new + liste[longueurSegment + timesdone]) - liste[timesdone] 
    if new >= previous:
        previous = new
    timesdone +=1
print(previous)