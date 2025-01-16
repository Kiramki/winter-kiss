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

    # Declare current week
    week = 0

    # Declare number of encounters
    mage_encounters = 0
    knight_encounters = 0
    duke_encounters = 0

    # Flags for areas of the map that are available

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



# Define positions
transform slight_left:
    xalign 0.25

transform slight_left_from_center:
    xalign 0.5
    linear 0.5 xalign 0.25

transform slight_right:
    xalign 0.75

# Declare the characters + sprites that will be used in the game.

define narrate = Character('Narrator')
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

# The game starts here.

label start:
    # GAME START
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

    # INPUT NAME
    angel "So you've decided to join this new world?"
    angel "Then, tell me. What did they call you here on earth?"
    $ player_name = renpy.input("Enter your name.").title().strip() or __("Stranger")

    # If the player doesn't enter a name, they will be referred to as "Stranger"
    if player_name == "Stranger":
        narrate "No? Alright, then you are a stranger."
    else:
        angel "Then, [player_name]. There is one last thing you have to do."

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

    # Current
    doctor "Time of death: [current_hour]:[minute] [ampm]." #insert actual time # dear LORD

    narrate "WISP. THIS IS. FOR YOU!"
    narrate "Before you an ivory structure threatens to scrape the clouds that hang just above its highest peak; piercing the sky like the icy sun rays themselves. It is no wonder they call it The Mage Tower."

    narrate "Upon approaching its doors, you find that you are hastily ushered inside and out of the winter's reach."
    narrate "Fire sprites dance lazily through the foyer, illuminating their surroundings with curiosity; as who you assume to be mages scurry about on their routine business."
    narrate "Already, you can hear passing murmurs regarding their conductor - The Arch-Mage."
    narrate "It is easy to gather already that he is a person of importance to those within the tower; further proven by the sheer amount of textbooks that appear to be signed by him."
    narrate "Pulling your attention away, you inquire about an audience with none other than the arch-mage himself."

    narrate "Guided to the tower's uppermost floor, you come face to face with the mage."
    narrate "He stands near the center before a table littered with dozens of different texts and rather strange looking specimens, leaning heavily with a palm to the tabletop."
    narrate "Believing you to be simply another one of the mages, he begins rambling about something you couldn't even begin fathoming to summarize before sighing and coming to a pause."

    mage "Oh… It's rare to get a visitor - I suppose I was getting carried away. How may I be of assistance?"

    narrate "You announce that you are the chosen one foretold by the prophecy. A flash of unease crosses his face and his posture seems to stiffen up."

    mage "The… prophecy-? Good Amari. You know what you're claiming, aren't you?"

    narrate "You explain that he is stated to be one of the companions of the prophecy."

    narrate "You must be mistaken. There is no way the prophecy would have any use for me. I'm certain Amari would have chosen a more promising mage if anything."

    menu mage_tutorial:
        "Reassure him that it seems he is already rather looked up to by his peers.":
            narrate "You explain to him that from the moment you walked in the doors, you've already heard several passing conversations concerning him and his steady tutelage. Surely someone as looked up to as he would have a place in the prophecy."
            narrate "Giving him a sincere look, you request that he assists you as well on your journey."
            mage "If you truly think you need my guidance.. I suppose I can try my best to aid you. But please do not be disappointed when my methods prove subpar."
        "Assert the prophecy's undeniability and your determination to see it through.":
            narrate "You ask him if he was the one who read the prophecy or if it was you, as you clearly recall. What was written was not a question, but a demand. Standing firm, you tell him that he is who was called for whether he likes it or not."
            mage "... If you insist."
        "Announce that you've already seen the number of study materials he's published as a knowledgeable mage.":
            narrate "You point to the books on the table and blatantly show that he is the author of the study material being referenced. You ask him what he could even mean by a 'more promising' mage when he's already proven to be quite dedicated and knowledgeable."
            mage "…You're braver than you look. If you're willing to stand by me, I guess I can take a leap of faith. Let's hope you're as good as your word."
    narrate "The mage agrees to meet with you at the temple tonight with the rest of the companions."
    narrate"Despite this triumph, you feel a heavily charged atmosphere at your back that crackles with uncertainty and raises the hairs along the back of your neck as you turn to leave."


    # sprite shenanigans
    narrate "sprite shenanigans"
    show mage happy
    mage "I've got a weapon, and I'm..."
    show mage concerned
    mage "I've got a weapon, and I'm... admittedly VERY afraid to use it!"

    hide mage

    # Pronoun menus

    narrate "tell me ur pronouns"

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
            $ p_possessive_adj = "her"
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
    narrate "TUTORIAL MOMENT"
    player "oh damn. what do i do now."
    player "that knight guy said that like. i could visit him. maybe i should do that....."
    player "tryna figure out what the hell to do with this prophecy is like kinda daunting actually."

label day_start:
    $ week += 1
    narrate "you are now in the day_start label"
    narrate "It is currently week [week]."

    show screen map
    window hide

    pause

label day_end:
    narrate "you are now in the day_end label. on certain weeks you might have a dream sequence or a main event."

