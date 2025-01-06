# You can place the script of your game in this file.
## You may reuse the GUI, but please refrain from reusing Z since she's my OC. Thankies so much. Also, please do credit me if you use any of my graphics here: z
## You are also allowed to copy paste the codes. I also don't like it when the redistribute the game, I made this for free so please just link them to my blog or my page.
## I made this tutorial since I know the struggles of a newbie in studying the codes, I'm no expert but these are almost everything I knew in coding renpy.
## I hope it can help you create your own visual novels.
## zishy signing off! huehe~!


## This is the code for the animated main menu:
image slideshow: ##I use slideshow to define them, check the screens.rpy
    "gui/mm1.png" with dissolve
    pause 1.0
    "gui/mm2.png" with dissolve
    pause 1.0
    "gui/mm3.png" with dissolve
    pause 1.0
    "gui/mm4.png" with dissolve
    pause 1.0
    "gui/mm5.png" with dissolve
    pause 1.0
    
    ##### You can add as many as you like!
    #"gui/mm6.png" with dissolve
    #pause 1.0
    #"gui/mm7.png" with dissolve
    #pause 1.0
    repeat
    
    
#########################################################
#########################################################
##### THESE ARE THE IMAGES USED IN THE GAME!

## BACKGROUNDS
image bg park = "bg.png"
##### These backgrounds are available in my itch.io resources visit (https://zhaieyuemn.itch.io/zhaies-free-vn-assets-backgrounds)

## SPRITES
image z = "zsprite.png"
##### Z is my OC. She will appear in most of my games ^O^)/ Though she appeared at the first After Guardian Angel Game :'D

## CHARACTERS
define z = Character("Z", color="#a366ff", show_two_window=True, ctc="ctc_blink",
        ctc_position="nestled")
##### For more colors visit: w3schools.com/colors/colors_picker.asp

##### These codes are used for side images. When you want to see your mc on the screen! You can add as many as you want :'D
define zdef = Character('Z', color="#a366ff", show_two_window=True, ctc="ctc_blink",
        ctc_position="nestled", show_side_image=Image("zasmc.png", xalign=0.0, yalign=1.0))

### "show_two_window=True" is used when you want to see the character's name inside the name box. Don't forget to add that in your coding for the other characters!

### The code for customizing the text in the namebox is in the options.rpy

### This code is for the narrative of the story, enabling the Click To Continue Icon by typing: "ctc_position".
define narrator = Character(ctc="ctc_blink", ctc_position="nestled")

## CG 
image cg1 = "cg1.png"
image cg2 = "cg2.png"
image cg3 = "cg3.png"
image cg4 = "cg4.png"

########################################################
########################################################
##### OTHER FEATURES:

init:
    
##### Define points here!
    $ correct_answer = 0
    $ persistent.zugly = False
    
##### You define the MC here!

    define mc = DynamicCharacter('mc', color="#ff1a8c")
    $ mc = "Chupacabra"
    
##### This is the code for the animated rain! 
    image rain:
        "rain1.png"
        0.2
        "rain3.png"
        0.2
        "rain2.png"
        0.2
        repeat
        
    
    ##### THIS IS THE CODE FOR THE MOUSE, I use 100 x 100 as default for the mouse pointer but you can make it smaller
    $ config.mouse = { "default": [ ('mouse.png', 0, 0) ] }
    
##### This is the Click to Continue Icon code. Do you see it in the textbox? The heart one? That is the CTC, you can customize your own.
image ctc_blink:
       "ctc.png"
       linear 0.75 alpha 1.0
       linear 0.75 alpha 0.0
       repeat 
       


##### This code is for the namebox. If you want it be above the textbox, you use this :'D
init python:
    style.say_two_window_vbox.order_reverse=True


#########################################################
#########################################################
##### This is the video that will appear as you open the game! :'D

label splashscreen:
    scene black with dissolve
    voice "zishy.mp3"
    centered "{color=ffe6f2}z-ish prouductions{/color}"
    return

# The game starts here.
label start:
    ## Press SHIFT+R so you can refresh the game so you don't have to close and open it, all the time.
    scene black with dissolve
    ## black is not an image, you can set black as background without making an image for it.
    centered "{color=ffe6f2}This is a tutorial for Ren'py!{/color}"
    if persistent.tutorialdone:
        menu:
            "Let me be.":
                jump continuation
            "Straight to Z.":
                jump z_introduction
            "About Choices.":
                jump abt_choices
            "About Galleries.":
                jump abt_gallery
            "Outta here yo.":
                return
    
label continuation:
    centered "{color=ffe6f2}The game's resolution is 1280 by 720.{p}This game is using the Legacy Theme Interface.{/color}"
    centered "{color=ffe6f2}This will feature the most basic codes{p} for making your own visual novel!{/color}"
    centered "{color=ffe6f2}Like {b}BOLD{/b}, {i}Italic{/i}, and {u}Underlined{/u}{/color}.{p}{color=ff4d4d}Oh yeah.{w} Changing colors too!{/color}" ##If you are going to use a color for the font here, remove the hashtag.
    centered "{color=ffe6f2}You can check the codes by putting the game in your destination project folder and opening it using Renpy!{/color}"
    stop music fadeout 1.0 ##stop the music using this code
    
    scene bg with dissolve
    "Let there be new music!"
    play music "Digital Lemonade.mp3" ##insert music using this code
    "We shall now start with the tutorial."
    "As we start the game, you might want to rename the MC. Press Enter if you want to use the default name of the MC."
    $ mc = renpy.input("What is your name?", length=10) ##You may add length so you can limit the characters used
    $ mc = mc.title() ##This is to ensure that the mc's name will start with a capital letter
    $ mc = mc.strip()
    if mc == "":
        $ mc = "Chupacabra" ##In case, the player wants to skip the naming, he/she can use a default name!
    "Hello, {color=ff1a8c}[mc]{/color}!{w} Welcome to the tutorial!{p}Thank you for downloading the game!{w} Very much appreciated." 

