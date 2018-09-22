import random
import math

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

RhyBank = [[], EVEN1, EVEN2, EVEN3, MIX1, MIX2, TRIP1, DOT1, DURA1, DURA2, DURA3,
DURA4, DURA5, DURA6, DURA7, DURA8, PAUSE1, PAUSE2, PAUSE3, PAUSE4, SYNC1, PAUSE5,
PAUSE6, DURP1, DURP2, DURP3, DURP4]
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
"""
@test RhyBank and RhyDic
print(RhyBank[RhyDic["DURP4"]][0])
print(RhyBank[RhyDic["DURP4"]][23])
"""

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

	def bassBallad(self):
		randomizer = random.randint(1,100)
		if randomizer <= 57:
			return list(EVEN2)
		elif randomizer > 57 and randomizer <= 62:
			return list(EVEN3)
		elif randomizer > 62 and randomizer <= 67:
			return list(MIX1)
		elif randomizer > 67 and randomizer <= 80:
			return list(TRIP)
		elif randomizer > 80 and randomizer <= 85:
			return list(DURA2)
		elif randomizer > 85 and randomizer <= 90:
			return list(DURA3)
		else:
			return list(DURA6)
	def bassBop(self):
		rand

	def generateBass(self):
		if(GenDic[self.genre] == 4): #Bossa Nova
			self.bassBossa(self)
		else:
			Result = []
			n = round(1/self.duration)
			for index in range(1, n): 
				if (QuarterIndex(self, index) == 0):
					#this quarternote is the first quarternote of this chord
					randomizer = random.randint(1, 100)
					if randomizer <= 65:
						Result.append(list(EVEN2))
					elif randomizer > 65 and randomizer <= 95:
						Result.append(list(EVEN3))
					else:
						Result.append(list(MIX1))
				elif (QuarterIndex(self, index) == 1):
					#this quarternote is the 3rd/5th/7th quarternote of this chord
					randomizer = random.randint(1,100)
					if randomizer <= 80:
						Result.append(list(EVEN2))
					elif randomizer > 80 and randomizer <= 90:
						Result.append(list(EVEN3))
					else:
						Result.append(list(MIX1))
				else
					if (GenDic[self.genre] == 1): #Ballad
						Result.append(self.bassBallad)
					elif (GenDic[self.genre] == 2): #Bebop
						Result.append(self.bassBop)
					elif (GenDic[self.genre] == 3): #Blues
						Result.append(self.bassBlues)
			return Result 
#pseudocode ends

	def generateRhythm(self):
		if (self.line == 1):
			self.generateBass(self)
			return
		elif(self.line == 0):
			self.generatePiano(self)
			return
