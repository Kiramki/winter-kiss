# The script of the game goes in this file.

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
transform slight_left:
    xalign 0.25
    yalign 1.0

transform slight_left_from_center:
    xalign 0.5
    yalign 1.0
    linear 0.5 xalign 0.25

transform slight_right:
    xalign 0.75
    yalign 1.0

# Declare the characters + sprites that will be used in the game.

define narrate = Character('Narrator')
define prophecy = Character('', kind=nvl, color="#c8ffc8")

define butler = Character('Butler')

define angel = Character('Angel')

define devil = Character('[devil_name]')
image devil angry = "images/sprites/devil_angry.png"
image devil fear = "images/sprites/devil_fear.png"
image devil happy = "images/sprites/devil_happy.png"
image devil love = "images/sprites/devil_love.png"
image devil malicious = "images/sprites/devil_malicious.png"
image devil neutral = "images/sprites/devil_neutral.png"
image devil pleading = "images/sprites/devil_pleading.png"
image devil sad = "images/sprites/devil_sad.png"

define knight = Character('[knight_name]')

define mage = Character('[mage_name]')
image mage angry = "images/sprites/Mage_Angry_WCane.png"
image mage concerned = "images/sprites/Mage_Concerned_WCane.png"
image mage happy = "images/sprites/Mage_Happy_WCane.png"
image mage love = "images/sprites/Mage_Love_WCane.png"
image mage neutral = "images/sprites/Mage_Neutral_WCane.png"
image mage sad = "images/sprites/Mage_Sad_WCane.png"
image mage angry nocane = "images/sprites/Mage_Angry_WOCane.png"
image mage concerned nocane = "images/sprites/Mage_Concerned_WOCane.png"
image mage happy nocane = "images/sprites/Mage_Happy_WOCane.png"
image mage love nocane = "images/sprites/Mage_Love_WOCane.png"
image mage neutral nocane = "images/sprites/Mage_Neutral_WOCane.png"
image mage sad nocane = "images/sprites/Mage_Sad_WOCane.png"


define duke = Character('[duke_name]')
image duke concern = "images/sprites/duke_Concern.png"
image duke happy = "images/sprites/duke_Happy.png"
image duke love = "images/sprites/duke_Love.png"
image duke neutral = "images/sprites/duke_Neutral.png"
image duke sad = "images/sprites/duke_Sad.png"
image duke shock = "images/sprites/duke_Shock.png"

define player = Character('[player_name]')

# Declare backgrounds
image white = "#ffffff"

# The game starts here.

