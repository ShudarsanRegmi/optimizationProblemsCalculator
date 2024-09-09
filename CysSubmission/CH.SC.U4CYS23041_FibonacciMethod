#include <iostream>
#include <vector>
using namespace std;

double f(double x, double a, double b, double c) {
    return a * x * x + b * x + c;
}

vector<int> fibonacci(int n) {
    vector<int> fib(n + 1, 0);
    fib[1] = 1;
    for (int i = 2; i <= n; ++i) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
    return fib;
}

double fibonacciSearch(double a, double b, int n, double coefA, double coefB, double coefC) {
    vector<int> fib = fibonacci(n + 1);

    double x1 = a + (fib[n - 2] / (double)fib[n]) * (b - a);
    double x2 = a + (fib[n - 1] / (double)fib[n]) * (b - a);

    double f1 = f(x1, coefA, coefB, coefC);
    double f2 = f(x2, coefA, coefB, coefC);

    for (int i = n; i > 1; --i) {
        if (f1 < f2) {  // Maximize by choosing larger value
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
    double a, b, c, left, right;
    int n;

    cout << "Enter coefficients a, b, c: ";
    cin >> a >> b >> c;

    cout << "Enter the interval [left, right]: ";
    cin >> left >> right;

    cout << "Enter number of Fibonacci iterations: ";
    cin >> n;

    double maximum = fibonacciSearch(left, right, n, a, b, c);
    cout << "Maximum is at x = " << maximum << endl;
    cout << "f(x) = " << f(maximum, a, b, c) << endl;

    return 0;
}
