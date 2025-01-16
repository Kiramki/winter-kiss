# This file is meant to contain the encounters with the Duke that the player has when they visit their location on the map.

label duke_check:
    scene duke_bg_large
    hide screen map with Dissolve(0.5)

    narrate "{i}You make your way to the Duke's fancyass house.{/i}"

    duke "Hello."

    narrate "{i}Should I spend time with the Duke?{/i}"
    menu duke_menu:
        "Yes":
            jump duke_encounter_0
        "No":
            narrate "{i}You decide to leave the Duke's FANCYASS HOUSE.{/i}"
            show screen map with Dissolve(0.5)
            pause

label duke_encounter_0:
    player "haha hey im here to recruit you for the-"
    duke "no u are not. frankly i dont think u need my help"
    player "but"
    narrate "(recruitment noises)"

    duke "FINE. i guess. ill entertain u."
    player "(THANK GOD)"

    $ duke_available = True
    $ mage_available = True
    $ knight_available = True

    scene black with Dissolve(0.5)
    jump event_1_start