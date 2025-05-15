# Prime Factorizer

A Python library and command-line tool for prime factorization of positive integers.

## Overview

This project provides functionality to decompose any positive integer into its prime factors. Prime factorization is the process of determining which prime numbers multiply together to give the original number.

## Features

- Fast prime factorization algorithm
- Command-line interface for quick factorization
- Python API for integration into other projects
- Handles edge cases (e.g., 1 has no prime factors)
- Comprehensive error handling for invalid inputs

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/prime_factorizer.git
cd prime_factorizer

# Install the package
pip install .
```

## Usage

### Command Line Interface

After installation, you can use the command-line tool:

```bash
# Using the installed command
prime_factorize 60

# Or directly with Python
python prime_factorize.py 60
```

Both methods will output:
```
2
2
3
5
```

### Python API

You can also use the library in your Python code:

```python
from prime_factorizer.factorizer import prime_factorize

# Get prime factors as a list
factors = prime_factorize(60)
print(factors)  # Output: [2, 2, 3, 5]

# Example with a prime number
print(prime_factorize(17))  # Output: [17]

# Edge case
print(prime_factorize(1))  # Output: [] (1 has no prime factors)
```

## Error Handling

The library raises a `ValueError` for invalid inputs:
- Non-integer values
- Zero or negative integers

## Development

### Running Tests

```bash
pytest
```

## License

This project is open source and available under the [MIT License](LICENSE).
