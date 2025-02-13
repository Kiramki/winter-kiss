﻿# The script of the game goes in this file.

# Initialize python code here.
init python:
    # importing a module. fuck u
    import time
    import check

    # Declare the stats
    resolve = 0
    fortitude = 0
    empathy = 0

    # Declare character names
    player_name = "Stranger"

    duke_name = "The Duke"
    knight_name = "The Holy Knight"
    mage_name = "The Mage"
    devil_name = "The Devil"

    nurse = "Nurse"
    doctor = "Doctor"
    unknown = "???"
    priest = "Priest"

    # Declare affection levels
    duke_affection = 0
    knight_affection = 0
    mage_affection = 0
    devil_affection = 0

    # Declare number of encounters
    mage_encounters = 0
    knight_encounters = 0
    duke_encounters = 0

    # Flags for areas of the map that are available
    duke_available = False
    mage_available = False
    knight_available = False

    # yo... yo what time is it
    year, month, day, hour, minute, second, dow, doy, dst = time.localtime() # stealing from the INTERNET idk how this works

    if hour == 0 or hour == 12:
        current_hour = 12
    elif hour <= 11:
        current_hour = hour
    elif hour >= 13:
        current_hour = hour - 12

    if hour <= 11:
        ampm = "AM"
    if hour >= 12:
        ampm = "PM"

    minute = "{0:0=2d}".format(minute)

    # Declare current week
    week = 0


# Define positions
transform left:
    yalign 1.0
    on replace:
        linear 0.5 xalign 0.05
    on show:
        xalign 0.05

transform slight_left:
    yalign 1.0
    on replace:
        linear 0.5 xalign 0.25
    on show:
        xalign 0.25

transform center:
    yalign 1.0
    on replace:
        linear 0.5 xalign 0.5
    on show:
        xalign 0.5

transform slight_right:
    yalign 1.0
    on replace:
        linear 0.5 xalign 0.75
    on show:
        xalign 0.75

transform right:
    yalign 1.0
    on replace:
        linear 0.5 xalign 0.95
    on show:
        xalign 0.95

# Declare the characters + sprites that will be used in the game.

define narrate = Character('Narrator')
define prophecy = Character('', kind=nvl, color="#c8ffc8")

define butler = Character('Butler')

define angel = Character('Angel')
image angel neutral = "images/sprites/angel/Angel_Neutral_Sprite.png"
image angel sad = "images/sprites/angel/Angel_Sad_Sprite.png"

define devil = Character('[devil_name]')
image devil malicious = "images/sprites/devil/Minerva_Malice_Sprite.png"
image devil neutral = "images/sprites/devil/Minerva_Neutral_Sprite.png"

define knight = Character('[knight_name]')
image knight angry = "images/sprites/knight/Knight_Angry_Sprite.png"
image knight concern = "images/sprites/knight/Knight_Concern_Sprite.png"
image knight happy = "images/sprites/knight/Knight_Happy_Sprite.png"
image knight love = "images/sprites/knight/Knight_Love_Sprite.png"
image knight nervous = "images/sprites/knight/Knight_Nervous_Sprite.png"
image knight neutral = "images/sprites/knight/Knight_Neutral_Sprite.png"
image knight sad = "images/sprites/knight/Knight_Sad_Sprite.png"
image knight shock = "images/sprites/knight/Knight_Shocked_Sprite.png"


define mage = Character('[mage_name]')
image mage angry = "images/sprites/mage/Mage_Angry_sprite.png"
image mage concern = "images/sprites/mage/Mage_Concern_sprite.png"
image mage happy = "images/sprites/mage/Mage_Happy_sprite.png"
image mage love = "images/sprites/mage/Mage_Love_sprite.png"
image mage neutral = "images/sprites/mage/Mage_Neutral_sprite.png"
image mage sad = "images/sprites/mage/Mage_Sad_sprite.png"


