import pygame, parle
import tools, interperter
from pygame import mixer




pygame.mixer.init()
pygame.init()


screen= pygame.display.set_mode((1000, 550))
pygame.display.set_caption('bob')
font=pygame.font.Font('freesansbold.ttf', 40)
font_2=pygame.font.Font('freesansbold.ttf', 20)


run=True

input_active=True

text = ""

#mixer.music.load('joke.ogg')


parle.repond(tools.tools('presentation'))
aw=""

while run:

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False

		elif event.type == pygame.KEYDOWN and input_active:
			if event.key == pygame.K_BACKSPACE:
				text =  text[:-1]

			elif event.key == pygame.K_RETURN :
				respons=interperter.main(text)
				if "blague" in text:
					parle.repond(respons)
				elif "exit"==text:
					print(voila)

				elif "musique" in text:
					mixer.music.load(respons)
					mixer.music.play()
				else:
					parle.repond(respons)
				aw=respons
				text=""


			else:
				text += event.unicode

		screen.fill((255, 255, 255))
		text_surf = font.render(text, True, (0, 0, 0))
		screen.blit(text_surf, text_surf.get_rect())

		text_aw = font_2.render(aw, True, (0, 0, 0))
		screen.blit(text_aw, (50, 100))

		run=True
		pygame.display.flip()

	pygame.display.update()







