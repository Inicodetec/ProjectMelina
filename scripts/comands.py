import subprocess
import pygame
from pygame.locals import *
import time

pygame.init()
pygame.mixer.music.load('./audios/bv.mp3')
pygame.mixer.music.play()

while True:
    #digitar nome
    nome = "Fabio"
    print ("Olá", nome)

    cm = input("Como posso ajudar? ")
    if cm == "abrir desktop":
        pygame.mixer.music.load('./audios/abrindo.mp3')
        pygame.mixer.music.play()
        comando = (r'start %windir%\explorer.exe "c:\users\Inicode Dev\desktop"')
        print(subprocess.getoutput(comando))
    elif cm == "abrir downloads":
        pygame.mixer.music.load('./audios/abrindo.mp3')
        pygame.mixer.music.play()
        comando = (r'start %windir%\explorer.exe "c:\users\Inicode Dev\downloads"')
        print(subprocess.getoutput(comando))
    elif cm == "abrir google":
        pygame.mixer.music.load('./audios/google.mp3')
        pygame.mixer.music.play()
        comando = (r'start %windir%\explorer.exe "C:\Program Files\Google\Chrome\Application\chrome.exe"')
        print(subprocess.getoutput(comando))
    elif cm == "desligar":
        pygame.mixer.music.load('./audios/desligar.mp3')
        pygame.mixer.music.play()
        comando = (r'shutdown -s -t 10')
        print(subprocess.getoutput(comando))
    elif cm == "encerrar":
        print("Ok, até mais...")
        pygame.mixer.music.load('./audios/encerrar.mp3')
        pygame.mixer.music.play()
        time.sleep(5)
        exit()
    else:
        print("Comando não encontrado")

    

