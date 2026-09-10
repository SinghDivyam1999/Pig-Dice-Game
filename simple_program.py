# simple_program.py

import math
import random

def main():
    # Greeting
    print("Hello, Divyam! Welcome to Python.")

    # Demonstrate math module
    number = 16
    sqrt_value = math.sqrt(number)
    print(f"The square root of {number} is {sqrt_value}")

    # Demonstrate random module
    random_numbers = [random.randin(1, 100) for _ in range(5)]
    print(f"Here are 5 random numbers between 1 and 100: {random_numbers}")

    # Do a small calculation
    total = sum(random_numbers)
    average = total / len(random_numbers)
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")

if __name__ == "__main__":
    main()
