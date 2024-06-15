# Collecting coefficients a, b, and c
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))
import numpy as np

def calculate_y(a, b, c, x_values):
    return a * x_values**2 + b * x_values + c

x_values = np.linspace(-10, 10, 400)
y_values = calculate_y(a, b, c, x_values)
import matplotlib.pyplot as plt

plt.plot(x_values, y_values, label=f'{a}x^2 + {b}x + {c}')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.title('Quadratic Equation Graph')
plt.xlabel('x')
plt.ylabel('y')

# Highlighting the vertex
vertex_x = -b / (2 * a)
vertex_y = calculate_y(a, b, c, vertex_x)
plt.scatter([vertex_x], [vertex_y], color='red')
plt.legend()
plt.show()