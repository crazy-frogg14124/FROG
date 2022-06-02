import pygame
import sys
import random
import pygame_menu

pygame.init()

pygame.mixer.music.load("game.mp3")
pygame.mixer.music.set_volume(0.3)
s = pygame.mixer.Sound("food.mp3")
p = pygame.mixer.Sound("lose.mp3")

bg_image = pygame.image.load("1.jpg")
SIZE_BLOCK = 20
FRAME_COLOR = (138, 43, 226)
WHITE = (230, 230, 250)
BLUE = (221, 160, 221)
RED = (224, 0, 0)
HEADER_COLOR = (105, 190, 250)
HEADER_MARGIN = 70
COUNT_BLOCKS = 20
SNAKE_COLOR = (173, 255, 47)
MARGIN = 1
size = [SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS,
        SIZE_BLOCK * COUNT_BLOCKS + 2 * SIZE_BLOCK + MARGIN * COUNT_BLOCKS + HEADER_MARGIN]

print(size)
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')
timer = pygame.time.Clock()
courier = pygame.font.SysFont('courier', 36)

class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return 0<=self.x<SIZE_BLOCK and 0<=self.y<SIZE_BLOCK

    def __eq__(self, other):
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y

def draw_block(color, row, column):
    pygame.draw.rect(screen, color, [SIZE_BLOCK + column * SIZE_BLOCK + MARGIN * (column + 1),
                                     HEADER_MARGIN + SIZE_BLOCK + row * SIZE_BLOCK + MARGIN * (row + 1),
                                     SIZE_BLOCK,
                                     SIZE_BLOCK])
def start_the_game():

    pygame.mixer.music.play(-1)
    
    def get_randon_empty_block():
        x = random.randint (0, COUNT_BLOCKS - 1)
        y = random.randint (0, COUNT_BLOCKS - 1)
        empty_block = SnakeBlock(x, y)
        while empty_block in snake_blocks:
            empty_block.x = random.randint (0, COUNT_BLOCKS - 1)
            empty_block.y = random.randint (0, COUNT_BLOCKS - 1)
        return empty_block
    
    snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
    apple = get_randon_empty_block()
    d_row = buf_row = 0
    d_col = buf_col = 1
    total = 0
    speed = 1
    
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('exit')
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and d_col!=0:
                    buf_row = -1
                    buf_col = 0
                elif event.key == pygame.K_DOWN and d_col!=0:
                    buf_row = 1
                    buf_col = 0
                elif event.key == pygame.K_LEFT and d_row!=0:
                    buf_row = 0
                    buf_col = -1
                elif event.key == pygame.K_RIGHT and d_row!=0:
                    buf_row = 0
                    buf_col = 1

        screen.fill(FRAME_COLOR)
        pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_MARGIN])

        text_total = courier.render(f"Счёт: {total}", 0, WHITE)
        screen.blit(text_total, (SIZE_BLOCK, SIZE_BLOCK))
         
        for row in range(COUNT_BLOCKS):
            for column in range(COUNT_BLOCKS):
                if (row + column) % 2 == 0:
                    color = BLUE
                else:
                    color = WHITE

                draw_block(color, row, column)

        head = snake_blocks[-1]
        if not head.is_inside():
            print('crash')
            pygame.mixer.music.stop()
            p.play()
            break

        draw_block(RED, apple.x, apple.y)
        for block in snake_blocks:
            draw_block(SNAKE_COLOR, block.x, block.y)

        pygame.display.flip()

        if apple == head:
            total += 1
            speed = total// 5 + 1
            snake_blocks.append(apple)
            apple = get_randon_empty_block()
            s.play()

        d_row = buf_row
        d_col = buf_col
        new_head = SnakeBlock(head.x + d_row, head.y + d_col)

        if new_head in snake_blocks:
            print('crash yourself')
            pygame.mixer.music.stop()
            p.play()
            break

        snake_blocks.append(new_head)
        snake_blocks.pop(0)
    
        timer.tick(3 + speed)

menu = pygame_menu.Menu('Добро пожаловать', 460, 250, theme=pygame_menu.themes.THEME_BLUE)
menu.add.button('НАЧАТЬ', start_the_game)
menu.add.button('ВЫХОД', pygame_menu.events.EXIT)

while True:
    screen.blit(bg_image, (0,0))
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            exit()
    if menu.is_enabled():
        menu.update(events)
        menu.draw(screen)
    pygame.display.update()
