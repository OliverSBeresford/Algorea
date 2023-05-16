#include <iostream>
#include <vector>

int calculateMaxSum(int longueurSegment, int nbNombres, std::vector<int> liste) {
    int timesdone = 0;
    int somme1 = liste[0];
    for (int i = 0; i < longueurSegment - 1; i++) {
        somme1 += liste[i+1];
    }
    int previous = somme1;
    int newSum = somme1;
    for (int count = 0; count < nbNombres - longueurSegment; count++) {
        newSum = (newSum + liste[longueurSegment + timesdone]) - liste[timesdone];
        if (newSum >= previous) {
            previous = newSum;
        }
        timesdone++;
    }
    return previous;
}

int main() {
    int longueurSegment, nbNombres;
    std::cin >> longueurSegment >> nbNombres;
    std::vector<int> liste(nbNombres);
    for (int i = 0; i < nbNombres; i++) {
        std::cin >> liste[i];
    }
    int maxSum = calculateMaxSum(longueurSegment, nbNombres, liste);
    std::cout << maxSum << std::endl;
    return 0;
}