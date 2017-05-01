import tkinter
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
import winsound

#cluesfound = 0
#foundkey = 0


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
        if self.X == 0:
            self.laptop = Laptop(self.window)
        else:
            try:
                self.window.canvas.delete(self.laptop.idnumber)
            except:
                 pass

    def click(self, event):
        if self.direction == 'left':
            self.window.canvas.itemconfig(self.window.currentimage,image=self.window.walls[(self.X-1)%len(self.window.walls)])
            self.window.arrow1.X=(self.X-1)%len(self.window.walls)
            self.window.arrow2.X=(self.X-1)%len(self.window.walls)
        else:
            self.window.canvas.itemconfig(self.window.currentimage,image=self.window.walls[(self.X+1)%len(self.window.walls)])
            self.window.arrow1.X=(self.X+1)%len(self.window.walls)
            self.window.arrow2.X=(self.X+1)%len(self.window.walls)
        if self.X == 0:
            self.laptop = Laptop(self.window)
        else:
            try:
                self.window.canvas.delete(self.laptop.idnumber)
            except:
                 pass
        if self.X == 1:
            self.speaker = Speaker(self.window)
        else:
            try:
                self.window.canvas.delete(self.speaker.idnumber)
            except:
                pass
        if self.X == 3:
            self.waterbottle = WaterBottle(self.window)
        else:
            try:
                self.window.canvas.delete(self.waterbottle.idnumber)
            except:
                pass
        if self.X == 2 and self.window.cluesfound == 3:
            self.key = Key(self.window)
        else:
            try:
                self.window.canvas.delete(self.key.idnumber)
            except:
                pass
        #if self.X == 2 and self.window.cluesfound == 3 and self.window.keyfound ==1:
            #self.door = Door(self.window)



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
        winsound.PlaySound("C:/Users/aripl/Documents/college/CS 110/project1/Escape_the_Room/Believer.wav",winsound.SND_FILENAME)
        clue1 = simpledialog.askstring("Input", "What is the name of this song?")
        if clue1 == "Believer":
            messagebox.showinfo("You did it!", "Congratulations! You found a clue!")
            #global cluesfound
            self.window.cluesfound += 1
            self.window.canvas.delete(self.idnumber)
            if self.window.cluesfound == 3:
                messagebox.showinfo("Input","You've found all the clues! Now you can look for the key to open the door!")

        else:
            messagebox.showerror("That's not it!", "Nope! Try again.")
class Laptop:
    def __init__(self,window):
        self.window = window
        self.a = 600
        self.b = 350
        self.c = 640
        self.d = 370
        self.idnumber = self.window.canvas.create_rectangle(self.a,self.b,self.c,self.d, outline = '')
        self.window.canvas.tag_bind(self.idnumber, "<Button-1>", self.click)

    def click(self,event):
        clue2 = simpledialog.askstring("Input", "What is the name of the game you are playing right now?")
        if clue2 == "Escape the Room":
            messagebox.showinfo("You did it!", "Congratulations! You found a clue!")
            #global cluesfound
            self.window.cluesfound += 1
            self.window.canvas.delete(self.idnumber)
            if self.window.cluesfound == 3:
                messagebox.showinfo("Input","You've found all the clues! Now you can look for the key to open the door!")
        else:
            messagebox.showerror("That's not it!", "Nope! Try again")

class WaterBottle:
    def __init__(self,window):
        self.window = window
        self.a = 160
        self.b = 320
        self.c = 170
        self.d = 350
        self.idnumber = self.window.canvas.create_rectangle(self.a, self.b, self.c, self.d, outline = '')
        self.window.canvas.tag_bind(self.idnumber, "<Button-1>", self.click)

    def click(self, event):
        clue3 = simpledialog.askstring("Input", "What did you just click on?")
        if clue3 == "Water Bottle":
            #global cluesfound
            self.window.cluesfound += 1
            messagebox.showinfo("You did it!", "Congratulation! You found a clue!")
            self.window.canvas.delete(self.idnumber)
            if self.window.cluesfound == 3:
                messagebox.showinfo("Input","You've found all the clues! Now you can look for the key to open the door!")
        else:
            messagebox.showerror("That's not it!", "Nope! Try again")

class Key:
    def __init__(self,window):
        self.window = window
        self.a = 405
        self.b = 485
        self.c = 426
        self.d = 520
        self.idnumber = self.window.canvas.create_rectangle(self.a,self.b,self.c,self.d,outline = "")
        self.window.canvas.tag_bind(self.idnumber, "<Button-1>", self.click)

    def click(self,event):
            messagebox.showinfo("Congratulations!","You've found the key! Now use the door to escape!")
             #foundkey
            door = Door(self.window)
            self.window.keyfound = 1

class Door:
    def __init__(self,window):
        self.window = window
        self.a = 150
        self.b = 275
        self.c = 240
        self.d = 400
        self.idnumber = self.window.canvas.create_rectangle(self.a, self.b, self.c, self.d, outline = '')
        self.window.canvas.tag_bind(self.idnumber, "<Button-1>", self.click)
    def click(self, event):
        messagebox.showinfo("Congratulations!", "You have escaped!!")
        #global cluesfound
        self.window.cluesfound += 1
        #self.window.window.destroy()

#view
class Window:
    def __init__(self):
        self.cluesfound = 0
        self.keyfound = 0
        self.window = tkinter.Tk()
        self.window.wm_title("Escape the Room")
        self.canvas = tkinter.Canvas(self.window,width=800,height=600)
        self.canvas.grid()
        basepath = "C:/Users/aripl/Documents/college/CS 110/project1/Escape_the_Room/"
        paths = ["image1_3_.gif", "image3.gif","image4.gif", "image2.gif"]
        self.walls = [tkinter.PhotoImage(file = basepath + path) for path in paths]
        self.currentimage = self.canvas.create_image(400,300,image=self.walls[0])
        self.arrow1 = Arrow(self)
        self.arrow2 = Arrow(self,direction='right')

        self.canvas.pack()
        #if self.cluesfound == 1:
            #self.window.destroy()
        tkinter.mainloop()


    #def mainLoop(self):
        #self.window.mainloop()

#controller
#def main():
    #window = Window()
    #window.mainLoop()

#main()

