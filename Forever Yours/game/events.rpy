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


## EVENT 1 ##
label event_1_start:
    scene mage_bg_large with Dissolve(0.5)
    narrate "GOOD JOB TEAM. YOUVE ASSEMBLED THE... prophecy guys???"
    narrate "(fuck. this doesnt look like a great team at all)"

    show duke neutral at center
    duke "ok so like the world is literally going to end. we need to do this shit fast we all have things to do"
    show duke at slight_left
    show mage concerned at slight_right
    mage "um. no. uh. im pretty sure we need to like.... prepare"
    duke "so like actually. fuck you"
    knight "ha HA HA GUYS what if we like DONT be mean to each other and"
    player "AAAA CAN WE FOCUS"

    narrate "my god. we have our work cut out for us."

    narrate "something something, a super appropriate transition to everyone going home after agreeing...."
    scene black with Dissolve(0.5)
    jump day_start