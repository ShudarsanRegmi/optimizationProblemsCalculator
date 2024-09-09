import math

def f(x):
  if x == 0:
    return 0.65 - 0.75 
  else:
    return 0.65 - 0.75/(1 + x**2) - 0.65 * math.atan(1/x)

def secant_method(f, x0, x1, epsilon):
  """
  Finds the root of a function using the secant method.

  Args:
    f: The function to find the root of.
    x0: The initial guess for the root.
    x1: The second initial guess for the root.
    epsilon: The tolerance for the root.

  Returns:
    The approximate root of the function.
  """
  x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
  while abs(x2 - x1) > epsilon:
    x0 = x1
    x1 = x2
    x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
  return x2

x0 = -0.1
x1 = 0.0
epsilon = 0.01
minimum = secant_method(f, x0, x1, epsilon)
print(minimum) 
