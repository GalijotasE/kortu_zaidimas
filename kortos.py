import random
from tkinter import *
import tkinter as tk

class Zaidimas():
    def kortos():
        kortos_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        kortos_zenklai = ['♠', '♦', '♥', '♣']
        kortu_kalade = []
        for i in kortos_zenklai:
            for j in kortos_values:
                kortu_kalade.append(j + ' ' +  i)
        return kortu_kalade

    def traukimas(kortu_kalade):
        random.shuffle(kortu_kalade)
        kortu_kalade = kortu_kalade.pop()
        return kortu_kalade

    def aukstesniu_vertes(korta):
        korta = str(korta)
        if korta[0] == 'J':
            return 10
        elif korta[0] == 'Q':
            return 12
        elif korta[0] == 'K':
            return 13
        elif korta[0] == 'A':
            return 14
        else:
            korta = int(korta[0:2])
            return korta

    teisingi_spejimai = 0
    kortu_kalade = kortos()
    korta = traukimas(kortu_kalade)


    while True:
        taskai = aukstesniu_vertes(korta)
        if not kortu_kalade:
            print("Congrats! You have won with", teisingi_spejimai, "correct guesses!")
            break
        sekanti_korta = traukimas(kortu_kalade)
        sekanti_taskai = aukstesniu_vertes(sekanti_korta)
        print("\nYour card is: ", korta)
        spejimai = input('\nH - if higher, L - if lower, or S - if same:\t')
        spejimai = spejimai.lower()
        if spejimai not in ('h', 'l', 's'):
            break
        if taskai < sekanti_taskai and spejimai == 'h':
            print("Correct!")
            teisingi_spejimai += 1
            korta = sekanti_korta
            continue
        elif taskai > sekanti_taskai and spejimai == 'l':
            print("Correct!")
            teisingi_spejimai += 1
            korta = sekanti_korta
            continue
        elif taskai == sekanti_taskai and spejimai == 's':
            print("Correct!")
            teisingi_spejimai += 1
            korta = sekanti_korta
            continue
        else:
            print('You have lost! The new card was ', sekanti_korta)
            print('You had', teisingi_spejimai, 'correct guesses in a row!!!.')
            break