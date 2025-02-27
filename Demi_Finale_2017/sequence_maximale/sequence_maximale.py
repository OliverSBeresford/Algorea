def main():
    nbnombres = int(input())
    currentnum = 0
    previous = 0
    temp = 0
    lenprev = 0
    lencur = 0
    lentemp = 0
    i = 0
    max = 0
    while i < nbnombres:
        new = int(input())
        if currentnum < new:
            previous = currentnum
            currentnum = new
            lencur += 1
        else:
            i += 1
            while i < nbnombres:
                x = int(input())
                if temp < x:
                    temp = x
                    lentemp += 1
                else:
                    break
                i += 1
            
            if lentemp > lenprev:
                lenprev = lencur
                lencur = lentemp
                lentemp = 0

        i += 1
    print(lencur + lenprev)
main()