"""Module for prime factorization functionality."""

def prime_factorize(n):
    """
    Perform prime factorization of a positive integer.
    
    Args:
        n (int): A positive integer to factorize
        
    Returns:
        list: A list of prime factors of n
        
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 1:
        return []  # 1 has no prime factors
    
    factors = []
    
    # Check for factor 2 first
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Check for odd factors
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2  # Only check odd numbers
    
    # If n is a prime number greater than 2
    if n > 1:
        factors.append(n)
    
    return factors