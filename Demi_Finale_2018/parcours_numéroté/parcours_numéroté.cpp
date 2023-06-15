#include <cstdio>

int main() {
    int nbcases, num = 1, i;
    std::scanf("%d", &nbcases);
    int list[nbcases];
    for (i = 0; i < nbcases; i++) {
        std::scanf("%d", &list[i]);
    }
    for (i = 0; i < 10; i++) {
        std::printf("%d\n", num);
        num = list[num - 1];
    }

    return 0;
}