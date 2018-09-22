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
# Variables
####################################

allChords = []





####################################
# Color Scheme
####################################

color1 = "#011935"
color2 = "#00343F"
color3 = "#1DB0B8"
color4 = "#37C6C0"
color5 = "#D0E9FF"


#####################################
# Grid functions
#####################################


def init(data):
	data.rows = 3
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
	gridWidth  = 2*data.width/3 - 2*data.margin
	gridHeight = data.height/2 - 2*data.margin
	cellWidth  = gridWidth / (data.cols)
	cellHeight = gridHeight / (data.rows)
	row = (y - data.margin) // cellHeight
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
			fill = color5 if (data.selection == (row, col)) else "white"
			canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline=color3, dash=(1,5))

	# The first extra bar line as start
	canvas.create_line(15, 15, 15, 125, fill=color2, width=2)

	# draw barlines
	for row in range(data.rows):
		for col in range(data.cols/2 + 1):
			(x0, y0, x1, y1) = getCellBounds(row, col, data)
			canvas.create_line(x0*2, y0+10, x0*2, y1-10, fill=color2, width=2)


	canvas.create_text(150, 450, text="New song 0",
					   font=("Tahoma", "30"), fill=color2)



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


	# set up events
	root.bind("<Button-1>", lambda event:
							mousePressedWrapper(event, canvas, data))
	root.bind("<Key>", lambda event:
							keyPressedWrapper(event, canvas, data))
	redrawAll(canvas, data)
	# and launch the app

	root.mainloop()  # blocks until window is closed
	print("bye!")

run(1200, 800)