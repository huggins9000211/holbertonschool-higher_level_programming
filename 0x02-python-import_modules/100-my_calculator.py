#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
arggs = sys.argv
opp = arggs[2]
num1 = int(arggs[1])
num2 = int(arggs[3])
if len(arggs) != 4:
    print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    exit(1)
if opp == '+':
    temp = add(num1, num2)
    print("{} {} {} = {}".format(num1, opp, num2, temp))
elif opp == '-':
    temp = sub(num1, num2)
    print("{} {} {} = {}".format(num1, opp, num2, temp))
elif opp == '*':
    temp = mul(num1, num2)
    print("{} {} {} = {}".format(num1, opp, num2, temp))
elif opp == '/':
    temp = div(num1, num2)
    print("{} {} {} = {}".format(num1, opp, num2, temp))
else:
    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)
