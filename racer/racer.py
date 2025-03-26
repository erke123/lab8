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

# Игрок
player_image = pygame.image.load("c:/Users/Еркенур/Desktop/lab8/racer/Player.png")
player_rect = player_image.get_rect()
player_rect.center = (160, 520)

# Враг
enemy_image = pygame.image.load("c:/Users/Еркенур/Desktop/lab8/racer/Enemy.png")
enemy_rect = enemy_image.get_rect()
enemy_rect.center = (random.randint(40, W - 40), 0)

# Монета
coin_image = pygame.image.load("c:/Users/Еркенур/Desktop/lab8/racer/coin.png")
coin_image = pygame.transform.scale(coin_image, (coin_image.get_width() // 12, coin_image.get_height() // 12))
coin_rect = coin_image.get_rect()
coin_rect.center = (random.randint(40, W - 40), 0)

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

    # Движение игрока
    pressed_key = pygame.key.get_pressed()
    if player_rect.left > 1:
        if pressed_key[K_LEFT]:
            player_rect.move_ip(-5, 0)
        if pressed_key[K_RIGHT]:
            player_rect.move_ip(5, 0)

    # Движение врага
    enemy_rect.move_ip(0, SPEED)
    if enemy_rect.top > H:
        SCORE += 1
        enemy_rect.top = 0
        enemy_rect.center = (random.randint(40, W - 40), 0)

    # Движение монеты
    coin_rect.move_ip(0, 5)
    if coin_rect.top > H:
        coin_rect.top = 0
        coin_rect.center = (random.randint(40, W - 40), 0)

    # Столкновение игрока с врагами
    if player_rect.colliderect(enemy_rect):
        pygame.mixer.Sound("c:/Users/Еркенур/Desktop/lab8/racer/racer_crash.wav").play()  # Проигрывание звука
        time.sleep(0.5)

        SC.fill(RED)
        SC.blit(game_over, (30, 250))
        result = font_small.render(f"Your result: {COINS}", True, BLACK)
        SC.blit(result, (120, 350))
        pygame.display.update()

        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Столкновение игрока с монетами
    if player_rect.colliderect(coin_rect):
        COINS += 1  # Увеличиваем счет за монеты
        coin_rect.top = 0
        coin_rect.center = (random.randint(40, W - 40), 0)

    # Отображаем все объекты на экране
    SC.blit(player_image, player_rect)
    SC.blit(enemy_image, enemy_rect)
    SC.blit(coin_image, coin_rect)

    pygame.display.update()
    clock.tick(FPS)