define duke = Character('[duke_name]')
image duke angry = "images/sprites/duke/Duke_Angry_Sprite.png"
image duke concern = "images/sprites/duke/Duke_Concern_Sprite.png"
image duke happy = "images/sprites/duke/Duke_Happy_Sprite.png"
image duke love = "images/sprites/duke/Duke_Love_Sprite.png"
image duke neutral = "images/sprites/duke/Duke_Neutral_Sprite.png"
image duke sad = "images/sprites/duke/Duke_Sad_Sprite.png"
image duke shock = "images/sprites/duke/Duke_Shock_Sprite.png"

define player = Character('[player_name]')

# Declare backgrounds
image white = "#ffffff"
image logo_white = "gui/logo/logo_white.png"


label splashscreen:
    play sound "audio/hook/angel_spell.mp3"
    play music "<loop 43.94 to 141.97>ForeverYoursTheme.ogg"
    $ renpy.movie_cutscene("gui/logo/gloamy_logo.webm")
    return
# The game starts here.

label start:
    # GAME START
    # Stop menu music
    stop music fadeout 1.0
    play sound "audio/hook/you_are_dying.mp3"
    pause 1
    scene black with Dissolve(0.5)
    show text "You are dying." with dissolve
    pause 2
    hide text with dissolve
    pause 1
    centered "A team of medical professionals surround you, electrodes are strapped to your chest." 
    centered "Your mother is holding a small bundle of paper cranes."
    centered "With trembling fingers, she folds and unfolds one as the doctor speaks grimly about your condition."
    nurse "—for a pulse check?"
    doctor "Resume compressions. Thirty seconds until the next check."
    play sound "audio/hook/flatline.mp3" fadeout 0.5
    scene flatline
    centered "The monitor blares a flatline."
    pause 1
    play sound "audio/hook/light_appear.mp3"
    play music "audio/hook/angel_appears.mp3"
    scene white with Dissolve(0.5)
    narrate "Suddenly, the room around you is eclipsed in a flash of light and a figure emerges."

    show angel sad at center
    with Dissolve(0.5)
    voice "audio/voice/devil/line0001.ogg"
    angel "They're going to let you go. I'm sorry."

    menu question_angel:
        "Who are you?":
            show angel neutral
            narrate "The figure smiles serenely."
            voice "audio/voice/devil/line0002.ogg"
            angel "I am what lies between you and the end of all things."
        "No, that can't be right.":
            narrate "The figure shakes her head, eyes filled with sympathy."

            show angel sad
            voice "audio/voice/devil/line0003.ogg"
            angel "They tried their best, but it won't be long now."

    #narrate "The light surrounding her grows brighter, your mother's face is lost in the sea of white."
    show angel sad
    voice "audio/voice/devil/line0004.ogg"
    angel "It's almost time to let go. Are you ready?"
    narrate "Grief crushes you, winding itself around your heart like a vice in your chest."
    narrate "No, this can't be all there is. You are not ready. You never..."

    menu life_goals:
        "Left your mark on the world":
            $ goal = "impact"

        "Meant something to someone":
            $ goal = "meaning"
        
        "Discovered your true purpose":
            $ goal = "purpose"

        "Explored the world":
            $ goal = "exploration"
    
    show angel neutral
    narrate "The angel seems to sympathize with your words, then tilts her head, offering a soft smile."
    voice "audio/voice/devil/line0005.ogg"
    angel "What if this doesn't have to be the end?"
    
    # ooooo scene change
    play sound "audio/hook/angel_spell.mp3"
    scene parcae_flash with Dissolve(1)
    narrate "In that vast emptiness, a faded, blurry image of a sunny land appears before you."
    show angel neutral with Dissolve(0.5)
    voice "audio/voice/devil/line0006.ogg"
    angel "This is the Empire of Parcae. A land of peace, virtue, and balance. But it's in peril."
    voice "audio/voice/devil/line0007.ogg"
    show angel sad
    angel "When winter comes, it will be the end of everything."
    show angel neutral
    voice "audio/voice/devil/line0008.ogg"
    angel "I can offer you a second chance — to save this world and become the hero in the prophecy."
    narrate "A second chance... but why you? You don't understand."

    show angel sad
    if goal == "impact":
        voice "audio/voice/devil/line0009.ogg"
        angel "Because this world has chosen you. This is your chance to {color=#8b67b0}leave your mark on the world{/color}."
    elif goal == "meaning":
        voice "audio/voice/devil/line0010.ogg"
        angel "Because this world has chosen you. This is your chance to {color=#8b67b0}mean something to someone{/color}."
    elif goal == "purpose":
        voice "audio/voice/devil/line0011.ogg"
        angel "Because this world has chosen you. This is your chance to {color=#8b67b0}discover your true purpose{/color}."
    elif goal == "exploration":
        voice "audio/voice/devil/line0012.ogg"
        angel "Because this world has chosen you. This is your chance to {color=#8b67b0}explore a brand new world{/color}."
    else:
        voice "audio/voice/devil/line009.ogg"
        angel "Because this world has chosen you. This is your second chance."
    voice "audio/voice/devil/line0013.ogg"
    show angel neutral
    angel "But to join, you must let go of this life - {color=#8b67b0}sacrifice a piece of yourself{/color}."

    scene white with Dissolve(0.5)
    play sound "audio/hook/light_appear.mp3"
    scene white with Dissolve(0.5)
    nurse "Charging to 200!"
    doctor "Pause compressions. Stand clear."
    show angel sad with Dissolve(0.5)
    voice "audio/voice/devil/line0014.ogg"
    angel "Time is running out. The light will take you soon. What is your choice?"
    play sound "audio/hook/you_are_dying.mp3" fadein 1.0
        
    menu sacrifice:
        # Trust sacrifice
        "Sacrifice a memory of Resolve":
            $ fortitude = 10
            $ empathy = 20
            $ resolve = 5
            prophecy "You've chased ambition like a moth to a flame, only to find yourself burned time and time again."
            prophecy "You've pushed too hard, too far, and left behind the people and moments that truly mattered."
            prophecy "What good is determination when it blinds you to everything else?"
            prophecy "Sacrificing resolve might be the only way to finally slow down and stop trading the things you truly care about. "

        # Courage sacrifice
        "Sacrifice a memory of Fortitude":
            $ fortitude = 5
            $ empathy = 10
            $ resolve = 20
            prophecy "You can endure through almost anything, but that's exactly the problem."
            prophecy "It makes you complacent, sticking with things that don't serve you because you don't think you deserve better."
            prophecy "Maybe it's time to let go of this endless endurance."
            prophecy "Sacrificing fortitude could mean gaining something new - a sense of standards, of self-worth."

        # Honesty
        "Sacrifice a memory of Empathy":
            $ fortitude = 20
            $ empathy = 5
            $ resolve = 10
            prophecy "You've always had a fickle heart—an open door for everyone and everything."
            prophecy "Always trying to please, always trying to make everyone else happy."
            prophecy "But where has it gotten you? Perhaps letting go could mean freedom from that constant inner tug-of-war."
            prophecy "It would give you some space to breathe - to prioritize yourself for once."

    prophecy "Is this what you want to sacrifice?"
    menu sacrifice_confirm:
        "Yes":
            prophecy "{color=#8b67b0}{b}You close your eyes, and let the thought go.{/b}{/color}"
        "No":
            nvl clear
            jump sacrifice
            
            
    prophecy "Your current stats are:\nFortitude: [fortitude]\nEmpathy: [empathy]\nResolve: [resolve]"
    nvl clear
    show angel neutral
    voice "audio/voice/devil/line0015.ogg"
    angel "So you've decided to join this new world?"
    narrate "She smiles prettily and leans in towards you."
    voice "audio/voice/devil/line0016.ogg"
    angel "Then, touch your lips to mine, and seal your choice."

    menu kiss_her:
        "Kiss her":
            play sound "<loop 0.0>audio/hook/angel_spell.mp3"
            scene kiss_cg with Dissolve(0.5)
            pause 1.0
            narrate "You lean in, your lips brushing against hers."
            narrate "As she cradles your face, something dances at the back of your mind - light and fleeting, like snowfall."
            narrate "For a moment, everything is still."
            stop music
            narrate "Then, something inside you cracks."
    play sound "audio/hook/dark_ambiance.mp3" 
    scene black with Dissolve(0.5)
    voice "audio/voice/devil/laugh.ogg"
    pause 2.5

    # OH SHITTTTTT (scene change)
    play music "audio/hook/minerva_reveal.mp3" fadein 1.0
    scene black_smoke with Dissolve (0.5)  
    narrate "Suddenly, light drips from the walls around you and oozes down into a thick, viscous murkiness."

    show devil malicious with Dissolve(0.5)
    narrate "The angelic figure from before has morphed into something sinister."
    narrate "She looks at you with mirthful eyes."
    voice "audio/voice/devil/line0017.ogg"
    devil "So naive, {i}as always{/i}. It's time you learned there are no second chances."
    play sound "audio/hook/you_died.mp3" fadeout 0.5
    scene black with Dissolve (0.5)  
    narrate "Reality shatters around you. Darkness consumes the room and swallows you whole."
    # Current
    scene flatline 
    stop music fadeout 1.0
    pause(3)
    centered "The doctor pronounced your time of death as {color=#8b67b0}[current_hour]:[minute] [ampm]{/color}." #insert actual time
    scene black with Dissolve (0.5)
    pause(3)

    jump tutorial_start #MIA. COMMENT THIS OUT. IF YOU WANT TO DO YOUR TESTING. 

