#include <iostream>
#include <algorithm>

int main() {
    int arr[3];
    for (int i=0;i<3;i++) {
        std::cin >> arr[i];
    }
    std::cout << *std::min_element(arr,arr+(sizeof(arr)/sizeof(arr[0])));
    return 0;
}