
```
Maximize: Z = 40x1 + 30x2
Subject to: x1 + x2 <= 12
2x1 + x2 <= 16
x1 >= 0, x2 >= 0
Solution: Z = 400 @ x1 = 4 and x2 = 8
```

```
Maximize: Z = 12x1 + 3x2 + x3
Subject to: 10x1 + 2x2 + x3 <= 100
7x1 + 3x2 + 2x3 <= 77
2x1 + 4x2 + x3 <= 80
x1 >= 0, x2 >= 0, x3 >= 0
```

```
Minimize:
Z = -4x1 - x2 - 3x3 - 5x4
Subject to:
4x1 - 6x2 - 5x3 - 4x4 >= -20
-3x1 - 2x2 + 4x3 + x4 <= 10
-8x1 - 3x2 + 3x3 + 2x4 <= 20
x1, x2, x3, x4 >= 0
This is not optimizable due to not having positive ratio in the second iteration
```

```
# Dual Simplex Method
Find solution using dual-simplex method
MAX Z = -2x1 - x2
subject to
-3x1 - x2 <= -3
-4x1 - 3x2 <= -6
-x1 - 2x2 <= -3
and x1,x2 >= 0
https://cbom.atozmath.com/example/CBOM/Simplex.aspx?q=ds&q1=E1
```

```
# Two Phase Method Problem
MIN Z = x1 + x2
subject to
2x1 + x2 >= 4
x1 + 7x2 >= 7
and x1,x2 >= 0
```

```
# Fibonacci Search
F(X) = X**2
Int: [-5, 15]

Minimize: 0.05674 
```
![image](https://github.com/user-attachments/assets/d96aa608-b608-451b-8920-afc19ba837f0)

# Secant method

```
f(x) = x**3 - x - 1
x0 = 1, x1 = 2
x6=1.32471
∴f(x6)=f(1.32471)=-0.00004
```
https://atozmath.com/example/CONM/Bisection.aspx?q=se&q1=E1

# Interval Halving Method

### Problem 1
```
f(x) = x * (x - 1.5)
Optimal Point: 0.75
Optimal Value: -0.5625
```


### Problem 2
```
x**3 - 6*x**2 + 4*x + 12
Interval: [-2, 6]
---
Given Accuracy: 10%
n >=7
-- 
Optimal Point = 3.65625
Optimal Value = -4.70663
```

### Problem 3
```
f(x) = x**2 + 54/x
a = 2.5
b = 4.5
Optimal Value: 27
Optimal Point: 3
```
