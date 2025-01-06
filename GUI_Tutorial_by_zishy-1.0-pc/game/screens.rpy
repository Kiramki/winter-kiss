# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
##############################################################################

# Zishy notes: I only changed the main menu, preference, save/load, quickmenu and the yes/no prompt. That is all I customized in this tutorial.
# The NVL is pretty easy to customize so I leave that to you :3
# Every GUI here has their own psd file in the folders, be sure to check them!
# Oh but I didn't include the psd file for the textbox, namebox and quickmenu! Sorry OvO);
# Anyway, I hope this codes will help even a little.

##############################################################################
##############################################################################

# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice:

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5  

        
        vbox:
            style "menu"
            spacing 2
            
            for caption, action, chosen in items:
                
                if action:  
                    if chosen:
                        button:
                            action action
                            style "menu_choice_chosen_button"                        

                            text caption style "menu_choice_chosen"
                    else:
                        button:
                            action action
                            style "menu_choice_button"                        

                            text caption style "menu_choice"
                    
                else:
                    text caption style "menu_caption"



init python:
    #### You declare here the choice buttons. 
    style.menu_choice_button.background = Frame("choice_chosen.png",44,44)
    style.menu_choice_button.hover_background = Frame("hchoice.png",44,44)
    style.menu_choice_chosen_button.background = Frame("choice.png",44,44)
    style.menu_choice_chosen_button.hover_background = Frame("hchosen.png",44,44)

    #### These is where you customize the font of the choice buttons.
    style.menu_choice.color = "#1a0d00"
    style.menu_choice_chosen.color = "#006666"
    style.menu_choice.size = 33

    

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.44)
        xmaximum int(config.screen_width * 0.77)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
screen main_menu:

    # This ensures that any other menu screen is replaced.
    tag menu

    # The background of the main menu.
    window:
        style "mm_root"

    imagemap:
        ground "slideshow"
        idle "gui/mm_idle.png"
        hover "gui/mm_hover.png"

        hotspot (911, 117, 224, 89) action Start()
        hotspot (911, 206, 224, 85) action ShowMenu("load")
        hotspot (911, 291, 319, 98) action ShowMenu("preferences")
        hotspot (911, 389, 290, 85) action ShowMenu("extras")
        hotspot (911, 474, 182, 104) action Quit(confirm=False)
        
        ### How to get the 4 dimensions? (1) Open the Main Menu.psd in the folders, (2) Right Click CROP and Click SLICE TOOL, (3) then Right click the area where the button is placed/sliced and hit EDIT SLICE OPTIONS
        ### Same thing with the other psd files and menus.

init -2 python:

    # Make all the main menu buttons be the same size.
    style.mm_button.size_group = "mm"



##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():

    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    frame:
        style_group "gm_nav"
        xalign .98
        yalign .98

        has vbox

        textbutton _("Return") action Return()
        textbutton _("Preferences") action ShowMenu("preferences")
        textbutton _("Save Game") action ShowMenu("save")
        textbutton _("Load Game") action ShowMenu("load")
        textbutton _("Main Menu") action MainMenu()
        textbutton _("Help") action Help()
        textbutton _("Quit") action Quit()

init -2:

    # Make all game menu navigation buttons the same size.
    style gm_nav_button:
        size_group "gm_nav"


##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot"), FileSaveName(number))
    add FileScreenshot(number) xpos -1 ypos 0
    text file_text xpos 11 ypos -24 size 15  color "#000000"
 
screen load:
    
    tag menu
    
    imagemap:
        ground 'saveload_ground.png'
        idle 'saveload_idle.png'
        hover 'saveload_hover.png'
        selected_idle 'saveload_selected.png'
        selected_hover 'saveload_hover.png'
        cache False
        
        hotspot (712, 616, 74, 96) action FilePage(1) 
        hotspot (883, 616, 75, 96) action FilePage(2)
        
        ## You might get confused but these one below are the save/load slots, those boxes.
        hotspot (442, 58, 339, 244) action FileAction(1):
            use load_save_slot(number=1)
        hotspot (886, 58, 339, 244) action FileAction(2):
            use load_save_slot(number=2)
        hotspot (442, 348, 339, 244) action FileAction(3):
            use load_save_slot(number=3)
        hotspot (886, 348, 339, 244) action FileAction(4):
            use load_save_slot(number=4)

        
        hotspot (31, 31, 257, 79) action ShowMenu('preferences')
        hotspot (31, 110, 189, 70) action ShowMenu('load')
        hotspot (31, 180, 173, 77) action ShowMenu('save')
        hotspot (31, 311, 245, 78) action ShowMenu('extras')
        hotspot (31, 389, 321, 70) action MainMenu()
        hotspot (31, 459, 147, 62) action Quit()
        hotspot (31, 593, 224, 94) action Return()
        
        
        
