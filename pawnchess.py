import tkinter as tkin
from PIL import ImageTk, Image
import random

root = tkin.Tk()
root.title('Bauernschach')
root.geometry('1300x1000')

header = tkin.Label(root, text='PawnChess')
header.config(font=('courier', 20))
header.grid(column=0, row=0)

def roundLabel():
    global moveNo

    roundText = tkin.Label(root, text='MOVE')
    roundNo = tkin.Label(root, text=moveNo)
    roundText.grid(column=0, row=9, sticky='w')
    roundNo.grid(column=0, row=9)

def playerLabel(playerGo):
    pass

def labelTop():
    topLabels = ['A', 'B', 'C', 'D', 'E', 'F']
    count = 1
    for letter in topLabels:
        letter = tkin.Label(root, text=letter)
        letter.grid(column=count, row=0, sticky='S')
        count += 1

def labelSide():
    sideLabel = []
    sideLabel += range(6,0,-1)
    count = 1
    for num in sideLabel:
        num = tkin.Label(root, text=num)
        num.grid(column=0, row=count, sticky='E')
        count += 1

def padding():
    lLabel = tkin.Label(root)
    lLabel.grid(column=0, ipadx=50)

def makeBoardCanvases():
    global blackSquares
    global whiteSquares

    blackSquares = []
    blackSquares += range(0,18)
    
    whiteSquares = []
    whiteSquares += range(0,18)
    
    for variable in blackSquares:
        ind = blackSquares.index(variable)
        blackSquares[ind] = tkin.Canvas(root, width=110, height=110, border=0, bg="brown", cursor="hand2")
    
    for variable in whiteSquares:
        ind = whiteSquares.index(variable)
        whiteSquares[ind] = tkin.Canvas(root, width=110, height=110, border=0, bg="white", cursor="hand2")

    return blackSquares, whiteSquares

def positionBoardCanvases(blackSquares, whiteSquares):
    bCol = 0
    wCol = -1
    for num in range(0,3):
        bCol+=2
        wCol+=2
        blackSquares[num].grid(column=bCol,row=1)
        whiteSquares[num].grid(column=wCol,row=1)

    bCol = -1
    wCol = 0
    for num in range(3,6):
        bCol+=2
        wCol+=2
        blackSquares[num].grid(column=bCol,row=2)
        whiteSquares[num].grid(column=wCol,row=2)

    bCol = 0
    wCol = -1
    for num in range(6,9):
        bCol+=2
        wCol+=2
        blackSquares[num].grid(column=bCol,row=3)
        whiteSquares[num].grid(column=wCol,row=3)

    bCol = -1
    wCol = 0
    for num in range(9,12):
        bCol+=2
        wCol+=2
        blackSquares[num].grid(column=bCol,row=4)
        whiteSquares[num].grid(column=wCol,row=4)

    bCol = 0
    wCol = -1
    for num in range(12,15):
        bCol+=2
        wCol+=2
        blackSquares[num].grid(column=bCol,row=5)
        whiteSquares[num].grid(column=wCol,row=5)

    bCol = -1
    wCol = 0
    for num in range(15,18):
        bCol+=2
        wCol+=2
        blackSquares[num].grid(column=bCol,row=6)
        whiteSquares[num].grid(column=wCol,row=6)

    return blackSquares, whiteSquares

def boardSpaces(blackSquares, whiteSquares):
    board = []
    for num in range(0,3):
        board.append(whiteSquares[num])
        board.append(blackSquares[num])
    for num in range(3,6):
        board.append(whiteSquares[num])
        board.append(blackSquares[num])    
    for num in range(6,9):
        board.append(whiteSquares[num])
        board.append(blackSquares[num])  
    for num in range(9,12):
        board.append(whiteSquares[num])
        board.append(blackSquares[num])
    for num in range(12, 15):
        board.append(whiteSquares[num])
        board.append(blackSquares[num])    
    for num in range(15, 18):
        board.append(whiteSquares[num])
        board.append(blackSquares[num]) 
    return board

boardObjectSpaces = []
for num in range(0,36):
    boardObjectSpaces.append("")

wSet = []
bSet = []

class Piece(object):
    def __init__(self, color, mySet):
        self.color = color
        self.mySet = mySet.append(self)
    
    alive = True
    sqaureIndex = 0

    global row1
    global row2
    global row3
    global row4
    global row5
    global row6

    global col1
    global col2
    global col3
    global col4
    global col5
    global col6

    row1 = range(0, 6)
    row2 = range(6, 12)
    row3 = range(12, 18)
    row4 = range(18, 24)
    row5 = range(24, 30)
    row6 = range(30, 36)

    col1 = range(0, 31, +6)
    col2 = range(1, 32, +6)
    col3 = range(2, 33, +6)
    col4 = range(3, 34, +6)
    col5 = range(4, 35, +6)
    col6 = range(5, 36, +6) 

    def unbindAll(self):
        pass

class Pawn(Piece):
    bOpen = Image.open("mats/blackp.png")
    bImage = ImageTk.PhotoImage(bOpen)
    wOpen = Image.open("mats/whitep.png")
    wImage = ImageTk.PhotoImage(wOpen)
    kind = "pawn"

    def moves(self, squareIndex):
        print("PAWN MOVE")
        print(squareIndex, "\n")

        piece = boardObjectSpaces[squareIndex]

        up = squareIndex - 6
        up2 = up - 6
        nw = squareIndex - 7
        ne = squareIndex - 5

        if self.color == "w":
            up = squareIndex - 6
            nw = squareIndex - 4
            ne = squareIndex - 5
            up2 = up - 6
        
        if self.color == "b":
            up = squareIndex + 6
            nw = squareIndex + 5
            ne = squareIndex + 7
            up2 = up + 6
        
        possibleSpaces = [up, nw, ne]

        if self.color == "w":
            for space in row6:
                print(space)
                if boardObjectSpaces.index(self) == space:
                    possibleSpaces.append(up2)

        if self.color == "b":
            for space in row1:
                print(space)
                if boardObjectSpaces.index(self) == space:
                    possibleSpaces.append(up2)
        
        origSquare = board[squareIndex]

        copyPossibleSpaces = possibleSpaces

        print(copyPossibleSpaces)

        playColor = boardObjectSpaces[squareIndex].color
        deleteSpaces = []

        for var in copyPossibleSpaces:
            if var == up:
                if boardObjectSpaces[var] != "":
                    deleteSpaces.append(up)
                    deleteSpaces.append(up2)
                else:
                    pass
            if var == up2:
                if boardObjectSpaces[var] != "":
                    deleteSpaces.append(up2)
                else:
                    pass
            if var == nw:
                if squareIndex in col1:
                    deleteSpaces.append(nw)
                else:
                    if boardObjectSpaces[var] != "":
                            if boardObjectSpaces[var].color == playColor:
                                    deleteSpaces.append(nw)
                            if boardObjectSpaces[var].color != playColor:
                                    pass
                    else:
                            deleteSpaces.append(nw)
            if var == ne:
                if squareIndex in col6:
                        deleteSpaces.append(ne)
                else:
                    if boardObjectSpaces[var] != "":
                            if boardObjectSpaces[var].color == playColor:
                                    deleteSpaces.append(ne)
                            if boardObjectSpaces[var].color != playColor:
                                    pass
                    else:
                            deleteSpaces.append(ne)
        
        for var in copyPossibleSpaces:
            posSpace = board[var]
            posSpace.config(bg="mediumpurple4")
            posSpace.bind("<Button-1>", lambda event: doMove(event, origSquare = origSquare, possibleMoves = copyPossibleSpaces))
        origSquare.bind("<Button-3>", lambda event: deSelect(event, possibleSpaces = possibleSpaces))

