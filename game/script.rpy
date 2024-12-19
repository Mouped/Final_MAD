# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

screen man:
    imagebutton:
        xalign 0.0
        yalign 0.5
        idle "man_idle.png"
        hover "man_hover.png"
        action Jump("man")

screen woman:
    imagebutton:
        xalign 1.0
        yalign 0.5
        idle "woman_idle.png"
        hover "woman_hover.png"
        action Jump("woman")

# opening

label start:

    scene bg opening:
        fit "cover"
        xsize 1080
        ysize 1920

    show screen man
    show screen woman
    
    pause

label man:
    hide screen woman
    with dissolve
    hide screen man
    with None
    show man_hover:
        xalign 0.0
        yalign 0.5
    pause(0.3)

    show man_hover at center
    with move

    $ playername = renpy.input("Your Name:", length=32)
    $ playername = playername.strip()

    if not playername:
        $ playername = "Yanto"
    "Your name is {b}[playername]{/b}."
    hide man_hover
    with dissolve
    jump csmale_1
    pause

label woman:
    hide screen man
    with dissolve
    hide screen woman
    with None
    show woman_hover:
        xalign 1.0
        yalign 0.5
    pause(0.3)

    show woman_hover at center
    with move

    $ playername = renpy.input("Your Name:", length=32)
    $ playername = playername.strip()

    if not playername:
        $ playername = "Yanti"
    "Your name is {b}[playername]{/b}."
    hide woman_hover
    jump csfemale_1
    pause

label csmale_1:
    scene scene 1 tr:
        fit "cover"
        xsize 1080
        ysize 1920
    $ renpy.movie_cutscene("images/scenemale 1.webm", delay=None, loops=0)
    jump opmale_1
    pause


label opmale_1:
    scene scene 1 tr:
        fit "cover"
        xsize 1080
        ysize 1920

    menu:
        "Stable Job":
            jump csmale_career_1
        "Music":
            jump csmale_music_1
    pause

#career
label csmale_career_1:
    hide scene 1 tr
    scene black
    $ renpy.movie_cutscene("images/scenemale 2.webm", delay=None, loops=0, stop_music=True)
    $ renpy.movie_cutscene("images/scenemale 3.webm", delay=None, loops=0, stop_music=True)

    jump fingerprint
    pause

screen fingerprint:
    imagebutton:
        xalign 0.51
        yalign 0.695
        idle "fingerprint_idle.png"
        hover "fingerprint_hover.png"
        action Jump("fingerprint_2")
    
label fingerprint:
    hide black
    scene bg fingerprint
    show screen fingerprint
    $ renpy.pause(hard=True)
    pause



image ftext = ParameterizedText(xalign=0.51, yalign=0.4, size=30, color='#8dfdff', xmaximum=300)

label fingerprint_2:
    hide screen fingerprint
    scene bg fingerprint
    with None
    show ftext "Welcome, [playername]."
    with wiperight
    $ renpy.pause (2)
    jump csmale_career_2
    pause

label csmale_career_2:
    hide bg fingerprint
    scene bg op2:
        fit "cover"
        xsize 1080
        ysize 1920
    $ renpy.movie_cutscene("images/scenemale 4.webm", delay=None, loops=0)
    jump opmale_2
    pause

image op2 = Movie(play="images/scene tr 2.webm", loops=True)

label opmale_2:
    scene bg op2:
        fit "cover"
        xsize 1080
        ysize 1920
    menu:
        "Stay at Work":
            jump csmale_career_3

        "Give Up":
            jump csmale_career_4
    return

label csmale_career_3:
    hide bg op2
    scene black
    $ renpy.movie_cutscene("images/scenemale5.webm", delay=None, loops=0, stop_music=True)
    return

label csmale_career_4:
    hide bg op2
    scene black
    $ renpy.movie_cutscene("images/scenemale7.webm", delay=None, loops=0, stop_music=True)
    return

#music
label csmale_music_1:
    hide scene 1 tr
    scene black
    $ renpy.movie_cutscene("images/scenemale6.webm", delay=None, loops=0, stop_music=True)
    $ renpy.movie_cutscene("images/scenemale 3.webm", delay=None, loops=0, stop_music=True)

    jump fingerprint
    pause


label csfemale_1:
    scene scene 1 tr:
        fit "cover"
        xsize 1080
        ysize 1920
    $ renpy.movie_cutscene("images/scenefemale 1.webm", delay=None, loops=0)
    jump opfemale_1
    pause

label opfemale_1:
    scene scene 1 tr:
        fit "cover"
        xsize 1080
        ysize 1920

    menu:
        "Stable Job":
            jump csfemale_career_1
        "Music":
            jump csfemale_music_1
    pause

label csfemale_career_1:
    hide scene 1 tr
    scene black
    $ renpy.movie_cutscene("images/scenefemale 2.webm", delay=None, loops=0, stop_music=True)
    $ renpy.movie_cutscene("images/scenefemale 3.webm", delay=None, loops=0, stop_music=True)

    jump fingerprint_fe
    pause


screen fingerprint_fe:
    imagebutton:
        xalign 0.51
        yalign 0.695
        idle "fingerprint_idle.png"
        hover "fingerprint_hover.png"
        action Jump("fingerprint_fe2")
    
label fingerprint_fe:
    hide black
    scene bg fingerprint
    show screen fingerprint_fe
    $ renpy.pause(hard=True)
    pause

label fingerprint_fe2:
    hide screen fingerprint_fe
    scene bg fingerprint
    with None
    show ftext "Welcome, [playername]."
    with wiperight
    $ renpy.pause (2)
    jump csfemale_career_2
    pause

label csfemale_career_2:
    scene black
    $ renpy.movie_cutscene("images/scenefemale 5.webm", delay=None, loops=0)
    return

label csfemale_music_1:
    hide scene 1 tr
    scene black
    $ renpy.movie_cutscene("images/scenefemale 6.webm", delay=None, loops=0, stop_music=True)
    $ renpy.movie_cutscene("images/scenefemale 3.webm", delay=None, loops=0, stop_music=True)

    jump fingerprint_fe
    pause