import tkinter as tk
from tkinter import *
import webbrowser
from PIL import ImageTk, Image
import random

class Menu:
    def __init__(self, pagrindinis):
        self.pagrindinis = pagrindinis
        self.frame = tk.Frame(self.pagrindinis)
        self.img = ImageTk.PhotoImage(Image.open("logo.png"))
        #self.name = Label(pagrindinis, text="\u2660 get.ACE() \u2660", width=15, font=("Bahnschrift", 20))
        self.meniu_extra = Label(pagrindinis, text="Please choose an item of a menu:")
        self.start_game = Button(pagrindinis, text="\u2660 Start Game \u2660",command=self.start, width=30, font=("Bahnschrift", 13))
        self.taisykles = tk.Button(pagrindinis, text="\u2665 Rules Of The Game \u2665",command = self.taisykles, width=30, font=("Bahnschrift", 13))
        self.readme = Button(pagrindinis, text="\u2666 Open README Notes \u2666",command=self.readme, width=30, font=("Bahnschrift", 13))
        self.quit = Button(pagrindinis, text="\u2663 Quit Game \u2663", command=self.quit, width=30, font=("Bahnschrift", 13))
        self.label = Label(image=self.img)
        self.label.pack(side=TOP)
        #self.name.pack(side=TOP)
        self.meniu_extra.pack(side=TOP)
        self.start_game.pack(side=TOP)
        self.taisykles.pack(side=TOP)
        self.readme.pack(side=TOP)
        self.quit.pack(side=BOTTOM)
        self.frame.pack()

    def start(self):
        self.newWindow = tk.Toplevel(self.pagrindinis)
        self.app = Start(self.newWindow)
        self.newWindow.geometry("500x300")

    def taisykles(self):
        self.newWindow = tk.Toplevel(self.pagrindinis)
        self.app = Rules(self.newWindow)
        self.newWindow.geometry("500x300")

    def readme(self):
        webbrowser.open(url="https://github.com/GalijotasE/kortu_zaidimas/blob/master/README.md")
        pass

    def quit(self):
        self.quit = quit
        self.pagrindinis.destroy()

class Start:
    def __init__(self, pagrindinis):
        self.pagrindinis = pagrindinis
        self.frame = tk.Frame(self.pagrindinis)
        ipadding = {'ipadx': 10, 'ipady': 10}
        ivesti = Label(self.pagrindinis, text='Please Choose If A Card Is Lower, Same Or Higher',font=("Bahnschrift", 13))
        card = Label(self.pagrindinis, text= "korta bus cia", font=("Bahnschrift", 13))
        spejimas1 = Button(self.pagrindinis, text= "Lower",font=("Bahnschrift", 13))
        spejimas2 = Button(self.pagrindinis, text= "Same",font=("Bahnschrift", 13))
        spejimas3 = Button(self.pagrindinis, text= "Higher",font=("Bahnschrift", 13))
        ivesti.pack(**ipadding, fill=tk.X)
        card.pack(**ipadding, fill=tk.X)
        spejimas1.pack(**ipadding, expand=True, fill=tk.BOTH, side=tk.LEFT)
        spejimas2.pack(**ipadding, expand=True, fill=tk.BOTH, side=tk.LEFT)
        spejimas3.pack(**ipadding, expand=True, fill=tk.BOTH, side=tk.LEFT)
        self.frame.pack()
    
    def kortos(self):
        self.kortos_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.kortos_zenklai = ['♠', '♦', '♥', '♣']
        self.kortu_kalade = []
        for i in self.kortos_zenklai:
            for j in self.kortos_values:
                self.kortu_kalade.append(j + '' + i)
        return self.kortu_kalade

    def traukimas(self):
        random.shuffle(self.kortu_kalade)
        self.kortu_kalade = self.kortu_kalade.pop()
        return self.kortu_kalade

    def aukstesniu_vertes(self, korta):
        self.korta = str(korta)
        if self.korta[0] == "J":
            return 11
        elif self.korta[0] == "Q":
            return 12
        elif self.korta[0] == "K":
            return 13
        elif self.korta[0] == "A":
            return 14
        else:
            self.korta = int(korta[0:2])
            return self.korta

    def zaidimas(self):
        while True:
            kortu_kalade = self.kortos()
            teisingi_spejimai = 0
            self.korta = self.traukimas(kortu_kalade)
            self.taskai = self.aukstesniu_vertes(self.korta)
            if not kortu_kalade:
                ats = Label(self.pagrindinis, text= "congrats, you did pretty well!")
                ats.pack(side=BOTTOM)
                break
            sekanti_korta = self.traukimas(kortu_kalade)
            sekanti_taskai = self.aukstesniu_vertes(sekanti_korta)
            jusu_korta = Label(self.pagrindinis, text = self.korta)
            jusu_korta.pack(side=TOP)
            #if self.taskai < sekanti_taskai and spejimas3 *mygtuko paspaudimas*:
                #print("Correct!")
                #teisingi_spejimai += 1
                #korta = sekanti_korta
                #continue
        

class Rules:
    def __init__(self, pagrindinis):
        self.pagrindinis = pagrindinis
        self.frame = tk.Frame(self.pagrindinis)
        self.name = Label(pagrindinis, text="\u2660 get.ACE() \u2660", width=15, font=("Bahnschrift", 20))
        self.meniu_extra = Label(pagrindinis, text="Rules of the game:",font=("Bahnschrift", 14))
        self.meniu_extra1 = Label(pagrindinis, text="As soon as you start the game",font=("Bahnschrift", 11))
        self.meniu_extra2 = Label(pagrindinis, text="you will be given a choice - to pick",font=("Bahnschrift", 11))
        self.meniu_extra3 = Label(pagrindinis, text="if a card is lower, same or higher. ",font=("Bahnschrift", 11))
        self.meniu_extra4 = Label(pagrindinis, text="Your objective - To make a correct choice.",font=("Bahnschrift", 11))
        self.meniu_extra5 = Label(pagrindinis, text="Every correct answer will give you +1 point",font=("Bahnschrift", 11))
        self.meniu_extra6 = Label(pagrindinis, text="and incorrect will instantly restart the game.",font=("Bahnschrift", 11))
        self.meniu_extra7 = Label(pagrindinis, text="BEST OF LUCK!",font=("Bahnschrift", 11))
        self.quitButton = tk.Button(self.frame, text = 'Exit to menu', command = self.close_windows, width=30, font=("Bahnschrift", 13))
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


def pagrindinis_langas():
    langas = tk.Tk()
    app = Menu(langas)
    langas.geometry("500x300")
    langas.title("get.ACE() - card game v1.3")
    langas.mainloop()

if __name__ == '__main__':
    pagrindinis_langas()