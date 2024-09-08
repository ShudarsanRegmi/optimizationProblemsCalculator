#include <iostream>
#include <vector>

int fibonacci_search(const std::vector<int>& arr, int x) {
    int n = arr.size();

    // Initialize Fibonacci numbers
    int fib_m_2 = 0; // (m-2)'th Fibonacci number
    int fib_m_1 = 1; // (m-1)'th Fibonacci number
    int fib_m = fib_m_1 + fib_m_2; // m'th Fibonacci number

    // Find the smallest Fibonacci number greater than or equal to n
    while (fib_m < n) {
        fib_m_2 = fib_m_1;
        fib_m_1 = fib_m;
        fib_m = fib_m_1 + fib_m_2;
    }

    // Mark the eliminated range from the front
    int offset = -1;

    // While there are elements to be inspected
    while (fib_m > 1) {
        // Calculate the index to be compared
        int i = std::min(offset + fib_m_2, n - 1);

        // If x is greater than the value at index i, cut the subarray array from offset to i
        if (arr[i] < x) {
            fib_m = fib_m_1;
            fib_m_1 = fib_m_2;
            fib_m_2 = fib_m - fib_m_1;
            offset = i;
        }
        // If x is less than the value at index i, cut the subarray after i+1
        else if (arr[i] > x) {
            fib_m = fib_m_2;
            fib_m_1 = fib_m_1 - fib_m_2;
            fib_m_2 = fib_m - fib_m_1;
        }
        // Element found. Return index
        else {
            return i;
        }
    }

    // Comparing the last element with x
    if (fib_m_1 && arr[offset + 1] == x) {
        return offset + 1;
    }

    // Element not found
    return -1;
}

int main() {
    std::vector<int> arr = {10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100, 110, 120, 130, 140, 150};
    int x = 85;
    
    int result = fibonacci_search(arr, x);
    
    if (result != -1) {
        std::cout << "Element found at index " << result << std::endl;
    } else {
        std::cout << "Element not found" << std::endl;
    }

    return 0;
}
