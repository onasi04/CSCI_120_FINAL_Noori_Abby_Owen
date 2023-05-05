import pygame

class Health():
    def __init__(self, status_x_pos, status_y_pos, status_w, status_h, max_health, current_health):
        self.status_x_pos = status_x_pos
        self.status_y_pos = status_y_pos
        self.status_w = status_w
        self.status_h = status_h
        self.max_health = max_health
        self.current_health = current_health
        self.health_ratio = self.max_health/self.status_w

    def loss(self,amount):
        if self.current_health > 0:
            self.current_health -= amount
        if self.current_health <= 0:
            self.current_health = 0

    def gain(self,amount):
        if self.current_health < self.max_health:
            self.current_health += amount
        if self.current_health >= self.max_health:
            self.current_health = self.max_health

    def health(self,win):
        pygame.draw.rect(win,(255,0,0),(self.status_x_pos,self.status_y_pos,self.current_health / self.health_ratio,25))
        pygame.draw.rect(win,(0,0,0),(self.status_x_pos,self.status_y_pos,self.status_w,25),3)