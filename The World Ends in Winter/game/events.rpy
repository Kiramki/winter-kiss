# This file is meant to contain the main events.

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

