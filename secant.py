import math

def secant_method(func, x0, x1, TOL, NMAX):
    for i in range(1, NMAX + 1):
        f_x0 = func(x0)
        f_x1 = func(x1)
        
        if abs(f_x1 - f_x0) < 1e-10:
            return None

        x2 = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        print(f"Iteration {i}: x2 = {x2:.3f}")

        if abs(x2 - x1) < TOL:
            print(f"Root found: {x2:.3f}")
            return x2

        x0, x1 = x1, x2

    return None

def f1(x):
    return math.exp(-x) - x

root1 = secant_method(f1, 0, 1, 0.001, 100)
print(f"Approximate root for e^-x - x = 0: {root1:.3f}" if root1 else "Root not found.")

def f2(x):
    return x**3 + x**2 + x + 7

root2 = secant_method(f2, -2, -1, 0.001, 100)
print(f"Approximate root for x^3 + x^2 + x + 7 = 0: {root2:.3f}" if root2 else "Root not found.")

def f3(x):
    return x**2 + 4 * math.sin(x)

root3 = secant_method(f3, -1, -1.2, 0.001, 100)
print(f"Approximate root for x^2 + 4sin(x) = 0: {root3:.3f}" if root3 else "Root not found.")

def f4(x):
    return math.cos(x) - x * math.exp(x)

root4 = secant_method(f4, 0, 0.5, 0.001, 100)
print(f"Approximate root for cos(x) - x e^x = 0: {root4:.3f}" if root4 else "Root not found.")

def f5(x):
    return x**3 - x - 1

root5 = secant_method(f5, 1, 2, 0.001, 100)
print(f"Approximate root for x^3 - x - 1 = 0: {root5:.3f}" if root5 else "Root not found.")

def f6(x):
    return x - math.cos(x)

root6 = secant_method(f6, 0.5, 1, 0.001, 100)
print(f"Approximate root for x - cos(x) = 0: {root6:.3f}" if root6 else "Root not found.")
