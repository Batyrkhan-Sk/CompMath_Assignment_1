import math
TOL = 0.001
NMAX = 8

def bisection(a, b):
    i = 1
    c = (a + b) / 2.0

    while i < NMAX:
        print(f"Iteration {i}: a = {a:.6f}, b = {b:.6f}, c = {c:.6f}, f(c) = {f(c):.6f}")

        if abs(f(c)) < TOL:
            print(f"Root found at c = {c:.6f}")
            return c
        if math.copysign(1, f(c)) == math.copysign(1, f(a)):
            a = c
        else:
            b = c

        c = (a + b) / 2.0
        i += 1

    print("Maximum iterations reached.")
    return c

def f(x):
    return math.exp(x) - x**2

a = -2
b = 0
root = bisection(a, b)
print(f"Approximate root: {root:.6f}")
    


