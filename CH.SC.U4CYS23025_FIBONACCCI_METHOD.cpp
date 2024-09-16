#include <iostream>
#include <cmath>
#include <functional>

using namespace std;

// Function to compute Fibonacci numbers
int fibonacci(int n) {
    if (n <= 1)
        return n;
    int fib = 0;
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        fib = a + b;
        a = b;
        b = fib;
    }
    return fib;
}

// Fibonacci Search to find the minimum of a unimodal function
double fibonacciSearchMin(function<double(double)> f, double a, double b, double tol) {
    int k = 0;
    while (fibonacci(k) < (b - a) / tol)
        k++;

    int fib_k = fibonacci(k);
    int fib_k1 = fibonacci(k - 1);
    int fib_k2 = fibonacci(k - 2);

    double x1 = a + (fib_k1 / double(fib_k)) * (b - a);
    double x2 = a + (fib_k2 / double(fib_k)) * (b - a);

    while (fib_k2 > tol) {
        if (f(x1) < f(x2)) {
            b = x2;
        } else {
            a = x1;
        }

        x1 = a + (fib_k1 / double(fib_k)) * (b - a);
        x2 = a + (fib_k2 / double(fib_k)) * (b - a);

        fib_k = fib_k1;
        fib_k1 = fib_k2;
        fib_k2 = fib_k - fib_k1;
    }

    return (a + b) / 2;
}

// Fibonacci Search to find the maximum of a unimodal function
double fibonacciSearchMax(function<double(double)> f, double a, double b, double tol) {
    int k = 0;
    while (fibonacci(k) < (b - a) / tol)
        k++;

    int fib_k = fibonacci(k);
    int fib_k1 = fibonacci(k - 1);
    int fib_k2 = fibonacci(k - 2);

    double x1 = a + (fib_k1 / double(fib_k)) * (b - a);
    double x2 = a + (fib_k2 / double(fib_k)) * (b - a);

    while (fib_k2 > tol) {
        if (f(x1) > f(x2)) {
            b = x2;
        } else {
            a = x1;
        }

        x1 = a + (fib_k1 / double(fib_k)) * (b - a);
        x2 = a + (fib_k2 / double(fib_k)) * (b - a);

        fib_k = fib_k1;
        fib_k1 = fib_k2;
        fib_k2 = fib_k - fib_k1;
    }

    return (a + b) / 2;
}

double sampleFunction(double x) {
    // Example function: f(x) = - (x - 2)^2 + 3
    // This function has a maximum at x = 2
    return - (x - 2) * (x - 2) + 3;
}

int main() {
    double a = 0;       // Lower bound of the interval
    double b = 4;       // Upper bound of the interval
    double tol = 1e-5;  // Tolerance for convergence

    // Find minimum
    double minPoint = fibonacciSearchMin(sampleFunction, a, b, tol);
    cout << "The minimum point is at x = " << minPoint << endl;
    cout << "The minimum value is f(x) = " << sampleFunction(minPoint) << endl;

    // Find maximum
    double maxPoint = fibonacciSearchMax(sampleFunction, a, b, tol);
    cout << "The maximum point is at x = " << maxPoint << endl;
    cout << "The maximum value is f(x) = " << sampleFunction(maxPoint) << endl;

    return 0;
}
