import random

# with attack at the begining of this 1/4 beat
#4 * 1/16
EVEN1 = [2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
#2 * 1/8
EVEN2 = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#1 * 1/4
EVEN3 = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#1/8 1/16 1/16
MIX1  = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
#1/16 1/16 1/8
MIX2  = [2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#trip
TRIP1 = [2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
#doted
DOT1  = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
#DOT2  = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1]
#DOT3  = [2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#DOT4  = [2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1]
#DOT5  = [2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1]


# no attack at the beginning of this beat
# even dura
DURA1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
DURA2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
DURA3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
DURA4 = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
DURA5 = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
#trip dura
DURA6 = [1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
#dot dura
DURA7 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
DURA8 = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# pause
# trip pause upbeat
PAUSE1 = [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
# pause1/8 + 1/8
PAUSE2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# pause1/8 + 1/16 + 1/16
PAUSE3 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
# even pause
PAUSE4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#Syncopation
SYNC1 = [0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# 1/16 + 1/16 + pause1/8
PAUSE5 = [2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 1/8 + pause1/8
PAUSE6 = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# mix of prolonged duration and pause
DURP1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DURP2 = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DURP3 = [1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
DURP4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

GenDic = {"Ballad":1, "Bebop":2, "Blues":3, "Bossa Nova":4}

"""
1-15: DOES NOT START WITH PAUSE
16-20: START WITH PAUSE
21-26: END WITH PAUSE
1-7, 21, 22: START WITH ATTACK
"""

RhyDic = {"EVEN1":1, "EVEN2":2, "EVEN3":3, "MIX1":4, "MIX2":5, "TRIP1":6, "DOT1":7,
 "DURA1":8, "DURA2":9, "DURA3":10, "DURA4":11, "DURA5":12, "DURA6":13,
"DURA7":14, "DURA8":15, "PAUSE1":16, "PAUSE2":17, "PAUSE3":18, "PAUSE4":19,"SYNC1":20,
 "PAUSE5":21, "PAUSE6":22, "DURP1":23, "DURP2":24, "DURP3":25, "DURP4":26}



class rhythm:
	def __init__(self, Duration, Genre, Line, Dynamix):
		#Line: True-Bass; False-Piano
		self.genre = Genre #string
		self.duration = Duration #double
		self.line = Line #boolean
		self.dynamix = Dynamix #int
		self.generateRhythm(self)

	def QuarterIndex(self, index):
		if (self.duration == 1):
			return 0 #First quarternote of this chord-phrase
		elif (index % 2 == 1):
			return 1 #Odd quarternote
		elif (index % 2 == 0):
			return 2 #Even quarternote

	def generatePiano(self):

	def bassBossa(self):

	def generateBass(self):
		if(GenDic[self.genre] == 4): #Bossa Nova
			self.bassBossa(self)
		else:
			Result = []
			for (every quarternote in this duration)
				if (QuarterIndex < 2)
				Result.append(randomized even stuff)
				else
					if (GenDic[self.genre] == 1): #Ballad
						Result.append(randomized even and trip stuff)
					elif (GenDic[self.genre] == 2): #Bebop
						Result.append(randomized even and doted stuff)
					elif (GenDic[self.genre] == 3): #Blues
						Result.append(randomize even stuff)
			return Result 


	def generateRhythm(self):
		if (self.line == 1):
			self.generateBass(self)
			return
		elif(self.line == 0):
			self.generatePiano(self)
			return
