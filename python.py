#!/usr/bin/env python3
# simple_program.py

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

def main():
    print("Simple Python Program")
    num1 = 5
    num2 = 7
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is {result}")

if __name__ == "__main__":
    main()