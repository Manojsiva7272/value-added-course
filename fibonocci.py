def fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage:
num_of_terms = 25
series = fibonacci_series(num_of_terms)
print(f"The first {num_of_terms} terms of the Fibonacci series are:")
print(series)

