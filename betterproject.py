import tkinter
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import winsound

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
        if self.X == 1:
            self.speaker = Speaker(self.window)
        else:
            self.window.canvas.delete(self.speaker.idnumber)

class Speaker:
    def __init__(self, window):
        self.window = window
        self.a = 360
        self.b = 138
        self.c = 380
        self.d = 183
        self.idnumber = self.window.canvas.create_rectangle(self.a,self.b,self.c,self.d,outline = "")
        self.window.canvas.tag_bind(self.idnumber, "<Button-1>", self.click)

    def click(self,event):
        winsound.PlaySound("C:/Users/sarah/OneDrive/Documents/CS 110/Believer.wav",winsound.SND_FILENAME)
        clue = simpledialog.askstring("Input", "What is the name of this song?")
        if clue == "Believer":
            messagebox.showinfo("You did it!", "Congratulations! You found a clue!")
        else:
            messagebox.showerror("That's not it!", "Nope! Try again.")

#view
class Window:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(self.window,width=800,height=600)
        self.canvas.grid()
        basepath = "C:/Users/sarah/OneDrive/Documents/CS 110/"
        paths = ["image1_3_.gif", "image3.gif","image4.gif", "image2.gif"]
        self.walls = [tkinter.PhotoImage(file = basepath + path) for path in paths]
        self.currentimage = self.canvas.create_image(400,300,image=self.walls[0])
        self.arrow1 = Arrow(self)
        self.arrow2 = Arrow(self,direction='right')
        self.canvas.pack()

    def mainLoop(self):
        self.window.mainloop()

#controller
def main():
    window = Window()
    window.mainLoop()
main()
