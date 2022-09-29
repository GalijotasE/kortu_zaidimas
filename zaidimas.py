import tkinter as tk
from tkinter import *
from random import shuffle

class Menu:
    def __init__(self, pagrindinis):
        self.pagrindinis = pagrindinis
        self.frame = tk.Frame(self.pagrindinis)
        self.name = Label(pagrindinis, text="\u2660 get.ACE() \u2660", width=15, font=("Bahnschrift", 20))
        self.meniu_extra = Label(pagrindinis, text="Please choose an item of a menu:")
        self.start_game = Button(pagrindinis, text="\u2660 Start Game \u2660",command=self.start, width=30, font=("Bahnschrift", 13))
        self.taisykles = tk.Button(pagrindinis, text="\u2665 Rules Of The Game \u2665",command = self.taisykles, width=30, font=("Bahnschrift", 13))
        self.readme = Button(pagrindinis, text="\u2666 Open README Notes \u2666",command=self.readme, width=30, font=("Bahnschrift", 13))
        self.quit = Button(pagrindinis, text="\u2663 Quit Game \u2663", command=self.quit, width=30, font=("Bahnschrift", 13))
        self.name.pack(side=TOP)
        self.meniu_extra.pack(side=TOP)
        self.start_game.pack(side=TOP)
        self.taisykles.pack(side=TOP)
        self.readme.pack(side=TOP)
        self.quit.pack(side=BOTTOM)
        self.frame.pack()

    def start(self):
        self.newWindow = tk.Toplevel(self.pagrindinis)
        self.app = Start(self.newWindow)

    def taisykles(self):
        self.newWindow = tk.Toplevel(self.pagrindinis)
        self.app = Rules(self.newWindow)

    def readme(self):
        self.newWindow = tk.Toplevel(self.pagrindinis)
        self.app = Readme(self.newWindow)

    def quit(self):
        self.quit = quit
        self.pagrindinis.destroy()

class Start:
    def __init__(self, pagrindinis):
        self.pagrindinis = pagrindinis
        self.frame = tk.Frame(self.pagrindinis)
        self.name = Label(pagrindinis, text="\u2660 get.ACE() \u2660", width=15, font=("Bahnschrift", 20))
        self.name.pack(side=TOP)
        self.frame.pack()

class Rules:
    def __init__(self, pagrindinis):
        self.pagrindinis = pagrindinis
        self.frame = tk.Frame(self.pagrindinis)
        self.name = Label(pagrindinis, text="\u2660 get.ACE() \u2660", width=15, font=("Bahnschrift", 20))
        self.meniu_extra = Label(pagrindinis, text="Rules of the game:",font=("Bahnschrift", 14))
        self.meniu_extra1 = Label(pagrindinis, text="As soon as you start the game",font=("Bahnschrift", 11))
        self.meniu_extra2 = Label(pagrindinis, text="you will be given a choice",font=("Bahnschrift", 11))
        self.meniu_extra3 = Label(pagrindinis, text="to pick a random number between 1-52",font=("Bahnschrift", 11))
        self.meniu_extra4 = Label(pagrindinis, text="all of these numbers contain a random card.",font=("Bahnschrift", 11))
        self.meniu_extra5 = Label(pagrindinis, text="Your objective - To randomly select a card",font=("Bahnschrift", 11))
        self.meniu_extra6 = Label(pagrindinis, text="that is higher than your AI opponent's",font=("Bahnschrift", 11))
        self.meniu_extra7 = Label(pagrindinis, text="BEST OF LUCK!",font=("Bahnschrift", 11))
        self.quitButton = tk.Button(self.frame, text = 'Quit Rules', command = self.close_windows, width=30, font=("Bahnschrift", 13))
        self.name.pack(side=TOP)
        self.meniu_extra.pack(side=TOP)
        self.meniu_extra1.pack(side=TOP)
        self.meniu_extra2.pack(side=TOP)
        self.meniu_extra3.pack(side=TOP)
        self.meniu_extra4.pack(side=TOP)
        self.meniu_extra5.pack(side=TOP)
        self.meniu_extra6.pack(side=TOP)
        self.meniu_extra7.pack(side=TOP)
        self.quitButton.pack()
        self.frame.pack()

    def close_windows(self):
        self.pagrindinis.destroy()

class Readme():
    def __init__(self, pagrindinis):
        self.pagrindinis = pagrindinis


def pagrindinis_langas():
    langas = tk.Tk()
    app = Menu(langas)
    langas.geometry("500x300")
    langas.title("get.ACE() - card game v1.2")
    langas.mainloop()

if __name__ == '__main__':
    pagrindinis_langas()