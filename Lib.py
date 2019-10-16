
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()