import matplotlib.pyplot as plt
import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def lines_intersection(A: Point, B: Point, l: int) -> Point:
    t = ((A.y - B.y) - l * (A.x - B.x)) / (2 * l)
    return Point(A.x + t, A.y - t * l)


def shubert_piyavskii(f, a, b, l, epsilon, delta=0.001):
    m = (a + b) / 2  # Calculate the midpoint of the interval [a, b]

    A, M, B = Point(a, f(a)), Point(m, f(m)), Point(
        b, f(b))

    sample_points = [A, lines_intersection(A, M, l), M, lines_intersection(
        M, B, l), B]

    delta_value = float('inf')

    while delta_value > epsilon:  # Continue loop until convergence criterion is met

        # Find the index of the point with the minimum y-coordinate
        i = min(range(len(sample_points)), key=lambda i: sample_points[i].y)

        # Create a new point P based on the function evaluation
        P = Point(sample_points[i].x, f(sample_points[i].x))

        delta_value = P.y - sample_points[i].y

        # Calculate the previous intersection point
        P_prev = lines_intersection(sample_points[i - 1], P, l)

        # Calculate the next intersection point
        P_next = lines_intersection(P, sample_points[i + 1], l)

        del sample_points[i]
        sample_points.insert(i, P_next)
        sample_points.insert(i, P)
        sample_points.insert(i, P_prev)

    intervals = []

    # Calculate the starting index
    i = 2 * (sample_points[0:len(sample_points):2].index(
        min(sample_points[0:len(sample_points):2], key=lambda P: P.y)))

    j = 1
    while j < len(sample_points):

        if sample_points[j].y < sample_points[i].y:

            # Calculate the difference in y-coordinates
            dy = sample_points[i].y - sample_points[j].y

            # Calculate the lower bound of the interval
            x_lo = max(a, sample_points[j].x - dy / l)

            # Calculate the upper bound of the interval
            x_hi = min(b, sample_points[j].x + dy / l)

            # Check if intervals overlap
            if intervals and intervals[-1][1] + delta >= x_lo:
                # Update the last interval
                intervals[-1] = (intervals[-1][0], x_hi)
            else:
                intervals.append((x_lo, x_hi))
        j += 2

    return sample_points[i], intervals


# Example usage:
def test_function(x):
    return x ** 2 


a = -4  # Start of the interval
b = 4  # End of the interval
l = 8  # Lipschitz function
epsilon = 1e-4  # Convergence criterion

p, interval = shubert_piyavskii(test_function, a, b, l, epsilon)
print(p.x, p.y, interval)  # Print the minimum point and intervals

x_values = np.linspace(a, b, 100)  # Generate x-values
y_values = test_function(x_values)  # Calculate y-values

# Find minimum point using shubert_piyavskii
result = shubert_piyavskii(test_function, a, b, l, epsilon)

# Plot the function and the iterations
plt.plot(x_values, y_values, label='Function')  # Plot the function
for pt in result[1]:  # Plot the intervals
    # Plot lower bound of intervals
    plt.axvline(pt[0], color='red', linestyle='--')

    # Plot upper bound of intervals
    plt.axvline(pt[1], color='red', linestyle='--')

plt.plot(result[0].x, result[0].y, 'ro',
         label='Minimum Point')  # Plot the minimum point

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Visualization of Finding Minimum Point')
plt.legend()
plt.grid(True)
plt.show()
