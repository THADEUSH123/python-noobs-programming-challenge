# Write a function fib() that a takes an integer nn and returns the nnth fibonacci ↴ number.
# Let's say our fibonacci series is 0-indexed and starts with 0. So:
#
# fib(0) # => 0
# fib(1) # => 1
# fib(2) # => 1
# fib(3) # => 2
# fib(4) # => 3
# ...

prev_values = {0: 0, 1: 1}


def prepopulate(biggest_n):
    """Prepopulated memoized values to largest integer encountered."""
    for n in range(biggest_n):
        prev_values[n] = fib(n)


def fib(n):
    """Return fib value for that iteration."""
    if n not in prev_values:
        prev_values[n] = fib(n-2) + fib(n-1)
    return prev_values[n]


prepopulate(11000)
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(10))
print(fib(11))
print(fib(110))
print(fib(110))
print(fib(110))
print(fib(110))
print(fib(111))
print(fib(112))
print(fib(110))
print(fib(11000))
