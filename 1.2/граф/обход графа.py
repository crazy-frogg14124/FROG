import pygame
pygame.init()

W, H = 600, 500
sc = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Дороги между пунктами")

WHITE = (255,255,255)
GREEN = (0, 255, 0)
SPRING = (0,250,154)
PURPLE = (128,0,128)
PINK = (255,20,147)
YELLOW = (255,255,0)
RED = (255,0,0)
ORANGE = (255,140,0)
BLACK = [0, 0, 0]

pygame.draw.line(sc, WHITE, (50, 50), (500, 50)) #линия А до В
pygame.draw.line(sc, WHITE, (50, 50), (500, 250)) #линия А до С
pygame.draw.line(sc, WHITE, (50, 50), (700, 460)) #линия А до D
pygame.draw.line(sc, WHITE, (50, 50), (240, 550)) #линия А до E
pygame.draw.line(sc, WHITE, (50, 50), (50, 650)) #линия А до F
pygame.draw.line(sc, WHITE, (50, 50), (700, 110)) #линия А до G
pygame.draw.line(sc, WHITE, (50, 50), (240, 300)) #линия А до H

pygame.draw.line(sc, GREEN, (500, 70), (50, 50))#линия В до А
pygame.draw.line(sc, GREEN, (500, 70), (500, 250))#линия В до С
pygame.draw.line(sc, GREEN, (500, 70), (700, 460))#линия B до D
pygame.draw.line(sc, GREEN, (500, 70), (240, 550))#линия B до E
pygame.draw.line(sc, GREEN, (500, 70), (50, 650))#линия B до F
pygame.draw.line(sc, GREEN, (500, 70), (700, 110))#линия B до G
pygame.draw.line(sc, GREEN, (500, 70), (240, 300))#линия B до H

pygame.draw.line(sc, SPRING, (500, 250), (50, 50))#линия С до А
pygame.draw.line(sc, SPRING, (500, 250), (500,50))#линия С до В
pygame.draw.line(sc, SPRING, (500, 250), (700, 460))#линия C до D
pygame.draw.line(sc, SPRING, (500, 250), (240, 550))#линия C до E
pygame.draw.line(sc, SPRING, (500, 250), (50, 650))#линия C до F
pygame.draw.line(sc, SPRING, (500, 250), (700, 110))#линия C до G
pygame.draw.line(sc, SPRING, (500, 250), (240, 300))#линия C до H

pygame.draw.line(sc, PURPLE, (700, 460), (50, 50))#линия D до А
pygame.draw.line(sc, PURPLE, (700, 460), (500,50))#линия D до В
pygame.draw.line(sc, PURPLE, (700, 460), (500, 250))#линия D до С
pygame.draw.line(sc, PURPLE, (700, 460), (240, 550))#линия D до E
pygame.draw.line(sc, PURPLE, (700, 460), (700, 110))#линия D до G
pygame.draw.line(sc, PURPLE, (700, 460), (240, 300))#линия D до H

pygame.draw.line(sc, PINK, (240, 550), (50, 50)) #линия Е до А
pygame.draw.line(sc, PINK, (240, 550), (500, 50)) #линия Е до В
pygame.draw.line(sc, PINK, (240, 550), (700, 460)) #линия Е до D
pygame.draw.line(sc, PINK, (240, 550), (50, 650)) #линия Е до F
pygame.draw.line(sc, PINK, (240, 550), (700, 110)) #линия Е до G
pygame.draw.line(sc, PINK, (240, 550), (240, 300)) #линия Е до H

pygame.draw.line(sc, YELLOW, (50, 650), (50, 50)) #линия F до А
pygame.draw.line(sc, YELLOW, (50, 650), (500, 50)) #линия F до В
pygame.draw.line(sc, YELLOW, (50, 650), (500, 250)) #линия F до С
pygame.draw.line(sc, YELLOW, (50, 650), (700, 460)) #линия F до D
pygame.draw.line(sc, YELLOW, (50, 650), (240, 550)) #линия F до E
pygame.draw.line(sc, YELLOW, (50, 650), (700, 110)) #линия F до G
pygame.draw.line(sc, YELLOW, (50, 650), (240, 300)) #линия F до H