label start:
    # GAME START
    # stop the menu music pls
    stop music fadeout 1.0

    scene black
    narrate "You are dying." 
    narrate "A team of medical professionals surround you. Electrodes are strapped to your chest, the monitor blares a flatline."
    nurse "—for a pulse check?"
    doctor "Resume compressions. Thirty seconds until next check."
    narrate "Your mother is holding a small bundle of paper cranes. With trembling fingers, she folds and unfolds one as the doctor speaks grimly about your condition."
    narrate "Suddenly, a blinding light tears your attention away from the scene."
    narrate "Beside you, a figure appears, silently observing the chaos below."
    angel "They're going to let you go, I'm sorry."
    menu question_angel:
        "Who are you?":
            narrate "The figure smiles serenely."
            angel "I am what lies between you and the end of all things."
        "No, that can't be right.":
            narrate "The figure shakes her head, eyes filled with sympathy."
            angel "They tried their best, but it won't be long now."
    narrate "The light in the room grows brighter. Your mom's face blurs away into the the sea of white."
    angel "It's time to let go. Are you ready?"
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

    if goal == "impact":
        angel "I see that you want to make an impact on the world."
    
    elif goal == "meaning":
        angel "I see that you want to mean something to someone."

    elif goal == "purpose":
        angel "I see that you want to discover your true purpose."

    elif goal == "exploration":
        angel "I see that you want to explore the world."
    
    narrate "The angel seems to sympathize with your words, then tilts her head, offering a soft smile."
    angel "What if it doesn't have to be?"
    
    # ooooo scene change
    scene black
    narrate "(imagine a scene change to a REALLY cool portal)"

    angel "This is the Empire of Parcae. A land of peace, virtue, and balance. But it's in peril."
    angel "When winter comes, it will be the end of everything."
    angel "I can offer you a second chance—to save this world and become the hero in the prophecy."
    narrate "A second chance.. but why you? You don't understand."
    angel "Because this world has chosen you. This is your chance to mean something to someone."
    angel "But to join, you must let go of this life and sacrifice a piece of yourself."
    nurse "Charging to 200!"
    doctor "Pause compressions. Stand clear."
    angel "Time is running out, The light will take you soon. What is your choice?"
        
    menu sacrifice:
        # Trust sacrifice
        "Sacrifice a memory of trust":
            $ fortitude = 10
            $ empathy = 20
            $ resolve = 5

        # Courage sacrifice
        "Sacrifice a memory of courage":
            $ fortitude = 5
            $ empathy = 10
            $ resolve = 20

        # Honesty
        "Sacrifice a memory of honesty":
            $ fortitude = 20
            $ empathy = 5
            $ resolve = 10
    narrate "Your current stats are:\nFortitude: [fortitude]\nEmpathy: [empathy]\nResolve: [resolve]"

    # # IM CHANGING THIS, YOU INPUT IN TUTORIAL - EMILY; INPUT NAME
    # angel "So you've decided to join this new world?"
    # angel "Then, tell me. What did they call you here on earth?"
    # $ player_name = renpy.input("Enter your name.").title().strip() or __("Stranger")

    # # If the player doesn't enter a name, they will be referred to as "Stranger"
    # if player_name == "Stranger":
    #     narrate "No? Alright, then you are a stranger."
    # else:
    #     angel "Then, [player_name]. There is one last thing you have to do."

    narrate "She smiles prettily and leans in towards you."
    angel "Touch your lips to mine, and seal your choice."

    menu kiss_her:
        "Kiss Her":
            narrate "You lean in, your lips brushing against theirs."
            narrate "The moment the kiss lands, the air thickens, and something shifts inside you."
    narrate "Suddenly, the light wilts and oozes down into thick, viscous liquid."
    narrate "Your stomach drops as the angelic figure before you morphs into something sinister."
    devil "Foolish human. There are no second chances."
    narrate "Everything shatters around you. The darkness consumes everything and swallows you whole."

    jump tutorial_start #MIA. COMMENT THIS OUT. IF YOU WANT TO DO YOUR TESTING. 

    # Current
    doctor "Time of death: [current_hour]:[minute] [ampm]." #insert actual time

    # sprite shenanigans
    narrate "sprite shenanigans"
    show mage happy
    mage "I've got a weapon, and I'm..."
    show mage concerned
    mage "I've got a weapon, and I'm... admittedly VERY afraid to use it!"

    hide mage

    # # Pronoun menus - IM MOVING THIS TOO

    # narrate "tell me ur pronouns"

    # menu pronouns:
    #     "he/him":
    #         $ p_subject = "he"
    #         $ p_object = "him"
    #         $ p_possessive = "his"
    #         $ p_possessive_adj = "his"
    #         $ p_reflexive = "himself"
    #         $ p_is = "he's"
    #         $ p_be = "is"

    #     "she/her":
    #         $ p_subject = "she"
    #         $ p_object = "her"
    #         $ p_possessive = "her"
    #         $ p_possessive_adj = "her"
    #         $ p_reflexive = "herself"
    #         $ p_is = "she's"
    #         $ p_be = "is"

    #     "they/them":
    #         $ p_subject = "they"
    #         $ p_object = "them"
    #         $ p_possessive = "their"
    #         $ p_possessive_adj = "theirs"
    #         $ p_reflexive = "themself"
    #         $ p_is = "they're"
    #         $ p_be = "are"

    # narrate "I will now refer to you as [p_subject]."
        
    # menu sacrifice:
    #     # Trust sacrifice
    #     "Your trust":
    #         $ fortitude = 10
    #         $ empathy = 20
    #         $ resolve = 5

    #     # Courage sacrifice
    #     "Your courage":
    #         $ fortitude = 5
    #         $ empathy = 10
    #         $ resolve = 20

    #     # Honesty
    #     "Your honesty":
    #         $ fortitude = 20
    #         $ empathy = 5
    #         $ resolve = 10


    jump event_0_start

