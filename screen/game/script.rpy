init python:
    import clues # Import the clues module
    selected_clue = None # Create a variable to store the selected clue

define n = Character("Narrating")

label start:
    # Set up clue system
    default player_clues = {} # Reset the player clues dictionary

    n "This is a test game."
    n "Push this button to see a screen."

    show screen clue_button

    n "The button is now visible."
    n "Now you can continue."

    ## Append clue 1 to player clues
    $ player_clues['clue_1'] = clues.get_clue('clue_1')
    n "You have found a clue."

    ## Append clue 2
    $ player_clues['clue_2'] = clues.get_clue('clue_2')
    n "You have found another clue."

    ## Make sure player going back in the game will not see an updated description.
    $ player_clues['clue_1'] = clues.get_clue('clue_1')
    $ update_1 = False
    $ update_2 = False

    menu updated_clue:
        "I want to see the first update about clue 1!":
            $ update_1 = True
            jump update_run

        "I want to see the second update about clue 1!":
            $ update_2 = True
            jump update_run

        "I don't want to know about the first update anymore.":
            $ update_1 = False
            jump update_run

        "I don't want to know about the second update anymore.":
            $ update_2 = False
            jump update_run

        "I'm done!":
            jump finished

label update_run:
    python:
        if update_1 and update_2 == True:
            clues.update_clue(player_clues["clue_1"], "update 1+2")
        elif update_1 == True:
            clues.update_clue(player_clues["clue_1"], "update 1")
        elif update_2 == True:
            clues.update_clue(player_clues["clue_1"], "update 2")
        else:
            player_clues['clue_1'] = clues.get_clue('clue_1')

    jump updated_clue


label finished:
    n "Check now!"
    return