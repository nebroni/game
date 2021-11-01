import pygame
from settings import Settings

class Ship:
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = self.rect.x
		self.moving_right = False
		self.moving_left = False
		self.settings = Settings()

	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def update(self):
		if self.moving_right:
			if self.x < self.settings.screen_width - 60:
				self.x += self.settings.ship_speed
		if self.moving_left:
			if self.x > 0:
				self.x -= self.settings.ship_speed
		self.rect.x = self.x
