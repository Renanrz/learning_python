#tocar uma musica para cada um dos 4 e uma quinta musica caso seja outro valor
import pygame
pygame.mixer.init()
pygame.init()
p1 = str(input('Digite aqui o nome de uma pessoa q mora no 206: '))
if p1 == 'Renan':
    pygame.mixer.music.load('RR.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
else:
    if p1 == 'Mayara':
        pygame.mixer.music.load('MB.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()
    else:
        if p1 == 'Rai':
            pygame.mixer.music.load('RS.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
        else:
            if p1 == 'Dave':
                pygame.mixer.music.load('Dave.mp3')
                pygame.mixer.music.play()
                pygame.event.wait()
            else:
                pygame.mixer.music.load('other.mp3')
                pygame.mixer.music.play()
                pygame.event.wait()

