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
    narrate "You stand before a tall gate not unlike the gates at the Grand Temple."
    narrate "They are shut firmly, attached to a fence of iron and stone that wraps around the large estate belonging to the Ducal House of Thornwick."
    narrate "Just like on the map, a crest of silver in the shape of a shield rests in the center of the gate just above your head."
    narrate "There are two knights on either side of the gate who wear the shield crest engraved in their pauldrons and on the badge attached to the front of their dark uniforms. They demand to know why you're there."
    narrate "Before you can properly answer them, a well-dressed gentleman approaches you from the other side of the gate."
    narrate "From the looks of it, he appears to be almost grandfatherly in age yet his hardened expression holds no warmth that you would expect of such a figure."
    narrate "He holds up a hand as if to gesture the knights to stand down and they huff before resuming their original guarding positions. You can see they're still watching you warily."
    unknown "State your identity and purpose for visiting, please."
    menu duke_encounter_tutorial_guess:
        "Tell him your name and why you're there":
            narrate "You state your name and explain that you're visiting because you believe the Duke has something to do with the Prophecy that was received two weeks ago in the Grand Temple."
            narrate "The man looks troubled for a moment as if he's unsure whether to truly let you in or not."
        "Ask if he's the duke":
            narrate "Without thinking, you blurt out the question and watch as the harsh expression on the older gentleman relaxes and he almost looks amused."
            narrate "There's a kind twinkle in his eyes behind the glasses he wears and he appears more like the grandfather figure he appears as."
            narrate "He clears his throat and the amusement is gone but his tone is a bit warmer when he repeats his question."
            jump duke_encounter_tutorial_guess
    narrate "He tells you to wait there after a few minutes and turns away to walk back up the well-maintained sidewalk and disappear inside the large estate."
    narrate "You wait there only for what must've been 5 minutes before the man returns and he allows the gates to be opened."
    narrate "Now that you've been allowed inside, you follow the man and realize you don't actually know who he is but context clues suggest that he's not the master of this property."
    narrate "As if sensing your curiosity, the man finally introduces himself as Wilfred and asks that you simply refer to him by name."
    narrate "You think to introduce yourself again but remember that you've already technically done so and opt to stay silent instead."
    narrate "The two of you walk down rather intricate  halls that showcase wealth and yet somehow feel almost lonely. The paintings hold no people in them and the colors feel as cold as the winter outside."
    narrate "There's minimal furnishings in any of the rooms you can see into when you walk past them, as if the home was only for show rather than living in."
    narrate "Wilfred stops suddenly at two large wooden doors and knocks twice on one."
    narrate "From within the room, you can hear a man's voice respond and Wilfred opens one of the doors inward for you with a gesture."
    narrate "A man younger than Wilfred sits at a large oak desk that's stacked with papers and various other important looking things."
    narrate "His dark hair is swept back save for a few snowy strands that fall into his face."
    duke "Wilfred told me you're here because of the prophecy the Grand Temple announced two weeks ago. I'm not sorry to say that I'm not much affiliated with the temple, so I see no reason why you're even standing before me."
    menu:
        "Appeal to the Duke's household title as the Empire's Shield.":
            narrate "You tell the duke that his house is mentioned in the prophecy and watch as one eyebrow raises in an arch. The papers in his hands are put down and he fixes his full attention on you compared to the half-attentive greeting he'd given."
            duke "I don't recall hearing this in the prophecy the temple released."
            narrate "You recall both the shield on the map and the shield crest outside on the gates of the home. You tell him as such and repeat the line of the prophecy that states the empire's shield. He needs to join you and the other prophetic saviors at the temple tonight in order to go over the new information about the prophecy and figure out what must be done to save the world."
            narrate "The Duke doesn't seem very moved but seems to recognize that there's no better way to check if the information is true than to go to the temple like you're asking of him."
        "State that you refuse to leave":
            narrate "You can already tell that it won't be easy to convince the Duke that you believe he's a necessary part of the prophecy."
            narrate "If you proved it, would he even believe you? Or would he have you tossed out of his estate?"
            narrate "For some reason you don't doubt that he's keeping track of the seconds that tick by before he does just that."
            narrate "You tell him you won't leave until he promises to go to the temple tonight. You know he's the Shield part of the prophecy and believe he's part of the chosen group of saviors for the world."
            narrate "Those words seem to catch his attention but you're not sure why."
            duke "Fine, {i}fine{/i}. Now leave. I have work to do."
        "Claim your understanding of the prophecy":
            narrate "When you recall the prophecy, you remember that you came here on a hunch that the 'Shield of the Empire' meant the Thornwick Ducal house."
            narrate "You explain to the Duke that the prophecy says the empire has a shield and that you believe it's this household."
            narrate "It's a bold move, but you can't back down now."
            narrate "To prove your point you pull out the scroll you've been allowed to carry with you by grace of the Grand Priest and unroll it to place it on the Duke's desk."
            narrate "He looks momentarily miffed by your actions but quickly fixes his gaze on the page before him in interest."
            narrate "Before the two of you, the line only you can read begins to shimmer and waver ever so slightly in place before the letters start to emit a soft golden glow much like they did with the knight."
            narrate "The Duke is rendered speechless as he stares at the letters coming to life before him. He doesn't answer you right away, but when he does he seems more convinced than you thought he'd be."
            Duke "...Fine. I'll be there tonight."
    narrate "Now that you've managed to capture the Duke's interest, you feel as though you can breathe a little easier after stepping outside of the rather large and empty home."
    narrate "Wilfred sees you off but you barely think to say goodbye as you step outside the gates and head back towards the temple."
    $ duke_available = True
    $ mage_available = True
    $ knight_available = True

    # From here player goes to events.rpy
    $ duke_encounters += 1
    scene black with Dissolve(0.5)
    jump event_1_start

