import pygame

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (180, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 100, 220)
YELLOW = (220, 200, 0)
GRAY = (60, 60, 60)

def draw_layout(screen, turn, remaining, chambers):
    font = pygame.font.SysFont('Arial', 20)
    small_font = pygame.font.SysFont('Arial', 20)

    # divider for player and machine
    pygame.draw.line(screen, GRAY, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

    ## player side
    player_label = font.render('PLAYER', True, BLUE if turn == 'player' else GRAY)
    screen.blit(player_label, (150, 40))

    ## machine side
    machine_label = font.render('MACHINE', True, RED if turn == 'machine' else GRAY)
    screen.blit(machine_label, (150, 40))

    # chambers remaining
    chambers_text = small_font.render(f"Chambers: {remaining}/{chambers}", True, WHITE)
    screen.blit(chambers_text, (WIDTH // 2 - 70, HEIGHT - 40))

def draw_outcome(screen, actor, outcome, alpha):
    font = pygame.font.SysFont('Arial', 42, bold=True)

    if outcome == 'bang':
        text = "BANG! You're Dead..." if actor == 'player' else "BANG! Machine's Dead!"
        color = BLUE if actor == 'player' else YELLOW
    else:
        return

    surface = font.render(text, True, color)
    surface.set_alpha(alpha)
    screen.blit(surface, surface.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

def draw_spin(screen, actor, frame):
    font = pygame.font.SysFont('Arial', 36, bold=True)
    dots = '.' * (frame % 4)
    text = f"{actor.captalize()} spins the chamber {dots}"
    label = font.render(text, True, YELLOW)
    screen.blit(label, label.get_rect(center=(WIDTH // 2, HEIGHT // 2)))
