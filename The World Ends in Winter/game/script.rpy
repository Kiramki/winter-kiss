# The script of the game goes in this file.

# Initialize python code here.
init python:
    # Declare the stats
    resolve = 0
    fortitude = 0
    empathy = 0

    # Declare character names
    player_name = "Stranger"

    duke_name = "The Duke"

    knight_name = "The Holy Knight"

    wizard_name = "The Wizard"

    devil_name = "The Devil"

    # Declare current week
    week = 0

    # Declare number of encounters
    wizard_encounters = 0
    knight_encounters = 0
    duke_encounters = 0

    # Check if the player is currently in the tutorial.
    tutorial_stage = 0

# Define positions
transform slight_left:
    xalign 0.25

transform slight_left_from_center:
    xalign 0.5
    linear 0.5 xalign 0.25

transform slight_right:
    xalign 0.75

# Declare the characters + sprites that will be used in the game.

define narrate = Character('Narrator')
define angel = Character('Angel')
define devil = Character('[devil_name]')
define knight = Character('[knight_name]')

define wizard = Character('[wizard_name]')
image wizard angry = "images/sprites/wizard_angry_cane.png"
image wizard concerned = "images/sprites/wizard_concerned_cane.png"
image wizard happy = "images/sprites/wizard_happy_cane.png"
image wizard neutral = "images/sprites/wizard_neutral_cane.png"
image wizard sad = "images/sprites/wizard_sad_cane.png"
image wizard love = "images/sprites/wizard_love_cane.png"

define duke = Character('[duke_name]')
image duke angry = "images/sprites/duke_angry.png"

define player = Character('[player_name]')

# The game starts here.

label start:
    # THIS IS THE HOOK
    scene black
    narrate "this is SUCH a COOL INTRODUCTION SPACE"
    narrate "WOW i am INTRODUCING EVERYTHING"
    narrate "i hope you feel INTRODUCED!!!!"

    # sprite shenanigans
    narrate "sprite shenanigans"
    show wizard happy
    wizard "I've got a weapon, and I'm..."
    show wizard concerned
    wizard "I've got a weapon, and I'm... admittedly VERY afraid to use it!"

    hide wizard

    # Pronoun menus

    narrate "tell me ur pronouns"

    menu pronouns:
        "he/him":
            $ p_subject = "he"
            $ p_object = "him"
            $ p_possessive = "his"
            $ p_possessive_adj = "his"
            $ p_reflexive = "himself"
            $ p_is = "he's"
            $ p_be = "is"

        "she/her":
            $ p_subject = "she"
            $ p_object = "her"
            $ p_possessive = "her"
            $ p_possessive_adj = "her"
            $ p_reflexive = "herself"
            $ p_is = "she's"
            $ p_be = "is"

        "they/them":
            $ p_subject = "they"
            $ p_object = "them"
            $ p_possessive = "their"
            $ p_possessive_adj = "theirs"
            $ p_reflexive = "themself"
            $ p_is = "they're"
            $ p_be = "are"

    narrate "I will now refer to you as [p_subject]."

    # Name input
    narrate "tell me ur name"
    $ player_name = renpy.input("Enter your name.").title().strip() or __("Stranger")

    # If the player doesn't enter a name, they will be referred to as "Stranger"
    if player_name == "Stranger":
        narrate "No? Alright, stranger."
    else:
        narrate "I will now refer to you as [player_name]."

    angel "what do u want in life, [player_name]"

    menu life_goals:
        "Leave my mark on the world":
            $ goal = "impact"

        "Mean something to someone":
            $ goal = "meaning"
        
        "Discover my true purpose":
            $ goal = "purpose"

        "Explore the world":
            $ goal = "exploration"

    if goal == "impact":
        angel "I see that you want to make an impact on the world."
    
    elif goal == "meaning":
        angel "I see that you want to mean something to someone."

    elif goal == "purpose":
        angel "I see that you want to discover your true purpose."

    elif goal == "exploration":
        angel "I see that you want to explore the world."

    # ooooo scene change
    scene black

    narrate "(imagine a scene change to a REALLY cool portal)"
    angel "hey this is parcae. ur gonna go here if u like. agree"
    angel "but u need to pick something to sacrifice"
        
    menu sacrifice:
        # Trust sacrifice
        "Your trust":
            $ fortitude = 10
            $ empathy = 20
            $ resolve = 5

        # Courage sacrifice
        "Your courage":
            $ fortitude = 5
            $ empathy = 10
            $ resolve = 20

        # Honesty
        "Your honesty":
            $ fortitude = 20
            $ empathy = 5
            $ resolve = 10

    narrate "Your current stats are:\nFortitude: [fortitude]\nEmpathy: [empathy]\nResolve: [resolve]"

    angel "very good :) now kiss me lol"

    narrate "(kissing scene)"

    devil "HAHA FUCK YOU"

    narrate "(dying scene)"

    jump event_0_start

label day_start:
    $ week += 1
    narrate "you are now in the day_start label"
    narrate "It is currently week [week]."

    show screen map
    window hide

    pause

label day_end:
    narrate "you are now in the day_end label. on certain weeks you might have a dream sequence or a main event."

