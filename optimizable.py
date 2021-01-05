# -*- coding: utf-8 -*-
"""

Optimizable forms module, to enable curve-fitting in SciPy

1 - standardHyperbola - typical differentiable hyperbola of form b/a*n + c
1b - preprocessing methods - in order to run a standard hyperbola in curve_fit,
you will need to process your x vector to eliminate divide by zero errors. Two
methods are provided. preprocess1 is a numerical analysis inspired method that
substitutes zero for an arbitrarily close value, while preprocess2 shifts your
entire x vector by a specified amount. Which one you choose to use will depend
upon which aspect of the hyperbola fits your data the best: the finite
conversion upon the x-axis, or the asymptotic conversion upon the y-axis. If
the former, use the offset method (preprocess2). If the latter, use the
numerical analysis method and step your substitute up to get closer and closer
to a perfect approximation of asymptotic behavior (preprocess1).

Created on Fri Sep 25 09:58:03 2020

@author: Alexander Fretheim
"""

#hyperbola section:

def standardHyperbola(x, a, b):
    return (a/x)+b

#preprocess functions converts x to form that won't divide by zero. Two are available:

#preprocess 1 converts zero in to a value near zero, and is most useful if the near y-axis part of the distribution fits the data well:
def preprocess1(X, zrSub):
    ret = [];
    for x in X:
        if x == 0:
            ret.append(zrSub);
        else:
            ret.append(x);
    return ret;

def preprocessInt1(x, zrSub):
    if x != 0:
        return x;
    else:
        return zrSub;

#preporcess 2 offsets your x by a stated amount, and is most ueful if the mid and right portions of the hyperbola fit the data the best:
def preprocess2(X, offset):
    ret = [];
    for x in X:
            ret.append(x + offset);
    return ret;

#end hyperbola section.

#Linear section:
def linear1(x, a, b):
    return a*x + b;

def linear2(X, a, b, c):
    x, y = X;
    return a*x + b*y + c

def linear3(X, a, b, c, d):
    x, y, z = X;
    return a*x + b*y + c*z + d;

def linear4(X, a, b, c, d, e):
    x1, x2, x3, x4 = X;
    return a*x1 + b*x2 + c*x3 + d*x4 + e;

def linear5(X, a, b, c, d, e, f):
    x1, x2, x3, x4, x5 = X;
    return a*x1 + b*x2 + c*x3 + d*x4 + e*x5 + f;

#pure exponential fit:
def exp(X, a, b, c):
    x1 = X;
    e = getNaturalExponent();
    return a*e**(x1*b) + c;

def exp2(X, a, b, c, d, e):
    x1, x2 = X;
    E = getNaturalExponent();
    return a*E**(x1*b) + c*E**(x2*d) + e;

#one power term and treatments - preprocess x1:

def p1t4(X, a, b, c, d, e, f, g):
    x1, x2, x3, x4, x5 = X;
    return a*x1**g + b*x2 + c*x3 + d*x4 + e*x5 + f;

def p2t4(X, a, b, c, d, e, f, g, h, i):
    x1, x2, x3, x4, x5, x6 = X;
    return a*x1**b + c*x2**d + e*x3 + f*x4 + g*x5 + h*x6 + i;

#could we build an autogenerator for semipolynomial functions?
#one exponent term and treatments - preprocess x1:
    
def e1t4(X, a, b, c, d, e, f, g):
    x1, x2, x3, x4, x5 = X;
    E = getNaturalExponent();
    return a*E**(x1*g) + b*x2 + c*x3 + d*x4 + e*x5 + f;

def e2t4(X, a, b, c, d, e, f, g, h, i):
    x1, x2, x3, x4, x5, x6 = X;
    E = getNaturalExponent();
    return a*E**(x1*b) + c*E**(x2*d) + e*x3 + f*x4 + g*x5 + h*x6 + i;

#this "function" returns an approximation of the mathematical constant e, its first 25 digits.:
def getNaturalExponent():
    return 2.71828182845904523536;