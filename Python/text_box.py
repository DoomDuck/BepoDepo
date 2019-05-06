"""
Test program to understand the basics of text input in pygame


Issues :
> Can not handle to use the modifier keys ( ctrl, shift, etc.. )
    Hypothesis : maybe the os is handeling these events
    This would explain why there are no events while holding ctrl
    Proof : while running pygame.examples.eventlist.main()
    you can see that pygame looses keyboard focus on the first ctrl click

global TODOs :
> Check the freetype module ( it is supposed to propose better fonts rendering )
    ex: Ability to render directly without creating temporary surface
> Add sweet sweet duck in this description
> Add a cursor and the possiblity to use the arrows
"""

import pygame as pg
# freetype must be import as well
import pygame.freetype


# Colors
WHITE	= pg.Color( 255,255,255 )
RED		= pg.Color( 255,0,	0   )
GREEN 	= pg.Color( 0,	255,255 )
BLUE	= pg.Color( 0,	0,	255 )
BLACK	= pg.Color( 0,	0,	0   )
# IDEA: Use the pg.color module to use some well predefined colors


# Some constants
WIDTH       = 800
HEIGHT      = 640
BG_COLOR    = WHITE
TEXT_COLOR  = BLACK
FONT_SIZE   = 24
TEXT_POS    = pg.Vector2( 0, 0 )

# Initialization
pg.init()
pg.freetype.init()

# Pygame variables
screen = pg.display.set_mode( ( WIDTH, HEIGHT ) )
clock = pg.time.Clock()

# My font
font = pg.freetype.Font( "../fonts/my-type-of-font/mytype.ttf", 32 )

text_lines  = [""]
go_on = True

while go_on:
	# Event loop
	for e in pg.event.get():
		# Quit event handeling ( the cross )
		if e.type == pg.QUIT:
			go_on = False
		# Keypress handeling
		elif e.type == pg.KEYDOWN:
			print( e.key, pg.K_RETURN )
			if e.key == pg.K_BACKSPACE:
				if  text_lines[-1] == "":
					# If no text on the line delete the line
					text_lines.pop()
				text_lines[-1] = text_lines[-1][:-1]
			elif e.key == pg.K_RETURN:
				text_lines.append( "" )
			else :
				text_lines[-1] += e.unicode
	# Drawing
	screen.fill( BG_COLOR )

	text_pos = pg.Vector2( TEXT_POS.x, TEXT_POS.y )
	for line in text_lines:
		text_pos.y += font.render_to( screen, ( int( text_pos.x ), int( text_pos.y ) ), line, TEXT_COLOR ).h


	# Updating display
	pg.time.delay( 1000 // 60 )
	pg.display.flip()


# Quitting pygame
pg.freetype.quit()
pg.quit()
