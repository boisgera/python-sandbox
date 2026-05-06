"""
The module provides a single function `is_prime` that tests if an integer is a **prime number**.

Reference: [prime number](https://en.wikipedia.org/wiki/Prime_number)
"""

import sys

def is_prime(n: int) -> bool:
    """
    Test if `n` is prime.
        
    ### Use case

        >>> is_prime(100)
        False
        >>> is_prime(7)
        True

    En cours de test ! 🚧
        
        >>> is_prime(1)
        False
        >>> is_prime(2)
        True

    A `ValueError` is raised if `n` is negative.
        
        >>> is_prime(-1)  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        ValueError: ...
    """
    if n < 0:
        raise ValueError("n should be positive.")
    if n == 1:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False 
    return True

def main():
    n = int(sys.argv[1])
    p = is_prime(n)
    if p:
        print(f"✅ {n} is prime.")
    else:
        print(f"❌ {n} is not prime.")

if __name__ == "__main__":
    main()