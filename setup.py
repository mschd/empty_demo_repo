"""Setup script for the prime factorizer package."""

from setuptools import setup, find_packages

setup(
    name="prime_factorizer",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "prime_factorize=prime_factorizer.cli:main",
        ],
    },
    python_requires=">=3.6",
)