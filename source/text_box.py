"""
Test program to understand the basics of text input in pygame


Issues :
> Can not handle to use the modifier keys ( ctrl, shift, etc.. )
    Hypothesis : maybe the os is handeling these events
    This would explain why there are no events while holding ctrl
    Proof : while running pygame.examples.eventlist.main()
    you can see that pygame looses keyboard focus on the first ctrl click

"""
import pygame as pg

# Colors
WHITE   = ( 255, 255, 255 )
RED     = ( 255, 0,   0   )
GREEN   = ( 0,   255, 255 )
BLUE    = ( 0,   0,   255 )
BLACK   = ( 0,   0,   0   )
# IDEA: Use the pg.Color module to use some well predefined colors


# Some constants
WIDTH       = 800
HEIGHT      = 640
BG_COLOR    = WHITE
TEXT_COLOR  = BLACK
FONT_SIZE   = 24
TEXT_POS    = ( 0, 0 )

# Initialization
pg.init()
pg.sysfont.initsysfonts()

# Pygame variables
screen = pg.display.set_mode( ( WIDTH, HEIGHT ) )
clock = pg.time.Clock()

all_fonts = pg.sysfont.get_fonts()

# Using the first available font ( for now )
font = pg.sysfont.SysFont( all_fonts[0], FONT_SIZE )
# IDEA: we can as well use the pg.font.Font( None, FONT_SIZE ) syntax
# None stands for default font here


text  = ""
go_on = True

while go_on:
    # Event loop
    for e in pg.event.get():
        # Quit event handeling ( the cross )
        if e.type == pg.QUIT:
            go_on = False
        # Keypress handeling
        elif e.type == pg.KEYDOWN:
            if e.key == pg.K_BACKSPACE:
                text = text[:-1]
            elif e.key == pg.K_RETURN:
                text += '\n'
            else :
                text += e.unicode
    
    # Drawing
    screen.fill( BG_COLOR )

    # I haven't been able to find a way to render text directly on the screen surface
    #text_surface = font.render( text, True, TEXT_COLOR )
    #pg.Surface.blit( screen, text_surface, TEXT_POS )

    font.render_to( screen, )

    # Updating display
    clock.tick( 60 )
    pg.display.flip()


# Quitting pygame
pg.quit()
