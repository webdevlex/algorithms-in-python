"""
Question: There are three ants on different vertices of a triangle. What is the probability of
collision (between any two or all of them) if they start walking on the sides of the triangle? Assume
that each ant randomly picks a direction, with either direction being equally likely to be chosen, and
that they walk at the same speed.
Similarly, find the probability of collision with n ants on an n-vertex polygon.

-- 3 Ants --
P(1L) and P(1R) and P(2R) = (1/2) * (1/2) * (1/2) = 1/8
P(1L) and P(1R) and P(3R) = (1/2) * (1/2) * (1/2) = 1/8
P(1L) and P(2R) and P(3R) = (1/2) * (1/2) * (1/2) = 1/8
P(2L) and P(3L) and P(1R) = (1/2) * (1/2) * (1/2) = 1/8
P(2L) and P(2R) and P(3R) = (1/2) * (1/2) * (1/2) = 1/8
P(3L) and P(1R) and P(3R) = (1/2) * (1/2) * (1/2) = 1/8
(1/8) * 6 = 6/8 = 3/4 = 75%

P(1L) and P(2L) and P(3L) = (1/2) * (1/2) * (1/2) = 1/8
P(1R) and P(2R) and P(3R) = (1/2) * (1/2) * (1/2) = 1/8
(1/8) * 2 = 2/8 = 1/4 = 25%

-- Generalized --
Given n ants there will be 2^n combinations
Only 2 of those will ever have no collisions (when they all go in the direction)
So the probability there will be a collision is

P(collision) = (2^n - 2)/2^n
"""
