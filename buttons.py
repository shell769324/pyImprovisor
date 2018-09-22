# Updated Animation Starter Code

from tkinter import *

####################################
# customize these functions
####################################
class Buttons(object):
    Buttons.allButton=[]
    def __init__(self,size,shape,location,text,on=False):
        Buttons.allButton.append(self)
        self.on=on          # indicate if it's on
        self.size=size      #size of it. 
        self.shape=shape    #1 is a ball and 0 is a square
        self.loc=location   #a tuple in the form (x,y)
        self.text=text      #the text being displayed on it.
        self.color=None

    def drawButton(self,canvas,data): #draw a button
        if self.shape==1:
            canvas.create_oval(self.loc[0]-self.size,
                self.loc[1]-self.size,self.loc[1]+self.size,self.loc[1]+self.size,fill=self.color)
        elif self.shape==0:
            canvas.create_rectangle(self.loc[0]-self.size,
                self.loc[1]-self.size,self.loc[1]+self.size,self.loc[1]+self.size,fill=self.color)
    
    def detectButton(self,x,y): #Detect whether the button is pressed, if pressed, turn it on.
        if abs(self.loc[0]-x)<self.size and abs(self.loc[1]-y)<self.size:
            self.on=True
            print("haha")

def init(data):
    
    pass

def mousePressed(event, data):
    for button in Buttons.allButton:
        button.detectButton(event.x,event.y)

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    for button in Buttons.allButton:
        button.drawButton(canvas,data)







def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.configure(bd=0, highlightthickness=0)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1200, 800)