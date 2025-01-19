# This file is meant to contain the main events.

## EVENT 1 - Recruitment Conflict ##
label event_1_start:
    scene mage_bg_large with Dissolve(0.5)
    # narrate "GOOD JOB TEAM. YOUVE ASSEMBLED THE... prophecy guys???"
    # narrate "(fuck. this doesnt look like a great team at all)"
    narrate "You stand at the entrance of the temple, the Holy Knight at your side."
    narrate "Their calm demeanor doesn’t betray much, but something in their rigid posture hints at unease."
    narrate "The sky above is painted in amber and gold, an unnatural beauty that makes it feel like someone painted over reality."
    narrate "This world isn’t yours. Even the light feels alien."
    narrate "The rhythmic clatter of hooves pulls your attention to the temple’s winding path. The Duke is the first to arrive, seated atop an elegant, coal-black steed."
    show duke neutral at center
    duke "I hope this isn't a waste of my time." 
    narrate "He looks like he’s bitten into something sour as he's dismounting. It's clear he doesn't want to be here."
    show mage concerned at slight_right
    show duke at slight_left
    narrate "Not long after the mage appears, looking small with his arms crossed over himself; and hastily trails into the temple entrance almost as if it will keep him safe from what’s to come."
    mage "..."
    narrate "The air is thick with awkward tension as the group gathers in the temple’s grand hall."
    knight "Well, this is everyone, then: the Shield of the Empire, the Conductor of Magics, and the Right Hand of the Sun. Together, we are tasked with fulfilling the prophecy."
    narrate "A pause. They glance at each of you, their tone softening."
    knight "Before we begin... I should warn you. Things have been worsening across the land—the monster attacks, the bitter cold—it’s all connected. The curse has taken root, and based on the prophecy…"
    narrate "They hesitate for a moment before continuing."
    knight "…we have ten weeks before the world ends."
    narrate "There’s silence for a moment before the words seem to ripple across the group."
    duke "{i}Ten weeks?{/i} That’s absurd! The temple spoke of no cause for concern!"
    narrator "The Mage seems to grip himself tighter and sits down shakily on a nearby bench, while the Duke paces around the room."
    duke "If that’s true, I should be back at my duchy preparing evacuation plans—not. gallivanting off on some wild prophecy hunt! My people need me."
    mage "Yes, I- I shouldn’t be here. All my, studies are at the tower. All my resources - There’s no way we can, face whatever this is if we don’t understand it."
    show knight at center
    with hpunch
    show mage at right
    show duke at left
    knight "Please, everyone! Let’s not panic."
    narrate "The Knight gestures at the group in a frantic motion reminiscent of someone trying to disperse smoke before it sets off a fire alarm."
    knight "The prophecy chose us for a reason, and the Chosen Witch will lead us. We can trust [p_object]."
    duke "Trust [p_object]? {i}Trust [p_object]{/i}? We’ve just met [p_object]! Blind faith in words on a scroll isn’t leadership— it’s madness."
    duke "And I will be damned before I allow some scroll to dictate what may be right or wrong."
    mage "I know you, value this prophecy quite a bit and it is rather… formal;"
    mage "but this is an enormous responsibility you’re putting onto this, unfortunate - ‘chosen one’, and not to mention the rest of us…"
    narrate "To this, the knight seems to falter for the first time. They turn to you, clearly expecting you to say something that will steady the group."
    menu event_1_convince:
        "Convince them earnestly":
            jump event_1_convince_earnest
        "Use the prophecy to assert credibility":
            jump event_1_convince_assert

label event_1_convince_earnest:
    narrate "You hesitate for a moment, listening and understanding just where the Mage and Duke are coming from in their worries."
    narrate "It's true that the Grand Temple has placed a lot of heavy responsibilities on your shoulders despite you barely existing in the world for more than 24 hours."
    narrate "Still, it's your job as the Chosen One to save the world now…isn't it?"
    narrate "You express your understanding of their concerns and sympathize, stating that you didn't know this would be happening either."
    narrate "But now that it's been proven they're also chosen by the prophecy, it's clear this must be what the deity Amari wants even if it doesn't seem clear right away."
    narrate "The knight seems relieved that you've brought up the god and relaxes the tension in their shoulders a bit, but the Duke and the Mage still seem a bit stand-offish."
    narrate "You continue by saying that the four of you will learn as you go together, through whatever trials the deity chooses to throw your way."
    narrate "You may be a newcomer, but you don't want this world to end and you know neither do they."
    jump event_1_middle

