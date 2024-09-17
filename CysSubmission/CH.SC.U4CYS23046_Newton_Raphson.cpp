#include <iostream>
#include <cmath>  // For mathematical operations
#include <iomanip>  // For setting precision
#include <limits>   // For epsilon
#include <vector>   // For table storage

using namespace std;

// Function to get user input safely
template <typename T>
T get_input(const string& prompt) {
    T value;
    while (true) {
        cout << prompt;
        if (cin >> value) {
            break;
        } else {
            cout << "Invalid input. Please try again." << endl;
            cin.clear();  // Clear the error flag
            cin.ignore(numeric_limits<streamsize>::max(), '\n');  // Discard invalid input
        }
    }
    return value;
}

// Function to evaluate the polynomial f(x) using the given coefficients
double f_x(const vector<double>& coefficients, double x) {
    double result = 0;
    int degree = coefficients.size() - 1;
    for (int i = 0; i <= degree; ++i) {
        result += coefficients[i] * pow(x, degree - i);
    }
    return result;
}

// Function to evaluate the first derivative of the polynomial f'(x)
double f_prime(const vector<double>& coefficients, double x) {
    double result = 0;
    int degree = coefficients.size() - 1;
    for (int i = 0; i < degree; ++i) {  // Stop before the constant term
        result += (degree - i) * coefficients[i] * pow(x, degree - i - 1);
    }
    return result;
}

// Function to evaluate the second derivative of the polynomial f''(x)
double f_double_prime(const vector<double>& coefficients, double x) {
    double result = 0;
    int degree = coefficients.size() - 1;
    for (int i = 0; i < degree - 1; ++i) {  // Stop before the linear term
        result += (degree - i) * (degree - i - 1) * coefficients[i] * pow(x, degree - i - 2);
    }
    return result;
}

int main() {
    // Get degree of polynomial
    int degree = get_input<int>("Enter the degree of the polynomial: ");
    
    // Get coefficients of the polynomial
    vector<double> coefficients(degree + 1);
    for (int i = 0; i <= degree; ++i) {
        coefficients[i] = get_input<double>("Enter the coefficient of x^" + to_string(degree - i) + ": ");
    }

    // User input for Newton's method
    double y = get_input<double>("Enter the value of x0: ");
    double epsilon = get_input<double>("Enter the value of epsilon: ");
    int max_iterations = 100;  // Limit to prevent infinite loop

    // Variables for Newton's method
    double last = y + 2 * epsilon;  // Ensure loop starts
    double last2 = y;
    int iteration = 1;

    // Vector to store table values
    vector<vector<double>> table;

    // Newton's method loop
    while (abs(last2 - last) > epsilon) {
        last = last2;
        double f_prime_val = f_prime(coefficients, last2);
        double f_double_prime_val = f_double_prime(coefficients, last2);

        if (f_double_prime_val == 0) {  // Prevent division by zero
            cout << "Division by zero error at iteration " << iteration << endl;
            break;
        }

        last2 = last2 - (f_prime_val / f_double_prime_val);

        // Store iteration data for later display
        table.push_back({(double)iteration, last2, abs(last2 - last)});
        iteration++;

        // Output intermediate results every 10 iterations to track progress
        if (iteration % 10 == 0) {
            cout << "Iteration: " << iteration << ", x_n: " << setprecision(14) << last2 << endl;
        }

        // Stop if maximum iterations reached
        if (iteration >= max_iterations) {
            cout << "Maximum iterations reached. The method may not have converged." << endl;
            break;
        }
    }

    // Output the table
    cout << left << setw(20) << "No. of iteration" << setw(20) << "x_n"
         << setw(20) << "x_n+1 - x_n" << endl;
    for (const auto& row : table) {
        cout << left << setw(20) << row[0] << setw(20) << setprecision(14) << row[1]
             << setw(20) << setprecision(14) << row[2] << endl;
    }

    // Output the results
    cout << "Least value (x): " << setprecision(14) << last2 << endl;
    cout << "Optimal Value of function (f(x)): " << setprecision(14) << f_x(coefficients, last2) << endl;

    return 0;
}
