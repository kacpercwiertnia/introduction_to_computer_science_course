import math

def derivative(x):
  return function(x+1/2) - function(x-1/2)

def function(x):
  return x**x - 2020

x = 0

while abs(function(x)) > 0.001:
  x = x - function(x)/derivative(x)


print(x)