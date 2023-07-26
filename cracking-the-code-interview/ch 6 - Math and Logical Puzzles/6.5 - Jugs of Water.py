"""
Question: You have a five-quart jug, a three-quart jug, and an unlimited supply of water (but
no measuring cups). How would you come up with exactly four quarts of water? Note that the jugs
are oddly shaped, such that filling up exactly "half" of the jug would be impossible.


If we just play with the jugs, we'll find that we can pour water
back and forth between them as follows:

+---------+---------+---------------------------------------+
| 5-quart | 3-quart |                 Action                |
+---------+---------+---------------------------------------+
|    5    |    0    |        Filled 5-quart jug.            |
+---------+---------+---------------------------------------+
|    2    |    3    | Filled 3-quart with 5-quart's contents. |
+---------+---------+---------------------------------------+
|    2    |    0    |            Dumped 3-quart.            |
+---------+---------+---------------------------------------+
|    0    |    2    | Fill 3-quart with 5-quart's contents.  |
+---------+---------+---------------------------------------+
|    5    |    2    |         Filled 5-quart.                |
+---------+---------+---------------------------------------+
|    4    |    3    |   Fill remainder of 3-quart with       |
|         |         |             5-quart.                   |
+---------+---------+---------------------------------------+
|    4    |         |       Done! We have 4 quarts.          |
+---------+---------+---------------------------------------+
"""
