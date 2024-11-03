import numpy as np


def backtracking_line_search(f, grad_f, x, d, alpha, epsilon=0.1, eta=0.5):
    # Define the function phi(alpha_k)
    phi = lambda alpha_k: f(x + alpha_k * d)
    
    # Compute the directional derivative of phi at alpha = 0
    phi_diff = grad_f(x).dot(d)
    
    # Compute the initial value of phi
    phi_0 = f(x)
    
    # Backtracking line search loop
    while True:
        # Update alpha
        alpha *= eta
        
        # Check the Armijo condition and the curvature condition (Armijo-Goldstein condition)
        if phi(alpha) <= phi_0 + epsilon * alpha * phi_diff \
        and \
        phi(alpha) >= phi_0 + eta * alpha * phi_diff:
            break
    
    return alpha


def optimize_function(f, grad_f, x0, d, initial_alpha=100, epsilon=0.1, eta=0.5, max_iter=100, tol=1e-6):
    x = x0
    for _ in range(max_iter):
        direction = d
        
        # Perform backtracking line search to find a suitable step size
        alpha = backtracking_line_search(f, grad_f, x, direction, initial_alpha, epsilon, eta)
        
        # Update the current point
        x_new = x + alpha * direction
        
        # Print the current step size and the new point
        print("alpha: ", alpha)
        print("x_new: ", x_new)
        
        # Check for convergence
        if abs(f(x_new) - f(x)) < tol:
            break
        
        x = x_new
    
    return x


def test_fuction(x: np.ndarray) -> np.ndarray:
    return np.sin(x)

def grad_test_fuciton(x: np.ndarray) -> np.ndarray:
    return np.cos(x)


# Initial point
x0 = np.array([0])
d = np.array([-8])
initial_alpha = 1000

# Optimize the test function
result = optimize_function(test_fuction, grad_test_fuciton, x0, d, initial_alpha)

print("Optimal solution:", result)
print("Optimal value:", test_fuction(result))