import pygame

class Button():
	def __init__(self, x_pos, y_pos, button_w, button_h, base_image, hovering_image):
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.button_w = button_w
		self.button_h = button_h
		self.base_image = base_image
		self.hovering_image = hovering_image
		self.rect = pygame.Rect(self.x_pos, self.y_pos,self.button_w,self.button_w)
		'''self.rect is the rectangle that will represent the button'''


	def checkForInput(self, position, button_w, button_h):
		if (self.rect.x <= position[0] <= self.rect.x + button_w) and (self.rect.y <= position[1] <= self.rect.y + button_h):
			return True
		else:
			return False

	def changeColor(self,position, win, button_w, button_h):
		if (self.rect.x <= position[0] <= self.rect.x + button_w) and (self.rect.y <= position[1] <= self.rect.y + button_h):
			win.blit(self.hovering_image, (self.x_pos,self.y_pos))
		else:
			win.blit(self.base_image, (self.x_pos,self.y_pos))