# This file is meant to contain the main events.

## EVENT 1 - Recruitment Conflict ##
label event_1_start:
    scene knight_outside with Dissolve(0.5)
    # narrate "GOOD JOB TEAM. YOUVE ASSEMBLED THE... prophecy guys???"
    # narrate "(fuck. this doesnt look like a great team at all)"
    narrate "You stand at the entrance of the temple, the Holy Knight at your side."
    narrate "Their calm demeanor doesn't betray much, but something in their rigid posture hints at unease."
    narrate "The sky above is painted in amber and gold, an unnatural beauty that makes it feel like someone painted over reality."
    narrate "This world isn't yours. Even the light feels alien."
    narrate "The rhythmic clatter of hooves pulls your attention to the temple's winding path. The Duke is the first to arrive, seated atop an elegant, coal-black steed."
    show duke neutral at center
    duke "I hope this isn't a waste of my time." 
    narrate "He looks like he's bitten into something sour as he's dismounting. It's clear he doesn't want to be here."
    show mage concerned at slight_right
    show duke at slight_left
    narrate "Not long after the mage appears, looking small with his arms crossed over himself; and hastily trails into the temple entrance almost as if it will keep him safe from what’s to come."
    mage "..."
    narrate "The air is thick with awkward tension as the group gathers in the temple's grand hall."
    scene knight_main with Dissolve(0.5)
    voice "audio/voice/knight/line0019.ogg"
    knight "Well, this is everyone, then: the Shield of the Empire, the Conductor of Magics, and the Right Hand of the Sun."
    voice "audio/voice/knight/line0020.ogg"
    knight "Together, we are tasked with fulfilling the prophecy."
    narrate "A pause. They glance at each of you, their tone softening."
    voice "audio/voice/knight/line0021.ogg"
    knight "Before we begin... I should warn you. Things have been worsening across the land."
    voice "audio/voice/knight/line0022.ogg"
    knight "The monster attacks, the bitter cold—it's all connected."
    voice "audio/voice/knight/line0023.ogg"
    knight "The curse has taken root, and based on the prophecy…"
    narrate "They hesitate for a moment before continuing."
    voice "audio/voice/knight/line0024.ogg"
    knight "…We have {color=#8b67b0}{b}10 WEEKS{/b}{/color} before the world ends."
    narrate "There's silence for a moment before the words seem to ripple across the group."
    duke "{i}Ten weeks?{/i} That's absurd! The temple spoke of no cause for concern!"
    voice "audio/voice/mage/noise2.ogg"
    narrator "The Mage seems to grip himself tighter and sits down shakily on a nearby bench, while the Duke paces around the room."
    duke "If that's true, I should be back at my duchy preparing evacuation plans—not. gallivanting off on some wild prophecy hunt! My people need me."
    voice "audio/voice/mage/line0009.ogg"
    mage "Yes, I- I shouldn't be here. All my, studies are at the tower. All my resources - There's no way we can, face whatever this is if we don't understand it."
    show knight at center
    with hpunch
    show mage at right
    show duke at left
    voice "audio/voice/knight/line0025.ogg"
    knight "Please, everyone! Let's not panic."
    narrate "The Knight gestures at the group in a frantic motion reminiscent of someone trying to disperse smoke before it sets off a fire alarm."
    voice "audio/voice/knight/line0026.ogg"
    knight "The prophecy chose us for a reason, and the Chosen Witch will lead us."
    if p_object == "her":
        voice "audio/voice/knight/line0027.ogg"
    elif p_object == "them":
        voice "audio/voice/knight/line0028.ogg"
    else:
        voice "audio/voice/knight/line0029.ogg"
    knight "We can trust [p_object]."
    duke "Trust [p_object]? {i}Trust [p_object]{/i}? We've just met [p_object]! Blind faith in words on a scroll isn't leadership— it's madness."
    duke "And I will be damned before I allow some scroll to dictate what may be right or wrong."
    voice "audio/voice/mage/line0010.ogg"
    mage "I know you, value this prophecy quite a bit and it is rather… formal..."
    voice "audio/voice/mage/line0011.ogg"
    mage "but this is an enormous responsibility you're putting onto this, unfortunate - 'chosen one', and not to mention the rest of us…"
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
    duke "This is a waste of time. I won't stand by while my people suffer. If you need me, you know where to find me."
    narrate "Just as the Duke moves to leave, the ground trembles violently beneath your feet. Dust and debris rain down from the temple's ceiling as the air hums with unfamiliar magic."
    voice "audio/voice/mage/line0012.ogg"
    mage "What was that?"
    narrate "From the look on everyone else's faces, it seems no one knows for sure. Both the knight and Duke grab the swords at their hips and move to stand on guard. For now it seems that the Duke has forgotten about leaving."
    narrate "The floor beneath you shifts and, with a groaning creak, a hidden staircase reveals itself leading deeper into the temple. The group exchanges wary glances before descending - the Duke and Knight in lead, with you and the Mage following behind."
    scene black with Dissolve(0.5)
    narrate "When you reach the bottom, your shoes step onto a somewhat slick, reflective surface, and you are met with an entirely different setting—a vast chamber stretching before you."
    narrate "As the group cautiously files deeper into the room, your steps leave faint glowing footprints behind you as you walk."
    narrate "Before you looms three grand doors, each adorned with unique, intricate carvings."
    narrate "Scratched into the wall above the doors is a singular line."
    centered "{i}Three gates shall bow down for each price once paid{/i}"
    narrate "The Holy Knight watches you as you mutter the words under your breath, tilting your head in perplexity. What could this mean?"
    narrate "Suddenly, each door begins to glow. You can clearly make out the inscriptions above them."
    centered "The first door, addressed to The Empire's Shield, reads: {color=#8b67b0}{b}The Trial of Trust{/b}{/color}"
    narrate "The Duke takes a visible step back, his expression hardening."
    duke "Absolutely not. I refuse to participate in a 'trust trial'."
    centered "The second, for The Conductor of Magics, reads: {color=#8b67b0}{b}The Trial of Courage{/b}{/color}"
    voice "audio/voice/mage/line0013.ogg"
    mage "I'm not sure I like the implications of this…"
    narrate "This seems to unsettle him, but he does not elaborate further."
    centered "The third, for The Hand of the Sun, reads: {color=#8b67b0}{b}The Trial of Honesty{/b}{/color}"
    voice "audio/voice/knight/line0030.ogg"
    knight "Oh, this is fitting for me! As a knight of the Holy Order, I have been sworn to an oath of honesty."
    narrate "A heavy silence settles over the group as the reality of the trials sinks in."
    narrate "Without another word, you ascend back up to the main area of the temple with the others, the spirits of the group seem to have shifted."
    scene knight_main
    voice "audio/voice/knight/line0031.ogg"
    knight "As we all saw, with these trials it looks like we'll need all of us present in order to piece together what we have to do."
    voice "audio/voice/knight/line0032.ogg"
    knight "If we want to stop the world from ending, we need to at least try to work together..."
    voice "audio/voice/knight/line0033.ogg"
    knight "It could very well be the key to breaking the curse!"
    voice "audio/voice/mage/line0014.ogg"
    mage "Yes, I suppose you are correct. I'll do more research on the trials…the nature of these doors…"
    duke "…I still intend to prioritize the monster attacks threatening the empire. But, if there's information to be found, I'll readily track it down. If you all believe we truly can vanquish this evil, I suppose I can cooperate."
    narrate "Though still hesitant, the gathering seems to conclude with a reluctant agreement to work together as a team."
    scene knight_bg_large
    narrate "The Knight leads you to a room the other priests and hands have prepared for you in the temple. Despite the exhausting day, you don't retire immediately."
    scene hazy_sun
    narrate "Instead, you find yourself staring out the window at the world beyond. You feel like you're forgetting something important— something you can't quite grasp."
    narrate "The sun dips below the horizon and, as its warm glow fades, a quiet comfort settles within you."
    narrate "Watching it, you realize that tomorrow, you will get to see it rise again."
    scene black with Dissolve(0.5)
    centered "Your dreams are faint echoes, drifting through smoke and flame." with dissolve
    centered "your skin sears, as if burning alive."
    centered "A familiar voice emerges, soft and mocking."
    devil "Are you enjoying this little world I built?"
    devil "Or have you already forgotten the price you paid to be here?"
    pause 2.0
    centered "You have reached the end of the tutorial! Thank you for playing Forever Yours, The Devil. If you enjoyed this game, please consider following us {color=#8b67b0}@Gloamy Studios{/color} <3"
    return
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