import numpy as np
from scipy.optimize import minimize

def f(values):
    x, y = values
    return (x - 2)**2 + (y - 2)**2

initial_guess = [0, 0]

result = minimize(f, initial_guess)
print("Optimization Result\n")
print("Minimum value =", result.fun)
print("x =", result.x[0])
print("y =", result.x[1])
