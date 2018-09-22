# Updated Animation Starter Code

from tkinter import *

####################################
# customize these functions
####################################
class Buttons(object):
    allButton=[]
    keyEx=None #Indicate whether there is already a key button on. If there is, the button take the place.
    ShFlEx=None #Indicate whether there is already a sharp/flat button on
    Mod=[]
    def __init__(self,size,shape,location,text,ButtonType="Key",on=False):
        Buttons.allButton.append(self)
        self.on=on          # indicate if it's on
        self.size=size      #size of it. 
        self.shape=shape    #1 is a ball and 0 is a square
        self.loc=location   #a tuple in the form (x,y)
        self.text=text      #the text being displayed on it.
        self.color="red"
        self.valid=True
        self.ButtonType=ButtonType

    def drawButton(self,canvas,data): #draw a button
        if self.on:
            color=self.color
        else: color = "white"
        if self.shape==1:
            canvas.create_oval(self.loc[0]-self.size,
                self.loc[1]-self.size,self.loc[0]+self.size,self.loc[1]+self.size,fill=color)
        elif self.shape==0:
            canvas.create_rectangle(self.loc[0]-self.size,
                self.loc[1]-self.size,self.loc[0]+self.size,self.loc[1]+self.size,fill=color)
        canvas.create_text(self.loc[0],self.loc[1],text=self.text)
    
    def detectButton(self,x,y): #Detect whether the button is pressed, if pressed, turn it on.
        if abs(self.loc[0]-x)<self.size and abs(self.loc[1]-y)<self.size:
            if self.ButtonType=="Key":
                if Buttons.keyEx!=self:
                    if Buttons.keyEx!=None:
                        Buttons.keyEx.on=False
                        Buttons.keyEx=self       #If the button is a key and is not the current key, it's 
                        self.on=True              #then switched to this button.
                    else:
                        Buttons.keyEx=self
                        self.on=True
                else:
                    self.on=False
                    Buttons.keyEx=None
            elif self.ButtonType=="ShFl":
                if Buttons.ShFl!=self:
                    if Buttons.ShFlEx!=None:
                        Buttons.ShFlEx.on=False
                        Buttons.ShFlEx=self       #If the button is a flat/sharp and is not the current key, it's 
                        self.on=True              #then switched to this button.
                    else:
                        Buttons.ShFlEx=self
                        self.on=True
                else:
                    self.on=False
                    Buttons.ShFlEx=None
                
def init(data):
    AKeyButton=Buttons(30,0,(800,600-0*50),"A")
    BKeyButton=Buttons(30,0,(800,600-1*50),"B")
    CKeyButton=Buttons(30,0,(800,600-2*50),"C")
    DKeyButton=Buttons(30,0,(800,600-3*50),"D")
    EKeyButton=Buttons(30,0,(800,600-4*50),"E")
    FKeyButton=Buttons(30,0,(800,600-5*50),"F")
    GKeyButton=Buttons(30,0,(800,600-6*50),"G")

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