# animation class

import pygame

class movement():

    def __init__(self, images, fps, x_pos, y_pos):
        self.images = images # list of images (in forrm of pygame.image.load("1sleep_2.png"))
        self.fps = fps
        self.x_pos = x_pos # x coord of image
        self.y_pos = y_pos # y coord of image
        self.surface = []
        for image in self.images:
            self.surface.append(image) 
        self.index = 0 

    def draw_ani(self,win): # function for actually drawing image
        clock = pygame.time.Clock()
        if self.index >= len(self.surface):
            self.index=0
        win.blit(self.surface[self.index],(self.x_pos,self.y_pos))
        self.index += 1
        clock.tick(self.fps)
        pygame.display.flip()