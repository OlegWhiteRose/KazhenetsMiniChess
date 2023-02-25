import pygame
import sys
import os
from data.classes.Board import Board

pygame.init()

WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)

board = Board(WINDOW_SIZE[0], WINDOW_SIZE[1])


def load_image(name, color_key=None):
    fullname = os.path.join('data\imgs', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()


def terminate():
    pygame.quit()
    sys.exit


def start_screen():
    fon = pygame.transform.scale(load_image('start_screen_chess.jpg'), WINDOW_SIZE)
    screen.blit(fon, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()


if __name__ == '__main__':
    start_screen()
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            # Quit the game if the user presses the close button
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # If the mouse is clicked
                if event.button == 1:
                    board.handle_click(mx, my)
        if board.is_in_checkmate('black'):  # If black is in checkmate
            print('White wins!')
            running = False
        elif board.is_in_checkmate('white'):  # If white is in checkmate
            print('Black wins!')
            running = False
        # Draw the board
        draw(screen)
