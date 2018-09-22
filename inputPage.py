
from Tkinter import *
import MidiConverter


# def draw(canvas, width, height):
#     canvas.create_rectangle(0,0,150,150, fill="yellow")

# def runDrawing(width=300, height=300):
#     root = Tk()
#     root.resizable(width=False, height=False) # prevents resizing window
#     canvas = Canvas(root, width=width, height=height)
#     canvas.configure(bd=0, highlightthickness=0)
#     canvas.pack()
#     draw(canvas, width, height)
#     root.mainloop()
#     print("bye!")


# runDrawing(800, 1200)




####################################
# Variables
####################################

allChords = ["Am7", NONE, NONE, NONE, NONE, NONE, NONE, NONE,
			"Cm7", NONE, NONE, NONE, NONE, NONE, NONE, "F7",
			"BbM7", NONE, "Bbm7", "Eb7", "AbM7", NONE, "Abm7", "Db7",]

inputs = []


def compileInputs(allChords):
	thisChord = ""
	count = 0
	for chord in allChords:
		if chord != NONE:
			count = count + 1
			if thisChord != "": 
				inputs.append((thisChord, 0.5*count))
			thisChord = chord
			count = 0
		else:
			count = count + 1
	return True

compileInputs(allChords)

print(inputs)

####################################
# Color Scheme
####################################

color1 = "#011935"
color2 = "#00343F"
color3 = "#1DB0B8"
color4 = "#37C6C0"
color5 = "#D0E9FF"


#####################################
# Button Class
#####################################
class Buttons(object):
	allButton=[]
	keyEx=None 			#Indicate whether there is already a key button on. If there is, the button take the place.
	ShFlEx=None 		#Indicate whether there is already a sharp/flat button on
	ProEx=None
	tones=[]
	quality=None
	quality7=None
	GenEx=None
	def __init__(self,size,shape,location,text,ButtonType="Key",on=False,color=color4,aff=None,tone=None):
		Buttons.allButton.append(self)
		self.on=on          			# indicate if it's on
		self.size=size      			#size of it. 
		self.shape=shape    			#1 is a ball and 0 is a square
		self.loc=location   			#a tuple in the form (x,y)
		self.text=text      			#the text being displayed on it.
		self.color=color
		self.tone=tone
		self.ButtonType=ButtonType
		self.mod=None	 				#Show what affiliations a tone has
		self.aff=aff					#Affiliation to a tone, only extension options have this


	@staticmethod						#used to initialize the button class when switching to another chord box.
	def initialize():
		for item in Buttons.allButton:
			item.on=False
			item.forbidden=False
			item.mod=None
		Buttons.allButton=[]
		Buttons.keyEx=None
		Buttons.ShFlEx=None
		Buttons.ProEx=None
		Buttons.tones=[]
		Buttons.quality=None
		Buttons.quality7=None

	# @staticmethod
	# def RawCompile(data):
	# 	ChordSym=''
	# 	sel=data.selection
	# 	num=(sel[1]-1)*8+sel[1]
	# 	tempLst=[Buttons.keyEx,Buttons.ShFlEx,Buttons.quality,Buttons.quality7]
	# 	for item in tempLst:
	# 		if item!=None:
	# 			if item.text!="Dom":
	# 				ChordSym+=item.text
	# 			else: ChordSym+=7
	# 	for item in Buttons.tones:
	# 		if item.text=="9":
	# 			if "M" in ChordSym:
	# 				ChordSym=ChordSym[0:-1]+"9"
	# 			if "m" in ChordSym:
	# 				if "b" in ChordSym:
	# 					ChordSym=ChordSym[0:2]+"9"
	# 				else:
	# 					ChordSym=ChordSym[0:1]+"9"
	# 			if item.mod!=None:
	# 				ChodSym+=item.mod.text+"9"
	# 			else:
	# 				ChodSym+=
	# 		elif item.text=="13":
	# 			if "M" in ChordSym:
	# 				ChordSym=ChordSym[0:-1]+"13"
	# 			else:
	# 				if item.mod
	# 		elif item.text="11"
			

	def drawButton(self,canvas,data): 	#draw a button
		if self.on:
			color=self.color
		else: color = "white"
		if self.shape==1:
			canvas.create_oval(self.loc[0]-self.size,
				self.loc[1]-self.size,self.loc[0]+self.size,self.loc[1]+self.size,
				fill=color, outline=color1, dash=(1,5))
			canvas.create_text(self.loc[0],self.loc[1],text=self.text, font=("Comic Sans MS", "15"))
			
		elif self.shape==0:
			canvas.create_rectangle(self.loc[0]-self.size,
				self.loc[1]-self.size,self.loc[0]+self.size,self.loc[1]+self.size,
				fill=color, outline=color1, dash=(1,5))
			canvas.create_text(self.loc[0],self.loc[1],text=self.text, font=("Comic Sans MS", "15"))
	

	def detectButton(self,x,y,data):
		if abs(self.loc[0]-x)<self.size and abs(self.loc[1]-y)<self.size:
			if self.ButtonType=="Key":
				if Buttons.keyEx!=self:
					if Buttons.keyEx!=None:  		 #The case of changing a key button
						Buttons.keyEx.on=False
						Buttons.keyEx=self      	 #If the button is a key and is not the current key, it's 
						self.on=True            	 #then switched to this button.
						if Buttons.ShFlEx!=None:   	 #If previously chose a shfl button, abort the change
							Buttons.ShFlEx.on=False
							Buttons.ShFlEx=None
					else:
						Buttons.keyEx=self
						self.on=True
				else:
					if Buttons.ShFlEx!=None:
							Buttons.ShFlEx.on=False
							Buttons.ShFlEx=None
					self.on=False
					Buttons.keyEx=None
			elif self.ButtonType=="ShFl":
				if Buttons.ShFlEx!=self:
					if Buttons.ShFlEx!=None:
						Buttons.ShFlEx.on=False
						Buttons.ShFlEx=self      	 #If the button is a flat/sharp and is not the current key, it's 
						self.on=True             	 #then switched to this button.
					else:
						Buttons.ShFlEx=self
						self.on=True
				else:
					self.on=False
					Buttons.ShFlEx=None
			elif self.ButtonType=="Proceed":
				if Buttons.ProEx!=self:
					if Buttons.ProEx!=None:
						Buttons.ProEx.on=False
						Buttons.ProEx=self       	#If the button is a proceed button and is not the current key, it's 
						self.on=True              	#then switched to this button.
					else:
						Buttons.ProEx=self
						self.on=True
						data.renderflag = True
						print ("render flag is True!")
				else:
					self.on=False
					Buttons.ProEx=None
			elif self.ButtonType=="Tone" and self.tone!=5:
				if not self.on:
					Buttons.tones.append(self)		#If a tone is selected, it either gets appended to chord tones,
					self.on=True					#or it's removed from there.
				else:
					self.on=False
					Buttons.tones.remove(self)
					if self.mod!=None:
						self.mod.on=False
						self.mod=None
			elif self.ButtonType=="ShFlTone":
				if self.aff.mod==None:
					if self.aff.on == False:
						Buttons.tones.append(self.aff)
						self.aff.on=True
					self.aff.mod=self
					self.on=True
				else:
					if self.aff.mod==self:
						self.aff.mod=None
						self.on=False
					elif self.aff.mod!=self:
						self.aff.mod.on=False
						self.aff.mod=self
						self.on=True
			elif self.ButtonType=="Quality":
				if Buttons.quality==None:
					Buttons.quality=self
					self.on=True
				else:
					if Buttons.quality==self:
						self.on=False
						Buttons.quality=None
					else:
						Buttons.quality.on=False
						Buttons.quality=self
						self.on=True
			elif self.ButtonType=="7Quality":
				if Buttons.quality7==False:
					self.on=True
					Buttons.quality7=True
				else: 
					self.on=False
					Buttons.quality7=False
			elif self.ButtonType=="Genre":
				if Buttons.GenEx!=self:
					if Buttons.GenEx!=None:
						Buttons.GenEx.on=False
						Buttons.GenEx=self      	 #If the button is a genre and is not the current key, it's 
						self.on=True             	 #then switched to this button.
					else:
						Buttons.GenEx=self
						self.on=True
				else:
					self.on=False
					Buttons.GenEx=None

#####################################
# Grid functions
#####################################

def getIndex(row, col):
	return 8*row + col

