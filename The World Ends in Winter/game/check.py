'''Pick a number needed to guarantee success: e.g. 50 (call this difficulty)

Roll a number between 1 and the number required: e.g. 1 and 50

The roll needed to succeed is a roll equal to or lower than your stat being checked
    e.g. The difficulty of a Fortitude check is 50. Your current Fortitude stat is 40. 
        You will need to roll a 40 or lower to succeed - you have an 80% chance of success.'''

import random

def skill_check(difficulty, stat):
    roll = random.randint(1, difficulty)
    if roll <= stat:
        return True
    else:
        return False
    
