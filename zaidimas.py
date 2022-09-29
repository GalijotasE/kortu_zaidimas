### kortu zaidimas
# 52 kortos, 1,2,3,4,5,6,7,8,9,10,J,Q,K,A su skirtingais zenklais
# zaidimo meniu - zaidimo pavadinimas, pradeti zaidima, taisykles.
# verciamos 2 kortos, 1 dealerio, kita zaidejo. kas turi didesne- laimi.

### daugiau arba maziau kortu zaidimas

#importai:
from random import shuffle
import random
from tkinter import *

langas = Tk()
langas.title("Kortu zaidimas v1.00") # pridedame lango pavadinima.
langas.geometry("500x500")
#meniu funkcija:
zaidimo_pav = Label(langas, text="Kortu Zaidimas", width=15, font=("Bahnschrift", 20))
meniu_pav = Label(langas, text="Prasome pasirinkti veiksma:", font="Bahnschrift", )
start_button = Button(langas, text="Start Game", width=30, font=("Bahnschrift", 13))
taisykles_button = Button(langas, text="Rules Of The Game", width=30, font=("Bahnschrift", 13))
readme_button = Button(langas, text="Open README Notes", width=30, font=("Bahnschrift", 13))
iseiti_button = Button(langas, text="Quit Game", width=30, font=("Bahnschrift", 13))

#pack'inam meniu:
zaidimo_pav.pack(side=TOP)
meniu_pav.pack(side=TOP)
start_button.pack(side=TOP)
taisykles_button.pack(side=TOP)
readme_button.pack(side=TOP)
iseiti_button.pack(side=BOTTOM)


#langas.iconphoto("img")


langas.mainloop() # paleidziame tKinterio programa.

#print("card game V1.00")
#meniu
#print("Menu")
#print("1.Start Game") 
#print("2.Game Rules")
#print("3.Quit")
#veiksmas = int(input("Please choose an action: "))

#if veiksmas == 1:
    #cards = []
    #for symbols in ["\u2660", "\u2663", "\u2665", "\u2666"]:
        #for value in [*range(2,10), "J", "Q", "K", "A"]:
            #cards.append(f"{value} {symbols}")
            #shuffle(cards)
    #print("Cards have been shuffled.")

#elif veiksmas == 2:
    #print("Rules Of this card game..")
#elif veiksmas == 3:
    #print("Thank you for playing")
