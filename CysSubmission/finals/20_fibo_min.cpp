#include <iostream>
#include <cmath>
#include <vector>
using namespace std;


double f(double x, double a, double b, double c) {
    return a * x * x + b * x + c;  // Quadratic function: ax^2 + bx + c
}


vector<int> fibonacci(int n) {
    vector<int> fib(n + 1, 0);
    fib[1] = 1;
    for (int i = 2; i <= n; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib;
}


double fibonacciSearch(double a, double b, int n, double epsilon, double coefA, double coefB, double coefC) {
    vector<int> fib = fibonacci(n + 1);

    double x1 = a + (fib[n - 2] / (double)fib[n]) * (b - a);
    double x2 = a + (fib[n - 1] / (double)fib[n]) * (b - a);

    double f1 = f(x1, coefA, coefB, coefC);
    double f2 = f(x2, coefA, coefB, coefC);

    for (int i = n; i > 1; --i) {
        if (f1 > f2) {
            a = x1;
            x1 = x2;
            f1 = f2;
            x2 = a + (fib[i - 1] / (double)fib[i]) * (b - a);
            f2 = f(x2, coefA, coefB, coefC);
        } else {
            b = x2;
            x2 = x1;
            f2 = f1;
            x1 = a + (fib[i - 2] / (double)fib[i]) * (b - a);
            f1 = f(x1, coefA, coefB, coefC);
        }
    }

    return (x1 + x2) / 2;  
}

int main() {

    double a, b, c;
    cout << "Enter coefficients for the quadratic function ax^2 + bx + c:" << endl;
    cout << "Enter a: ";
    cin >> a;
    cout << "Enter b: ";
    cin >> b;
    cout << "Enter c: ";
    cin >> c;

    double left, right;
    cout << "Enter the left endpoint of the interval: ";
    cin >> left;
    cout << "Enter the right endpoint of the interval: ";
    cin >> right;

    int n;
    cout << "Enter the number of Fibonacci numbers to use (higher means more precision): ";
    cin >> n;

    double epsilon = 1e-5;  

    double minimum = fibonacciSearch(left, right, n, epsilon, a, b, c);
    cout << "The estimated minimum of the function is at x = " << minimum << endl;
    cout << "Function value at minimum: f(x) = " << f(minimum, a, b, c) << endl;

    return 0;
}
