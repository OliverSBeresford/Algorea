#include <cstdio>

int main() {
    int nbnombres, previous, current, total = 0;
    std::scanf("%d", &nbnombres);
    std::scanf("%d", &previous);
    for (int i = 0; i < nbnombres - 1; i++) {
        std::scanf("%d", &current);
        if (previous < current) {
            total += (current - previous) * 2;
        } else if (previous > current) {
            total += previous - current;
        }
        previous = current;
    }
    std::printf("%d", total);

    return 0;
}