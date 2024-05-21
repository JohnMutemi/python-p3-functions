#!/usr/bin/env python3
                  
def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

greet_with_default("Sunny")

def add(num1, num2):
    return num1+ num2

result_add=add(45,55)
print(result_add)

def halve(number):
    return number/2

result_halve=halve(100)
print(result_halve)