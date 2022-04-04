from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import *

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Směnárna"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.lbl = tk.Label(self, text="Směnárna")
        self.lbl.grid(row=0, column=0, padx=20)
        self.geometry("225x600")
        self.configure(bg='#FFFFFF')

       
        self.variable = tk.IntVar(self)
        self.radiobutton1 = Radiobutton(self, text="Nakoupit",variable=self.variable, value=1).grid(row=1, column=0)
        self.radiobutton2 = Radiobutton(self, text="Prodat", variable=self.variable, value=2).grid(row=2, column=0)
        self.variable.set(1)

        
        self.lbl2 = tk.Label(self, text="Nabídka měn")
        self.lbl2.grid(row=3, column=0)
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=4, column=0)
        self.listbox.bind("<ButtonRelease-1>", self.kliknuti)       
        f = open('listek.txt', 'r')
        slovnik = {}
        for line in f:
            self.listbox.insert(tk.END,line.split()[0])
            slovnik[line.split()[0]] = (line.split()[1:])

     
        self.lbl3 = tk.Label(self, text="Kurz")
        self.lbl3.grid(row=5, column=0)
        self.hodnota = tk.StringVar()
        self.cena = tk.IntVar()
        self.cenaLbl= tk.Label(self, textvariable=self.cena) 
        self.cenaLbl.grid(row=6, column=0)
        self.hodnotal= tk.Label(self, textvariable= self.hodnota) 
        self.hodnotal.grid(row=7, column=0)


        self.lbl2 = tk.Label(self, text="Počet:")
        self.lbl2.grid(row=8, column=0)
        self.mnozstvi = tk.Entry(self,)
        self.mnozstvi.grid(row=9, column=0)
        self.btn2 = tk.Button(self, text="Vypočítej", command=self.vypocet)
        self.btn2.grid(row=10, column=0)
        self.vysledek = tk.IntVar()
        self.vysledekl= tk.Label(self, textvariable= self.vysledek)
        self.vysledekl.grid(row=11, column=0)
        self.lbl4 = tk.Label(self)
        self.lbl4.grid(row=12, column=0)
        

        self.bind("<Escape>", self.quit)
        self.btn1 = tk.Button(self, text="Konec")
        self.btn1.grid(row=13, column=0)

    
    def vypocet(self,event=None):

        a = int(self.mnozstvi.get())
        b = int(self.cena.get())
        c = float(self.hodnota.get().replace(",","."))
        self.vysledekVar = float(a*c/b)
        self.vysledek.set(self.vysledekVar)

    def kliknuti(self, event):
        index = self.listbox.curselection()[0]
        f = open("listek.txt")
        self.lines = f.readlines()
        self.cenaVar = self.lines[index].split()[1]
        self.cena.set(self.cenaVar)
        if self.variable.get() == 1: 
            self.hodnotaVar = self.lines[index].split()[3] 
        else:
            self.hodnotaVar = self.lines[index].split()[2] 
        self.hodnota.set(self.hodnotaVar)

    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()
