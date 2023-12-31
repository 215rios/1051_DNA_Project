import pygame



class Button():
    def __init__(self, x , y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width*scale),(int(height*scale))) )
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False
        self.visible = True

    def draw(self,surface): #can only be met once
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]==1 and self.clicked == False: #zero means left click
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
            self.visible = True


        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action