label z_introduction:
    scene bg with dissolve
    ## Character Enters
    show z with dissolve
    z "Hi, creatures with no life.{w} Just kidding."
    z "I am Z."
    z "I am here to show you the way, the truth and the life...{w} or not."
    z "Anyway..."
    z "This tutorial will just feature the most basic stuff for visual novel making."
    z "Since Zishy knows the struggles of self-studying,{w} she will rescue your souls with this tutorial...{w} Hopefully."
    z "You may follow this game as you look through the codes."
    z "There are lot of ways to make your game."
    z "You are the god of your own story. Like for example..."
    z "Let there be rain!"
    show rain
    z "See there's rain now."
    z "But there's no sound...{w} Let there be rain sound!"
    play sound "rain.mp3"
    z "Okay, there's rain sound now.{w} Lmao!"
    z "Now, that's enough rain."
    stop sound fadeout 1.0
    hide rain
    z "Okay, now. I shall show you about the interactions."
    z "Pretend that I'm the mc of some visual novel."
    
label abt_choices:
    scene bg with dissolve
#### About choices
    hide z with dissolve
    zdef "Okay, I'm here now."
    zdef "Let's begin with answering few questions to give an overview about flags and points."
    menu:
        zdef "1 + 1 = ?"
        "2":
            zdef "Uh-uh."
            $ correct_answer += 1
            jump question2
        "Window":
            zdef "Well, that's another way to put it..."
            zdef "But..."
            jump question2
        "Magellan":
            zdef "Those who picked this answer is a noypi for sure."
            zdef "This is the kind of humor they are most familiar with it."
            zdef "But it's wrong.{w} You guys, are funny."
            jump question2
        "What kind of question is that?":
            zdef "Come on, it's just a sample question."
            zdef "Such a party pooper."
            jump question2

label question2:
    zdef "Let's move to the next random question."
    menu:
        zdef "If you're happy and you know it..."
        "Shake your butt.":
            zdef "Yeah, shake that booty-"
            zdef "Just kidding."
            jump question3
        "I just know it.":
            zdef "Well, yeah sure."
            jump question3
        "Clap your hands.":
            zdef "Clap Clap Clap!"
            $ correct_answer += 1
            jump question3
        "I was never happy.":
            zdef "What are you emo?"
            zdef "That's not good.{w} Don't be emo."
            jump question3
        
label question3:
    zdef "And for the last but not the least, nonsense question."
    menu:
        zdef "Is zishy pretty?"
        "No.":
            $ persistent.zugly = True
            zdef "Good thing she doesn't know you're picking this option.{w} Haha."
            jump questioningends
        "Yes.":
            zdef "I shall thank you in behalf of her."
            jump questioningends
        "How should I know?":
            zdef "I also want to question why there's such question like this appearing here."
            jump questioningends
            
label questioningends:
    zdef "And that's it for the set of questions."
    if correct_answer >= 2:
        zdef "You have 2 correct answers."
        zdef "Very good~"
        jump moreconvo
    elif correct_answer >= 1:
        zdef "You got one correct answer."
        jump moreconvo
    elif correct_answer >= 0:
        zdef "You are randomly picking answers, aren't you?"
        jump moreconvo
        
label moreconvo:
    if persistent.zugly:
        zdef "I still can't forget that you think Zishy is ugly.{w} Haha."
    zdef "Anyway, you can check the codes as we go on with the tutorial so you can apply it on your project."
    
label abt_gallery:
    scene bg with dissolve
    ### About the Gallery
    zdef "I shall now show you how the CG works."
    zdef "Just in case you are not aware, there is a CG and Music Gallery in this tutorial."
    zdef "I'll be borrowing free CG's online."
    scene cg1 with dissolve
    zdef "See this is a sample of a good CG.{w} This one is drawn by BCS."
    zdef "Zishy's CG's are crappy."
    scene cg2 with dissolve
    zdef "This is the second CG."
    zdef "While we're at it, you might want to check the CG Gallery if it's working."
    zdef "..."
    zdef "Have you checked it?"
    scene cg3 with dissolve
    zdef "Okay, we're going to continue this until the last one."
    zdef "Is it working?{w} Nah?"
    scene cg4 with dissolve
    zdef "It's working right?"
    zdef "Yehey for us!"
    scene bg with dissolve
    show z with dissolve
    z "You can also check the Music Room or Music Gallery."
    z "The sample GUI for the Music Room is available in the folders along with the PSD file, and the RPY file."
    z "Kindly consult that if you're lost."
    z "You may reuse the GUI's and customize it to your liking."
    z "I think that's it for this tutorial."
    z "I don't have anything else to teach to be honest."
    z "I do hope this helps...{w} If not, too bad."
    z "Bye-bye, [mc]."
    z "See you soon!"
    
    $ persistent.tutorialdone = True
    ## Remember to clear the persistent before distributing!
    $ renpy.movie_cutscene("zishy.webm")
    ## Remember to convert your videos to webm, okay?
    return
