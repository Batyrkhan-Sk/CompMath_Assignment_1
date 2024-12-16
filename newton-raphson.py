import math

def newton_raphson_method(func, func_prime, x0, TOL, NMAX):
    for i in range(1, NMAX + 1):
        f_x = func(x0)
        f_prime_x = func_prime(x0)

        if abs(f_prime_x) < 1e-10:  
            return None

        x1 = x0 - f_x / f_prime_x
        print(f"Iteration {i}: x1 = {x1:.3f}")

        if abs(x1 - x0) < TOL:
            print(f"Root found: {x1:.3f}")
            return x1

        x0 = x1

    return None


def f1(x):
    return math.exp(-x) - x

def f1_prime(x):
    return -math.exp(-x) - 1

root1 = newton_raphson_method(f1, f1_prime, 0.5, 0.001, 100)
print(f"Approximate root for e^-x - x = 0: {root1:.3f}" if root1 else "Root not found.")

def f2(x):
    return x**3 + x**2 + x + 7

def f2_prime(x):
    return 3*x**2 + 2*x + 1

root2 = newton_raphson_method(f2, f2_prime, -2, 0.001, 100)
print(f"Approximate root for x^3 + x^2 + x + 7 = 0: {root2:.3f}" if root2 else "Root not found.")

def f3(x):
    return math.cos(x) - x * math.exp(x)

def f3_prime(x):
    return -math.sin(x) - math.exp(x) - x * math.exp(x)

root3 = newton_raphson_method(f3, f3_prime, 0, 0.001, 100)
print(f"Approximate root for cos(x) - x e^x = 0: {root3:.3f}" if root3 else "Root not found.")

def f4(x):
    return x**3 - x - 1

def f4_prime(x):
    return 3*x**2 - 1

root4 = newton_raphson_method(f4, f4_prime, 1.5, 0.001, 100)
print(f"Approximate root for x^3 - x - 1 = 0: {root4:.3f}" if root4 else "Root not found.")

def f5(x):
    return x - math.cos(x)

def f5_prime(x):
    return 1 + math.sin(x)

root5 = newton_raphson_method(f5, f5_prime, 0.5, 0.001, 100)
print(f"Approximate root for x - cos(x) = 0: {root5:.3f}" if root5 else "Root not found.")