def doMove(event, origSquare, possibleMoves):
    print("DOMOVE")

    newSquare = event.widget
    origSquare = origSquare

    print(origSquare)
    print(newSquare)

    oldIndex = board.index(origSquare)
    newIndex = board.index(newSquare)

    piece = boardObjectSpaces[oldIndex]
    otherPiece = boardObjectSpaces[newIndex]

    print(piece)
    print(otherPiece)

    if piece.color == "w":
        ourSetPiece = wPlaces[oldIndex]
        ourColor = "w"
        turn = "b"
        img = boardObjectSpaces[oldIndex].wImage
    elif piece.color == "b":
        ourSetPiece = bPlaces[oldIndex]
        ourColor = "b"
        turn = "w"
        img = boardObjectSpaces[oldIndex].bImage
    if otherPiece == "":
        pass
    elif otherPiece.color == "w":
        otherSetPiece = wPlaces[newIndex]
        otherColor = "w"
        otherImg = boardObjectSpaces[newIndex].wImage
    elif otherPiece.color == "b":
        otherSetPiece = bPlaces[oldIndex]
        otherColor = "b"
        otherImg = boardObjectSpaces[newIndex].bImage
    
    print("HIGHLIGHT REMOVAL")

    if origSquare in whiteSquares:
        bgcol = "white"
    elif origSquare in blackSquares:
        bgcol = "brown"
    origSquare.config(bg=bgcol)

    selfCanvases = []

    for index in possibleMoves:
        if index >= 0 and index <= 35:
            selfCanvases.append(board[index])
    
    for canvas in selfCanvases:
        if canvas in whiteSquares:
            canvas.config(bg="white")
        elif canvas in blackSquares:
            canvas.config(bg="brown")
    
    setMove = turn

    if otherPiece == "":

        board[oldIndex].delete("all")
        board[newIndex].create_image(50, 50, image=img)
        boardObjectSpaces[newIndex] = boardObjectSpaces[oldIndex]
        boardObjectSpaces[oldIndex] = ""
        if ourColor == "w":
            wPlaces[newIndex] = wPlaces[oldIndex]
            wPlaces[oldIndex] = ""
        elif ourColor == "b":
            bPlaces[newIndex] = bPlaces[oldIndex]
            bPlaces[oldIndex] = ""
    else:
        if otherPiece.color == turn:
            board[newIndex].delete("all")
            board[newIndex].create_image(50, 50, image=img)
            board[oldIndex].delete("all")

            boardObjectSpaces[newIndex] = piece
            boardObjectSpaces[oldIndex] = ""

            if turn == "w":
                wPlaces[newIndex] = ""
                bPlaces[newIndex] = piece
                bPlaces[oldIndex] = ""
            elif turn == "b":
                bPlaces[newIndex] = ""
                wPlaces[newIndex] = piece
                wPlaces[oldIndex] = ""
        elif otherPiece.color == ourColor:
            board[oldIndex].delete("all")
            board[oldIndex].create_image(50, 50, image=otherImg)
            board[newIndex].delete("all")
            board[newIndex].create_image(50, 50, image=img)

            boardObjectSpaces[oldIndex] = otherPiece
            boardObjectSpaces[newIndex] = piece

            if ourColor == "w":
                wPlaces[oldIndex] = otherPiece
                wPlaces[newIndex] = piece
            elif ourColor == "b":
                bPlaces[oldIndex] = otherPiece
                bPlaces[newIndex] = piece

    pIndex = boardObjectSpaces.index(piece)

    if piece.kind == "pawn":
        if piece.color == "w":
            if pIndex in row1:
                winLose(otherPiece)
        if piece.color == "b":
            if pIndex in row6:
               winLose(otherPiece)

    global moveNo
    moveNo += 1

    roundText = tkin.Label(root, text="MOVE")
    roundNo = tkin.Label(root, text=moveNo)
    roundText.grid(column=0, row=9, sticky="w")
    roundNo.grid(column=0, row=9)     

    pickPiece(setMove, places, origSquare)  

def setStartPosition(bSet, wSet, board, boardObjectSpaces):
    for num in range(0,6):
        piece = bSet[num]
        boardObjectSpaces[num] = piece
        display = bSet[num].bImage
        place = board[num].create_image(55,55, image=display)
        bPlaces[num] = piece
    
    setCounter = 0
    for num in range(34,28, -1):
        piece = wSet[setCounter]
        boardObjectSpaces[num] = piece
        display = wSet[setCounter].wImage
        place = board[num].create_image(55,55, image=display)
        wPlaces[num] = piece
        setCounter +=1
    
    return bSet, wSet, board, bPlaces, wPlaces, boardObjectSpaces

