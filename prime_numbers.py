"""
Example of Generating prime numbers
"""


_list = range(1,50)

for prim in range(2,8):
    _list = filter(lambda x: x == 1 or x%prim, _list)

print _list

