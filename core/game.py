import random
import pygame
from core.gun import load_gun, pull_trigger, spin_chamber
from interface.render import draw_layout, draw_outcome, draw_spin, draw_timer_bar, draw_button
from config import FPS
from config import PLAYER_TURN, MACHINE_TURN, SPIN, OUTCOME, GAME_OVER
from config import BLACK, RED, HOVER_RED


def get_timer(player_turn_count):
    if player_turn_count <= 3:
        return 10
    elif player_turn_count <= 5:
        return 7
    else:
        return 4

def should_machine_spin():
    return random.randint(1, 5) == 1

# def player_turn(remaining, bullet_position, player_turn_count):
#     timer = get_timer(player_turn_count)
#     trigger = get_player_input(timer)

#     if trigger is None:
#         show_timeout()
#         return 'bang', remaining
#     elif trigger == 'n':
#         show_chicken()
#         return 'quit', remaining
#     elif trigger != 'y':
#         show_invalid()
#         return 'quit', remaining

    # outcome, remaining = pull_trigger(remaining, bullet_position)
    # show_outcome('player', outcome)
    # return outcome, remaining

def handle_player_input(mouse_pos, remaining, bullet_position, pull_rect, pass_rect, spin_rect):
    if pull_rect.collidepoint(mouse_pos):
        outcome, remaining = pull_trigger(remaining, bullet_position)
        return outcome, remaining, OUTCOME
    elif pass_rect.collidepoint(mouse_pos):
        return 'quit', remaining, OUTCOME
    elif spin_rect.collidepoint(mouse_pos):
        remaining, bullet_position = spin_chamber()
        return 'spin', remaining, SPIN
    else:
        return None, remaining, PLAYER_TURN

def handle_player_timeout(now, turn_start_ticks, current_timer):
    elapsed = (now - turn_start_ticks) / 1000
    if elapsed >= current_timer:
        return 'bang', OUTCOME
    else:
        return None, PLAYER_TURN

# def machine_turn(remaining, bullet_position):
#     if should_machine_spin():
#         remaining, bullet_position = spin_chamber()
#         show_spin('machine')

#     outcome, remaining = pull_trigger(remaining, bullet_position)
#     show_outcome('machine', outcome)
#     return outcome, remaining, bullet_position

def handle_machine_turn(remaining, bullet_position, now):
    if should_machine_spin():
        remaining, bullet_position = spin_chamber()
        return None, remaining, bullet_position, 'machine', SPIN
    outcome, remaining = pull_trigger(remaining, bullet_position)
    return outcome, remaining, bullet_position, 'machine', OUTCOME

def handle_outcome_transition(outcome, actor, player_turn_count):
    if outcome in ('bang', 'quit'):
        return GAME_OVER, player_turn_count, get_timer(player_turn_count)
    elif outcome == 'spin' and actor == 'player':
        return PLAYER_TURN, player_turn_count, get_timer(player_turn_count)
    elif actor == 'player':
        return MACHINE_TURN, player_turn_count, get_timer(player_turn_count)
    else:
        player_turn_count += 1
        current_timer = get_timer(player_turn_count)
        return PLAYER_TURN, player_turn_count, current_timer

def draw_game(screen, state, remaining, chambers, now, turn_start_ticks,
              current_timer, mouse_pos, actor, outcome, alpha, spin_frame,
              pull_rect, pass_rect, spin_rect, button_font):
    if state == PLAYER_TURN:
        elapsed = (now - turn_start_ticks) / 1000
        draw_layout(screen, 'player', remaining, chambers)
        draw_timer_bar(screen, elapsed, current_timer)

        if pull_rect.collidepoint(mouse_pos):
            pull_color = HOVER_RED
        else:
            pull_color = RED
        if pass_rect.collidepoint(mouse_pos):
            pass_color = HOVER_RED
        else:
            pass_color = RED
        if spin_rect.collidepoint(mouse_pos):
            spin_color = HOVER_RED
        else:
            spin_color = RED

        draw_button(screen, 'Pull', pull_rect, pull_color, button_font)
        draw_button(screen, 'Pass', pass_rect, pass_color, button_font)
        draw_button(screen, 'Spin', spin_rect, spin_color, button_font)
    elif state == MACHINE_TURN:
        draw_layout(screen, 'machine', remaining, chambers)
    elif state == SPIN:
        draw_layout(screen, actor, remaining, chambers)
        draw_spin(screen, actor, spin_frame)
    elif state == OUTCOME:
        draw_layout(screen, actor, remaining, chambers)
        draw_outcome(screen, actor, outcome, alpha)

def game_loop(screen):
    clock = pygame.time.Clock()
    remaining, bullet_position = load_gun()
    chambers = remaining
    turn = random.choice([PLAYER_TURN, MACHINE_TURN])
    state = turn
    player_turn_count = 0
    outcome = None
    actor = None
    anim_timer = 0
    anim_duration = 2000
    spin_duration = 1500
    spin_frame = 0
    frame_tick = 0
    mouse_pos = (0, 0)
    machine_turn_handled = False
    turn_start_ticks = pygame.time.get_ticks()
    current_timer = get_timer(player_turn_count)
    button_font = pygame.font.SysFont('Arial', 28)

    pull_rect = pygame.Rect(150, 480, 120, 45)
    pass_rect = pygame.Rect(290, 480, 120, 45)
    spin_rect = pygame.Rect(430, 480, 120, 45)

    while True:
        screen.fill(BLACK)
        now = pygame.time.get_ticks()
        mouse_pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if state == PLAYER_TURN and event.type == pygame.MOUSEBUTTONDOWN:
                outcome, remaining, state = handle_player_input(
                    mouse_pos, remaining, bullet_position, pull_rect, pass_rect, spin_rect)
                if state in (OUTCOME, SPIN):
                    actor = 'player'
                    anim_timer = now

        if state == PLAYER_TURN:
            timeout_outcome, new_state = handle_player_timeout(now, turn_start_ticks, current_timer)
            if new_state == OUTCOME:
                outcome = timeout_outcome
                actor = 'player'
                anim_timer = now
                state = OUTCOME

        if state == MACHINE_TURN and not machine_turn_handled:
            outcome, remaining, bullet_position, actor, state = handle_machine_turn(remaining, bullet_position, now)
            anim_timer = now
            machine_turn_handled = True

        if state == SPIN:
            frame_tick += 1
            spin_frame = frame_tick // 10
            if now - anim_timer >= spin_duration:
                if actor == 'machine':
                    outcome, remaining = pull_trigger(remaining, bullet_position)
                anim_timer = now
                state = OUTCOME

        if state == OUTCOME:
            alpha = min(255, (now - anim_timer) * 2)
            if now - anim_timer >= anim_duration:
                state, player_turn_count, current_timer = handle_outcome_transition(outcome, actor, player_turn_count)
                if state == PLAYER_TURN:
                    turn_start_ticks = pygame.time.get_ticks()
                    machine_turn_handled = False
                elif state == MACHINE_TURN:
                    machine_turn_handled = False
        else:
            alpha = 0

        draw_game(screen, state, remaining, chambers, now, turn_start_ticks,
                  current_timer, mouse_pos, actor, outcome, alpha, spin_frame,
                  pull_rect, pass_rect, spin_rect, button_font)

        if state == GAME_OVER or remaining <= 0:
            return

        pygame.display.flip()
        clock.tick(FPS)
