import tkinter
import betterproject
from PIL import Image, ImageTk
import tkinter.messagebox
import time
import timer



class StartMenu:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Escape the Room")
        #self.main_window.geometry("500x500")
        self.canvas = tkinter.Canvas(self.main_window, width = 800, height = 600)
        #self.canvas.grid()
        self.image = tkinter.PhotoImage(file = "C:/Users/aripl/Documents/college/CS 110/our project/BalconyDoortoBdR.gif")
        self.canvas.create_image(400,350,image = self.image)

        #self.myframe = tkinter.Frame(master = self.main_window, width = 1000, height = 1000)
        #self.myframe.pack()
        #self.aframe = tkinter.Frame(self.main_window)
        self.label = tkinter.Label(self.main_window, text = "Escape the Room")
        self.label.pack(side = "top")
        self.tutoriallabel = tkinter.Label(self.main_window, text = "How to Play:")
        self.tutoriallabel.pack()
        self.instructions = tkinter.Label(self.main_window, text = "Click on the Screen with the Mouse to find the Keys")
        self.instructions.pack()
        self.differentrooms = tkinter.Label(self.main_window, text = "Use the left and right arrow keys to look around the room")
        self.differentrooms.pack()

        #self.b_frame = tkinter.Frame(self.main_window)
        self.startbutton = tkinter.Button(self.main_window, text = "Start Game", command = self.startgame)
        self.startbutton.pack()

        self.exitbutton = tkinter.Button(self.main_window, text = "Quit", command = self.popup)
        self.exitbutton.pack()
        self.canvas.pack()


        #self.aframe.pack()
        #self.b_frame.pack()
        #self.c_frame.pack()


        tkinter.mainloop()

    #def tutorial(self):
    def startgame(self):
        self.main_window.destroy()
        window = betterproject.Window()
        betterproject.window.mainloop()


    def popup(self):
        #self.message = "Are you sure you want to quit"
        #self.label.config(text = self.message)
        #tkinter.messagebox.showinfo("Exit", "Are you sure you want to quit?")
        if tkinter.messagebox.askyesno("Exit","Are you sure you want to quit?"):
            self.main_window.destroy()

def main():
    starttime = time.time()
    StartMenu()
    elapsedtime = time.time() - starttime
    timer.openfile(elapsedtime)

main()
