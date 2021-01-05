# optimizable
A small Python module containing functions to be used in SciPy's curve-fit, as well as preprocessing functions to avoid divide-by-zero errors

Section A: Fit functions

1 - standardHyperbola - typical differentiable hyperbola of form b/a*n + c. Will generally need to preprocess X and Y data to avoid divide-by-zero errors (see Section B)
2 - linear1 - a one-term linear function. Requires X in R1
3 - linear2 - a two-term linear function. Requires X in R2
4 - linear3 - a three-term linear function. Requires X in R3
5 - linear4 - a four-term linear function. Requires X in R4
6 - exp1 - a one-term exponential function. Requires X in R1
7 - exp2 - a two-term exponential function. Requires X in R2
8 - p1t4 - a five-term function with one power term and four linear terms. Requires X in R5
9 - p2t4 - a six-term function with two power terms and four linear terms. Requires X in R6
10 - e1t4 - p1t4, but with the natural exponent. Requires X in R5
11 - e2t4 - p2t4, but with the natural exponent. Requires X in R6

Section B: Preproccessing functions

1 - preprocess1 - Takes a list of X values and a substitute value. If an x in X is 0, substitutes the value, otherwise keeps list the same.
2 - preprocessInt1 - Same logic as preprocess1, but for a single value.
3 - preprocess2 - Offsets all X by a set amount for the hyperbola fit, which can be undone for predictions.

Note that preprocess1 typically works best if the part of the hyperbola near the y-axis fits the data best, while preprocess2 typically works best if the part of the hyperbola near the x-axis fits the data best.

Section C: Other functions

1 - getNaturalExponent - returns the value of the natural exponent used in this module, which in the present version is the first 25 digits of the natural exponent.

Version 1.0
