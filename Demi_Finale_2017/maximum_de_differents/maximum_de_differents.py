def main():
    nbNombres = int(input())
    extrait = int(input())
    list1 = [int(input()) for x in range(nbNombres)]
    set1 = set(list1[x:extrait + x])
    maxLength = len(set1)
    for x in list1[extrait:]:
        if not x in set1:
            maxLength += 1
        length = len(set1)
        if length > maxLength:
            maxLength = length
        if maxLength >= extrait:
            break
    print(maxLength)
main()