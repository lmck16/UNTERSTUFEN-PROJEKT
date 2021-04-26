from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')

# X start = True, O = False
clicked = True
count = 0

#DisableButton                 # if someone win. Disable all the buttons.
def disable_all_buttons():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    b10.config(state=DISABLED)
    b11.config(state=DISABLED)
    b12.config(state=DISABLED)
    b13.config(state=DISABLED)
    b14.config(state=DISABLED)
    b15.config(state=DISABLED)
    b16.config(state=DISABLED)
    b17.config(state=DISABLED)
    b18.config(state=DISABLED)
    b19.config(state=DISABLED)
    b20.config(state=DISABLED)
    b21.config(state=DISABLED)
    b22.config(state=DISABLED)
    b23.config(state=DISABLED)
    b24.config(state=DISABLED)
    b25.config(state=DISABLED)
    b26.config(state=DISABLED)
    b27.config(state=DISABLED)
    b28.config(state=DISABLED)
    b29.config(state=DISABLED)
    b30.config(state=DISABLED)
    b31.config(state=DISABLED)
    b32.config(state=DISABLED)
    b33.config(state=DISABLED)
    b34.config(state=DISABLED)
    b35.config(state=DISABLED)
    b36.config(state=DISABLED)

#CheckWon
def checkifwon():
    global winner
    winner = False                            # Set Winner = False. If Winner. will be change to True

    #Check for X's Win
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X" and b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b1.config(bg="green")                 # Set Color to green
        b2.config(bg="green")
        b3.config(bg="green")
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True                         # Set winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()                 # Call this function
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X" and b10["text"] == "X" and b11["text"] == "X" and b12["text"] == "X":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        b10.config(bg="green")
        b11.config(bg="green")
        b12.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b13["text"] == "X" and b14["text"] == "X" and b15["text"] == "X" and b16["text"] == "X" and b17["text"] == "X" and b18["text"] == "X":
        b13.config(bg="green")
        b14.config(bg="green")
        b15.config(bg="green")
        b16.config(bg="green")
        b17.config(bg="green")
        b18.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b19["text"] == "X" and b20["text"] == "X" and b21["text"] == "X" and b22["text"] == "X" and b23["text"] == "X" and b24["text"] == "X":
        b19.config(bg="green")
        b20.config(bg="green")
        b21.config(bg="green")
        b22.config(bg="green")
        b23.config(bg="green")
        b24.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b25["text"] == "X" and b26["text"] == "X" and b27["text"] == "X" and b28["text"] == "X" and b29["text"] == "X" and b30["text"] == "X":
        b25.config(bg="green")
        b26.config(bg="green")
        b27.config(bg="green")
        b28.config(bg="green")
        b29.config(bg="green")
        b30.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b31["text"] == "X" and b32["text"] == "X" and b33["text"] == "X" and b34["text"] == "X" and b35["text"] == "X" and b36["text"] == "X":
        b31.config(bg="green")
        b32.config(bg="green")
        b33.config(bg="green")
        b34.config(bg="green")
        b35.config(bg="green")
        b36.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b1["text"] == "X" and b7["text"] == "X" and b13["text"] == "X" and b19["text"] == "X" and b25["text"] == "X" and b31["text"] == "X":
        b1.config(bg="green")
        b7.config(bg="green")
        b13.config(bg="green")
        b19.config(bg="green")
        b25.config(bg="green")
        b31.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b2["text"] == "X" and b8["text"] == "X" and b14["text"] == "X" and b20["text"] == "X" and b26["text"] == "X" and b32["text"] == "X":
        b2.config(bg="green")
        b8.config(bg="green")
        b14.config(bg="green")
        b20.config(bg="green")
        b26.config(bg="green")
        b32.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b3["text"] == "X" and b9["text"] == "X" and b15["text"] == "X" and b21["text"] == "X" and b27["text"] == "X" and b33["text"] == "X":
        b3.config(bg="green")
        b9.config(bg="green")
        b15.config(bg="green")
        b21.config(bg="green")
        b27.config(bg="green")
        b33.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b4["text"] == "X" and b10["text"] == "X" and b16["text"] == "X" and b22["text"] == "X" and b28["text"] == "X" and b34["text"] == "X":
        b4.config(bg="green")
        b10.config(bg="green")
        b16.config(bg="green")
        b22.config(bg="green")
        b28.config(bg="green")
        b34.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b5["text"] == "X" and b11["text"] == "X" and b17["text"] == "X" and b23["text"] == "X" and b29["text"] == "X" and b35["text"] == "X":
        b5.config(bg="green")
        b11.config(bg="green")
        b17.config(bg="green")
        b23.config(bg="green")
        b29.config(bg="green")
        b35.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b6["text"] == "X" and b12["text"] == "X" and b18["text"] == "X" and b24["text"] == "X" and b30["text"] == "X" and b36["text"] == "X":
        b6.config(bg="green")
        b12.config(bg="green")
        b18.config(bg="green")
        b24.config(bg="green")
        b30.config(bg="green")
        b36.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b1["text"] == "X" and b8["text"] == "X" and b15["text"] == "X" and b22["text"] == "X" and b29["text"] == "X" and b36["text"] == "X":
        b1.config(bg="green")
        b8.config(bg="green")
        b15.config(bg="green")
        b22.config(bg="green")
        b29.config(bg="green")
        b36.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()
    elif b6["text"] == "X" and b11["text"] == "X" and b16["text"] == "X" and b21["text"] == "X" and b26["text"] == "X" and b31["text"] == "X":
        b6.config(bg="green")
        b11.config(bg="green")
        b16.config(bg="green")
        b21.config(bg="green")
        b26.config(bg="green")
        b31.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n X Win!!")
        disable_all_buttons()

        #Check for O's Win
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O" and b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O" and b10["text"] == "O" and b11["text"] == "O" and b12["text"] == "O":
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        b10.config(bg="green")
        b11.config(bg="green")
        b12.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b13["text"] == "O" and b14["text"] == "O" and b15["text"] == "O" and b16["text"] == "O" and b17["text"] == "O" and b18["text"] == "O":
        b13.config(bg="green")
        b14.config(bg="green")
        b15.config(bg="green")
        b16.config(bg="green")
        b17.config(bg="green")
        b18.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b19["text"] == "O" and b20["text"] == "O" and b21["text"] == "O" and b22["text"] == "O" and b23["text"] == "O" and b24["text"] == "O":
        b19.config(bg="green")
        b20.config(bg="green")
        b21.config(bg="green")
        b22.config(bg="green")
        b23.config(bg="green")
        b24.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b25["text"] == "O" and b26["text"] == "O" and b27["text"] == "O" and b28["text"] == "O" and b29["text"] == "O" and b30["text"] == "O":
        b25.config(bg="green")
        b26.config(bg="green")
        b27.config(bg="green")
        b28.config(bg="green")
        b29.config(bg="green")
        b30.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b31["text"] == "O" and b32["text"] == "O" and b33["text"] == "O" and b34["text"] == "O" and b35["text"] == "O" and b36["text"] == "O":
        b31.config(bg="green")
        b32.config(bg="green")
        b33.config(bg="green")
        b34.config(bg="green")
        b35.config(bg="green")
        b36.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b1["text"] == "O" and b7["text"] == "O" and b13["text"] == "O" and b19["text"] == "O" and b25["text"] == "O" and b31["text"] == "O":
        b1.config(bg="green")
        b7.config(bg="green")
        b13.config(bg="green")
        b19.config(bg="green")
        b25.config(bg="green")
        b31.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b2["text"] == "O" and b8["text"] == "O" and b14["text"] == "O" and b20["text"] == "O" and b26["text"] == "O" and b32["text"] == "O":
        b2.config(bg="green")
        b8.config(bg="green")
        b14.config(bg="green")
        b20.config(bg="green")
        b26.config(bg="green")
        b32.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b3["text"] == "O" and b9["text"] == "O" and b15["text"] == "O" and b21["text"] == "O" and b27["text"] == "O" and b33["text"] == "O":
        b3.config(bg="green")
        b9.config(bg="green")
        b15.config(bg="green")
        b21.config(bg="green")
        b27.config(bg="green")
        b33.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b4["text"] == "O" and b10["text"] == "O" and b16["text"] == "O" and b22["text"] == "O" and b28["text"] == "O" and b34["text"] == "O":
        b4.config(bg="green")
        b10.config(bg="green")
        b16.config(bg="green")
        b22.config(bg="green")
        b28.config(bg="green")
        b34.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b5["text"] == "O" and b11["text"] == "O" and b17["text"] == "O" and b23["text"] == "O" and b29["text"] == "O" and b35["text"] == "O":
        b5.config(bg="green")
        b11.config(bg="green")
        b17.config(bg="green")
        b23.config(bg="green")
        b29.config(bg="green")
        b35.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b6["text"] == "O" and b12["text"] == "O" and b18["text"] == "O" and b24["text"] == "O" and b30["text"] == "O" and b36["text"] == "O":
        b6.config(bg="green")
        b12.config(bg="green")
        b18.config(bg="green")
        b24.config(bg="green")
        b30.config(bg="green")
        b36.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b1["text"] == "O" and b8["text"] == "O" and b15["text"] == "O" and b22["text"] == "O" and b29["text"] == "O" and b36["text"] == "O":
        b1.config(bg="green")
        b8.config(bg="green")
        b15.config(bg="green")
        b22.config(bg="green")
        b29.config(bg="green")
        b36.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()
    elif b6["text"] == "O" and b11["text"] == "O" and b16["text"] == "O" and b21["text"] == "O" and b26["text"] == "O" and b31["text"] == "O":
        b6.config(bg="green")
        b11.config(bg="green")
        b16.config(bg="green")
        b21.config(bg="green")
        b26.config(bg="green")
        b31.config(bg="green")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "Congratulations \n O Win!!")
        disable_all_buttons()

    #Check if Tie
    if count == 36 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie! \n No one Wins!.")
        disable_all_buttons()


