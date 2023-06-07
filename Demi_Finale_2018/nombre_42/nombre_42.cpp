#include <cstdio>

int main() {
    int input, num = 0;
    for (int i = 0; i < 10; i++ ) {
        std::scanf("%d", &input);
        if (input == 42) {
            num++;
        }
    }
    std::printf("%d", num);
}