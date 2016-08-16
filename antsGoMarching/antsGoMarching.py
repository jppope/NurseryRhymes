""" The Ants Go Marching
"""

littleOne = []
howTheyMarch = ["one by one", "two by two", "three by three", "four by four", "five by five",
                "six by six", "seven by seven", "eight by eight", "nine by nine", "ten by ten"];
actions = ["suck her thumb", "tie his shoe", "climb a tree", "shut the door", "take a dive",
         "pick up sticks", "pray to heaven", "roll a skate", "check the time", "shout \"The End!\""]


for action in actions:
    littleOne.append("The little one stops to " + action)


def howManyByHowMany(number):
    numbers = howTheyMarch[number]
    hurrah = ", hurrah, hurrah\n"
    march = "The ants go marching " + numbers
    print(march + hurrah + march + hurrah + march);


def theAntsGoMarching():
    for i in range(len(howTheyMarch)):
        howManyByHowMany(i)
        print(littleOne[i])
        print("And they all go marching down to the ground to get out of the rain, BOOM! BOOM! BOOM!\n")

theAntsGoMarching();