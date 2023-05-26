#include <iostream>
#include <unordered_map>

int main() {
    std::unordered_map<int, int> dictionary;
    int nbnombres;
    std::cin >> nbnombres;
    int nouv;
    std::cin >> nouv;
    int lowscore = nbnombres - 1;
    for (int i = 0; i < nbnombres - 1; i++) {
        if (dictionary.find(nouv) == dictionary.end()) {
            dictionary.insert(std::make_pair(nouv, i));
        } else {
            if (i - dictionary[nouv] <= lowscore) {
                lowscore = i - dictionary[nouv];
                dictionary[nouv] = i;
            } else {
                dictionary[nouv] = i;
            }
        }
        std::cin >> nouv;
    }
    std::cout << lowscore << std::endl;
    return 0;
}