#Buttin click funtion
def b_click(b):
    global clicked, count

    if b["text"] == " " and clicked == True:  # If Button is nothing and someone click
        b["text"] = "X"                       # Write X
        clicked = False                       # Set clicked = False, Means O turn
        count += 1                            # Track how many moves, if 36 moves = Game Over.
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:                                     # Button has already been selected
       messagebox.showerror("Tic Tac Toe", "That box has already been selected!!\n Please Pick Another Box.")

# Build Button and Reset the game
def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, b32, b33, b34, b35, b36
    global clicked, count
    clicked = True
    count = 0

    #Buttons
    b1 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b1))
    b2 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b2))
    b3 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b3))
    b4 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b4))
    b5 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b5))
    b6 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b6))

    b7 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b7))
    b8 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b8))
    b9 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b9))
    b10 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b10))
    b11 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b11))
    b12 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b12))

    b13 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b13))
    b14 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b14))
    b15 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b15))
    b16 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b16))
    b17 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b17))
    b18 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b18))

    b19 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b19))
    b20 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b20))
    b21 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b21))
    b22 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b22))
    b23 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b23))
    b24 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b24))

    b25 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b25))
    b26 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b26))
    b27 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b27))
    b28 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b28))
    b29 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b29))
    b30 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b30))

    b31 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b31))
    b32 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b32))
    b33 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b33))
    b34 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b34))
    b35 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b35))
    b36 = Button(root, text=" ",font=("Helvetica", 10), height=3, width=6, bg="SystemButtonFace",command=lambda: b_click(b36))

    #Grid Button to the screen
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=0, column=3)
    b5.grid(row=0, column=4)
    b6.grid(row=0, column=5)

    b7.grid(row=1, column=0)
    b8.grid(row=1, column=1)
    b9.grid(row=1, column=2)
    b10.grid(row=1, column=3)
    b11.grid(row=1, column=4)
    b12.grid(row=1, column=5)

    b13.grid(row=2, column=0)
    b14.grid(row=2, column=1)
    b15.grid(row=2, column=2)
    b16.grid(row=2, column=3)
    b17.grid(row=2, column=4)
    b18.grid(row=2, column=5)

    b19.grid(row=3, column=0)
    b20.grid(row=3, column=1)
    b21.grid(row=3, column=2)
    b22.grid(row=3, column=3)
    b23.grid(row=3, column=4)
    b24.grid(row=3, column=5)

    b25.grid(row=4, column=0)
    b26.grid(row=4, column=1)
    b27.grid(row=4, column=2)
    b28.grid(row=4, column=3)
    b29.grid(row=4, column=4)
    b30.grid(row=4, column=5)

    b31.grid(row=5, column=0)
    b32.grid(row=5, column=1)
    b33.grid(row=5, column=2)
    b34.grid(row=5, column=3)
    b35.grid(row=5, column=4)
    b36.grid(row=5, column=5)

# Create menue
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command =reset)

reset()

root.mainloop()





