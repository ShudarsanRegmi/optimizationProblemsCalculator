#include <iostream>
#include <cmath>
#include <functional>

using namespace std;

// Golden Section Search function
double goldenSectionSearch(function<double(double)> f, double a, double b, double tol = 1e-5) {
    // Golden ratio
    const double phi = (1 + sqrt(5)) / 2;

    // Initial points
    double c = b - (b - a) / phi;
    double d = a + (b - a) / phi;

    while (fabs(b - a) > tol) {
        if (f(c) < f(d)) {
            b = d;
        } else {
            a = c;
        }

        // Recalculate the points
        c = b - (b - a) / phi;
        d = a + (b - a) / phi;
    }

    // Return the midpoint of the final interval
    return (a + b) / 2;
}

// Example function to minimize
double f(double x) {
    return pow(x - 2, 2);  // (x - 2)^2
}

int main() {
    double a = 0;   // Start of the interval
    double b = 4;   // End of the interval

    // Perform Golden Section Search
    double result = goldenSectionSearch(f, a, b);

    // Output the result
    cout << "The minimum value is at x = " << result << endl;
    cout << "The function value at this point is f(x) = " << f(result) << endl;

    return 0;
}
