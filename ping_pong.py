from pygame import *
from random import randint

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption('ping')
background = transform.scale(image.load("tup.png"), (win_width, win_height))

rocket1 = Player1('pop.jpg', 5, win_height - 80, 280, 4, 5)
rocket2 = Player2('pop.jpg', 5, win_width - 80, 280, 2, 5)
ball = GameSprite('hop.jpg', 5, win_width - 80, 280, 2, 5)

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        rocket1.update()
        rocket2.update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(rocket1, ball) or sprite.collide_rect(rocket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

    display.update()
    clock.tick(FPS)