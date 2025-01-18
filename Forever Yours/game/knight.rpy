# This file is meant to contain the encounters with the Knight that the player has when they visit their location on the map.

label knight_check:
    scene knight_bg_large
    hide screen map with Dissolve(0.5)

    narrate "{i}You make your way to wherever the knight is.{/i}"

    # Love
    if knight_affection >= 5:
        knight "There you are, [player_name]! I always have time for you, would you like to go for a meal together?"

    # Like
    elif knight_affection >= 3:
        knight "[player_name]! I was just thinking about you. Did you have time to chat?"

    # Neutral
    elif knight_affection >= -2:
        knight "Oh, hello [player_name]! How are you? Is there something you need from me?"

    # Dislike
    else:
        knight "I apologize, but I'm quite busy at the moment. Give me a moment and I'd be more than happy to help."

    narrate "{i}Should I spend time with [knight_name]?{/i}"
    menu knight_menu:
        "Yes":
            jump knight_idle
        "No":
            narrate "{i}You decide to ABANDON [knight_name] to... whatever they do.{/i}"
            show screen map with Dissolve(0.5)
            pause

label knight_idle:
    if knight_encounters == 0:
        jump knight_encounter_tutorial

    narrate "You decide to spend some time with [knight_name]."
    narrate "{i}+1 Empathy{/i}\n{i}+1 Knight's Affection{/i}"

    $ empathy += 1
    $ knight_affection += 1

    if knight_encounters == 1:
        jump knight_encounter_1
    
    if knight_encounters == 2:
        jump knight_encounter_2
    
    if knight_encounters == 3:
        jump knight_encounter_3

    if knight_encounters == 4:
        jump knight_encounter_4

    else:
        jump day_end

label knight_encounter_tutorial:
    player "hi knighttttt"
    knight "omg hey..... im like so glad that u came to see me i was like. kind of worried you were just gonna like forget about me and run off and like die or something"
    narrate "ok im not writing all that"
    narrate "u recruit the knight and stuff. next ur PRETTY sure u gotta go meet a mage....."
    narrate "better get on it"

    $ knight_encounters += 1

    # From here player goes to mage.rpy -> mage_check -> mage_encounter_tutorial
    $ knight_available = False
    $ mage_available = True
    show screen map with Dissolve(0.5)
    hide window
    pause

label knight_encounter_1:
    scene knight_bg_large with Dissolve(0.5)
    narrate "you guys are in like. a grand vestibule. i honestly dont actually know what that is but youre here!!!"
    narrate "u visit the knight. they're like... preparing for mass? for the nobility? wild"
    knight "oh hi [player_name]"
    knight "u know spirits have been rather low lately."
    knight "bc of like. the whole prophecy. the emperor announced that the world was gonna end. not in like so few words, but basically."
    knight "also like..... ik u like just got here so ur not really up to date on politics. but the other countries. theyre not happy"
    knight "..... and the deity of fate has been silent ever since the prophecy dropped"
    player "oh damn"
    player "so. how does that make u feel"
    player "do u think everything will be ok"
    knight "well. you know the prophecy outlines the way for the world to be saved"
    knight "im trying to keep our morale and faith high."
    knight "i have complete faith in you and trust you to lead us to victory"
    knight "i am exactly where i need to be, i've known nothing else."
    player "."
    player "what does... that mean"
    knight "what does wh-"
    narrate "(BELL NOISES)"
    knight "oh im sorry mass is starting. i better go"

    scene black with Dissolve(0.5)
    narrate "wait. but. but. aw goddamnit."
    narrate "man. guess you better just go home for the day"

    $ knight_encounters += 1
    jump day_end

label knight_encounter_2:
    scene knight_bg_large with Dissolve(0.5)
    narrate "You walk into the divination room, where it all began. You didn't get a good chance to look around, before."
    narrate "A large statue at the back of the room depicts the deity of Fate, a set of scales in one hand, an endless fountain pouring from the other."
    narrate "[knight_name] kneels at the center of the room, facing the statue. It doesn't look like they've noticed you yet."
    player "heyooo. what're you doing. you good?"
    knight "OH F oh. hi."
    knight "im just praying"
    knight "the temple's doing their best to make sure that Parcae's people are comforted and taken care of during these difficult times"
    player "but i dont want to know how the temple's doing. i wanna know how {i}you're{/i} doing"
    knight "oh. haha. um. h"
    knight "hhhhhhhI FORGOT. ABOUT A PRAYER I NEED TO DO. G. BYE"
    narrate "[knight_name] runs off. You're left alone in the room."
    
    scene black with Dissolve(0.5)
    narrate "... well."
    narrate "You decide to go home."

    $ knight_encounters += 1
    jump day_end

label knight_encounter_3:

label knight_encounter_4: