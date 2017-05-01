import json
import tkinter.messagebox
import betterproject
#import startmenu

def openfile(mytime):
    besttime = open("besttime.json", "r").read()
    mydictionary = json.loads(besttime)

    for key in mydictionary:
        mykey = mydictionary[key]

    if(mytime <= mykey):
        number= str(mytime)
        yourtime = str("Thanks for playing, your time was: " + number + " That's your best time!")
        createending(yourtime)
        besttime = open("besttime.json", "w")
        mynewdictionary = {"The best time is": mytime}
        towrite = json.dumps(mynewdictionary)
        besttime.write(towrite)
        besttime.close()

    else:
        number = str(mytime)
        besttimesofar = str(mykey)
        yourtime = str("Thanks for playing, your time was: " + number + " Try again for a better time!" + " The best time so far is " + besttimesofar)
        createending(yourtime)




class createending:
    def __init__(self, number):
        self.newwindow = tkinter.Tk()
        self.newwindow.wm_title("Escape the Room")
        self.number = number
        self.label = tkinter.Label(self.newwindow, text = self.number)
        self.label.pack()
        tkinter.mainloop()
