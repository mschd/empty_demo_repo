"""Command-line interface for prime factorization."""

import sys
from .factorizer import prime_factorize

def main():
    """Run the prime factorization CLI."""
    if len(sys.argv) != 2:
        print("Usage: python -m prime_factorizer.cli <positive_integer>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
        factors = prime_factorize(number)
        
        # Print each factor on a new line as specified in the requirements
        for factor in factors:
            print(factor)
            
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()