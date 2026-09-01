from scipy.integrate import quad
def f(x):
    return x**3 + 2*x**2 + x + 1

x = 2
h = 1e-6

d = (f(x + h) - f(x - h)) / (2 * h)
print("Function: f(x) = x^3 + 2x^2 + x + 1")
print("\nNumerical Differentiation")
print("Derivative at x =", x)
print("f'(x) =", d)

lower_limit = 0
upper_limit = 2

integral = quad(f, lower_limit, upper_limit)

print("\nNumerical Integration")
print("Integration limits:", lower_limit, "to", upper_limit)
print("Integral =", integral[0])
