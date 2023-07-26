"""
Question: A bunch of people are living on an island, when a visitor comes with a strange
order: all blue-eyed people must leave the island as soon as possible. There will be a flight out at
8:00pm every evening. Each person can see everyone else's eye color, but they do not know their
own (nor is anyone allowed to tell them). Additionally, they do not know how many people have
blue eyes, although they do know that at least one person does. How many days will it take the
blue-eyed people to leave?

Let's apply the Base Case and Build approach. Assume that there are n people
on the island, and c of them have blue eyes. We are explicitly told that c > 0.

Case c = 1: Exactly one person has blue eyes.
Assuming all the people are intelligent, the person with blue eyes should look
around and realize that no one else has blue eyes. Since they know that at least
one person has blue eyes, they must conclude that it is themselves who have blue
eyes. Therefore, they would take the flight that evening.

Case c = 2: Exactly two people have blue eyes.
The two blue-eyed people see each other but are unsure whether c is 1 or 2.
They know, from the previous case, that if c = 1, the person with blue eyes would
leave on the first night. Therefore, if the other blue-eyed person is still there,
they must deduce that c = 2, which means that they themselves have blue eyes. Both
individuals would then leave on the second night.

Case c > 2: The General Case.
As we increase c, we can see that this logic continues to apply. If c = 3,
then those three people will immediately know that there are either 2 or 3 people
with blue eyes. If there were two people, then those two people would have left on
the second night. So, when the others are still around after that night, each person
would conclude that c = 3 and that they, therefore, have blue eyes too. They would
leave that night.

This same pattern extends up through any value of c. Therefore, if c people have blue
eyes, it will take c nights for the people with blue eyes to leave. All will leave on
the same night.
"""
