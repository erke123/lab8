import pygame

# Инициализация Pygame
pygame.init()
w, h = 1000, 800
f = 60  # FPS
clock = pygame.time.Clock()
draw = False
radius = 5
colors = {'white': (255, 255, 255), 'black': (0, 0, 0), 'red': (255, 0, 0), 'green': (0, 255, 0), 'blue': (0, 0, 255),
          'orange': (252, 154, 8), 'yellow': (252, 248, 3), 'pink': (252, 3, 252), 'purple': (169, 3, 252),
          'gray': (206, 204, 207)}

# Шрифт
font = pygame.font.Font(None, 15)

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (252, 154, 8)
YELLOW = (252, 248, 3)
PINK = (252, 3, 252)
PURPLE = (169, 3, 252)
GRAY = (206, 204, 207)

# Экран
screen = pygame.display.set_mode((w, h))
screen.fill(WHITE)

# Режим рисования
mode = 'pen'
color = BLACK

# Загружаем изображения инструментов
eraser = pygame.image.load('c:/Users/Еркенур/Desktop/lab8/paint/eraser-removebg-preview.png')
eraser = pygame.transform.scale(eraser, (50, 50))  # Масштабируем изображение до нужного размера
penn = pygame.image.load('c:/Users/Еркенур/Desktop/lab8/paint/R.png')
penn = pygame.transform.scale(penn, (50, 50))

# Функция рисования линии
def drawLine(screen, start, end, width, color):
    x1, y1 = start
    x2, y2 = end
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)


def drawCircle(screen, start, end, width, color): 
    # Extract x and y coordinates of start and end points
    x1 = start[0]  # Extract x-coordinate of the start point
    x2 = end[0]  # Extract x-coordinate of the end point
    y1 = start[1]  # Extract y-coordinate of the start point
    y2 = end[1]  # Extract y-coordinate of the end point
    
    # Calculate the center of the circle
    x = (x1 + x2) / 2  # Calculate the center of the circle along the x-axis
    y = (y1 + y2) / 2  # Calculate the center of the circle along the y-axis
    
    # Calculate the radius of the circle
    radius = abs(x1 - x2) / 2  # Calculate the radius of the circle
    
    # Draw the circle on the screen
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)  # Draw the circle on the screen

 
 
def drawRectangle(screen, start, end, width, color): 
    # Extract x and y coordinates of start and end points
    x1 = start[0]  # Extract x-coordinate of the start point
    x2 = end[0]  # Extract x-coordinate of the end point
    y1 = start[1]  # Extract y-coordinate of the start point
    y2 = end[1]  # Extract y-coordinate of the end point
    
    # Calculate the width and height of the rectangle
    widthr = abs(x1 - x2)  # Calculate the width of the rectangle
    height = abs(y1 - y2)  # Calculate the height of the rectangle
    
    # Draw the rectangle on the screen based on the position of start and end points
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)  # Draw the rectangle on the screen
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)  # Draw the rectangle on the screen
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)  # Draw the rectangle on the screen
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)  # Draw the rectangle on the screen

     
 
 
def drawSquare(screen, start, end, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    mn = min(abs(x2 - x1), abs(y2 - y1)) 
 
 
    if x2 > x1 and y2 > y1: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn)) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn)) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn)) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn)) 
 
def drawRightTriangle(screen, start, end, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
     
    if x2 > x1 and y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2))) 
    if y2 > y1 and x1 > x2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2))) 
    if x1 > x2 and y1 > y2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1))) 
    if x2 > x1 and y1 > y2: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1))) 
 
 
def drawEquilateralTriangle(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
 
    width_b = abs(x2 - x1) 
    height = (3**0.5) * width_b / 2 
 
    if y2 > y1: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)), width) 
    else: 
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height))) 
     
 
def drawRhombus(screen, start, end, width, color): 
    x1 = start[0] 
    x2 = end[0] 
    y1 = start[1] 
    y2 = end[1] 
    pygame.draw.lines(screen, pygame.Color(color), True, (((x1 + x2) / 2, y1), (x1, (y1 + y2) / 2), ((x1 + x2) / 2, y2), (x2, (y1 + y2) / 2)), width) 
 

# Переменные
draw_area = pygame.Surface((1000, 600))
draw_area_rect = draw_area.get_rect(topleft=(0, 183))
is_erase = False
is_visible = True

