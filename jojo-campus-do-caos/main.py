import pygame
import sys
import imagens_jojos
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (70, 130, 180)

pygame.init()
pygame.display.set_caption("Menu Inicial - Jogo Exemplo")
FONT = pygame.font.SysFont(None, 48)
DIALOG_FONT = pygame.font.SysFont(None, 28)
BIG_FONT = pygame.font.SysFont(None, 48)

def load_image(path, scale=1.0):
    img = pygame.image.load(path).convert_alpha()
    if scale != 1.0:
        w, h = img.get_size()
        img = pygame.transform.scale(img, (int(w * scale), int(h * scale)))
    return img

class Button:
    def __init__(self, pos, callback, text=None, image_path=None, scale=1.0):
        self.callback = callback
        self.text = text
        self.image_path = image_path
        self.default_color = WHITE
        self.highlight_color = HIGHLIGHT

        if image_path:
            self.image = load_image(image_path, scale)
            self.rect = self.image.get_rect(center=pos)
        else:
            self.label = FONT.render(self.text, True, self.default_color)
            self.rect = self.label.get_rect(center=pos)

    def draw(self, surface, mouse_pos):
        if getattr(self, "image", None):
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
            Button((mid_x, start_y), self.start_game, text="Iniciar", image_path="imagens_jojos/button_iniciar.png", scale=0.5),
            Button((mid_x, start_y + gap), self.show_options, text="Opções", image_path="imagens_jojos/button_opcoes.png", scale=0.5),
            Button((mid_x, start_y + 2 * gap), self.exit_game, text="Sair", image_path="imagens_jojos/button_sair.png", scale=0.5),
        ]

        self.running = True
        original_bg = load_image("imagens_jojos/jojos_tela_inicial_sembotoes.png")
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
        self.show_if_frente()

    def show_if_frente(self):
        img = load_image("imagens_jojos/if_frente.png")
        img_w, img_h = img.get_size()
        screen_ratio = SCREEN_WIDTH / SCREEN_HEIGHT
        img_ratio = img_w / img_h
        if img_ratio > screen_ratio:
            scale_w = SCREEN_WIDTH
            scale_h = int(SCREEN_WIDTH / img_ratio)
        else:
            scale_h = SCREEN_HEIGHT
            scale_w = int(SCREEN_HEIGHT * img_ratio)
        img = pygame.transform.scale(img, (scale_w, scale_h))
        pos = ((SCREEN_WIDTH - scale_w) // 2, (SCREEN_HEIGHT - scale_h) // 2)

        caixa_img = load_image("imagens_jojos/caixa_dialogo.png", scale=0.5)
        caixa_pos = ((SCREEN_WIDTH - caixa_img.get_width()) // 2,
                     (SCREEN_HEIGHT - caixa_img.get_height()) // 2)

        texto_dialogo_paragrafos = [
            "OBS: Aperte espaço para avançar...",
            """Era uma sexta-feira, final de expediente. 
Eu, Jojo, como qualquer outro professor, contava os minutos para ir para casa.
Na sala dos servidores, durante o intervalo, todos já deixavam bem claro o quanto ansiavam pela liberdade do fim de semana.""",
            """O relógio bateu a hora, e fui bater o ponto, sonhando com o sofá e um café quente.  
Mas então, um pensamento me congelou:
As provas recém-aplicadas… ainda estavam na salinha de matemática!
Corri como um raio para não me atrasar mais ainda.
Assim que fechei a porta daquela pequena sala, um clarão ofuscante invadiu todo o campus.""",
            """Instintivamente, corri para ver o que estava acontecendo. 
Foi aí que vi meus colegas… ou melhor, o que restava deles.

O brilho havia desaparecido dos olhos.
A esperança parecia ter sido arrancada de suas almas.""",
            """Aproximando-me, tentei falar com eles, fazer com que voltassem a si. 
Mas as respostas eram sempre as mesmas:
Trabalho… produção… nada nos tirará do campus… nem que para isso tenhamos que lutar até o fim…

Foi nesse momento que entendi: eu era o único que tinha escapado daquele estranho controle. Talvez porque estivesse dentro da minha amada e escondida salinha, protegida de algo – ou alguém – havia tomado o controle de todos.

E se eu quisesse trazê-los de volta, teria que fazê-los lembrar de quem eram…
mesmo que para isso fosse preciso mostrar a eles o poder dos meus bíceps.""",
            """E foi assim,  que a minha missão começou!"""
        ]

        current_paragraph_index = 0
        texto_index = 0
        ultimo_tempo = pygame.time.get_ticks()
        intervalo = 65

        clock = pygame.time.Clock()
        running = True
        start_time = pygame.time.get_ticks()
        show_caixa = False
        texto_completo = False
        fade_alpha = 0
        fade_in_speed = 5

        while running:
            current_time = pygame.time.get_ticks()
            if current_time - start_time >= 2000:
                show_caixa = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    elif event.key == pygame.K_SPACE:
                        if current_paragraph_index < len(texto_dialogo_paragrafos) - 1:
                            if not texto_completo:
                                texto_index = len(texto_dialogo_paragrafos[current_paragraph_index])
                                texto_completo = True
                            else:
                                current_paragraph_index += 1
                                texto_index = 0
                                texto_completo = False
                                fade_alpha = 0
                        else:
                            if texto_completo and fade_alpha >= 255:
                                running = False
                            else:
                                texto_index = len(texto_dialogo_paragrafos[current_paragraph_index])
                                texto_completo = True

            self.screen.fill(BLACK)
            self.screen.blit(img, pos)

            if show_caixa and current_paragraph_index < len(texto_dialogo_paragrafos) - 1:
                self.screen.blit(caixa_img, caixa_pos)
                if not texto_completo and current_time - ultimo_tempo >= intervalo:
                    ultimo_tempo = current_time
                    texto_index += 1
                    if texto_index > len(texto_dialogo_paragrafos[current_paragraph_index]):
                        texto_index = len(texto_dialogo_paragrafos[current_paragraph_index])
                        texto_completo = True
                margem_x = int(caixa_img.get_width() * 0.1)
                margem_y = int(caixa_img.get_height() * 0.25)
                max_text_width = int(caixa_img.get_width() * 0.8)
                texto_a_exibir = texto_dialogo_paragrafos[current_paragraph_index][:texto_index]
                self.render_text(self.screen, texto_a_exibir,
                                 caixa_pos[0] + margem_x,
                                 caixa_pos[1] + margem_y,
                                 max_text_width)
            elif show_caixa:
                if texto_index < len(texto_dialogo_paragrafos[current_paragraph_index]):
                    if current_time - ultimo_tempo >= intervalo:
                        ultimo_tempo = current_time
                        texto_index += 1
                    texto_a_exibir = texto_dialogo_paragrafos[current_paragraph_index][:texto_index]
                else:
                    texto_a_exibir = texto_dialogo_paragrafos[current_paragraph_index]
                if fade_alpha < 255 and texto_completo:
                    fade_alpha = min(fade_alpha + fade_in_speed, 255)
                text_surface = self.render_text_surface(texto_a_exibir, BIG_FONT, WHITE, 700)
                text_surface.set_alpha(fade_alpha)
                text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                self.screen.blit(text_surface, text_rect)

            pygame.display.flip()
            clock.tick(FPS)

    def render_text(self, surface, text, x, y, max_width):
        words = text.split(' ')
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if DIALOG_FONT.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
        for i, line in enumerate(lines):
            line_surface = DIALOG_FONT.render(line, True, WHITE)
            surface.blit(line_surface, (x, y + i * int(DIALOG_FONT.get_height() * 1.2)))

    def render_text_surface(self, text, font, color, max_width):
        words = text.split(' ')
        lines = []
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
        line_surfaces = [font.render(line, True, color) for line in lines]
        height = sum(line.get_height() for line in line_surfaces) + (len(line_surfaces)-1) * int(font.get_height() * 0.2)
        width = max(line.get_width() for line in line_surfaces)
        surface = pygame.Surface((width, height), pygame.SRCALPHA)
        y = 0
        for line_surface in line_surfaces:
            surface.blit(line_surface, (0, y))
            y += line_surface.get_height() + int(font.get_height() * 0.2)
        return surface

if __name__ == "__main__":
    Game().run()
