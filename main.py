import pygame
import imageio
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Test")

background_path = "data/gif/menu.gif"

click_sound = pygame.mixer.Sound("data/sound/click.wav")
button_sound = pygame.mixer.Sound("data/sound/button.wav")

def load_video(path):
    reader = imageio.get_reader(path)
    frames = []
    for i, frame in enumerate(reader):
        surface = pygame.surfarray.make_surface(frame)
        frames.append(surface)
    return frames

def scale_image(image, target_width, target_height):
    return pygame.transform.scale(image, (target_width, target_height))

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def main_menu():
    menu = True
    current_frame = 0

    background = load_video(background_path)
    
    clock = pygame.time.Clock()

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if new_game.collidepoint(mouse_pos):
                    button_sound.play()
                    main()
                else:
                    click_sound.play()

        mouse_pos = pygame.mouse.get_pos()

        background_scaled = scale_image(background[current_frame], SCREEN_WIDTH, SCREEN_HEIGHT)
        screen.blit(background_scaled, (0, 0))

        title_font = pygame.font.Font(None, 105)
        draw_text("Заголовок", title_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)

        new_game = pygame.Rect((SCREEN_WIDTH - 200) // 2, (SCREEN_HEIGHT - 50) // 2, 200, 50)
        pygame.draw.rect(screen, WHITE, new_game)
        play_font = pygame.font.Font(None, 40)
        draw_text("Кнопка", play_font, BLACK, new_game.centerx, new_game.centery)

        if new_game.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BLACK, new_game, 3)

        current_frame += 1
        if current_frame >= len(background):
            current_frame = 0
            
        clock.tick(30)
        pygame.display.flip()

def main():
    pass

main_menu()