pygame.draw.line(sc, RED, (700, 110), (50, 50)) #линия G до А
pygame.draw.line(sc, RED, (700, 110), (500, 50)) #линия G до В
pygame.draw.line(sc, RED, (700, 110), (500, 250)) #линия G до С
pygame.draw.line(sc, RED, (700, 110), (700, 460)) #линия G до D
pygame.draw.line(sc, RED, (700, 110), (240, 550)) #линия G до E
pygame.draw.line(sc, RED, (700, 110), (50, 650)) #линия G до F
pygame.draw.line(sc, RED, (700, 110), (240, 300)) #линия G до H

pygame.draw.line(sc, ORANGE, (240, 300), (50, 50)) #линия H до А
pygame.draw.line(sc, ORANGE, (240, 300), (500, 50)) #линия H до В
pygame.draw.line(sc, ORANGE, (240, 300), (500, 250)) #линия H до С
pygame.draw.line(sc, ORANGE, (240, 300), (700, 460)) #линия H до D
pygame.draw.line(sc, ORANGE, (240, 300), (240, 550)) #линия H до E
pygame.draw.line(sc, ORANGE, (240, 300), (50, 650)) #линия H до F
pygame.draw.line(sc, ORANGE, (240, 300), (700, 110)) #линия H до G

pygame.draw.circle(sc, WHITE, (50,50), 30) #пункт А
pygame.draw.circle(sc, GREEN, (500,50), 30) #пункт В
pygame.draw.circle(sc, SPRING, (500, 250), 30) #пункт C
pygame.draw.circle(sc, PURPLE, (700, 460), 30) #пункт D
pygame.draw.circle(sc, PINK, (240, 550), 30) #пункт Е
pygame.draw.circle(sc, YELLOW, (50, 650), 30) #пункт F
pygame.draw.circle(sc, RED, (700, 110), 30) #пункт G
pygame.draw.circle(sc, ORANGE, (240, 300), 30) #пункт H

font = pygame.font.Font(None, 42)
А = font.render("А", True, BLACK)
B = font.render("B", True, BLACK)
C = font.render("C", True, BLACK)
D = font.render("D", True, BLACK)
E = font.render("E", True, BLACK)
F = font.render("F", True, BLACK)
G = font.render("G", True, BLACK)
H = font.render("H", True, BLACK)
sc.blit(А, [40, 40] )
sc.blit(B, [490,40] )
sc.blit(C, [490, 240] )
sc.blit(D, [690, 450] )
sc.blit(E, [230, 540] )
sc.blit(F, [40, 640] )
sc.blit(G, [690, 100] )
sc.blit(H, [230, 290] )

pygame.display.update()

import math as m
ms = {i[0]: i.split()[1:] for i in open('1.txt').readlines()[1:]}
l = [print(i, "". join(map(str, ms[i]))) for i in ms]
inp_correct = False
while not inp_correct:
    src = input('выбор начальной точки ' + str([i for i in ms.keys()]) + ': ')
    dest = input('выбор конечной точки ' + str([i for i in ms.keys()]) + ': ')
    inp_correct = src in ms.keys() and dest in ms.keys()
    if not inp_correct:
        print('начальной или конечной точки нет в графе.')
lengths, paths = {}, {}
visited = []
for i in ms.keys():
    lengths[i] = m.inf
paths[src] = []
lengths[src] = 0
while dest not in visited:
    l = m.inf
    minnode = ''
    for n in filter(lambda x: x not in visited, ms.keys()):
        if l > lengths[n]:
            minnode = n
            l = lengths[n]
    visited.append(minnode)
    for i in range(len(ms[minnode])):
        if ms[minnode][i] == 0:
            continue
        curnode = list(ms.keys())[i]
        if int(ms[minnode][i]) + lengths[minnode] < lengths[curnode]:
            lengths[curnode] = int(ms[minnode][i]) + lengths[minnode]
            paths[curnode] = paths[minnode] + [minnode]
print("Путь от ", src, "до ", dest, "по ", "-".join(paths[dest] + [dest]), "имеет минимальную длину ", lengths[dest])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           running = False
pygame.quit()
