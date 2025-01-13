# This file is meant to contain the encounters with the Wizard that the player has when they visit their location on the map.

label wizard_check:
    scene wizard_bg_large
    hide screen map with Dissolve(0.5)

    narrate "{i}You make your way to [wizard_name]'s tower.{/i}"

    show wizard neutral
    wizard "omg heyyyyyy :)"

    narrate "{i}Should I spend time with [wizard_name]?{/i}"
    menu wizard_menu:
        "Yes":
            # First encounter
            if wizard_encounters == 0:
                jump wizard_encounter_1

            # Second encounter
            elif wizard_encounters == 1:
                jump wizard_encounter_2

            # Third encounter
            elif wizard_encounters == 2:
                jump wizard_encounter_3

            # Fourth encounter
            elif wizard_encounters == 3:
                jump wizard_encounter_4

            # Fifth encounter
            elif wizard_encounters == 4:
                jump wizard_encounter_5

            # Subsequent encounters
            else:
                jump idle_wizard
        "No":
            narrate "{i}You decide to leave the Wizard's tower.{/i}"
            show screen map with Dissolve(0.5)
            pause

label wizard_encounter_1:
    scene black with Dissolve(0.5)
    narrate "ur prophecy says that you gotta be recruiting some like, wizard guy right now. better get on that"
    
    scene wizard_bg_1 with Dissolve(0.5)
    narrate "Well. This place looks. Wizard-y"

    show wizard neutral with Dissolve(0.5)
    wizard "hello........ what are u doing in my house"

    player "so like. u know about this prophecy where we like save the world"
    player "ur part of it. i need u"

    show wizard concerned 
    narrate "[wizard_name] looks out of sorts."
    wizard "oh no. haha. no uh. no i dont think. i dont think i can help you with that"
    wizard "arent there like. other wizards. better wizards."
    wizard "are u sure that im the one that ur actually looking for like thats uh. thats a lot of pressure"

    show wizard neutral
    player "haha yeah im. im sure."
    player "ur the guy. the cool guy. the cool prophecy guy."

    show wizard concerned
    wizard "but :("
    
    player "no no. ur the guy"
    player "i know this because..."

    menu convince_wizard:
        "ur like super knowledgeable":
            player "ur like super knowledgeable"
            player "theres books everywhere. u know everything"
            player "ur like literally The Arch-Mage. u fancy guy"

        "ur like a leader":
            player "ur like a leader"
            player "u have a tower. u have a robe"
            player "everyone i talk to out here looks up to you. its wild"

    show wizard neutral
    wizard "oh. um. i"
    wizard "i guess i can't. i can't say no to that"
    
    show wizard concerned
    wizard "i guess. ill help you. call me when u need me."

    narrate "{b}N I C E{/b}"

    narrate "You decide to leave [wizard_name]'s tower."

    $ wizard_encounters += 1

    jump day_end
