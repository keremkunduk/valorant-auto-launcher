from python_imagesearch.imagesearch import imagesearch
from time import sleep as sl
from pyautogui import moveTo, leftClick, keyDown, keyUp, position, press
import os
# import subprocess
from keyboard import write
import winreg

devam = True

def durum_al():
    global fare_hizi
    yol = r"Control Panel\Mouse"
    anahtar = winreg.OpenKey(winreg.HKEY_CURRENT_USER, yol)

    fare_hizi, _ = winreg.QueryValueEx(anahtar, "MouseSpeed")
    winreg.CloseKey(anahtar)

def durum_degistir():
    press('win')
    # sl(0.001)
    write('işaretçi hassasiyeti')
    sl(0.1)
    press('enter')
    sl(0.5)
    press('space')
    sl(0.1)
    keyDown('alt')
    sl(0.001)
    keyDown('f4')
    sl(0.001)
    keyUp('alt')
    keyUp('f4')  

try:
    # os.chdir('D:/[A]Projects/launch valorant')
    # os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Riot Games/VALORANT.lnk')
    # os.startfile('C:/Riot Games/Riot Client/RiotClientServices.exe') requires config parameters(--abcdx) and i didn't want to use subprocess.run() because it was unnecessary

    durum_al()

    os.startfile('VALORANT.lnk')


    print(f'ayar durumu: {fare_hizi}')

    if int(fare_hizi) == 1:
        durum_degistir()

    while devam:
        button = imagesearch('oyna.png')
        update = imagesearch('guncelle.png')
        print(button)

        if str(button[0]) != '-1':
            devam = False
        elif str(update[0]) != '-1':
            x = position()[0]
            y = position()[1]

            sl(0.002)

            moveTo(update[0], update[1], duration=0)

            sl(0.002)
            leftClick()

            sl(0.002)

            moveTo(x, y, duration=0)
        

    moveTo(button[0], button[1], duration=0)
    sl(0.002)
    leftClick()
    sl(0.1)
    keyDown('alt')
    sl(0.001)
    keyDown('f4')
    sl(0.001)

    keyUp('alt')
    keyUp('f4')

except Exception as hata:
    op = open('hata.txt', 'w')
    op.write(str(hata))
    op.close()
    os.startfile('hata.txt')