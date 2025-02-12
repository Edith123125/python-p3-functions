#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

def add(num1, num2):
    return num1 + num2  

def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2

# Call functions 
greet_programmer()
greet("Edith")
greet_with_default()
print(add(10, 5))  
print(halve(8))
print(halve("wrong input"))
