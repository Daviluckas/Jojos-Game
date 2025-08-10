import pygame
import sys
import imagens_jojos

# --------- Configurações ---------
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (70, 130, 180)

pygame.init()
pygame.display.set_caption("Menu Inicial - Jogo Exemplo")
FONT = pygame.font.SysFont(None, 48)


class Button:
    def __init__(self, pos, callback, text=None, image_path=None, scale=1.0):
        self.callback = callback
        self.text = text
        self.image_path = image_path

        self.default_color = WHITE
        self.highlight_color = HIGHLIGHT

        if image_path:
            self.image = pygame.image.load(image_path).convert_alpha()

            if scale != 1.0:
                self.image = pygame.transform.scale_by(self.image, scale)

            self.rect = self.image.get_rect(center=pos)
        else:
            self.label = FONT.render(self.text, True, self.default_color)
            self.rect = self.label.get_rect(center=pos)

    def draw(self, surface, mouse_pos):
        if self.image_path:
            surface.blit(self.image, self.rect)
        else:
            if self.rect.collidepoint(mouse_pos):
                label = FONT.render(self.text, True, self.highlight_color)
            else:
                label = self.label
            surface.blit(label, self.rect)

    def check_click(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.callback()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        mid_x = SCREEN_WIDTH // 2
        start_y = SCREEN_HEIGHT // 2 - 50
        gap = 150

        self.buttons = [
            Button((mid_x, start_y), self.start_game, image_path="imagens_jojos/button_iniciar.png", scale=0.5),
            Button((mid_x, start_y + gap), self.show_options, image_path="imagens_jojos/button_opcões.png", scale=0.5),
            Button((mid_x, start_y + 2 * gap), self.exit_game, image_path="imagens_jojos/button_sair.png", scale=0.5),
        ]

        self.running = True

        original_bg = pygame.image.load("imagens_jojos/jojos_tela_inicial_sembotoes.png").convert()

        img_w, img_h = original_bg.get_size()
        screen_ratio = SCREEN_WIDTH / SCREEN_HEIGHT
        img_ratio = img_w / img_h

        if img_ratio > screen_ratio:
            scale_w = SCREEN_WIDTH
            scale_h = int(SCREEN_WIDTH / img_ratio)
        else:
            scale_h = SCREEN_HEIGHT
            scale_w = int(SCREEN_HEIGHT * img_ratio)

        self.background = pygame.transform.scale(original_bg, (scale_w, scale_h))

        self.bg_pos = ((SCREEN_WIDTH - scale_w) // 2, (SCREEN_HEIGHT - scale_h) // 2)

    def start_game(self):
        print("Iniciando o jogo...")
        self.running = False

    def show_options(self):
        print("Abrindo opções...")

    def exit_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit_game()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for btn in self.buttons:
                        btn.check_click(mouse_pos)

            self.screen.fill(BLACK)

            self.screen.blit(self.background, self.bg_pos)
            
            for btn in self.buttons:
                btn.draw(self.screen, mouse_pos)

            pygame.display.flip()
            clock.tick(FPS)


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def run(self):
        menu = Menu(self.screen)
        menu.run()
        self.game_loop()

    def game_loop(self):
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((30, 30, 30))
            pygame.display.flip()
            clock.tick(FPS)
        pygame.quit()


if __name__ == "__main__":
    Game().run()
