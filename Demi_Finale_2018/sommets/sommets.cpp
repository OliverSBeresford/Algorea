#include <cstdio>

int main() {
    int nbnombres, left, current, right, total = 0;
    
    std::scanf("%d", &nbnombres);
    std::scanf("%d", &left);
    std::scanf("%d", &current);
    
    for (int i = 0; i < nbnombres - 2; i++) {
        std::scanf("%d", &right);
        
        if (left < current && current > right) {
            total++;
        }
        left = current;
        current = right;
    }
    
    std::printf("%d", total);
    
    return 0;
}