def init(data):
	data.select=False
	data.rows = 3
	data.cols = 8
	data.margin = 5 # margin around grid
	data.selection = (-1, -1) # (row, col) of selection, (-1,-1) for none
	
	#Key Buttons
	AKeyButton=Buttons(30,0,(900,50+0*70),"A") #Key Buttons
	BKeyButton=Buttons(30,0,(900,50+1*70),"B")
	CKeyButton=Buttons(30,0,(900,50+2*70),"C")
	DKeyButton=Buttons(30,0,(900,50+3*70),"D")
	EKeyButton=Buttons(30,0,(900,50+4*70),"E")
	FKeyButton=Buttons(30,0,(900,50+5*70),"F")
	GKeyButton=Buttons(30,0,(900,50+6*70),"G")

	Button5=Buttons(25,1,(1050,50+0*70),"5",ButtonType="Tone",tone=5,on=True)
	Button9=Buttons(25,1,(1050,50+1*70),"9",ButtonType="Tone",tone=9)
	Button11=Buttons(25,1,(1050,50+2*70),"11",ButtonType="Tone",tone=11)
	Button13=Buttons(25,1,(1050,50+3*70),"13",ButtonType="Tone",tone=13)
	ButtonM=Buttons(25,1,(1050,50+4*70),"M",ButtonType="Quality")
	Buttonm=Buttons(25,1,(1050,50+5*70),"m",ButtonType="Quality")
	ButtonDom=Buttons(25,1,(1050,50+6*70),"dom",ButtonType="Quality")
	Button7=Buttons(20,1,(1100,50+4.5*70),"7",ButtonType="7Quality")

	FlatButtonKey=Buttons(20,1,(900,500+1*50),"b",ButtonType="ShFl")
	SharpButtonKey=Buttons(20,1,(900,500+2*50),"#",ButtonType="ShFl")
	SharpButton5=Buttons(20,1,(1000,50+0*70),"#",ButtonType="ShFlTone",aff=Button5)
	FlatButton5=Buttons(20,1,(1100,50+0*70),"b",ButtonType="ShFlTone",aff=Button5)
	FlatButton9=Buttons(20,1,(1100,50+1*70),"b",ButtonType="ShFlTone",aff=Button9)
	SharpButton9=Buttons(20,1,(1000,50+1*70),"#",ButtonType="ShFlTone",aff=Button9)
	SharpButton11=Buttons(20,1,(1000,50+2*70),"#",ButtonType="ShFlTone",aff=Button11)
	FlatButton13=Buttons(20,1,(1100,50+3*70),"b",ButtonType="ShFlTone",aff=Button13)


	# The proceed button
	ProceedButton=Buttons(55, 1, (1050, 660), "Proceed!", ButtonType="Proceed")

	# The genre button
	BalladButton=Buttons(40, 0, (640, 500), "Ballad", ButtonType="Genre")
	BluesButton=Buttons(40, 0, (640, 600), "Blues", ButtonType="Genre")
	BebopButton=Buttons(40, 0, (740, 500), "Bebop", ButtonType="Genre")
	BosaNovaButton=Buttons(40, 0, (740, 600), "BosaNova", ButtonType="Genre")




def pointInGrid(x, y, data):
	# return True if (x, y) is inside the grid defined by data.
	return ((data.margin <= x <= (data.width*2)/3-data.margin) and
			(data.margin <= y <= data.height/2-data.margin))

def getCell(x, y, data):
	# aka "viewToModel"
	# return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
	if (not pointInGrid(x, y, data)):
		return (-1, -1)
	gridWidth  = 2*data.width/3 - 2*data.margin
	gridHeight = data.height/2 - 2*data.margin
	cellWidth  = gridWidth / (data.cols)
	cellHeight = gridHeight / (data.rows)
	row = ((y - 50) - data.margin) // cellHeight 
	col = (x - data.margin) // cellWidth
	# triple-check that we are in bounds
	row = min(data.rows-1, max(0, row))
	col = min(data.cols-1, max(0, col))
	return (row, col)

