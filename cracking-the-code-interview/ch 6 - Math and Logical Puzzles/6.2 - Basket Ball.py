# You have 20 bottles of pills. 19 bottles have 1.0 gram pills, but one has pills of weight 1.1 grams.
# Given a scale that provides an exact measurement, how would you find the heavy bottle?
# You can only use the scale once.


# Explanation

# Probability of winning Game 1:
# The probability of winning Game 1 is denoted as p.

# Probability of winning Game 2:
# Let (k, n) represent the probability of making exactly k shots out of n.
# The probability of winning Game 2 is the probability of making exactly two shots out of three OR making all three shots. In other words:
# P(winning) = s(2,3) + s(3,3)

# The probability of making all three shots is:
# s(3,3) = p^3

# The probability of making exactly two shots is:
# P(making 1 and 2, and missing 3) + P(making 1 and 3, and missing 2) + P(missing 1, and making 2 and 3)
# = p * p * (1-p) + p * (1-p) * p + (1-p) * p * p
# = 3(1-p)p^2

# Adding these together, we get:
# p^3 + 3(1 - p)p^2 = 3p^2 - 2p^3

# Which game should you play?
# You should play Game 1 if P(Game 1) > P(Game 2):
# p > 3p^2 - 2p^3

# Simplifying further:
# 1 > 3p - 2p^2
# 2p^2 - 3p + 1 > 0

# To determine the sign, both terms must be either positive or negative.
# Since p < 1, p - 1 < 0. This means both terms must be negative.

# 2p - 1 < 0
# 2p < 1
# p < 0.5

# So, we should play Game 1 if 0 < p < 0.5 and Game 2 if 0.5 < p < 1.
# If p = 0, 0.5, or 1, then P(Game 1) = P(Game 2), so it doesn't matter which game we play.
