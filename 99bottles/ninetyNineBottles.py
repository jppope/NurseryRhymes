""" 99 bottles of beer on the wall. 

Demonstrates classic for loop decrement
"""

plural = ["bottle", "bottles"]

for i in range(99, 1, -1):
    print("{0:} {1:} of beer on the wall, {0:} {1:} of beer.".format(i, plural[i > 1]))
    print("Take one down, pass it around, {0:} {1:} of beer on the wall.\n".format(i - 1, plural[i - 1 > 1]))

print("1 bottle of beer on the wall, 1 bottle of beer.")
print("Take one down and pass it around, no more bottles of beer on the wall.\n")

print("No more bottles of beer on the wall, no more bottles of beer. Go to the store and buy some more, 99 bottles of beer on the wall...")