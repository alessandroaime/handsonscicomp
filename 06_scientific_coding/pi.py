#!/usr/bin/env python3
from decimal import Decimal, getcontext
from math import factorial
import random

def is_in_circle(x, y):
    return x**2 + y**2 < 1

def points_in_circle(iterations, seed):
    gen = random.Random(seed)
    in_circle_points = 0
    for _ in range(iterations):
        x = gen.uniform(0, 1)
        y = gen.uniform(0, 1)
        if is_in_circle(x, y):
            in_circle_points += 1
    return in_circle_points

def chudnovsky(precision):
    getcontext().prec = precision + 1
    C = 426880*Decimal(10005).sqrt()
    M = Decimal(1)
    L = 13591409
    s = 13591409
    X = Decimal(1)
    K = Decimal(6)

    for i in range(0, precision):
        M *= (K**3 - 16*K) / ((i + 1)**3)
        X *= 262537412640768000
        L += 545140134
        K += 12
        s += Decimal((M*L)/X)

    pi = C/s
    return pi

def monte_carlo_pi(iterations, seed):
    in_circle_points=points_in_circle(iterations, seed)
    pi = in_circle_points*4/iterations
    return pi
