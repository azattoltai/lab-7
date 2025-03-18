import pygame
import os

pygame.init()

playlist = []
music_folder = "/Users/azattoltai/Desktop/Lab 7/musics"
allmusic = os.listdir(music_folder)

for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song))

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Ernar Amandyk")
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join("music-elements", "background.jpg"))
background = pygame.transform.scale(background, (800, 800))

panel_height = 150
bg = pygame.Surface((800, panel_height))
bg.fill((255, 255, 255))

font2 = pygame.font.SysFont(None, 30)

playb = pygame.image.load(os.path.join("music-elements", "play.png"))
pausb = pygame.image.load(os.path.join("music-elements", "pause.png"))
nextb = pygame.image.load(os.path.join("music-elements", "next.png"))
prevb = pygame.image.load(os.path.join("music-elements", "back.png"))

button_size = 70
playb = pygame.transform.scale(playb, (button_size, button_size))
pausb = pygame.transform.scale(pausb, (button_size, button_size))
nextb = pygame.transform.scale(nextb, (button_size, button_size))
prevb = pygame.transform.scale(prevb, (button_size, button_size))

button_y = 700  
play_x, next_x, prev_x = 365, 460, 273

index = 0
aplay = False

pygame.mixer.music.load(playlist[index]) 
pygame.mixer.music.play(-1)  
aplay = True 

run = True

while run:
    screen.blit(background, (0, 0))  
    screen.blit(bg, (0, 650)) 

    song_name = os.path.basename(playlist[index]).replace(".mp3", "")
    text2 = font2.render(song_name, True, (20, 20, 50))
    text_rect = text2.get_rect(center=(400, 670))
    screen.blit(text2, text_rect)

    if aplay:
        screen.blit(pausb, (play_x, button_y))
    else:
        screen.blit(playb, (play_x, button_y))

    screen.blit(nextb, (next_x, button_y))
    screen.blit(prevb, (prev_x, button_y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if event.key == pygame.K_RIGHT:
                index = (index + 1) % len(playlist)  
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_LEFT:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play(-1)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            if play_x <= mx <= play_x + button_size and button_y <= my <= button_y + button_size:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()

            if next_x <= mx <= next_x + button_size and button_y <= my <= button_y + button_size:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play(-1)

            if prev_x <= mx <= prev_x + button_size and button_y <= my <= button_y + button_size:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play(-1)

    clock.tick(24)