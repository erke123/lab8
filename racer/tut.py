import pygame, sys
from pygame.locals import *
import random, time

pygame.init()

# Настройки
FPS = 60
clock = pygame.time.Clock()
W, H = 400, 600
SPEED = 5
SCORE = 0
COINS = 0

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Шрифты
font = pygame.font.Font("font_user.ttf", 60)
font_small = pygame.font.Font("font_user.ttf", 20)
game_over = font.render("Game Over", True, BLACK)

# Загрузки изображений
coin_icon = pygame.image.load("c:/Users/Еркенур/Desktop/lab8/racer/coin.png")
coin_icon = pygame.transform.scale(coin_icon, (coin_icon.get_width() // 20, coin_icon.get_height() // 20))
bg = pygame.image.load("c:/Users/Еркенур/Desktop/lab8/racer/AnimatedStreet.png")

# Окно
SC = pygame.display.set_mode((W, H))
SC.fill(WHITE)
pygame.display.set_caption("My game")

# Классы игры

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("c:/Users/Еркенур/Desktop/lab8/racer/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > H:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("c:/Users/Еркенур/Desktop/lab8/racer/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 1:
            if pressed_key[K_LEFT]:
                self.rect.move_ip(-5, 0)
            if pressed_key[K_RIGHT]:
                self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("c:/Users/Еркенур/Desktop/lab8/racer/coin.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // 12, self.image.get_height() // 12))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > H:
            self.rect.top = 0
            self.rect.center = (random.randint(40, W - 40), 0)


# Создание объектов
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_group = pygame.sprite.Group()
coins_group.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Событие увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 4000)

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 1  # Увеличение скорости врагов и монет

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    SC.blit(bg, (0, 0))  # Отрисовка фона
    SC.blit(coin_icon, (10, 35))  # Отображение иконки монеты

    # Отображение монет
    coins_v = font_small.render(f"X{str(COINS)}", True, BLACK)
    SC.blit(coins_v, (50, 50))

    for entity in all_sprites:
        SC.blit(entity.image, entity.rect)
        entity.move()

    # Столкновение игрока с врагами
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("c:/Users/Еркенур/Desktop/lab8/racer/racer_crash.wav").play()  # Проигрывание звука
        time.sleep(0.5)

        SC.fill(RED)
        SC.blit(game_over, (30, 250))
        result = font_small.render(f"Your result: {COINS}", True, BLACK)
        SC.blit(result, (120, 350))
        pygame.display.update()

        for entity in all_sprites:
            entity.kill()  # Удаление всех объектов
        
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Столкновение игрока с монетами
    if pygame.sprite.spritecollideany(P1, coins_group):
        COINS += 1  # Увеличиваем счет за монеты
        for coin in coins_group:
            coin.rect.top = 0
            coin.rect.center = (random.randint(40, W - 40), 0)

    pygame.display.update()
    clock.tick(FPS)
