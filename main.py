
from pygame import *

class GameSprite(sprite.Sprite):
   def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
       super().__init__()
       self.image = transform.scale(image.load(player_image), (wight, height))
       self.speed = player_speed
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y


   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   def update_r(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < height - 80:
           self.rect.y += self.speed
   def update_l(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < height - 80:
           self.rect.y += self.speed

class Ball(GameSprite):
    def __init__(self, x, y, speed_x, speed_y, size):
        super().__init__("ball.png", x, y, 0, size, size)
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
    
        if self.rect.y <= 0 or self.rect.y >= height - self.rect.height:
            self.speed_y *= -1

init()

width = 700
height = 500
window = display.set_mode((width, height))

display.set_caption("Ping-Pong!")

clock = time.Clock()
fps = 60

white = (255, 255, 255)
black = (0,0,0)
red = (255, 0, 0)
blue = (0, 0, 255)

left_r = Player("racket.png", 30, 200, 8, 15, 80)
right_r = Player("racket.png", 650, 200, 8, 15, 80)

ball = Ball(350, 250, 5, 5, 20)

score_l = 0
score_r = 0
font = font.SysFont("Arial", 50)


game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if not finish:
        window.fill(black)

        left_r.update_l()
        right_r.update_r()

        ball.update()

        if sprite.collide_rect(left_r, ball):
            ball.speed_x *= -1
        if sprite.collide_rect(right_r, ball):
            ball.speed_x *= -1

        if ball.rect.x < 0:
            score_r += 1
            ball.rect.x = 350
            ball.rect.y = 250
            ball.speed_x *= -1

        if ball.rect.x > width:
            score_l += 1
            ball.rect.x = 350
            ball.rect.y = 250
            ball.speed_x *= -1

        if score_l >= 5:
            finish = True
            win_l = "Red Wins!"
            win_lc = red

        if score_r >= 5:
            finish = True
            win_l = "Blue Wins!"
            win_lc = blue
    
    left_r.reset()
    right_r.reset()
    ball.reset()

    text_1 = font.render(str(score_l), True, red)
    text_2 = font.render(str(score_r), True, blue)
    window.blit(text_1, (width//4, 20))
    window.blit(text_2, (width*3//4, 20))

    if finish:
        finish_text = font.render(win_l, True, win_lc)
        text_rect = finish_text.get_rect(center=(width//2, height//2))
        window.blit(finish_text, text_rect)


    display.update()

    clock.tick(fps)

