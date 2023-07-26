"""
Question: In the new post-apocalyptic world, the world queen is desperately concerned
about the birth rate. Therefore, she decrees that all families should ensure that they have one girl or
else they face massive fines. If all families abide by this policy-that is, they have continue to have
children until they have one girl, at which point they immediately stop-what will the gender ratio
of the new generation be? (Assume that the odds of someone having a boy or a girl on any given
pregnancy is equal.) Solve this out logically and then write a computer simulation of it.


We can work out the probability for each gender sequence.

- P(G) = 1/2.   That is, 50% of families will have a girl first. The others
                will go on to have more children.
- P(BG) = 1/4.  Of those who have a second child (which is 50%), 50% of them
                will have a girl the next time.
- P(BBG) = 1/8. Of those who have a third child (which is 25%), 50% of them
                will have a girl the next time.
And so on.

We know that every family has exactly one girl. How many boys does each
family have, on average? To compute this, we can look at the expected value
of the number of boys. The expected value of the number of boys is the
probability of each sequence multiplied by the number of boys in that
sequence.

E(x) = xi * P(xi)

Sequence | Number of Boys | Probability | Number of Boys Probability
G         | 0              | 1/2        | 0
BG        | 1              | 1/4        | 1/4
BBG       | 2              | 1/8        | 2/8
BBBG      | 3              | 1/16       | 3/16
BBBBG     | 4              | 1/32       | 4/32
BBBBBG    | 5              | 1/64       | 5/64
BBBBBBG   | 6              | 1/128      | 6/128

Or in other words, this is the sum of i to infinity of i divided by 2^i.

If you calculate this, you will see that the sum is 1. This would mean that
the gender ratio is even. Families contribute exactly one girl and, on
average, one boy. The birth policy is therefore ineffective. Does this make
sense?

At first glance, this seems wrong. The policy is designed to favor girls as it
ensures that all families have a girl.

On the other hand, the families that keep having children contribute
(potentially) multiple boys to the population. This could offset the impact of
the "one girl" policy.

One way to think about this is to imagine that we put all the gender sequences
of each family into one giant string. So if family 1 has BG, family 2 has
BBG, and family 3 has G, we would write BGBBGG.

In fact, we don't really care about the groupings of families because we're
concerned about the population as a whole. As soon as a child is born, we can
just append its gender (B or G) to the string.

What are the odds of the next character being a G? Well, if the odds of having
a boy and girl is the same, then the odds of the next character being a G is
50%. Therefore, roughly half of the string should be Gs and half should be Bs,
giving an even gender ratio.

This actually makes a lot of sense. Biology hasn't been changed. Half of
newborn babies are girls and half are boys. Abiding by some rule about when to
stop having children doesn't change this fact.

Therefore, the gender ratio is 50% girls and 50% boys.
"""