screen save:
    
    tag menu
    
    imagemap:
        ground 'saveload_ground.png'
        idle 'saveload_idle.png'
        hover 'saveload_hover.png'
        selected_idle 'saveload_selected.png'
        selected_hover 'saveload_hover.png'
        cache False
        
        hotspot (712, 616, 74, 96) action FilePage(1) 
        hotspot (883, 616, 75, 96) action FilePage(2)
        
        ## You might get confused but these one below are the save/load slots, those boxes.
        hotspot (442, 58, 339, 244) action FileAction(1):
            use load_save_slot(number=1)
        hotspot (886, 58, 339, 244) action FileAction(2):
            use load_save_slot(number=2)
        hotspot (442, 348, 339, 244) action FileAction(3):
            use load_save_slot(number=3)
        hotspot (886, 348, 339, 244) action FileAction(4):
            use load_save_slot(number=4)

        
        hotspot (31, 31, 257, 79) action ShowMenu('preferences')
        hotspot (31, 110, 189, 70) action ShowMenu('load')
        hotspot (31, 180, 173, 77) action ShowMenu('save')
        hotspot (31, 311, 245, 78) action ShowMenu('extras')
        hotspot (31, 389, 321, 70) action MainMenu()
        hotspot (31, 459, 147, 62) action Quit()
        hotspot (31, 593, 224, 94) action Return()
                    
init python:
    config.thumbnail_width = 340
    config.thumbnail_height = 245
##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces
screen preferences:
    tag menu
    
    imagemap:
        ground 'gui/config_ground.png'
        idle 'gui/config_idle.png'
        hover 'gui/config_hover.png'
        selected_idle 'gui/config_sidle.png'
        selected_hover 'gui/config_shover.png'
        cache False

        ## DISPLAY
        hotspot (932, 86, 75, 46) action Preference('display', 'fullscreen')
        hotspot (1032, 86, 145, 46) action Preference('display', 'window')
        
        ## TRANSITION
        hotspot (952, 223, 55, 53) action Preference('transitions', 'all')
        hotspot (1045, 223, 100, 53) action Preference('transitions', 'none')
         
        ## SKIP
        hotspot (956, 389, 99, 41) action Preference('skip', 'seen')
        hotspot (1079, 382, 66, 41) action Preference('skip', 'all')
        
        ## AFTER CHOICES
        hotspot (940, 532, 105, 58) action Preference('after choices', 'stop')
        hotspot (1055, 532, 114, 56) action Preference('after choices', 'skip')        
        ## BEGIN SKIPPING
        hotspot (696, 624, 260, 63) action Preference('begin skipping')

        
        hotbar (416, 82, 302, 46) value Preference('text speed')
        hotbar (413, 223, 302, 53) value Preference('music volume')
        hotbar (416, 369, 302, 61) value Preference('sound volume')
        hotbar (421, 529, 302, 56) value Preference('auto-forward time') 
        
        
        hotspot (31, 31, 257, 79) action ShowMenu('preferences')
        hotspot (31, 110, 189, 70) action ShowMenu('load')
        hotspot (31, 180, 174, 80) action ShowMenu('save')
        hotspot (31, 311, 245, 78) action ShowMenu('extras')
        hotspot (31, 389, 321, 70) action MainMenu()
        hotspot (31, 459, 147, 62) action Quit()
        hotspot (31, 593, 224, 94) action Return()


##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:

    imagemap:
        ground 'gui/yesno_ground.png'
        idle 'gui/yesno_idle.png'
        hover 'gui/yesno_hover.png'
        
        hotspot (383, 356, 234, 154) action yes_action
        hotspot (703, 356, 252, 154) action no_action

    if message == layout.ARE_YOU_SURE:
        add "gui/yesno_sure.png"
        
    elif message == layout.DELETE_SAVE:
        add "gui/yesno_delete.png"
        
    elif message == layout.OVERWRITE_SAVE:
        add "gui/yesno_overwrite.png"
        
    elif message == layout.LOADING:
        add "gui/yesno_load.png"
        
    elif message == layout.QUIT:
        add "gui/yesno_quit.png"
        
    elif message == layout.MAIN_MENU:
        add "gui/yesno_mm.png"

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu:
    hbox:
        style_group "quickmenu"
    
        xalign 1.0
        yalign 0.0
        
        imagemap:
            ground "gui/qm_idle.png"
            idle "gui/qm_idle.png"
            hover "gui/qm_hover.png"
            selected_idle "gui/qm_selected"
            selected_hover "gui/qm_selected.png"
            
            hotspot (1195, 17, 70, 70) action ShowMenu('preferences')
            hotspot (1195, 98, 70, 72) action ShowMenu("save")
            hotspot (1195, 180, 70, 72) action Preference("auto-forward", "toggle")
            hotspot (1194, 262, 71, 73) action Skip()
            hotspot (1194, 343, 71, 72) action Rollback()
            
            
            
            



