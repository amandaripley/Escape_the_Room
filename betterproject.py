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
        if self.direction == 'left':
            self.window.canvas.itemconfig(self.window.currentimage,image=self.window.walls[(self.X-1)%len(self.window.walls)])
            self.window.arrow1.X=(self.X-1)%len(self.window.walls)
            self.window.arrow2.X=(self.X-1)%len(self.window.walls)
        else:
            self.window.canvas.itemconfig(self.window.currentimage,image=self.window.walls[(self.X+1)%len(self.window.walls)])
            self.window.arrow1.X=(self.X+1)%len(self.window.walls)
            self.window.arrow2.X=(self.X+1)%len(self.window.walls)
#view
class Window:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window,width=800,height=600)
        self.canvas.grid()
        basepath = "C:/Users/sarah/OneDrive/Documents/CS 110/"
        paths = ["BalconyChairs.gif", "BalconyDoortoBdr.gif", "BRTV.gif", "BalconyWall.gif"]
        self.walls = [tkinter.PhotoImage(file = basepath + path) for path in paths]
        self.currentimage = self.canvas.create_image(400,300,image=self.walls[0])
        self.arrow1 = Arrow(self)
        self.arrow2 = Arrow(self,direction='right')
        self.canvas.pack()

    def mainLoop(self):
        self.window.mainloop()

def main():
    window = Window()
    window.mainLoop()
main()
