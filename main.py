import sys # untuk akses ke sistem oprasi secara universal

import pygame # library pygame untuk membangun game Constuctor

class AlienCounter:
	#kerangka objek untuk world dari game yamg akan kita bangun
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode([800,600])
		self.title = pygame.display.set_caption("Alien Counter")

	def run_game(self):

		while True: #infinite loop
			#monitoring kejadian / event
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit() 

			#rendering display every frame
			pygame.display.flip()

my_game = AlienCounter()
my_game.run_game()