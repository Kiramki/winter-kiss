# This file is meant to contain the main events.

## EVENT 0 ##
label event_0_start:
    narrate "YOOOOOO YOURE IN A TEMPLE NOW"
    narrate "AND THERES A KNIGHT HERE HOLYYYY SHIIIITTTTTTTTTT"

    knight "hey. theres like. a prophecy. and i cant read it"
    knight "also like ur the chosen one welcome to parcae"
    knight "here u go"

    narrate "(REALLY COOL PROPHECY WORLDBUILDING)"

    player "damn. what do i do now"

    menu what_now:
        "hey do u like have a map":
            jump event_0_map

        "(just leave)":
            jump event_0_leave

        "I DONT KNOWWWW :(((":
            jump event_0_idk

label event_0_map:
    player "do u like.... have a map"
    knight "I DO thank you for asking"
    knight "here u go"

    narrate "(a cool cool cool map appears and the player gets an initial look for a moment)"

    # imagine this map as a filled out map and not an empty one
    scene map_default
    with Dissolve(1)
    pause
    scene black
    with Dissolve(1)

    jump event_0_continue

label event_0_leave:
    player "alright. well. bye"
    knight "WAIT. WAIT. WAIT HANG ON. I HAVE A MAP FOR YOU. TAKE THE MAP"

    narrate "(map get! u look at it)"
    
    # imagine this map as a filled out map and not an empty one
    scene map_default
    with Dissolve(1)
    pause
    scene black
    with Dissolve(1)

    jump event_0_continue


label event_0_idk:
    player "i dont know what to do now :((( what do i do :("
    knight "well. maybe u should like. start with the prophecy. here take a map"

    narrate "(u look at a map)"

    # imagine this map as a filled out map and not an empty one
    scene map_default
    with Dissolve(1)
    pause
    scene black
    with Dissolve(1)

    jump event_0_continue

label event_0_continue:
    narrate "(continuing moment)"

    narrate "ooo u event so hard"
    narrate "u gotta save the world with three losers"
    narrate "and now u go to wherever the player goes to contemplate how to start their week"

    jump tutorial_start


## EVENT 1 - Recruitment Conflict ##
label event_1_start:
    scene mage_bg_large with Dissolve(0.5)
    narrate "GOOD JOB TEAM. YOUVE ASSEMBLED THE... prophecy guys???"
    narrate "(fuck. this doesnt look like a great team at all)"

    show duke neutral at center
    duke "ok so like the world is literally going to end. we need to do this shit fast we all have things to do"
    
    show mage concerned at slight_right
    show duke at slight_left
    mage "um. no. uh. im pretty sure we need to like.... prepare"
    duke "so like actually. fuck you"
    show knight at center
    with hpunch
    show mage at right
    show duke at left

    knight "ha HA HA GUYS what if we like DONT be mean to each other and"
    player "AAAA CAN WE FOCUS"

    narrate "my god. we have our work cut out for us."

    narrate "something something, a super appropriate transition to everyone going home after agreeing...."
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