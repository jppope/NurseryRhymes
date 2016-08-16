""" Baa, baa, black sheep,
    Have you any wool?
    Yes, sir, yes, sir,
    Three bags full;
    One for my master,
    And one for my dame,
    and one for the little boy
    Who lives down the lane.
"""

import logging
logging.basicConfig(level=logging.INFO)

woolOwners = []
woolOwners.append(("master", "one"))
woolOwners.append(("dame", "one"))
woolOwners.append(("little boy", "one"))

whereHeLives = "down the lane"

def haveYouAnyWool():
    totalBags = 0
    for i in woolOwners:
        logging.debug(i)
        totalBags += 1
    return totalBags

bags = haveYouAnyWool()


def baabaaBlackSheep():
    print("BaaBaa BlackSheep have you any wool?")
    if bags > 0:
        print("yes sir, yes sir " + str(bags) + " bags full");
    else:
        logging.debug("error: bags should be greater than 0");

baabaaBlackSheep()

def oneForMy():
    for person, _ in woolOwners[:2]:
        print("one for my " + person)

oneForMy();

boy = woolOwners[2]
littleBoy = boy[0]

print("one for the " + littleBoy + " that lives " + whereHeLives);