import pygame
import sys
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Breakout")

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 10))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = (screen_width // 2) - (self.rect.width // 2)
        self.rect.y = screen_height - 50
        self.speed = 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(green)
        self.rect = self.image.get_rect()
        self.rect.x = screen_width // 2
        self.rect.y = screen_height // 2
        self.velocity = [random.choice([3, -3]), 3]

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

        # Відскок від стін
        if self.rect.left <= 0 or self.rect.right >= screen_width:
            self.velocity[0] = -self.velocity[0]
        if self.rect.top <= 0:
            self.velocity[1] = -self.velocity[1]
        if self.rect.bottom >= screen_height:
            self.kill()

        # Відскок від платформи
        if pygame.sprite.spritecollide(self, paddles, False):
            self.velocity[1] = -self.velocity[1]

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill(red)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
paddles = pygame.sprite.Group()

paddle = Paddle()
all_sprites.add(paddle)
paddles.add(paddle)

ball = Ball()
all_sprites.add(ball)

for row in range(5):
    for col in range(10):
        block = Block(60 * col + 10 + (col * 10), 30 * row + 10 + (row * 10))
        all_sprites.add(block)
        blocks.add(block)

clock = pygame.time.Clock()
running = True
game_won = False
game_lost = False


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_won and not game_lost:
     all_sprites.update()

    collisions = pygame.sprite.spritecollide(ball, blocks, True)
    if collisions:
        ball.velocity[1] = -ball.velocity[1]


    if not blocks:
        game_won = True
        ball.kill()

    if ball.rect.bottom >= screen_height:
        game_lost = True
        ball.kill()
        paddle.kill()
        for block in blocks:
            block.kill()

    screen.fill(white)
    all_sprites.draw(screen)

    if game_won:
        font = pygame.font.Font(None, 74)
        text = font.render("Гра завершена. Ви перемогли!", True, black)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))
    elif game_lost:
        font = pygame.font.Font(None, 74)
        text = font.render("Гра завершена. Ви програли!", True, black)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, screen_height // 2 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
sys.exit()