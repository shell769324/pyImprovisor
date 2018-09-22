from Tkinter import *

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
# options and variables page
####################################


OPTIONS = [
"A",
"B",
"C"
] #etc


# w = OptionMenu(master, variable, *OPTIONS)
# w.pack()

# variable = StringVar(master)
# variable.set(OPTIONS[0]) # default value

def ok():
    print ("value is:" + variable.get())

# button = Button(master, text="OK", command=ok)
# button.pack()

# def drawOptionsPage(canvas, data):
# 	w = OptionMenu(master, variable, *OPTIONS)
# 	w.pack()

# 	button = Button(master, text="OK", command=ok)
# 	button.pack()



# def runOptionsPage(width=400, height=600):

# 	# Set up data and call init
# 	class Struct(object): pass
# 	data = Struct()
# 	data.width = width
# 	data.height = height
# 	optionsPage = Tk()
# 	optionsPage.resizable(width=False, height=False) # prevents resizing window
# 	init(data)
# 	# create the optionsPage and the canvas
# 	canvasOP = Canvas(optionsPage, width=data.width, height=data.height)
# 	canvasOP.configure(bd=0, highlightthickness=0)
# 	canvasOP.pack()

# 	# Variables
# 	variable = StringVar(optionsPage)
# 	variable.set(OPTIONS[0]) # default value

# 	# set up events
# 	optionsPage.bind("<Button-1>", lambda event:
# 							mousePressedWrapper(event, canvas, data))
# 	optionsPage.bind("<Key>", lambda event:
# 							keyPressedWrapper(event, canvas, data))
# 	drawOptionsPage(canvas, data)
# 	# and launch the app
# 	optionsPage.mainloop()  # blocks until window is closed

# runOptionsPage(500, 500)


#####################################
# Grid functions
#####################################


def init(data):
	data.rows = 4
	data.cols = 8
	data.margin = 5 # margin around grid
	data.selection = (-1, -1) # (row, col) of selection, (-1,-1) for none


def pointInGrid(x, y, data):
	# return True if (x, y) is inside the grid defined by data.
	return ((data.margin <= x <= data.width-data.margin) and
			(data.margin <= y <= data.height-data.margin))

def getCell(x, y, data):
	# aka "viewToModel"
	# return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
	if (not pointInGrid(x, y, data)):
		return (-1, -1)
	gridWidth  = data.width/2 - 2*data.margin
	gridHeight = data.height/2 - 2*data.margin
	cellWidth  = gridWidth / data.cols
	cellHeight = gridHeight / data.rows
	row = (y - data.margin) // cellHeight
	col = (x - data.margin) // cellWidth
	# triple-check that we are in bounds
	row = min(data.rows-1, max(0, row))
	col = min(data.cols-1, max(0, col))
	return (row, col)

def getCellBounds(row, col, data):
	# aka "modelToView"
	# returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
	gridWidth  = data.width/2 - 2*data.margin
	gridHeight = data.height/2 - 2*data.margin
	columnWidth = gridWidth / data.cols
	rowHeight = gridHeight / data.rows
	x0 = data.margin + col * columnWidth
	x1 = data.margin + (col+1) * columnWidth
	y0 = data.margin + row * rowHeight
	y1 = data.margin + (row+1) * rowHeight
	return (x0, y0, x1, y1)

def mousePressed(event, data):
	(row, col) = getCell(event.x, event.y, data)
	# select this (row, col) unless it is selected
	if (data.selection == (row, col)):
		data.selection = (-1, -1)
	else:
		data.selection = (row, col)

def keyPressed(event, data):
	pass

def redrawAll(canvas, data):
	# draw grid of cells
	for row in range(data.rows):
		for col in range(data.cols):
			(x0, y0, x1, y1) = getCellBounds(row, col, data)
			fill = "yellow" if (data.selection == (row, col)) else "white"
			canvas.create_rectangle(x0, y0, x1, y1, fill=fill)




	canvas.create_text(data.width/2, data.height/2 - 15, text="Click in grids!",
					   font="Arial 26 bold", fill="darkBlue")



####################################
# use the run function as-is
####################################

def run(width=400, height=600):
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

	# Set up data and call init
	class Struct(object): pass
	data = Struct()
	data.width = width
	data.height = height
	root = Tk()
	root.resizable(width=False, height=False) # prevents resizing window
	init(data)
	# create the root and the canvas
	canvas = Canvas(root, width=data.width, height=data.height)
	canvas.configure(bd=0, highlightthickness=0)
	canvas.pack()

	# set drop down menu and button
	variable = StringVar(root)
	variable.set(OPTIONS[0]) # default value

	# set up events
	root.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
							keyPressedWrapper(event, canvas, data))
	redrawAll(canvas, data)
	# and launch the app

	w = OptionMenu(root, variable, *OPTIONS)
	w.pack(side="right")

	button = Button(root, text="OK", command=ok)
	button.pack(side="right")

	root.mainloop()  # blocks until window is closed
	print("bye!")

run(800, 1200)