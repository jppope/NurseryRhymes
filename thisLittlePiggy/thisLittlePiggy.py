"""
This little piggy went to market.
This little piggy stayed home.
This little piggy had roast beef.
This little piggy had none.
This little piggy cried, "Wee, wee, wee, wee."
All the way home.
"""

from random import shuffle
whatPiggyDid = ["went to market", "stayed home", "had roast beer",
                "had none", "cried 'wee wee wee wee'... All the way home"]


def this_little_piggy(random=False):
    if random:
        shuffle(whatPiggyDid)

    for i in range(len(whatPiggyDid)):
        print("This little piggy " + whatPiggyDid[i])

this_little_piggy()

print()

this_little_piggy(random=True)