# hurgles. tutorial
label tutorial_start:
    stop sound fadeout 1.0
    narrate "..."
    narrate "Somewhere beyond you, there is music."
    play music "<loop 0.0>audio/opening/temple_ambiance.mp3" fadein 1.0
    scene knight_bg_large with Dissolve(1)
    narrate "Lights churn around your body like a kaleidoscope and you sludge towards the beckoning hymn."
    narrate "You burst from the miasma like a newborn thrust into the chill of open air for the first time; into somewhere you have never existed before."
    narrate "The material beneath your palms twist forward in impossible patterns of life. You are lost."
    unknown "Let them rest a moment..."
    unknown "Be at ease, you are in the Grand Temple of Amari. Welcome to Parcae."
    scene knight_main with Dissolve(1.5)
    narrate "Your vision clears. When you look up, you are met with a grand hall bathed in candlelight."
    show knight neutral at center
    with Dissolve(0.5)
    narrate "Two figures step forward. One dressed in fine armor stands at attention beside another in ceremonial robes."
    priest "Chosen One, blessed by our great deity Amari, we are so glad you've come to us."
    priest "Your arrival is a gift to the Empire. The Holy Order welcomes you."
    narrate "The knight beside him takes a step towards you and bows deeply."
    show knight happy
    voice "audio/voice/knight/line0001.ogg"
    knight "I know this must be overwhelming, but...we are honored to meet you."
    show knight neutral
    narrate "No. You shouldn't be here. You know that much. You shouldn't be here because... because…"
    narrate "You try to remember, fumbling to recall what came before the mirage of light and sound leading to your awakening here."
    priest "Tell us, what name should we call you by?"
    $ player_name = renpy.input("Enter your name.").title().strip() or __("Stranger")

    # If the player doesn't enter a name, they will be referred to as "Stranger"
    if player_name == "Stranger":
        narrate "There is an extended moment of silence, but nothing comes to mind."
    
    menu pronouns:
        narrate "What of your pronouns, [player_name]?"
        "he/him":
            $ p_subject = "he"
            $ p_object = "him"
            $ p_possessive = "his"
            $ p_possessive_adj = "his"
            $ p_reflexive = "himself"
            $ p_is = "he's"
            $ p_be = "is"
            $ p_title = "Sir"

        "she/her":
            $ p_subject = "she"
            $ p_object = "her"
            $ p_possessive = "her"
            $ p_possessive_adj = "hers"
            $ p_reflexive = "herself"
            $ p_is = "she's"
            $ p_be = "is"
            $ p_title = "Lady"

        "they/them":
            $ p_subject = "they"
            $ p_object = "them"
            $ p_possessive = "their"
            $ p_possessive_adj = "theirs"
            $ p_reflexive = "themself"
            $ p_is = "they're"
            $ p_be = "are"
            $ p_title = "Mx."
    
    narrate "You've remembered who you are and you tell the Grand Priest and the Holy Knight beside him as such."
    narrate "The priest offers a gentle smile with understanding and acceptance."
    priest "It is a pleasure to meet you, [player_name]. I understand you may have some questions. Please feel free to share them with me now."
    
    
    default opening_priest_set = set()
    
    menu opening_priest_questions:
        set opening_priest_set
        "Ask them where you are":
            priest "As I mentioned before, you are in the Holy Empire of Parcae. A country within the continent of Verum Lüge."
            priest "Our deity of Fate, Amari, sent down a prophecy predicting your arrival from another world to ours . That is, here in Atemporal."
        "Ask them what they mean by prophecy":
            priest "Two weeks ago we received a prophecy from our great deity, Amari. It foretold your arrival today and warned us of a great danger to the Parcae Empire."
        "{b}You have forgotten something terribly important{/b}":
            narrate "There was a world you lived in before this one. A life, a name, faces you should know but cannot recall."
            narrate "Hazy memories swirl around your head. You remember antiseptic, the crinkle of paper cranes, and haunting, melodic laughter."
            jump opening_priest_questions

    narrate "The Grand Priest gestures to the knight and they hand him a small rolled up scroll. The scroll is then handed to you and he encourages you to open and read it."
    priest "We were only able to decipher the first half of the prophecy when it descended. The second half remains a mystery, written in a language not familiar to this world."
    narrate "You study the scroll in your hands as it opens itself to you and the script dances across the page as if it were being written right before your eyes."
    narrate "Some sentences seem to shimmer and draw your attention more compared to the rest of the lines."
    narrate "The first half of the prophecy, despite being written in a different language, is plain as day to you."
    narrate "You read that the Chosen One - you - were set to arrive from another world and be the last hope in saving the Parcae Empire from the {i}End{/i}."
    narrate "You feel your heart drop to your stomach. {i}What does it mean by the End?{/i}"
    narrate "Continuing on, the second half appears to be written in English. Meant only for you to read."
    
    prophecy "Come diamond fractals, fiends and fare,"
    prophecy "A witch is born with two moons to spare."
    prophecy "If the old wall weeps and hears its tongue,"
    prophecy "The path is set with the right hand of the sun."
    prophecy "Then, for the empire's heart, bring forth its shield,"
    prophecy "and for knowledge, a conductor of the magic's field."
    prophecy "Three gates shall bow down for each price once paid,"
    prophecy "But the witch alone slays the umbra of Parcae."
    nvl clear
    
    narrate "After you've read the scroll over, the Grand Priest appears almost anxious as he questions what the second half of the prophecy said."
    show knight concern
    narrate "You recite it and his expression becomes puzzled, as does that of the knight beside him."
    narrate "For a moment, neither of them speak. "
    show knight neutral
    narrate "Then the Grand Priest speaks up, calmer now than he had been a moment ago."
    priest "I see... so this is a task only you may undergo. Please forgive me for being unable to help you but know you may always seek solace in the temple if you so need."
    priest "For now, I hope Ser Lurien may be of help to you in my stead."
    narrate "The knight offers another bow as they'd done before when you all first met."
    
    show knight happy
    voice "audio/voice/knight/line0002.ogg"
    knight "Should there be anything you need, please do not hesitate to request it. I will do everything within my power to assist you, [player_name]."
    show knight neutral
    narrate "Content, the Grand Priest excuses himself to attend to other matters and leaves the room so it's only you and the Knight left."
    voice "audio/voice/knight/line0003.ogg"
    knight "Allow me to show you around, [p_title] [player_name]."
    narrate "You ask the knight to be less formal with you and they nod before turning with the intent to guide you about the Temple grounds."
    scene knight_outside with Dissolve(0.5)
    narrate "The tour ends with the both of you now outside the Grand Temple."
    narrate "From here, you're able to marvel about the rather massive temple of ivory, decorated with gold on the ionic columns and above the wide doorway which leads further into the home of worship."
    narrate "All of it seems pristine and almost unreal in a way that's unlike anything you've ever seen before."
    show knight neutral with Dissolve(0.5)
    narrate "When your attention turns to the knight again, they seem to perk up as if realizing that now you might be looking to them for more guidance."
    
    show knight happy
    voice "audio/voice/knight/line0004.ogg"
    knight "I understand this must be a lot to a stranger of this world. I mean what I said before; if there's anything I can do to help you, please let me know."

    show knight neutral
    menu opening_knight_questions:
        "Explore on your own":
            jump opening_knight_questions_explore
        "Ask where you should start":
            jump opening_knight_questions_start
        "Express concerns about the prophecy":
            jump opening_knight_questions_concerns

