#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    print(num1 + num2)

def halve(number):
    if not isinstance(number, (int, float)):  # Ensure it's a number
        return None  # Python uses None instead of null
    return number / 2
greet_programmer()
greet("Edith")
greet_with_default()
add(10, 5)
print(halve(8))  # Use print() to display return values
print(halve("wrong input"))  # Test invalid input