# Основной игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Обработка нажатия клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                mode = 'pen'  # Карандаш
            elif event.key == pygame.K_e:
                mode = 'erase'  # Ластик
            elif event.key == pygame.K_q:
                screen.fill(WHITE)  # Очистка экрана
            elif event.key == pygame.K_r:
                mode = 'rectangle'
                  # Прямоугольник
            elif event.key == pygame.K_c:
                mode = 'circle'  # Круг
            elif event.key == pygame.K_s:
                mode = 'square'  # Квадрат

        # Обработка нажатия кнопки мыши
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            prevPos = event.pos

            # Проверка нажатия на цветовые иконки
            if 300 < event.pos[0] < 350 and 30 < event.pos[1] < 80:
                color = RED
            elif 380 < event.pos[0] < 430 and 30 < event.pos[1] < 80:
                color = YELLOW
            elif 460 < event.pos[0] < 510 and 30 < event.pos[1] < 80:
                color = GREEN
            elif 540 < event.pos[0] < 590 and 30 < event.pos[1] < 80:
                color = BLUE
            elif 300 < event.pos[0] < 350 and 110 < event.pos[1] < 160:
                color = ORANGE
            elif 380 < event.pos[0] < 430 and 110 < event.pos[1] < 160:
                color = PINK
            elif 460 < event.pos[0] < 510 and 110 < event.pos[1] < 160:
                color = PURPLE
            elif 540 < event.pos[0] < 590 and 110 < event.pos[1] < 160:
                color = BLACK

            # Проверка нажатия на инструменты (карандаш и ластик)
            if 660 < event.pos[0] < 710 and 30 < event.pos[1] < 80:
                mode = 'pen'  # Карандаш
            elif 660 < event.pos[0] < 710 and 110 < event.pos[1] < 160:
                mode = 'erase'  # Ластик

        if event.type == pygame.MOUSEBUTTONUP:
            draw = False

        if event.type == pygame.MOUSEMOTION:
            if draw:
                # Ограничиваем координаты рисования областью draw_area
                mouse_x, mouse_y = event.pos
                if draw_area_rect.collidepoint(mouse_x, mouse_y):  # Проверяем, в пределах ли области
                    if mode == 'pen':
                        drawLine(screen, prevPos, event.pos, radius, color)
                    elif mode == 'erase':
                        drawLine(screen, prevPos, event.pos, radius, WHITE)
                    elif mode == 'rectangle':
                        drawRectangle(screen, prevPos, event.pos, radius, color)
                    elif mode == 'circle':
                        drawCircle(screen, prevPos, event.pos, radius, color)
                    elif mode == 'square':
                        drawSquare(screen, prevPos, event.pos, color)
                prevPos = event.pos

    # Отображение иконок для выбора цвета
    pygame.draw.rect(screen, GRAY, (50, 30, 130, 130), 5)
    pygame.draw.rect(screen, color, (55, 35, 120, 120))  # Текущий цвет
    pygame.draw.rect(screen, RED, (300, 30, 50, 50))
    pygame.draw.rect(screen, YELLOW, (380, 30, 50, 50))
    pygame.draw.rect(screen, GREEN, (460, 30, 50, 50))
    pygame.draw.rect(screen, BLUE, (540, 30, 50, 50))
    pygame.draw.rect(screen, ORANGE, (300, 110, 50, 50))
    pygame.draw.rect(screen, PINK, (380, 110, 50, 50))
    pygame.draw.rect(screen, PURPLE, (460, 110, 50, 50))
    pygame.draw.rect(screen, BLACK, (540, 110, 50, 50))

    # Иконки для выбора инструментов (карандаш и ластик)
    pygame.draw.rect(screen, GRAY, (660, 30, 50, 50), 3)  # Карандаш
    pygame.draw.rect(screen, GRAY, (660, 110, 50, 50), 3)  # Ластик

    # Отображаем иконку ластика
    screen.blit(eraser, (660, 110))  # Рисуем ластик на экране
    screen.blit(penn, (660, 30))

    # Разделительные линии
    pygame.draw.line(screen, BLACK, (0, 180), (1000, 180), 3)
    pygame.draw.line(screen, BLACK, (270, 180), (270, 0), 3)
    pygame.draw.line(screen, BLACK, (600, 180), (600, 0), 3)

    # Тексты
    write_color = font.render("Colors", True, BLACK)
    write_current = font.render("Now using", True, BLACK)
    write_tools = font.render("Tools", True, BLACK)
    screen.blit(write_current, (60, 10))
    screen.blit(write_color, (420, 10))
    screen.blit(write_tools, (660, 10))

    # Отображение текущего радиуса
    renderRadius = font.render(str(radius), True, color)
    screen.blit(renderRadius, (5, 5))

    pygame.display.flip()
    clock.tick(f)  # Устанавливаем FPS