label opening_knight_questions_explore:
    narrate "You tell the Knight you want to explore on your own to better understand the empire you've appeared in."
    narrate "Maybe along the way you'll find the people meant for the prophecy?"

    show knight shock
    voice "audio/voice/knight/line0005.ogg"
    knight "That reminds me- I was supposed to hand it to you earlier during the tour. I apologize for forgetting until now."
    
    show knight neutral
    narrate "They hand you a carefully folded up piece of paper that turns out to be a map once you unfold it."
    narrate "The top declares 'Capital of Parcae', meaning it must be the capital city of the empire you're currently in."

    ###
    narrate "(Imagine a cool cg thing of the map)"
    ###

    narrate "A few places are marked specifically on the map and catch your eye. It looks like noble estates in the capital are marked with their house crests, but one in particular has a shield as its crest."
    narrate "There also appears to be a mage tower near the center of the capital."
    narrate "You thank the knight for the map and they bow, a curious smile on their face for what you might do next."
    narrate "You plan to explore some of the options within the capital and see if you can find a lead on who the other saviors of the prophecy are."

    # add something here to note that stats have increased?
    $ resolve += 1
    $ fortitude += 1

    jump opening_map

label opening_knight_questions_start:
    narrate "You feel a little hopeless - you've just appeared here and you're basically being told to fly the nest like a baby bird. You don't know where to go or how to get there!"
    show knight shock
    narrate "You express this to the knight and they blink as if processing what you said before realization dawns and they become apologetic."
    narrate " Immediately they're grabbing something from their pocket and they hold it out to you. It's a folded piece of paper that reveals itself to be a map once you unfold it."
    show knight concern
    voice "audio/voice/knight/line0006.ogg"
    knight "Please forgive me, I forgot to give this to you when you were reading the prophecy earlier."
    show knight neutral
    voice "audio/voice/knight/line0007.ogg"
    knight "This should be a map of the capital, since that's where the Grand Temple is located. It might help you in your search!"
    narrate "You study the map for a moment and notice a mage's tower marked near the center of the capital, not too far from the temple."
    narrate "There's also what looks to be noble estates marked with house crests, and one of the crests even looks similar to a shield."
    narrate "You thank the knight and they bow again, still apologetic about their blunder."
    narrate "With a new idea on where you are and the places you could explore, you think you're ready to leave past the gates into the capital to find who the other saviors of prophecy may be."
    
    $ fortitude += 1
    $ empathy += 1
    
    jump opening_map

