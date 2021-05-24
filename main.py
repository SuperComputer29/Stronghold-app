import pygame
import os
pygame.font.init()
pygame.mixer.init()

width, height = 1080, 720

win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Triangulation calculator")

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

border = pygame.Rect(width // 2 - 5, 0, 10, height)
bl, bw = (360, 40)              # bl stands for Button Length and bw stands for Button width

info1_image = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'Main menu', 'Info_1.png'))
info1 = pygame.transform.scale(info1_image, (bl, bw))

info2_image = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'Main menu', 'Info_2.png'))
info2 = pygame.transform.scale(info2_image, (bl, bw))

S1_image = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'Main menu', 'StrongholdButton_1.png'))
S1 = pygame.transform.scale(S1_image, (bl, bw))

S2_image = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'Main menu', 'StrongholdButton_2.png'))
S2 = pygame.transform.scale(S2_image, (bl, bw))

logo_image = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'Main menu', 'logo.png'))
logo = pygame.transform.scale(logo_image, (720, 120))

bg = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'Main menu', 'background.png'))

bare_menu = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'The action menu', 'bare menu.png'))

back = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'The action menu', 'back.png'))
calc = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'The action menu', 'calc_button.png'))

x1 = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'The action menu', 'First x coord.png'))
y1 = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'The action menu', 'First y coord.png'))
x2 = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'The action menu', 'Second x coord.png'))
y2 = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'The action menu', 'Second y coord.png'))

t1 = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'The action menu', 'First angle.png'))
t2 = pygame.image.load(os.path.join('Stronghold triangulation app', 'Triangulation assets', 'The action menu', 'Second angle.png'))
fps = 60


def draw_window(info_rect, calc_rect):
    win.blit(bg, (0, 0))
    win.blit(info1, (info_rect.x, info_rect.y))
    win.blit(S1, (calc_rect.x, calc_rect.y))
    win.blit(logo, (170, 100))
    pygame.display.update()


def draw_window_2(back_rect):
    win.blit(bare_menu, (0, 0))
    win.blit(x1, (330, 100))
    win.blit(y1, (330, 220))
    win.blit(x2, (330, 340))
    win.blit(y2, (330, 460))
    win.blit(t1, (760, 170))
    win.blit(t2, (760, 390))
    win.blit(back, (550, 620))
    win.blit(calc, (130, 620))
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if back_rect.collidepoint(x, y):
                    main()
    pygame.display.update()


def UpdateInfo():
    win.blit(info2, (340, 300))
    pygame.display.update()


def UpdateCalc():
    win.blit(S2, (340, 400))
    pygame.display.update()


def main():
    info_rect = pygame.Rect(340, 300, bl, bw)
    calc_rect = pygame.Rect(340, 400, bl, bw)
    back_rect = pygame.Rect(550, 620, bl, bw)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if info_rect.collidepoint(x, y):
                    print("yay")
                elif calc_rect.collidepoint(x, y):
                    for i in range(399):
                        draw_window_2(back_rect)
        if info_rect.collidepoint(pygame.mouse.get_pos()):
            UpdateInfo()
        if calc_rect.collidepoint(pygame.mouse.get_pos()):
            UpdateCalc()

        draw_window(info_rect, calc_rect)

    pygame.quit()


if __name__ == "__main__":
    main()


