import pygame
import sys

WIDTH, HEIGHT = 800, 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (100, 0, 0)
HOVER_RED = (220, 30, 30)

def init_window():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Russian Roulette')
    return screen

def draw_button(screen, text, rect, color, font):
    pygame.draw.rect(screen, color, rect, border_radius=8)
    label = font.render(text, True, WHITE)
    label_rect = label.get_rect(center=rect.center)
    screen.blit(label, label_rect)

def main_menu(screen):
    clock = pygame.time.Clock()
    title_font = pygame.font.SysFont('Arial', 64, bold=True)
    button_font = pygame.font.SysFont('Arial', 32)

    start_rect = pygame.Rect(300, 280, 200, 55)
    quit_rect = pygame.Rect(300, 360, 200, 55)

    while True:
        screen.fill(BLACK)
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_rect.collidepoint(mouse_pos):
                    return 'start'
                if quit_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()


        ## title
        title = title_font.render('Russian Roulette', True, RED)
        screen.blit(title, title.get_rect(center=(WIDTH // 2, 160)))

        # button with mouse hover
        draw_button(screen, 'Start', start_rect,
         HOVER_RED if start_rect.collidepoint(mouse_pos) else RED, button_font)
        draw_button(screen, 'Quit', quit_rect,
            HOVER_RED if quit_rect.collidepoint(mouse_pos) else RED, button_font)

        pygame.display.flip()
        clock.tick(FPS)
