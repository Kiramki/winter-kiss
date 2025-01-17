# This file is meant to contain the encounters with the Duke that the player has when they visit their location on the map.

label duke_check:
    scene duke_bg_large
    hide screen map with Dissolve(0.5)

    narrate "{i}You make your way to the Duke's fancyass house.{/i}"

    # Love
    if duke_affection >= 5:
        show duke happy with Dissolve(0.5)
        duke "It's been ages since I've sat in the garden and simply breathed. All thanks to you, my friend."

    # Like
    elif duke_affection >= 3:
        show duke neutral with Dissolve(0.5)
        duke "Hello, [player_name]. I had a feeling it was you. Looks like I'll have to do this another time."

    # Neutral
    elif duke_affection >= -2:
        show duke neutral with Dissolve(0.5)
        duke "Oh, it's you. I was in the middle of writing an expense report... but I can spare a moment."

    # Dislike
    else:
        show duke neutral with Dissolve(0.5)
        duke "There are things more pressing than idle chatter. I have work to do."

    narrate "{i}Should I spend time with the Duke?{/i}"
    menu duke_menu:
        "Yes":
            jump duke_idle
        "No":
            narrate "{i}You decide to leave the Duke's FANCYASS HOUSE.{/i}"
            show screen map with Dissolve(0.5)
            pause

label duke_idle:
    if duke_encounters == 0:
        jump duke_encounter_tutorial

    narrate "You decide to spend some time with the Duke."
    narrate "{i}+1 Resolve{/i}\n{i}+1 Duke's Affection{/i}"

    $ resolve += 1
    $ duke_affection += 1

    if duke_encounters == 1:
        jump duke_encounter_1
    
    if duke_encounters == 2:
        jump duke_encounter_2
    
    if duke_encounters == 3:
        jump duke_encounter_3

    if duke_encounters == 4:
        jump duke_encounter_4

    else:
        jump day_end

label duke_encounter_tutorial:
    player "haha hey im here to recruit you for the-"
    duke "no u are not. frankly i dont think u need my help"
    player "but"
    narrate "(recruitment noises)"

    duke "FINE. i guess. ill entertain u."
    player "(THANK GOD)"

    $ duke_available = True
    $ mage_available = True
    $ knight_available = True

    # From here player goes to events.rpy
    $ duke_encounters += 1
    scene black with Dissolve(0.5)
    jump event_1_start

label duke_encounter_1:


label duke_encounter_2:

label duke_encounter_3:

label duke_encounter_4: