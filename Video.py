from moviepy.editor import *
import pygame

pygame.display.set_caption('Hello World!')

clip = VideoFileClip('video.mp4')
print(type(clip))
clip.preview()


clip = VideoFileClip('giphy.gif')

clip.preview()

pygame.quit()