label event_1_convince_assert:
    narrate "You can't help but feel a bit upset by the Mage's words and the backlash from the Duke. The Knight and the Temple you all stand outside has placed this huge responsibility on your shoulders and did little to prepare you for the potential of failure."
    narrate "Squaring your shoulders, you clear your throat and now have the attention of the three as they wait in silence for you to speak."
    narrate "You tell the Duke and the Mage that {i}you{/i} were the one that was brought into this world to save it as proven by the prophecy. That you were able to decipher text even the Grand Priest could not and managed to find the three important saviors mentioned in the prophecy. Were it not for you, then it would have gone unread and the world would have ended unaware."
    narrate "You end your frustrated spiel by stating that you would like a little more cooperation and credibility, given that you appeared by the will of the Deity and were thrust into this situation just like the rest of them were."
    jump event_1_middle

label event_1_convince_silence:
    narrate "Just by looking back at the three who appear to clash and would never meet or band together outside of this bizarre situation, your chest feels tight and you struggle to find the words to comfort them."
    narrate "You silently agree with the Duke and the Mage, understanding where they're coming from and why they hesitate to just put faith in both you and the prophecy they'd only learned the most dire parts of. The Knight did put a lot of sudden responsibility on your shoulders despite you being a newcomer to this world barely 24 hours in."
    narrate "Your hesitance comes off as silence - you can't force yourself to bring confidence to a group you don't feel confident in, after all."
    jump event_1_middle

label event_1_middle:
    narrate "The Duke shakes his head, turning toward the exit."
    duke "This is a waste of time. I won’t stand by while my people suffer. If you need me, you know where to find me."
    narrate "Just as the Duke moves to leave, the ground trembles violently beneath your feet. Dust and debris rain down from the temple’s ceiling as the air hums with unfamiliar magic."
    mage "What was that?"
    narrate "From the look on everyone else's faces, it seems no one knows for sure. Both the knight and Duke grab the swords at their hips and move to stand on guard. For now it seems that the Duke has forgotten about leaving."
    narrate "The floor beneath you shifts and, with a groaning creak, a hidden staircase reveals itself leading deeper into the temple. The group exchanges wary glances before descending - the Duke and Knight in lead, with you and the Mage following behind."
    narrate "When you reach the bottom, your shoes step onto a somewhat slick, reflective surface, and you are met with an entirely different setting—a vast chamber stretching before you."
    narrate "As the group cautiously files deeper into the room, your steps leave faint glowing footprints behind you as you walk."
    narrate "Before you looms three grand doors, each adorned with unique, intricate carvings."
    narrate "On each of the doors is a somewhat legible engraving that resembles the prophecy written on the scroll. You squint at it in an attempt to better read it."
    narrate "(to be filled out once we have the background for it)"
    scene black with Dissolve(0.5)
    jump day_dreams



## EVENT 2 - Trying and FAILING to work together ##
label event_2_start:
    scene duke_bg_large with Dissolve(0.5)
    narrate "Alright team. We've assembled the prophecy guys. We gotta practice together"
    show duke neutral at center 
    with Dissolve(0.5)
    duke ">:("
    show duke neutral at slight_left
    show mage neutral at slight_right
    mage ">:("
    knight ">:("
    narrate "........ shit"

    scene black with Dissolve(0.5)
    jump day_dreams

## EVENT 3 - BIG CONFLICT ##
label event_3_start:
    scene knight_bg_large with Dissolve(0.5)
    narrate "ALRIGHT. ALRIGHT. SURELY WE WILL IMPROVE"
    show duke neutral at slight_left
    show mage neutral at slight_right
    duke "D:<"
    mage "D:<"
    knight "guys... guys......"
    show duke shock
    show mage concern
    narrate "ok... ok um. hm. uuuuuOHSHITISTHATAMONSTER"
    narrate "AUGHGUHGOHGOD"

    scene black with Dissolve(0.5)
    jump day_dreams

## EVENT 4 - GAY turning point ##
label event_4_start:
    scene knight_bg_large with Dissolve(0.5)
    knight "[player_name]. listen. we need to do something about [duke_name] and [mage_name]."
    player "youre. so right."
    narrate "(resolution noises)"
    narrate "(and then they kiss or something. ooo. gay people. i could write a 5+1 fanfic about this)"

    scene black with Dissolve(0.5)
    jump day_dreams

## EVENT 5 - Brace for the end ##
label event_5_start:
    scene mage_bg_large with Dissolve(0.5)
    narrate "so we're all getting together for a COOL HOLIDAY. WOOHOO"
    knight "we are all so cool :)"
    duke ":D"
    mage ":D"
    player "FANTASTIC. WE'RE SO READY FOR THIS."
    narrate "haha whats that sound"
    narrate "we really need to get to those trials"

    scene black with Dissolve(0.5)
    jump day_dreams