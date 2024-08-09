import math
import numpy as np
import threading
from typing import List, Tuple

class Optimizer:
    def __init__(self, num_vars: int, n: int, epsilon: float):
        self.num_vars = num_vars
        self.n = n
        self.epsilon = epsilon
        self.variables: List[Tuple[float, int]] = [(0, 0)] * num_vars
        self.Del: List[float] = [0] * num_vars

    def input_variables(self):
        for i in range(self.num_vars):
            while True:
                try:
                    coefficient = float(input(f"Enter the coefficient for x{i + 1}: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            
            while True:
                try:
                    power = int(input(f"Enter the power for x{i + 1}: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")
            
            self.variables[i] = (coefficient, power)

    def input_deltas(self):
        for i in range(self.num_vars):
            while True:
                try:
                    self.Del[i] = float(input(f"Enter the value for del{i + 1}: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

    def norm(self, v: List[float]) -> float:
        return np.linalg.norm(v)

    def function_value(self, x: List[float]) -> float:
        result = 0.0
        for i in range(self.num_vars):
            coefficient = x[i]
            power = self.variables[i][1]
            result += coefficient * math.pow(coefficient, power)
        return result

    def log_iteration(self, iteration: int, Del: List[float], fx0: float, f_vector: List[float]):
        print(f"Iteration {iteration}:")
        print(f"Del: {Del}")
        print(f"fx0: {fx0}")
        print(f"f_vector: {f_vector}")
        print()

    def optimize(self):
        results = []

        for i in range(self.n):
            fx0 = self.function_value(self.Del)

            A = self.Del[:]
            B = self.Del[:]
            C = self.Del[:]
            D = self.Del[:]

            for j in range(self.num_vars):
                A[j] = self.variables[j][0] + self.Del[j] / 2
                B[j] = self.variables[j][0] - (self.Del[j] / 2) * (-1 if j % 2 else 1)
                C[j] = self.variables[j][0] - self.Del[j] / 2
                D[j] = self.variables[j][0] + (self.Del[j] / 2) * (-1 if j % 2 else 1)

            x_vector = [self.Del, A, B, C, D]
            f_vector = [0.0] * 5

            def calculate_function_value(k: int):
                f_vector[k] = self.function_value(x_vector[k])

            threads = []
            for k in range(5):
                thread = threading.Thread(target=calculate_function_value, args=(k,))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            min_index = np.argmin(f_vector)
            xmin = x_vector[min_index][0]

            self.Del[0] = xmin
            results.append(self.Del[:])

            self.log_iteration(i + 1, self.Del, fx0, f_vector)

            if self.norm(self.Del) <= self.epsilon:
                break

            if f_vector[min_index] == fx0:
                self.Del = [d / 2 for d in self.Del]

        print("Optimal value of x =", self.Del)
        print("Optimal value of f(x) =", self.function_value(self.Del))

        self.save_results_to_file(results)

    def save_results_to_file(self, results: List[List[float]]):
        with open("optimization_results.txt", "w") as file:
            for result in results:
                file.write(" ".join(f"{val:.6f}" for val in result) + "\n")
        print("Results saved to optimization_results.txt")

if __name__ == "__main__":
    while True:
        try:
            num_vars = int(input("Enter the number of variables: "))
            if num_vars > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    while True:
        try:
            n = int(input("Enter the number of iterations (n): "))
            if n > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    while True:
        try:
            epsilon = float(input("Enter the terminal condition (epsilon): "))
            if epsilon > 0:
                break
        except ValueError:
            print("Invalid input. Please enter a positive number.")

    optimizer = Optimizer(num_vars, n, epsilon)
    optimizer.input_variables()
    optimizer.input_deltas()
    optimizer.optimize()
