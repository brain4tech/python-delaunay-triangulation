from lib.misc import addAlphaChannel


def renderText(plane, font, text, color, position, right_align=False):
	"""Renders text on passed plane"""
	text, text_rect = font.render(text, addAlphaChannel(color))
	if right_align:
		plane.blit(text, (position[0] - text_rect.width, position[1]))
	else:
		plane.blit(text, position)
