# This file is meant to contain the encounters with the Knight that the player has when they visit their location on the map.

label knight_check:
    scene knight_outside
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
    scene knight_outside
    narrate "Putting the prophecy scroll away once more, you head back to the front of the temple and slip inside."
    narrate "The sound of the doors as they creak open quietly is the same as when you had first woken up in this very room."
    scene knight_main
    narrate "Kneeling before the altar which is spread before the fountain of Amari is the Knight, their back turned to you while the soft sound of their murmured prayers is nearly buried under the trickling of Amari's flowing waters."
    
    show knight neutral at center 
    with Dissolve(0.5)
    narrate "When they realize they have company, the Knight stands up and turns to face you with a questioning gaze."
    narrate "They'd fully believed you would have left by now to explore the capital and find the others mentioned in the prophecy."
    knight "[player_name]? Is everything alright?"

    narrate "You tell them that you returned to look for…"

    default kn_tut_guess = set()
    menu knight_encounter_tutorial_guess:
        set kn_tut_guess
        narrate "You tell them that you returned to look for…"
        "The Grand Priest":
            jump knight_encounter_tutorial_guess_priest
        "The Knight":
            narrate "You explain that you had reread the prophecy lines and concluded that the 'right hand of the sun' must mean the Grand Priest. {b} fix this {/b}"

    knight "Me?! Surely that can't be right! I'm only a member of the clergy. The Grand Priest has far more divinity and experience than I!"
    narrate "Yet, undeniably, the line that led you here begins to glow a soft golden as you declare it must be the knight then."
    narrate "The three of you now have proof that the knight is the correct choice, even if they seem far from convinced it could be them."
    narrate "Now you have undeniable proof that you've made the right choice."
    narrate "Still, the knight looks hesitant and reluctant to believe that you're right."

    menu knight_encounter_tutorial_reassure:
        "Reassure them that it must be the will of Amari":
            narrate "You tell the knight that, much like what they had said to you at the gates outside, they must have faith in Amari's guidance if that is what this prophecy is supposed to be."
            narrate "Surely the deity would not have picked someone who was incapable of being a savior of the world."
            narrate "After all, the deity has never been wrong before."
            knight "If it truly is the will of Amari…I will do my best to be of assistance to you and the others in the prophecy. I trust you, [player_name]."
        "Assert the prophecy's undeniability and your determination to see it through":
            narrate "You gesture to the lit lines of prophecy to express their importance once again, determined for the knight to understand."
            narrate "You state that you are the one who was able to decipher the second half of the prophecy and were the Chosen One. There was no room for doubting your choice."
            knight  "...Please tell me whatever it is I can do to be of help to you, [player_name]. It is my duty."
        "Reiterate their importance to the Temple and their work beside the Grand Priest":
            narrate "You tell the knight that you understand their concern but that you've seen just how important they are, as a simple member of the clergy or not."
            narrate "They are the right hand of the Grand Priest and now, the deity as well."
            narrate "You could already tell just by their determination and faithfulness to the temple that they were an upstanding character. The prophecy only highlights that."
            narrate "You reaffirm that it has to be the will of Amari and you're going to put your faith in the knight just as the deity has, if the two of you are to figure out how to stop The End from ever reaching fruition."
            knight "If you're certain about this, how could I argue? I put my trust in you, [player_name]. Tell me what needs to be done and I will do it."
    narrate "The knight agrees to pardon themself from the late watch tonight in order to join you and the rest of the companions once you've found them."
    narrate "They reassure you that they'll be there regardless of your search's success or not."
    narrate "Despite this triumph, you feel a weighing uncertainty behind you as you leave the temple with a renewed sense of urgency and expectation."
    narrate "You can only hope that finding the other two will be as easy as the first one was."
    $ knight_encounters += 1

    # From here player goes to mage.rpy -> mage_check -> mage_encounter_tutorial
    $ knight_available = False
    $ mage_available = True
    show screen map with Dissolve(0.5)
    hide window
    pause

label knight_encounter_tutorial_guess_priest:
    narrate "You explain that you had reread the prophecy lines and concluded that the 'right hand of the sun' must mean the Grand Priest. You returned in search of him but aren't sure where to find him."
    narrate "The knight agrees that the line must mean the priest as well and vows to help you track him down within the temple."
    narrate "With their help, you're able to find the priest in a prayer room setting up for a sermon. He seems surprised to see you again but is quick to relax and ask how your search is going."
    narrate "You now explain to him that you've surmised the first line of the prophecy to be a call to recruit {i}him{/i} and his surprise returns."
    priest "Are you sure? I can see how I may fit the bill, but I've never done anything more adventurous than touring the empire to spread the faith and goodwill of Amari."
    narrate "Certain in your choice you take out the scroll to prove it to him, only to find that there are no changes to the lines of script."
    narrate "They continue to appear as simple scrawled lines of ink on the paper. There's no grand revelation on whether you're correct or not."
    narrate "Both the priest and the knight seem uncertain of how to handle your disappointment on the unchanging scroll. They share a look."
    narrate "...I'm sorry, [player_name]. Perhaps I'm not the one meant to accompany you."
    narrate "But this choice made so much sense, you thought. If not him, then who else?"
    jump knight_encounter_tutorial_guess

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