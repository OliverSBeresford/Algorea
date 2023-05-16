#include <iostream>
using namespace std;

int main() {
    int nbnombres;
    cin >> nbnombres;
    int nb1, nb2 = 0;
    int streak = 1;
    int highscore = 1;
    int highestscoring = 0;
    for (int i = 0; i < nbnombres-1; i++) {
        cin >> nb2;
        if (nb1 == nb2) {
            streak++;
        }
        if (streak > highscore) {
            highestscoring = nb1;
            highscore = streak;
        }
        if (nb2 != nb1) {
            streak = 1;
        }
        nb1 = nb2;
    }
    cout << highestscoring << endl;
    return 0;
}