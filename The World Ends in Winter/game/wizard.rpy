# This file is meant to contain the encounters with the Wizard that the player has when they visit their location on the map.

label wizard_check:
    scene wizard_bg_large
    hide screen map with Dissolve(0.5)

    narrate "{i}You make your way to the Wizard's tower.{/i}"

    show wizard neutral
    wizard "omg heyyyyyy :)"

    narrate "{i}Should I spend time with the Wizard?{/i}"
    menu wizard_menu:
        "Yes":
            jump wizard_encounter_1
        "No":
            narrate "{i}You decide to leave the Wizard's tower.{/i}"
            show screen map with Dissolve(0.5)
            pause

label wizard_encounter_1:
    scene 
    narrate "This is the first encounter lol"

label wizard_encounter_2:
    narrate "This is the second encounter with the Wizard."