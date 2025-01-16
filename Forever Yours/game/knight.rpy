# This file is meant to contain the encounters with the Knight that the player has when they visit their location on the map.

label knight_check:
    scene knight_bg_large
    hide screen map with Dissolve(0.5)

    narrate "{i}You make your way to wherever the knight is.{/i}"

    knight "HIII HIIIIIIII"

    narrate "{i}Should I spend time with the Knight?{/i}"
    menu knight_menu:
        "Yes":
            jump knight_encounter_0
        "No":
            narrate "{i}You decide to leave the Knight's place.{/i}"
            show screen map with Dissolve(0.5)
            pause

label knight_encounter_0:
    player "hi knighttttt"
    knight "omg hey..... im like so glad that u came to see me i was like. kind of worried you were just gonna like forget about me and run off and like die or something"
    narrate "ok im not writing all that"
    narrate "u recruit the knight and stuff. next ur PRETTY sure u gotta go meet a mage....."
    narrate "better get on it"

    $ knight_available = False
    $ mage_available = True
    show screen map with Dissolve(0.5)
    hide window
    pause