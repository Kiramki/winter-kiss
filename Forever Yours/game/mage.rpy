# This file is meant to contain the encounters with the Wizard that the player has when they visit their location on the map.

label mage_check:
    scene mage_bg_large
    hide screen map with Dissolve(0.5)

    narrate "{i}You make your way to [mage_name]'s tower.{/i}"

    show mage neutral
    mage "omg heyyyyyy :)"

    narrate "{i}Should I spend time with [mage_name]?{/i}"
    menu mage_menu:
        "Yes":
            # First encounter
            if mage_encounters == 0:
                jump mage_encounter_0

            # Second encounter
            elif mage_encounters == 1:
                jump mage_encounter_1

            # Third encounter
            elif mage_encounters == 2:
                jump mage_encounter_2

            # Fourth encounter
            elif mage_encounters == 3:
                jump mage_encounter_3

            # Fifth encounter
            elif mage_encounters == 4:
                jump mage_encounter_4

            # Sixth encounter
            elif mage_encounters == 5:
                jump mage_encounter_5

            # Subsequent encounters
            else:
                jump idle_mage
        "No":
            narrate "{i}You decide to leave the Mage's tower.{/i}"
            show screen map with Dissolve(0.5)
            pause

label mage_encounter_0:
    scene black with Dissolve(0.5)
    narrate "ur prophecy says that you gotta be recruiting some like, wizard guy right now. better get on that"
    
    scene mage_bg_1 with Dissolve(0.5)
    narrate "Well. This place looks. magic-y"

    show mage neutral with Dissolve(0.5)
    mage "hello........ what are u doing in my house"

    player "so like. u know about this prophecy where we like save the world"
    player "ur part of it. i need u"

    show mage concerned 
    narrate "[mage_name] looks out of sorts."
    mage "oh no. haha. no uh. no i dont think. i dont think i can help you with that"
    mage "arent there like. other wizards. better wizards."
    mage "are u sure that im the one that ur actually looking for like thats uh. thats a lot of pressure"

    show mage neutral
    player "haha yeah im. im sure."
    player "ur the guy. the cool guy. the cool prophecy guy."

    show mage concerned
    mage "but :("
    
    player "no no. ur the guy"
    player "i know this because..."

    menu convince_mage:
        "ur like super knowledgeable":
            player "ur like super knowledgeable"
            player "theres books everywhere. u know everything"
            player "ur like literally The Arch-Mage. u fancy guy"

        "ur like a leader":
            player "ur like a leader"
            player "u have a tower. u have a robe"
            player "everyone i talk to out here looks up to you. its wild"

    show mage neutral
    mage "oh. um. i"
    mage "i guess i can't. i can't say no to that"
    
    show mage concerned
    mage "i guess. ill help you. call me when u need me."

    narrate "{b}N I C E{/b}"

    scene black with Dissolve(0.5)

    narrate "You decide to leave [mage_name]'s tower."
    narrate "The last person you need to meet is the duke guy......"
    narrate "hope that recruiting this guy goes better than with the other two!! man, who woulda thought that trying to convince people that they're part of a prophecy where the world hangs in the balance would be so DIFFICULT"

    $ mage_encounters += 1
    $ mage_available = False
    $ duke_available = True

    show screen map with Dissolve(0.5)
    hide window
    pause