label opening_knight_questions_concerns:
    narrate "Now seems like as good a time as any to reveal your anxieties about the prophecy."
    narrate "You tell the knight that you're concerned by 'The End' that was mentioned and how you're not entirely sure you are the supposed Chosen One that the Grand Priest had called you earlier."
    narrate "You don't even know this land, the people, or the culture. You're more out of place than you want to be."
    show knight concern
    narrate "The knight seems to understand your struggles and anxieties as their expression shows their sympathy and concern, looking somewhat serious for the first time compared to how gentle and warm they'd been up until now."
    voice "audio/voice/knight/line0008.ogg"   
    knight "It may not make sense now, but our deity has never been wrong before and I'm certain with all my heart they're not wrong now either."
    voice "audio/voice/knight/line0009.ogg"  
    knight "You are the first foreigner to ever appear in our world through such divine means, appearing just like the prophecy said you would! Please have faith, [player_name]." 
    narrate "You feel a little better but still incredibly out of place and new to all of this."
    narrate "Then again, who {i}wouldn't{/i} feel the way you do in such a situation?"
    show knight neutral
    narrate "Taking a deep breath, you manage to calm enough to notice that the Knight is now holding a map out to you."
    voice "audio/voice/knight/line0010.ogg"  
    knight  "I hope this may be of help to you, [player_name]."
    voice "audio/voice/knight/line0011.ogg"  
    knight "It's a map of the capital here in the empire. Perhaps it will help direct you where you need to go on your search?"
    narrate "You thank the Knight and they appear to be visibly relieved that you're in better spirits now."
    narrate "The gates don't look as foreboding as they had minutes ago in the midst of your worries."

    $ empathy += 1
    $ resolve += 1

    jump opening_map

