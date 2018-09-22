from midiutil import MIDIFile
import time
import pygame

class MidiConverter(object):
	def __init__(self,tempo=90,track=0,swing=1,channel=1):
		self.tempo=tempo
		self.channel=channel
		self.track=track			
 
	def initialize(self): #Create MIDIFile object and add tempo, etc.
		self.MyMIDI=MIDIFile(1, True, True, False, 1, 120, True)
		self.MyMIDI.addTempo(self.track,0,self.tempo)

	def addNotes(self,list):  #the format of input: (note, time, duration, volume)
		for item in list:
			self.MyMIDI.addNote(self.track,self.channel,item[0],item[1],item[2],item[3])

	def writeFiles(self,name): #Create a .mid file in the current directory with the name passed in
		with open(name, "wb") as output_file:
			self.MyMIDI.writeFile(output_file)

GreenDolphin = [(72,0,240,100),(72,240,360,100),(71,240+360+120,80,120),(67,240+360+120+80,80,100),(64,240+360+120+80*2,80,100),(70,240+360+120+80*3,120*8,120)]
GreenDolphinChords=[(48,0,120*8,80),(52,0,120*8,80),(59,0,120*8,80),(48,120*8,120*8,80),(53,120*8,120*8,80),(58,120*8,120*8,80),(63,120*8,120*8,80)]
test = [(52, 0, 0, 0), (56, 0, 1, 0), (59, 0, 2, 0), (52, 0, 3, 30), (56, 30, 4, 30), (59, 60, 5, 30), (52, 90, 6, 75), (56, 165, 7, 75), (59, 240, 8, 75), (52, 315, 9, 82), (56, 397, 10, 82), (59, 479, 11, 82), (52, 561, 12, 90), (56, 651, 13, 90), (59, 741, 14, 90), (57, 831, 15, 0), (49, 831, 16, 0), (52, 831, 17, 0), (57, 831, 18, 30), (49, 861, 19, 30), (52, 891, 20, 30), (57, 921, 21, 45), (49, 966, 22, 45), (52, 1011, 23, 45), (57, 1056, 24, 52), (49, 1108, 25, 52), (52, 1160, 26, 52), (57, 1212, 27, 90), (49, 1302, 28, 90), (52, 1392, 29, 90), (57, 1482, 30, 97), (49, 1579, 31, 97), (52, 1676, 32, 97), (57, 1773, 33, 105), (49, 1878, 34, 105), (52, 1983, 35, 105), (57, 2088, 36, 112), (49, 2200, 37, 112), (52, 2312, 38, 112), (52, 2424, 0, 0), (56, 2424, 1, 0), (59, 2424, 2, 0), (52, 2424, 3, 60), (56, 2484, 4, 60), (59, 2544, 5, 60), (52, 2604, 6, 75), (56, 2679, 7, 75), (59, 2754, 8, 75), (52, 2829, 9, 82), (56, 2911, 10, 82), (59, 2993, 11, 82), (52, 3075, 12, 90), (56, 3165, 13, 90), (59, 3255, 14, 90), (57, 3345, 15, 0), (49, 3345, 16, 0), (52, 3345, 17, 0), (57, 3345, 18, 30), (49, 3375, 19, 30), (52, 3405, 20, 30), (57, 3435, 21, 45), (49, 3480, 22, 45), (52, 3525, 23, 45), (57, 3570, 24, 52), (49, 3622, 25, 52), (52, 3674, 26, 52), (57, 3726, 27, 60), (49, 3786, 28, 60), (52, 3846, 29, 60), (57, 3906, 30, 90), (49, 3996, 31, 90), (52, 4086, 32, 90)]
def Play(path):
	pygame.mixer.init()
	pygame.mixer.music.load(path)
	pygame.mixer.music.play()

A=MidiConverter(100,0,0,1)     #First create the class, then initialize it, then add notes as you want, then write them. 
A.initialize()
A.addNotes(GreenDolphin)
A.addNotes(GreenDolphinChords)
A.writeFiles("GreenDolphin1.mid")



"""Play("GreenDolphin1.mid")
for i in range(30):
	print("t=%d"%i)
	time.sleep(1)
"""