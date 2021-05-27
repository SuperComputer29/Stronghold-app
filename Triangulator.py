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
bl, bw = (360, 40)  # bl stands for Button Length and bw stands for Button width
font = pygame.font.Font(None, 32)

info1_image = pygame.image.load(os.path.join('Triangulation assets', 'Main menu', 'Info_1.png'))
info1 = pygame.transform.scale(info1_image, (bl, bw))

info2_image = pygame.image.load(os.path.join('Triangulation assets', 'Main menu', 'Info_2.png'))
info2 = pygame.transform.scale(info2_image, (bl, bw))

S1_image = pygame.image.load(os.path.join('Triangulation assets', 'Main menu', 'StrongholdButton_1.png'))
S1 = pygame.transform.scale(S1_image, (bl, bw))

S2_image = pygame.image.load(os.path.join('Triangulation assets', 'Main menu', 'StrongholdButton_2.png'))
S2 = pygame.transform.scale(S2_image, (bl, bw))

logo_image = pygame.image.load(os.path.join('Triangulation assets', 'Main menu', 'logo.png'))
logo = pygame.transform.scale(logo_image, (720, 120))

info_menu = pygame.image.load(os.path.join('Triangulation assets', 'Info_menu', 'info.png'))
bg = pygame.image.load(os.path.join('Triangulation assets', 'Main menu', 'background.png'))

bare_menu = pygame.image.load(os.path.join('Triangulation assets', 'The action menu', 'bare menu.png'))

back = pygame.image.load(os.path.join('Triangulation assets', 'The action menu', 'back.png'))
calc = pygame.image.load(os.path.join('Triangulation assets', 'The action menu', 'calc_button.png'))

x1 = pygame.image.load(os.path.join('Triangulation assets', 'The action menu', 'First x coord.png'))
y1 = pygame.image.load(os.path.join('Triangulation assets', 'The action menu', 'First y coord.png'))
x2 = pygame.image.load(os.path.join('Triangulation assets', 'The action menu', 'Second x coord.png'))
y2 = pygame.image.load(os.path.join('Triangulation assets', 'The action menu', 'Second y coord.png'))

t1 = pygame.image.load(os.path.join('Triangulation assets', 'The action menu', 'First angle.png'))
t2 = pygame.image.load(os.path.join('Triangulation assets', 'The action menu', 'Second angle.png'))
y_1 = ''
x_2 = ''
y_2 = ''
t_1 = ''
t_2 = ''

fps = 60


info_rect = pygame.Rect(340, 300, bl, bw)
calc_rect = pygame.Rect(340, 400, bl, bw)
back_rect = pygame.Rect(550, 620, bl+10, bw+20)
find_rect = pygame.Rect(130, 620, bl+10, bw+20)


def main_menu():
    win.blit(bg, (0, 0))
    win.blit(info1, (info_rect.x, info_rect.y))
    win.blit(S1, (calc_rect.x, calc_rect.y))
    win.blit(logo, (170, 100))
    pygame.display.update()


def stronghold_calculator():
    win.blit(bare_menu, (0, 0))
    win.blit(x1, (330, 100))
    win.blit(y1, (330, 220))
    win.blit(x2, (330, 340))
    win.blit(y2, (330, 460))
    win.blit(t1, (760, 170))
    win.blit(t2, (760, 390))
    win.blit(back, (550, 620))
    win.blit(calc, (130, 620))

    x_1 = ''
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if back_rect.collidepoint(x, y):
                    main()
                elif find_rect.collidepoint(x, y):
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            x_1 = x_1[:-1]
                        else:
                            x_1 += event.unicode
                            X1 = font.render(x_1, True, white)
                            win.blit(X1, (330, 620))
                            pygame.display.update( )
    pygame.display.update()


def Info_menu():
    win.blit(info_menu, (0, 0))
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main()


def UpdateInfo():
    win.blit(info2, (340, 300))
    pygame.display.update()


def UpdateCalc():
    win.blit(S2, (340, 400))
    pygame.display.update()


def main():
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
                    info = True
                    while info:
                        Info_menu()
                elif calc_rect.collidepoint(x, y):
                    go_back = True
                    while go_back:
                        stronghold_calculator()
        if info_rect.collidepoint(pygame.mouse.get_pos()):
            UpdateInfo()
        if calc_rect.collidepoint(pygame.mouse.get_pos()):
            UpdateCalc()

        main_menu()

    pygame.quit()


if __name__ == "__main__":
    main()
