nbnombres = int(input())
nb1,nb2 = int(input()),0
streak = 1
highscore = 1
highestscoring = ''
var1 = 1
for i in range(nbnombres-1):
    nb2 = int(input())
    if nb1 == nb2:
        streak += 1
    if streak > highscore:
        highestscoring = nb1
        highscore = streak
    if nb2 != nb1:
        streak = 1
    nb1 = nb2
print(highestscoring)

