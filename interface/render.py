import pygame
from config import WIDTH, HEIGHT
from config import (WHITE, GRAY, BLUE, RED, YELLOW, GREEN)


def draw_layout(screen, turn, remaining, chambers):
    font = pygame.font.SysFont('Arial', 20)
    small_font = pygame.font.SysFont('Arial', 20)

    # divider for player and machine
    pygame.draw.line(screen, GRAY, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT), 2)

    ## player side
    if turn == 'player':
        player_color = BLUE
    else:
        player_color = GRAY

    player_label = font.render('PLAYER', True, player_color)
    screen.blit(player_label, (150, 40))

    ## machine side
    if turn == 'machine':
        machine_color = RED
    else:
        machine_color = GRAY

    machine_label = font.render('MACHINE', True, machine_color)
    screen.blit(machine_label, (150, 40))

    # chambers remaining
    chambers_text = small_font.render(f"Chambers: {remaining}/{chambers}", True, WHITE)
    screen.blit(chambers_text, (WIDTH // 2 - 70, HEIGHT - 40))

def draw_outcome(screen, actor, outcome, alpha):
    font = pygame.font.SysFont('Arial', 42, bold=True)

    if outcome == 'bang':
        if actor == 'player':
            text = "BANG! You're Dead..."
            color = RED
        else:
            text = "BANG! Machine's Dead!"
            color = GREEN
    elif outcome == 'click':
        if actor == 'player':
            text = "Click! You Survived!"
            color = BLUE
        else:
            text = "Click! Machine Survived!"
            color = YELLOW
    else:
        return

    surface = font.render(text, True, color)
    surface.set_alpha(alpha)
    screen.blit(surface, surface.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

def draw_spin(screen, actor, frame):
    font = pygame.font.SysFont('Arial', 36, bold=True)

    actor = actor.capatalize()
    dots = '.' * (frame % 4)
    text = f"{actor} spins the chamber {dots}"

    label = font.render(text, True, YELLOW)
    screen.blit(label, label.get_rect(center=(WIDTH // 2, HEIGHT // 2)))

def draw_timer_bar(screen, elapsed, total):
    bar_width = 300
    bar_height = 24
    x, y = WIDTH // 4 - bar_width // 2, 520

    ratio = max(0, 1 - elapsed / total)
    if ratio > 0.5:
        color = GREEN
    elif ratio > 0.25:
        color = YELLOW
    else:
        color = RED

    pygame.draw.rect(screen, GRAY, (x, y, bar_width, bar_height), border_radius=6)
    pygame.draw.rect(screen, color, (x, y, int(bar_width * ratio), bar_height), border_radius=6)
