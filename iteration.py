def g(x):
    return (x + 1) ** (1/3)

def fixed_point_iteration(g, x0):
    TOL = 0.001
    NMAX = 100
    x = x0
    for i in range(NMAX):
        x_new = g(x)
        print(f"Iteration {i+1}: x = {x_new:.3f}")
        if abs(x_new - x) < TOL:
            print(f"Converged to {x_new:.3f} after {i+1} iterations.")
            return round(x_new, 3)
        x = x_new
    print("Max iterations reached.")
    return x


x0 = 1.5

result = fixed_point_iteration(g, x0)