label opening_map:
    scene knight_outside with Dissolve(0.5)
    narrate "Even though you feel ready to take off into the capital of Parcae and look closer at the two places that just might have a connection to the prophecy."
    narrate "It might be easiest to start here in the {color=#8b67b0}Grand Temple{/color} first and foremost on the first line."
    narrate "You pull out the prophecy scroll once more to reread it."
    prophecy "The path is set with the right hand of the {color=#8b67b0}sun{/color}."
    prophecy "Then, for the empire's heart, bring forth its {color=#8b67b0}shield{/color},"
    prophecy "and for knowledge, a conductor of the {color=#8b67b0}magic's field{/color}."
    nvl clear
    narrate "The first line could be hinting at someone important in the temple itself."
    narrate "A symbol of branching paths similar to a 'sun' appears all over the building and even the uniform that both the Grand Priest and the holy knight were wearing."
    stop music
    # From here player goes to knight.rpy -> knight_check -> knight_encounter_tutorial
    $ knight_available = True
    show screen map with Dissolve(0.5)
    window hide
    pause

label day_start:
    scene knight_main with Dissolve(0.5)
    $ week += 1
    narrate "u wake up. you have [11 - week] weeks left to save the world. (this is the day_start label)"
    narrate "It is currently week [week]."

    if week == 11:
        narrate "you are out of time."
        narrate "its time to face ur destiny or some shit."
        jump trial_1_start

    narrate "(pls god nothings implemented past this point u WILL run into an error if u interact with that map)"

    show screen map with Dissolve(0.5)
    window hide

    pause

label day_end:
    scene mage_bg_large with Dissolve(0.5)
    narrate "you are now in the day_end label. This label will direct you to a story event, if there is one to see."

    if week == 2:
        jump event_2_start
    elif week == 4:
        jump event_3_start
    elif week == 8:
        jump event_4_start
    elif week == 10:
        jump event_5_start

    else:
        jump day_dreams


label day_dreams:
    # If there's a dream event, jump there. Otherwise, jump to the next day.
    scene duke_bg_large with Dissolve(0.5)
    narrate "You are now in the day_dreams label. This label will direct you to a dream sequence, if there is one to see."
    if week == 2:
        jump ambiguous_memory_1
    else:
        jump day_start

