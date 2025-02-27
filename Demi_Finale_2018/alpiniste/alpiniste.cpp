#include <cstdio>

int main() {
    int nbnombres, previous, current, total = 0;
    std::scanf("%d", &nbnombres);  // Read the number of input values
    std::scanf("%d", &previous);   // Read the first input value

    for (int i = 0; i < nbnombres - 1; i++) {
        std::scanf("%d", &current);  // Read the next input value

        // Compare the previous value with the current value
        if (previous < current) {
            total += (current - previous) * 2;  // If current is greater, add the difference multiplied by 2 to the total
        } else if (previous > current) {
            total += previous - current;       // If previous is greater, add the difference to the total
        }
        previous = current;  // Set the current value as the new previous value for the next iteration
    }

    std::printf("%d", total);  // Print the calculated total
    return 0;
}