### Group:
- Ali Janloo
- Ali Alavizadeh
- Amir Ali Akhgari

# Shubert-Piyavskii Method Documentation


## Introduction
The Shubert-Piyavskii method is a global optimization technique used to find the global minimum of a function within a given interval. Unlike some other optimization methods, it can converge to the global minimum regardless of the presence of local minima or the function's shape. The method relies on the function being Lipschitz continuous, meaning it must be continuous and have an upper bound on the magnitude of its derivative.

## Lipschitz Continuity
A function $f$ is Lipschitz continuous on the interval $[a, b]$ if there exists a Lipschitz constant $\ell > 0$ such that:
$$ |f(x) - f(y)| \leq \ell |x - y| $$
for all $x, y$ in $[a, b]$. Intuitively, $\ell$ represents the largest unsigned instantaneous rate of change the function attains on the interval.

## Algorithm Overview
1. **Initialization**:
   - The method starts by sampling the midpoint of the interval.
   - It constructs a sawtooth lower bound using lines of slope $\pm \ell$ from this midpoint. These lines always lie below the function if $\ell$ is a valid Lipschitz constant.

2. **Iteration**:
   - The algorithm iteratively builds a tighter lower bound on the function.
   - It stops when the difference in height between the minimum sawtooth value and the function evaluation at that point is less than a given tolerance $\epsilon$.

3. **Uncertainty Regions**:
   - Regions where the minimum could lie are computed based on the update information.
   - An uncertainty region is computed for every peak, with contributions determined by the sawtooth lower vertices and the minimum sawtooth upper vertex.

## Output
The method returns the minimum point found and a list of intervals representing potential regions for the minimum within the given interval.

## Advantages
- Converges to the global minimum irrespective of local minima or function shape.
- Handles complex function landscapes effectively.
- Robust against local minima.

## Considerations
- Requires a valid Lipschitz constant, which may be a drawback.
- Poor performance may result from large Lipschitz constants.

## Applications
- Engineering optimization.
- Financial modeling.
- Machine learning parameter tuning.
- Scientific research.

## Conclusion
The Shubert-Piyavskii method offers a powerful approach to global optimization, **guaranteeing** convergence to the global minimum under certain conditions. By iteratively refining a lower bound on the function, it effectively navigates complex function landscapes and identifies potential regions for the minimum. While requiring knowledge of a valid Lipschitz constant, its robustness and ability to handle various function shapes make it a valuable tool in optimization problems.


### Usage
In `main.py` , you can specify function you want to minimize by modifying `test_function` and hyper-parameters like `a`, `b` and Lipschits constant `L` and convergenc criterion `epsilon`:


```python
def test_function(x):
    return -x ** 2

a = -2  
b = 2  
l = 4 
epsilon = 1e-4

```

and leave the rest as it is. then run the `main.py`:
```bash
python main.py
```