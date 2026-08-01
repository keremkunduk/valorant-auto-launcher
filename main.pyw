from python_imagesearch.imagesearch import imagesearch
from time import sleep as sl
from pyautogui import moveTo, leftClick, keyDown, keyUp
import os
import subprocess

devam = True

try:
    # os.chdir('D:/[A]Projects/launch valorant')
    # os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Riot Games/VALORANT.lnk')
    # os.startfile('C:/Riot Games/Riot Client/RiotClientServices.exe') requires config parameters(--abcdx) and i didn't want to use subprocess.run() because unnecessary

    os.startfile('VALORANT.lnk')

    while devam:
        button = imagesearch('oyna.png')
        print(button)
        sl(0.2)

        if str(button[0]) != '-1':
            devam = False

    moveTo(button[0], button[1], duration=0)
    sl(0.2)
    leftClick()
    sl(0.5)
    keyDown('alt')
    sl(0.01)
    keyDown('f4')
    sl(0.1)

    keyUp('alt')
    keyUp('f4')

except Exception as hata:
    op = open('hata.txt', 'w')
    op.write(str(hata))
    op.close()
    os.startfile('hata.txt')