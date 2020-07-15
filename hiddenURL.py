#!/usr/bin/python3
# Created by @OP
import os
import time
import pyshorteners
from time import sleep


def Main():
    print("\033[91mDeveloper assume no liability and are not responsible for any misuse or damage caused by this program")
    print("\033[96m-------------------------------------------")
 
    print("   Hide custom URL for social engineering   ")
    print("--------------------------------------------")
    print("\n[*1]  Google")
    print("[*2]  Youtube")
    print("[*3]  Spotify")
    print("[*4]  Instagram")
    print("[*5]  Facebook")
    print("[*6]  Personalized")
    print("\n[*10]  Exit")
    Chose()


def Chose():
    select= int(input("\nSelect your desired option:"))
    if select == 1:
        CallGoogle()
    elif select == 2:
        CallYoutube()
    elif select == 3:
        CallInstagram()
    elif select == 4:
        CallFacebook()
    elif select == 5:
        CallPersonalized()
    elif select == 10:
        os.system('clear')
        print("Thank you for using tool...")
        sleep(1)
        os.system('clear')
        exit()
    else:
        os.system('cls')
        print("Not an valid option")
        sleep(1)
        os.system('cls')
        Main()


def CallGoogle():
    os.system('clear')
    print("You have selected Google.")
    originalLink = str(input("\nOriginal URL you want to redirect to : "))

    print("\nInput any interesting text to append  ")
    midText = str(input("\nCenter text: "))
    os.system('clear')
    shortener = pyshorteners.Shortener()
    endLink = shortener.tinyurl.short(originalLink)
    # print(EndLink)
    # Removing protocol (https)
    withoutHttp = endLink[7:]
    print(f"\033[95m\nYour generated link is: https://www.google.com-{midText}@{withoutHttp}")
    anotherLink()


def CallYoutube():
        os.system('clear')
        print("You have selected Youtube.")
        originalLink = str(input("\nOriginal URL you want to redirect to : "))

        print("\nInput any interesting text to append  ")
        midText = str(input("\nCenter text: "))
        os.system('clear')
        shortener = pyshorteners.Shortener()
        endLink = shortener.tinyurl.short(originalLink)
        # print(EndLink)
        # Removing protocol (https)
        withoutHttp = endLink[7:]
        print(f"\033[95m\nYour generated link is: https://www.youtube.com-{midText}@{withoutHttp}")
        anotherLink()



def CallInstagram():
        os.system('clear')
        print("You have selected Instagram.")
        originalLink = str(input("\nOriginal URL you want to redirect to : "))

        print("\nInput any interesting text to append  ")
        midText = str(input("\nCenter text: "))
        os.system('clear')
        shortener = pyshorteners.Shortener()
        endLink = shortener.tinyurl.short(originalLink)
        # print(EndLink)
        # Removing protocol (https)
        withoutHttp = endLink[7:]
        print(f"\033[95m\nYour generated link is: https://www.youtube.com-{midText}@{withoutHttp}")
        anotherLink()



def CallFacebook():
    os.system('clear')
    print("You have selected Facebook.")
    originalLink = str(input("\nOriginal URL you want to redirect to : "))

    print("\nInput any interesting text to append  ")
    midText = str(input("\nCenter text: "))
    os.system('clear')
    shortener = pyshorteners.Shortener()
    endLink = shortener.tinyurl.short(originalLink)
    # print(EndLink)
    # Removing protocol (https)
    withoutHttp = endLink[7:]
    print(f"\033[95m\nYour generated link is: https://www.youtube.com-{midText}@{withoutHttp}")
    anotherLink()



def CallPersonalized():
    os.system('clear')
    print("You have selected Personalized.")
    Domain = str(input("Input any other domain you wish to customize:"))
    originalLink = str(input("\nOriginal URL: "))

    print("\nInput something that: new-post-in-new-york-times-this-is-a-perez-mascato-i-love")
    midLink = str(input("\nCenter text: "))

    Shortener = pyshorteners.Shortener()
    endLink = Shortener.tinyurl.short(originalLink)
    withoutHttp = endLink[7:]
    os.system('clear')
    print(f"\033[95m\nYour link is: https://www.{Domain}-{midLink}@{withoutHttp}")
    anotherLink()

def anotherLink():
    print("\033[95m\nDo you want to create another link?")
    print("Yes [*1] \nNo  [*2]")
    select=int(input("\nSelect a option: "))
    if select == 1:
        os.system('clear')
        Main()
    else:
        os.system('clear')
        exit()

Main()
