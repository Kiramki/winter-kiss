# This file is meant to contain the encounters with the Knight that the player has when they visit their location on the map.

label knight_check:
    scene knight_bg_large
    hide screen map with Dissolve(0.5)

    narrate "{i}You make your way to wherever the knight is.{/i}"

    knight "HIII HIIIIIIII"

    narrate "{i}Should I spend time with the Knight?{/i}"
    menu knight_menu:
        "Yes":
            jump knight_encounter_1
        "No":
            narrate "{i}You decide to leave the Knight's place.{/i}"
            show screen map with Dissolve(0.5)
            pause

label knight_encounter_1:
    narrate "This is the first knight encounter."