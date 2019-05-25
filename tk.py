import tkinter as tk

def getEntry():
    pieceList = str(userPiece.get()).split(',')
    positionList = str(userPosition.get()).split(',')
    pieceTuple = tuple(pieceList)
    positionTuple = tuple(positionList)
    return pieceTuple, positionTuple


HEIGHT = 100
WIDTH = 300

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root)
frame.place(relwidth=1, relheight=1)

label = tk.Label(frame, text='Please enter what piece you wish to move')
label.pack()

userPiece = tk.StringVar()

entry = tk.Entry(frame, textvariable=userPiece)
entry.pack()

label2 = tk.Label(frame, text='Please enter the desired position of your piece')
label2.pack()

userPosition = tk.StringVar()

entry2 = tk.Entry(frame, textvariable=userPosition)
entry2.pack()

button = tk.Button(frame, text='Enter move', command=getEntry)
button.pack()



root.mainloop()
