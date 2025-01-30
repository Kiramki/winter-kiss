# This file is meant to contain the encounters with the Wizard that the player has when they visit their location on the map.

label mage_check:
    scene mage_outside
    hide screen map with Dissolve(0.5)

    narrate "{i}You make your way to [mage_name]'s tower.{/i}"

    show mage neutral
    mage "omg heyyyyyy :)"

    narrate "{i}Should I spend time with [mage_name]?{/i}"
    menu mage_menu:
        "Yes":
            jump mage_idle
        "No":
            narrate "{i}You decide to leave the Mage's tower.{/i}"
            show screen map with Dissolve(0.5)
            pause

label mage_idle:
    jump mage_encounter_tutorial

label mage_encounter_tutorial:
    narrate "Before you an ivory structure threatens to scrape the clouds that hang just above its highest peak; piercing the sky like the icy sun rays themselves. It is no wonder they call it The Mage Tower."

    narrate "Upon approaching its doors, you find that you are hastily ushered inside and out of the winter’s reach."
    narrate "Fire sprites dance lazily through the foyer, illuminating their surroundings with curiosity; as who you assume to be mages scurry about on their routine business. "
    narrate "Already, you can hear passing murmurs regarding their conductor - The Arch-Mage."
    narrate "It is easy to gather already that he is a person of importance to those within the tower; further proven by the sheer amount of textbooks that appear to be signed by him."
    narrate "Pulling your attention away, you inquire about an audience with none other than the arch-mage himself."
    narrate "Guided to the tower’s uppermost floor, you come face to face with the mage."
    scene mage_main
    narrate "He stands near the center before a table littered with dozens of different texts and rather strange looking specimens, leaning heavily with a palm to the tabletop."
    narrate "Believing you to be simply another one of the mages, he begins rambling about something you couldn’t even begin fathoming to summarize before sighing and coming to a pause."
    mage "Oh… It's rare to get a visitor - I suppose I was getting a bit carried away. How may I be of assistance?"
    narrate "You announce that you are the chosen one foretold by the prophecy. A flash of unease crosses his face and his posture seems to stiffen up."
    mage "The… prophecy-? Good Amari. You know what you're claiming, aren't you?"
    narrate "You explain that he is stated to be one of the companions of the prophecy."
    mage "You must be mistaken. There is no way the prophecy would have any use for me. I'm certain Amari would have chosen a more promising mage if anything."

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
            mage "... I suppose you’re right. I have worked hard to get here.. I’ll do my best to be of use."
    narrate "The mage agrees to meet with you at the temple tonight with the rest of the companions."
    narrate "Despite this triumph, you feel a heavily charged atmosphere at your back that crackles with uncertainty and raises the hairs along the back of your neck as you turn to leave."

    scene mage_outside with Dissolve(0.5)
    narrate "You decide to leave [mage_name]'s tower."
    narrate "According to the prophecy, there's only one last member to recruit. {i}The shield of the empire{/i}."
    #narrate "The last person you need to meet is the duke guy......"
    #narrate "hope that recruiting this guy goes better than with the other two!! man, who woulda thought that trying to convince people that they're part of a prophecy where the world hangs in the balance would be so DIFFICULT"

    $ mage_encounters += 1
    $ mage_available = False
    $ duke_available = True

    show screen map with Dissolve(0.5)
    hide window
    pause

