import tkinter as tk
from tkinter import *
import PIL.Image
import PIL.ImageTk


class RulesLayout():

    def __init__(self, game):
        root = Toplevel()

        root.resizable(False,False)
        root.title("SPIELREGELN - {}".format(game))

        if game == "Bauernschach":
            im = PIL.Image.open("resources/bauernschach.png")
        elif game == "Tic Tac Toe":
            im = PIL.Image.open("resources/ttt.png")
        else:
            im = PIL.Image.open("resources/dame.png")


        photo = PIL.ImageTk.PhotoImage(im)

        label = Label(root, image=photo)
        label.image = photo
        label.pack()
