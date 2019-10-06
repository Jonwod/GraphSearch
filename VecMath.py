import math

# A set of functions for performing math operations on 2-element tuples as 2d Vectors


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def length(v):
    if not (v[0]==0 and v[1]==0):
        return math.sqrt(v[0]**2 + v[1]**2)
    else:
        return 0


def multiply(v, s):
    return v[0] * s, v[1] * s


def div(v, s):
    return v[0] / s, v[1] / s


def normal(v):
    if length(v) > 0:
        return div(v, length(v))
    else:
        return None
