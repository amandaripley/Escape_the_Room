import tkinter
from PIL import Image, ImageTk

#model

class Arrow:

    def __init__(self, window, color='red', direction='left',X=0):
        self.color = color
        self.direction = direction
        self.window = window
        if direction == 'left':
            self.a = 50,280
            self.b = 50,320
            self.c = 25,300
        else:
            self.a = 750,280
            self.b = 750,320
            self.c = 775,300
        self.idnumber = self.window.canvas.create_polygon(self.a,self.b,self.c,fill=self.color)
        self.window.canvas.tag_bind(self.idnumber, "<Button-1>", self.click)
        self.X = X

    def click(self, event):
        room = [self.window.wall1, self.window.wall2, self.window.wall3, self.window.wall4]
        if self.direction == 'left':
            if self.X == 0:
                self.window.canvas.create_image(400,300,image=room[1])
                arrow1 = Arrow(self.window,X=1)
                arrow2 = Arrow(self.window,direction='right',X=1)
                self.window.canvas.pack()
            elif self.X == 1:
                self.window.canvas.create_image(400,300,image=room[2])
                arrow1 = Arrow(self.window,X=2)
                arrow2 = Arrow(self.window,direction='right',X=2)
                self.window.canvas.pack()
            elif self.X == 2:
                self.window.canvas.create_image(400,300,image=room[3])
                arrow1 = Arrow(self.window,X=3)
                arrow2 = Arrow(self.window,direction='right',X=3)
                self.window.canvas.pack()
            elif self.X == 3:
                self.window.canvas.create_image(400,300,image=room[0])
                arrow1 = Arrow(self.window,X=0)
                arrow2 = Arrow(self.window,direction='right',X=0)
                self.window.canvas.pack()
        else:
            if self.X == 0:
                self.window.canvas.create_image(400,300,image=room[3])
                arrow1 = Arrow(self.window,X=3)
                arrow2 = Arrow(self.window,direction='right',X=3)
                self.window.canvas.pack()
            elif self.X == 1:
                self.window.canvas.create_image(400,300,image=room[0])
                arrow1 = Arrow(self.window,X=0)
                arrow2 = Arrow(self.window,direction='right',X=0)
                self.window.canvas.pack()
            elif self.X == 2:
                self.window.canvas.create_image(400,300,image=room[1])
                arrow1 = Arrow(self.window,X=1)
                arrow2 = Arrow(self.window,direction='right',X=1)
                self.window.canvas.pack()
            elif self.X == 3:
                self.window.canvas.create_image(400,300,image=room[2])
                arrow1 = Arrow(self.window,X=2)
                arrow2 = Arrow(self.window,direction='right',X=2)
                self.window.canvas.pack()

#view
class Window:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window,width=800,height=600)
        self.canvas.grid()
        self.wall1 = tkinter.PhotoImage(file = "C:/Users/sarah/OneDrive/Documents/CS 110/BalconyChairs.gif")
        self.wall2 = tkinter.PhotoImage(file = "C:/Users/sarah/OneDrive/Documents/CS 110/BalconyDoortoBdR.gif")
        self.wall3 = tkinter.PhotoImage(file = "C:/Users/sarah/OneDrive/Documents/CS 110/BRTV.gif")
        self.wall4 = tkinter.PhotoImage(file = "C:/Users/sarah/OneDrive/Documents/CS 110/BalconyWall.gif")
        self.canvas.create_image(400,300,image=self.wall1)
        self.arrow1 = Arrow(self)
        self.arrow2 = Arrow(self,direction='right')
        self.canvas.pack()

    def mainLoop(self):
        self.window.mainloop()

def main():
    window = Window()
    window.mainLoop()
main()
