"""Tests for the prime factorization functionality."""

import pytest
from prime_factorizer.factorizer import prime_factorize

def test_prime_factorize_basic():
    """Test basic prime factorization."""
    assert prime_factorize(12) == [2, 2, 3]
    assert prime_factorize(13) == [13]
    assert prime_factorize(24) == [2, 2, 2, 3]

def test_prime_factorize_edge_cases():
    """Test edge cases for prime factorization."""
    assert prime_factorize(1) == []
    assert prime_factorize(2) == [2]
    assert prime_factorize(4) == [2, 2]

def test_prime_factorize_large_number():
    """Test prime factorization with a larger number."""
    assert prime_factorize(9973) == [9973]  # A prime number
    assert prime_factorize(9975) == [3, 5, 5, 7, 19]  # 3 * 5 * 5 * 7 * 19 = 9975

def test_prime_factorize_invalid_input():
    """Test that invalid inputs raise appropriate exceptions."""
    with pytest.raises(ValueError):
        prime_factorize(0)
    
    with pytest.raises(ValueError):
        prime_factorize(-5)
    
    with pytest.raises(ValueError):
        prime_factorize(3.14)
    
    with pytest.raises(ValueError):
        prime_factorize("12")