label duke_encounter_1:
    scene duke_bg_large with Dissolve(0.5)

    narrate "u visit the duke in his estate"
    narrate "he looks. super busy. his desk is covered in an UNGODLY amount of paperwork"
    narrate "how can a single person handle that much paperwork..."
    show duke neutral
    duke "goddamnit"
    duke "u know. even though i try so hard. with my personal forces and resources to assist. people are still dying. to MONSTERS"
    player "damn..."
    player "hey so how do you feel about like. the prophecy. and how are you in general. u look stressed"
    duke "u know what. its just really frustrating that i cant keep my promise to protect the people of the empire"
    player "u seem like ur doing pretty well all things considered. working hard"
    duke "nah. no. people r still dying. its not good enough"
    player "well ! uh. okay !"
    scene black with Dissolve(0.5)
    narrate "me when i perfectionist huh."

    # Increase encounter counter - jump to the end of the day
    $ duke_encounters += 1
    jump day_end

label duke_encounter_2:
    scene duke_bg_large with Dissolve(0.5)
    narrate "u are with the duke once again."
    narrate "he looks stressed. but youve come to realize that might just be his face....... or maybe he's just always stressed"
    player "so. why are u always like. trying to do things urself"
    duke ">:("
    duke "get out"

    scene black with Dissolve(0.5)
    narrate "goddamn. ok"

    $ duke_encounters += 1
    jump day_end

label duke_encounter_3:
    scene duke_bg_large with Dissolve(0.5)
    narrate "teehee sneakink into the garden :) :D"
    butler "YO... WHAT THE FUCK ARE YOU DOING HERE"
    narrate "shit"
    show duke neutral at center
    duke "what the hell. is all that NOISE"
    narrate "shit (x2)"
    duke "everyone else. gtfo. you. >:("
    player "can i have a tour. pretty pls. pls. pls"
    duke "fine god. whatever. sure."
    player "do u like. why dont u like the garden"
    duke "its not that i dont like it. she was the only one i could go to when things were tough...."
    player "Who"
    duke "i have work to do. goodbye"
    scene black with Dissolve(0.5)
    narrate "oh"

    $ duke_encounters += 1
    jump day_end

label duke_encounter_4:
    scene duke_bg_large with Dissolve(0.5)
    narrate "we are HERE TO SEE THE DUKEEEEE"
    butler "duke's in the garden actually"
    narrate "oh"
    narrate "better go to the garden then"
    narrate "(garden noises)"
    show duke neutral
    narrate "oh damn. that guys having tea"
    duke "im having tea. my aide can do the work."
    narrate "(a super cool and emotional scene ensues)"

    scene black with Dissolve(0.5)
    pause 0.5
    narrate "(which im not writing)"

    $ duke_encounters += 1
    jump day_end