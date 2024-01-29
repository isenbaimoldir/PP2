print(6 | 2 + 1)

"""
Bitwise OR has a lower precedence than addition, and we need to calculate the addition first.
The calculation above reads 6 | 3 = 7

More explanation:
The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 000000000000011"""