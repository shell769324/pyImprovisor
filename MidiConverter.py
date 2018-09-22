from midiutil import MIDIFile
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

def Play(path):
	pygame.mixer.init()
	pygame.mixer.music.load(path)
	pygame.mixer.music.play()

A=MidiConverter(100,0,0,1)     #First create the class, then initialize it, then add notes as you want, then write them. 
A.initialize()
A.addNotes(GreenDolphin)
A.addNotes(GreenDolphinChords)
A.writeFiles("GreenDolphin1.mid")

Play("GreenDolphin1.mid")
for i in range(10):
	print("t=%d"%i)
	time.sleep(1)
