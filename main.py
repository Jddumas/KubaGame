import pygame
from Kuba.constants import WIDTH, HEIGHT, SQUARE_SIZE
from Kuba.board import Board
from Kuba.game import Game


FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Kuba')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    # piece = board.get_piece(0, 0)
    # board.make_move(piece, (4, 3))

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.get_piece(row, col)

        game.update()
    pygame.quit()


main()




