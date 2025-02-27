def main():
    nbsections, nbparties = int(input()), int(input())

    prev, cur = int(input()), 0
    liste = [0] * nbparties
    inputs = 1
    for i in range(nbparties):
        while True:
            cur = int(input())
            inputs += 1
            if cur != prev:
                prev = cur
                break
            else:
                liste[i] += 1
            prev = cur
        liste[i] += 1
    
    somme = sum(liste)
    maximum = 0
    newnum = 1
    while inputs < nbsections:
        while inputs < nbsections:
            new = int(input())
            inputs += 1
            if new == cur:
                newnum += 1
            else:
                if somme - liste[0] + newnum > somme:
                    somme = somme - liste[0] + newnum
                liste[0:-1] = liste[1:]
                liste[-1] = newnum
                newnum = 1
                break
            cur = new
    print(somme)
        
main()