import pygame
from Kuba.constants import WIDTH, HEIGHT
from Kuba.board import KubaGame


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Kuba')

def main():
    run = True
    clock = pygame.time.Clock()
    board = KubaGame(("player_1", "B"), ("player_2", "W"))

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()

main()