def getCellBounds(row, col, data):
	# aka "modelToView"
	# returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
	gridWidth  = 2*data.width/3 - 2*data.margin
	gridHeight = data.height/2 - 2*data.margin
	columnWidth = gridWidth / data.cols
	rowHeight = gridHeight / data.rows
	x0 = data.margin + col * columnWidth
	x1 = data.margin + (col+1) * columnWidth
	y0 = data.margin + row * rowHeight 
	y1 = data.margin + (row+1) * rowHeight 
	return (x0, y0, x1, y1)

def mousePressed(event, data):

	# if on the renderpage and we pressed the playing position, play music 
	if data.renderflag == True:
		if ((100 < event.x < 200) and (500 < event.y < 600)):
			MidiConverter.Play("GreenDolphin1.mid")

	for button in Buttons.allButton: #Check buttons status
		button.detectButton(event.x,event.y, data)
	
	if (not pointInGrid(event.x, event.y, data)):
		return
	(row, col) = getCell(event.x, event.y, data)
	# select this (row, col) unless it is selected
	if (data.selection == (row, col)):
		data.selection = (-1, -1)
	else:
		data.selection = (row, col)

def keyPressed(event, data):
	pass

def redrawAll(canvas, data):


	# Draw the play button
	if data.renderflag == True:
		canvas.create_oval(100, 500, 200, 600, fill=color3, outline=color3)
		canvas.create_polygon(130, 520, 130, 580, 185, 550, fill=color2, outline=color1)

	# draw grid of cells
	for row in range(data.rows):
		for col in range(data.cols):
			(x0, y0, x1, y1) = getCellBounds(row, col, data)
			fill = color4 if (data.selection == (row, col)) else color5
			canvas.create_rectangle(x0, y0 + 50, x1, y1 + 50, fill=fill, outline=color3, dash=(1,5))

	# The first extra bar line as start
	canvas.create_line(15, 65, 15, 175, fill=color2, width=2)

	# draw barlines
	for row in range(data.rows):
		for col in range(data.cols//2 + 1):
			(x0, y0, x1, y1) = getCellBounds(row, col, data)
			canvas.create_line(x0*2, y0+10 + 50, x0*2, y1-10 + 50, fill=color2, width=2)

	# show symbols
	for row in range(data.rows):
		for col in range(data.cols):
			(x0, y0, x1, y1) = getCellBounds(row, col, data)
			text = allChords[getIndex(row, col)]
			if text != NONE:
				bass = text[0]
				optionalFlat = True if (text[1]=="b") else False
				quality = text[2:] if optionalFlat == True else text[1:]

				# display the bass
				canvas.create_text((x0 + x1)/2 , (y0 + y1)/2 + 50, text=bass+("b" if optionalFlat==True else ""), 
					font=("Comic Sans MS", "30"), fill=color2)
				# display the quality
				canvas.create_text((x0 + x1)/2 + 20, (y0 + y1)/2 - 10 + 50, text=quality, 
					font=("Comic Sans MS", "15"), fill=color2)


	canvas.create_text(360, 25, text="New song 0",
					   font=("Comic Sans MS", "30"), fill=color2)

	# The chord construction buttons only show up when renderflag is false
	if data.renderflag == False:
		for button in Buttons.allButton:
			button.drawButton(canvas,data)



####################################
# use the run function as-is
####################################

def runInputPage(width=400, height=600):

	def redrawAllWrapper(canvas, data):
		canvas.delete(ALL)
		canvas.create_rectangle(0, 0, data.width, data.height,
								fill=color5, width=0)

		redrawAll(canvas, data)
		canvas.update()    

	def mousePressedWrapper(event, canvas, data):
		mousePressed(event, data)
		redrawAllWrapper(canvas, data)

	def keyPressedWrapper(event, canvas, data):
		keyPressed(event, data)
		redrawAllWrapper(canvas, data)

	# Set up data and call init
	class Struct(object): pass
	data = Struct()
	data.width = width
	data.height = height
	data.renderflag = False
	root = Tk()
	root.resizable(width=False, height=False) # prevents resizing window
	init(data)
	# create the root and the canvas
	canvas = Canvas(root, width=data.width, height=data.height, bg=color5)

	canvas.configure(bd=0, highlightthickness=0)
	canvas.pack()


	# set up events
	root.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
							keyPressedWrapper(event, canvas, data))
	redrawAll(canvas, data)
	# and launch the app

	root.mainloop()  # blocks until window closed

	print("bye!")


runInputPage(1200, 800)