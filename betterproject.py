import tkinter
from PIL import Image, ImageTk

#model
class Arrow:

    def __init__(self, color='red', direction='left',X=0):
        self.color = color
        self.direction = direction
        if direction == 'left':
            self.a = 50,280
            self.b = 50,320
            self.c = 25,300
        else:
            self.a = 750,280
            self.b = 750,320
            self.c = 775,300
        self.idnumber = canvas.create_polygon(self.a,self.b,self.c,fill=self.color)
        canvas.tag_bind(self.idnumber, "<Button-1>", self.click)
        self.X = X

    def click(self, event):
        room = [wall1, wall2, wall3, wall4]
        if self.direction == 'left':
            if self.X == 0:
                canvas.create_image(400,300,image=room[1])
                arrow1 = Arrow(X=1)
                arrow2 = Arrow(direction='right',X=1)
                canvas.pack()
            elif self.X == 1:
                canvas.create_image(400,300,image=room[2])
                arrow1 = Arrow(X=2)
                arrow2 = Arrow(direction='right',X=2)
                canvas.pack()
            elif self.X == 2:
                canvas.create_image(400,300,image=room[3])
                arrow1 = Arrow(X=3)
                arrow2 = Arrow(direction='right',X=3)
                canvas.pack()
            elif self.X == 3:
                canvas.create_image(400,300,image=room[0])
                arrow1 = Arrow(X=0)
                arrow2 = Arrow(direction='right',X=0)
                canvas.pack()
        else:
            if self.X == 0:
                canvas.create_image(400,300,image=room[3])
                arrow1 = Arrow(X=3)
                arrow2 = Arrow(direction='right',X=3)
                canvas.pack()
            elif self.X == 1:
                canvas.create_image(400,300,image=room[0])
                arrow1 = Arrow(X=0)
                arrow2 = Arrow(direction='right',X=0)
                canvas.pack()
            elif self.X == 2:
                canvas.create_image(400,300,image=room[1])
                arrow1 = Arrow(X=1)
                arrow2 = Arrow(direction='right',X=1)
                canvas.pack()
            elif self.X == 3:
                canvas.create_image(400,300,image=room[2])
                arrow1 = Arrow(X=2)
                arrow2 = Arrow(direction='right',X=2)
                canvas.pack()

#view
window = tkinter.Tk()
canvas = tkinter.Canvas(window,width=800,height=600)
canvas.grid()

wall1 = tkinter.PhotoImage(file = "C:/Users/sarah/OneDrive/Documents/CS 110/BalconyChairs.gif")
wall2 = tkinter.PhotoImage(file = "C:/Users/sarah/OneDrive/Documents/CS 110/BalconyDoortoBdR.gif")
wall3 = tkinter.PhotoImage(file = "C:/Users/sarah/OneDrive/Documents/CS 110/BRTV.gif")
wall4 = tkinter.PhotoImage(file = "C:/Users/sarah/OneDrive/Documents/CS 110/BalconyWall.gif")

canvas.create_image(400,300,image=wall1)
arrow1 = Arrow()
arrow2 = Arrow(direction='right')
canvas.pack()

window.mainloop()
