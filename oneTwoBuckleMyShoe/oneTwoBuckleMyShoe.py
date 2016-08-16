
""" One two buckle my shoe
    One two buckle my shoe
    Three, four, knock at the door
    Five, six, pick up sticks
    Seven, eight, lay them straight
    Nine, ten, a big fat hen
    Eleven, twelve, dig and delve
    Thirteen, fourteen, maids a-courting
    Fifteen, sixteen, maids in the kitchen
    Seventeen, eighteen, maids in waiting
    Nineteen, twenty, my plate's empty
"""

activities = ["buckle my shoe", "knock at the door", "pick up sticks",
              "lay them straight", "a big fat hen", "dig and delve",
              "maids a-courting", "maids in the kitchen", 
              "maids in waiting","my plate's empty"]
counter = 0

for i in range(1, 21):
    if (i % 2 == 0):
        print(str(i), end=", ")
        print(activities[counter])
        counter += 1
 
    else:
        print(str(i), end=", ")