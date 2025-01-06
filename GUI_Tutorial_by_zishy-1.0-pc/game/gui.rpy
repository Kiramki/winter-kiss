
screen extras:
    tag menu
    imagemap:
        ground "gui/extra_idle.png"
        idle "gui/extra_idle.png"
        hover "gui/extra_hover.png"
        
        hotspot (179, 98, 433, 261) action ShowMenu('cggallery')
        hotspot (694, 97, 429, 261) action ShowMenu('musicroom')
        hotspot (540, 508, 208, 80) action Return()
        


#######################################################################
#######################################################################
#### This the code for the customize Gallery
#### Almost the same with the default gallery but with some alterations.

init python:
    g = Gallery()
    

   # Step 2. Add buttons and images to the gallery.
    g.locked_background = "gui/cover.png"
    
    g.locked_button = "gui/commonlock.png" ##make one for this
    g.hover_border = "gui/ghover.png" ##optional, you can just set it to None
    g.idle_border = "gui/gidle.png" ##optional, you can just set it to None
   
   # A button that contains an image that automatically unlocks.

    g.button("cg1unlock") ##preview icon
    g.image("cg1")
    g.unlock("cg1")
    g.button("cg1")
    g.unlock_image ("cg1")

    g.button("cg2unlock") ##preview icon
    g.image("cg2")
    g.unlock("cg2")
    g.button("cg2")
    g.unlock_image ("cg2")
    
    g.button("cg3unlock") ##preview icon
    g.image("cg3")
    g.unlock("cg3")
    g.button("cg3")
    g.unlock_image ("cg3") 

    g.button("cg4unlock") ##preview icon
    g.image("cg4")
    g.unlock("cg4")
    g.button("cg4")
    g.unlock_image ("cg4")

    ####You may add more depending on how many CG's you have
    

screen cggallery:
    tag menu
    imagemap:
        ground 'gui/cg_ground.png'
        idle 'gui/cg_idle.png'
        hover 'gui/cg_hover.png'
        cache False
       
        hotspot (35, 557, 199, 91) action Return()
    
        hotspot (442, 71, 338, 243) action ShowMenu ("gallery")
        hotspot (886, 71, 338, 243) action ShowMenu ("gallery2")
        hotspot (442, 361, 338, 243) action ShowMenu ("gallery3")
        hotspot (886, 361, 338, 243) action ShowMenu ("gallery4")
    
    ### The sample CG Gallery is 2 columns with 2 rows
    grid 2 2:

        xfill True
        yfill True

        # Call make_button to show a particular button.
        ##xalign is the left to right setting (0.99+ makes it go to right)
        ##yalign is the upper then lower, (0.99+ makes it go lower)

        add g.make_button("cg1", "cg1unlock.png", xalign = 1.47, yalign = 0.6, xpadding = 0, ypadding = 0)
        add g.make_button("cg2", "cg2unlock.png", xalign = 0.82, yalign = 0.6, xpadding = 0, ypadding = 0)
        add g.make_button("cg3", "cg3unlock.png", xalign = 1.47, yalign = 0, xpadding = 0, ypadding = 0)
        add g.make_button("cg4", "cg4unlock.png", xalign = 0.82, yalign = 0, xpadding = 0, ypadding = 0)
        
        ##### REMEMBER!!
        # The common lock, hover and idle should be the same size as the dimension of the "box" where the CG preview will be placed.
        # Make a smaller preview of the CG for the gallery, that way the user will know which CG he/she view when clicked. The preview icon should also be the same size as the common lock.
    
    
    
    
    
#######################################################################
#######################################################################
#### This the code for the customize Music Room
#### Almost the same with the default gallery but with some alterations.

init python:

    # Step 1. Create a MusicRoom instance.
    mr = MusicRoom(fadeout=1.0)

    # Step 2. Add music files.
    mr.add("Happy Alley.mp3", always_unlocked=True)
    mr.add("Digital Lemonade.mp3")
    
screen musicroom:
    tag menu
    imagemap:
        ground 'gui/msc_idle.png'
        idle 'gui/msc_idle.png'
        hover 'gui/msc_hover.png'
        selected_idle 'gui/msc_hover.png'
        cache False
        
        # The buttons that play each track.
        hotspot (587, 167, 510, 82) action mr.Play ("Digital Lemonade.mp3")
        hotspot (643, 314, 378, 58) action mr.Play("Happy Alley.mp3")
        
        # Buttons that let us advance tracks.
        hotspot (845, 492, 95, 95) action mr.Next()
        hotspot (717, 492, 101, 95) action mr.Previous()
        
        # Return
        hotspot (35, 557, 199, 91) action Return()
        
        # Start the music playing on entry to the music room.
    on "replace" action mr.Play()

    # Restore the main menu music upon leaving.
    on "replaced" action Play("music", "Happy Alley.mp3")
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    