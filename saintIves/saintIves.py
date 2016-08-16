""" St. Ives Rhyme 
"As I was going to St. Ives
I met a man with seven wives,
Each wife had seven sacks,
each sack had seven cats,
Each cat had seven kits:
kits, cats, sacks and wives,
How many were going to St. Ives?"
"""

def Ives(narrators):
    """ Solves riddle with list comprehensions
    """
    people = ["men", "wives", "sacks", "cats", "kittens"]
    people = [7**i for i in range(len(people))]
    
    personsMet = sum(people)
    print("There were " + str(personsMet) + " total people in that guy's posse.")

    if narrators == 1:
        print("But I was the only one going to St. Ives.")

    else:
        print("you watched 'Die Hard with a Vengance' didn't you?")

Ives(1)