def pickPiece(setMove,places,origSquare):
    if places:
        for piece in places:
            if piece:
                pIndex = places.index(piece)
                board[pIndex].config(cursor="hand2")
                board[pIndex].bind("<Button-1>",unbind)
                origSquare.bind("<Button-3>",unbind)

    if setMove == "w":
        places = wPlaces
        playerGo = "It's white's move."
    elif setMove == "b":
        places = bPlaces
        playerGo = "It's black's move."

    playerText = tkin.Label(root, text=playerGo)
    playerText.grid(column=10, row=0)

    for piece in places:
        if piece != "":
            pIndex = places.index(piece)
            board[pIndex].config(cursor="plus")
            board[pIndex].bind("<Button-1>",lambda event: playerSelect(event,places = places))
        else:
            continue
    return places

def playerSelect(event,places):
    caller = event.widget
    caller.config(bg="mediumpurple1")
    squareIndex = board.index(caller)
    piece = boardObjectSpaces[squareIndex]

    fullCanvas = []

    for counter in places:
        if counter != "" or piece:
                pIndex = places.index(counter)
                fullCanvas.append(board[pIndex])
                counterIndex = places.index(counter)
                board[counterIndex].config(cursor="hand2")
                board[counterIndex].bind("<Button-1>", unbind)
    possibleMovements(caller,piece,squareIndex)

def unbind(event):
    pass

def deSelect(event, possibleSpaces):
    print("DESELECT")
    event = event.widget

    if event in whiteSquares:
        bgcol = "white"
    elif event in blackSquares:
        bgcol = "brown"
    
    event.config(bg=bgcol)

    selCanvases = []

    for index in possibleSpaces:
        selfCanvas = board[index]
        selCanvases.append(selfCanvas)
    
    for canvas in selCanvases:
        if canvas in whiteSquares:
            canvas.config(bg="white")
        elif canvas in blackSquares:
            canvas.config(bg="brown")
    
    for canvas in selfCanvas:
        canvas.bind("<Button-1>", unbind)
     
    ourIndex = board.index(event)
    setMove = boardObjectSpaces[ourIndex].color

    origSquare = event

    pickPiece(setMove, places, origSquare)

def possibleMovements(caller, piece, squareIndex):
    print("POSMOVE")
    piece.moves(squareIndex)

def playerMove(event, active, board, boardObjectSpaces):
    roundLabel(active, board, boardObjectSpaces)

def winLose(otherPiece):
    popup = tkin.Tk()
    popup.geometry("1000x800")
    popup.wm_title("YOU WIN!")

    label = tkin.Label(popup, font=("Helvetica", 100))

    if otherPiece.color == "b":
        msg = "White Wins!"
        popup.config(bg="white")
        label.config(bg="white", fg="black")
    if otherPiece.color == "w":
        msg = "Black Wins!"
        popup.config(bg="black")
        label.config(bg="black", fg="white")
    
    label.config(text=msg)
    label.pack()
    popup.mainloop()

bPawn1 = Pawn("b",bSet)
bPawn2 = Pawn("b",bSet)
bPawn3 = Pawn("b",bSet)
bPawn4 = Pawn("b",bSet)
bPawn5 = Pawn("b",bSet)
bPawn6 = Pawn("b",bSet)

wPawn1 = Pawn("w",wSet)
wPawn2 = Pawn("w",wSet)
wPawn3 = Pawn("w",wSet)
wPawn4 = Pawn("w",wSet)
wPawn5 = Pawn("w",wSet)
wPawn6 = Pawn("w",wSet)

def fillPlaces(wPlaces, bPlaces):
    for num in range(0, 35):
        wPlaces.append("")
        bPlaces.append("")
    return wPlaces, bPlaces
  
        
moveNo = 0
playerGo = "It's white move"
setMove = "w"

wPlaces = []
bPlaces = []
places = ""

wPlaces, bPlaces = fillPlaces(wPlaces, bPlaces)
labelTop()
labelSide()
roundLabel()

playerGo = playerLabel(playerGo)
blackSquares, whiteSquares = makeBoardCanvases()
blackSquares, whiteSquares = positionBoardCanvases(blackSquares, whiteSquares)
board = boardSpaces(blackSquares, whiteSquares)
bSet, wSet, board, bPlaces, wPlaces, boardObjectSpaces = setStartPosition(bSet, wSet, board, boardObjectSpaces)
places = pickPiece(setMove, places, origSquare=board[1])

root.mainloop()