# hurgles. tutorial
label tutorial_start:
    scene white with Dissolve(0.5)
    pause(0.5)
    narrate "Somewhere, not here, there is music. Everything in front of you shifts like a kaleidoscope held up to the sun."
    narrate "Your body sludges through the fractured colors, towards the light before you, until you fall through the miasma, into somewhere else."

    scene knight_bg_large with Dissolve(0.5)
    narrate "You are somewhere you have never existed before."
    narrate "The sounds that ring in your ears vibrate like waves but they are not."
    narrate "The floor beneath you looks like wood but it is not wood."
    narrate "Like a newborn thrust into cold air for the first time, you are lost."
    unknown "Let them rest a moment..."
    unknown "Be at ease, you are in the Temple of Amari. Welcome to Parcae."
    narrate "Your vision clears. When you look up, your eyes scan across a grand hall bathed in candlelight."
    narrate "Then, your eyes land on two figures, one fine armor is dressed in fine armor and stands at attention beside someone in ceremonial robes."
    priest "Chosen One, blessed by our great deity Amari, we are so glad you've come to us."
    priest "Your arrival is a gift to the Empire. The Holy Order welcomes you."
    narrate "The knight beside him takes a step towards you and bows deeply."
    knight "I know this must be overwhelming, but... you're here. We are honored to meet you."
    narrate "No. You shouldn't be here. You know that much. You shouldn't be here because... because..."
    narrate "You try to remember, reaching back to a time before this. Your head throbs."
    priest "Tell us, what name should we call you by?"
    $ player_name = renpy.input("Enter your name.").title().strip() or __("Stranger")

    # If the player doesn't enter a name, they will be referred to as "Stranger"
    if player_name == "Stranger":
        narrate "No? Alright, then you are a stranger."

    knight "We are honored to meet you [player_name]. May I also ask, how do you prefer to be referred to?"

    menu pronouns:
        "he/him":
            $ p_subject = "he"
            $ p_object = "him"
            $ p_possessive = "his"
            $ p_possessive_adj = "his"
            $ p_reflexive = "himself"
            $ p_is = "he's"
            $ p_be = "is"

        "she/her":
            $ p_subject = "she"
            $ p_object = "her"
            $ p_possessive = "her"
            $ p_possessive_adj = "hers"
            $ p_reflexive = "herself"
            $ p_is = "she's"
            $ p_be = "is"

        "they/them":
            $ p_subject = "they"
            $ p_object = "them"
            $ p_possessive = "their"
            $ p_possessive_adj = "theirs"
            $ p_reflexive = "themself"
            $ p_is = "they're"
            $ p_be = "are"

    narrate "I will now refer to you as [p_subject]."
    knight "I will notify the others to bring you to our prophecy."
    knight "Oh I'm getting ahead of myself I apologize. You must have questions, please let me know and I will do my best to answer."
    menu:
        "Who are these people?":
            narrate "Emily needs to write this still smh"
        "What do they mean by prophecy?":
            narrate "Emily still needs to write this smh"
        "{b}You have forgotten something horribly important{/b}":
            narrate "Emily still needs to write this smh"

    narrate "Basically, blah blah blah youre at the prophecy now  "
    prophecy " Come the diamond fractals in the air, a witch is born with two moons to spare."
    prophecy "If the old wall weeps and hears its tongue, the path is set with the right hand of the sun."
    prophecy "Then, for the empire's heart, bring forth its shield, and for knowledge, a conductor of the magic's field."
    prophecy "Three gates bow down for each price once paid,"
    prophecy "But the witch alone pierces the umbra of Parcae."

    narrate "OK its time for emily to go to bed"

    player "that knight guy said that like. i could visit him. maybe i should do that....."
    player "tryna figure out what the hell to do with this prophecy is like kinda daunting actually."
    player "yeah. yeah lets go visit that knight and see what hes got to say."

    # From here player goes to knight.rpy -> knight_check -> knight_encounter_tutorial
    $ knight_available = True
    show screen map
    window hide

    pause

label day_start:
    scene knight_bg_large with Dissolve(0.5)
    $ week += 1
    narrate "u wake up. you have [11 - week] weeks left to save the world. (this is the day_start label)"
    narrate "It is currently week [week]."

    if week == 11:
        narrate "you are out of time."
        narrate "its time to face ur destiny or some shit."
        jump trial_1_start

    narrate "(pls god nothings implemented past this point u WILL run into an error if u interact with that map)"

    show screen map
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

