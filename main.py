try:
    import tkinter as tk
    import queue as queue
except:
    import Tkinter as tk

import tkinter.ttk as ttk
import threading
from etl_podcast_downloader.downloader import Downloader

from PIL import Image, ImageTk
import time

def center(toplevel,desired_width=None,desired_height=None):
    toplevel.update_idletasks()
    w, h = toplevel.winfo_screenwidth() - 20, toplevel.winfo_screenheight() - 100
    if desired_width and desired_height:
        size = (desired_width,desired_height)
    else:
        size = tuple(int(Q) for Q in toplevel.geometry().split("+")[0].split("x"))
    toplevel.geometry("%dx%d+%d+%d" % (size + (w/2 - size[0]/2, h/2 - size[1]/2)))

class app(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        center(self,desired_width=300,desired_height=300)
        self.title('Eu Tava Lá - Downloader')

        index = 0

        img = tk.PhotoImage(file="eutavala_logo.png")
        self.header = tk.Label(image=img)
        self.header.pack()

        self.label1 = tk.Label(text="Selecione o podcast")
        self.label1.pack()

        self.cb = ttk.Combobox(self, width = 20)
        self.cb['values'] = ("Eu Tava Lá - Podcast", "")
        self.cb.current(0)
        self.cb.pack()

        self.label2 = tk.Label(text="Clique no botão abaixo para")
        self.label2.pack()

        self.label3 = tk.Label(text="baixar os últimos 10 episódios")
        self.label3.pack()


        self.button = tk.Button(self,
                                         text="Começar",
                                         font=("Calibri",15,"bold"),
                                         bg = ("Blue"),
                                         fg = ("white"),
                                         command=self.run_func)
        self.button.pack()

        self.label4 = tk.Label()
        self.label4.pack()

        self.label5 = tk.Label()
        self.label5.pack()

        self.label6 = tk.Label()


        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress.pack()
        self.label6.pack()

        self.label7 = tk.Label()
        self.label7.pack()

    def read_bytes(self):
        self.progress['maximum'] = 100

        for i in range (101):
            time.sleep(0.05)
            self.progress['value'] = i
            self.progress.update()
        self.progress['value'] = 0



    def run_func(self):
        threading.Thread(target=self.clickButton).start()

    def clickButton(self):
        if self.cb.current() == 0:
            self.label5.config(text='Inicializando...', font='Times', fg='green')
            self.read_bytes()
            self.label5.config(text='Seu download começou', font='Times', fg='green')
            self.label6.config(text='Baixando...', font='Times', fg='blue')
            Downloader().baixaEp()
            self.label6.config(text='Download finalizado, aproveite!', font='Times', fg='red')
            self.label5.config(text='Feito por: Guilherme Lithg', font='Times', fg='blue')



        else:
            self.label5.config(text='Podcast inválido', font='Times', fg='red')



app_start = app()
app_start.mainloop()
