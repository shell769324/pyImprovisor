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
#correlation list
Correlation = []
row = []
Correlation += [row]
for i in range(1, 27):
	row = []
	row.append(0.0)
	for j in range(1, 27):
		if RhyBank[i][23] == 0 and RhyBank[j][0] == 1: #Pause to Tie cannot occur
			row.append(0.0)
			continue
		if i <= 6 and (j <= 6 or j == 8 or j == 23):
			row.append(0.95)
		else:
			row.append(0.7)
	Correlation += [row]

"""
test Correlation
for i in range(1, 26):
	for j in range(1, 26):
		print(Correlation[i][j])
"""

class rhythm:
	def __init__(self):
		self.hasInit = False

	def QuarterIndex(self, index):
		if (index == 1):
			return 0 #First quarternote of this chord-phrase
		elif (index % 2 == 1):
			return 1 #Odd quarternote
		elif (index % 2 == 0):
			return 2 #Even quarternote

	def assignDynamix(self, original):
		#adjust dynamix of attacks according to upbeat/downbeat
		assigned = []
		original2 = []
		for i in original:
			for j in i:
				original2.append(j)

		for i in range(len(original2)):
			if original2[i] == 0:
				assigned.append(0)
			elif original2[i] == 1:
				assigned.append(-1)
			elif original2[i] == 2:
				dyn = self.dynamix
				if i % 12 == 0:
					dyn += 3
				if i % 24 == 0:
					dyn += 3
				if dyn > 127:
					assigned.append(127)
				else:
					assigned.append(dyn)

		return assigned


	def generatePiano(self):
		Result = [] # the actual rhythm
		resultNum = []
		resultNum = [0] * 27
		# if this call is for BR, whether the quarternotes appeared in the BR

		n = int(round((self.duration * 4), 0))
		if(self.br == True):
			self.cor = list(Correlation)
			#if this is for BR, initialize self.cor
		prev = 19
		for i in range(1, n + 1):
			if(self.QuarterIndex(i) == 0):
				prev = 19

			#weighted randomization
			summation = 0.0
			for j in range(1, 27):
				summation += self.cor[prev][j]
			normalize = []
			normalize.append(0.0)
			cumulative = []
			cumulative.append(0.0)
			for k in range(1, 27):
				normalize.append(self.cor[prev][k]/summation)
				cumulative.append(cumulative[k-1] + normalize[k])

					#randomize according to the row of self.cor[prev]
					#assign the result of randomization to prev
			randomizer = random.uniform(0, 1)
			k = 1
			while(cumulative[k] < randomizer):
				k += 1
			k %= 27
			#assert k is the index of the randomized result
			resultNum[k] = 1
			prev = k
			Result.append(RhyBank[k])
			#print(Result)
		if(self.br == True):
			#decrease the numbers in columns (column index not in resultNum) in self.cor
			for i in range(1, 27):
				for j in range(1, 27):
					if resultNum[j] == 0:
						self.cor[i][j] *= self.cor[i][j]
		#print(Result)
		return Result



	def bassBossa(self):
		Res = []
		n = int(round(self.duration * 0.25, 0))
		for index in range(1, n + 1):
			if(self.QuarterIndex(index) == 0):
				Res += list(DOT1)
			elif (self.QuarterIndex(index) == 1):
				randomizer = random.randint(1, 100)
				if randomizer <= 25:
					Res += list(DURA2)
				elif randomizer > 25 and randomizer <= 50:
					Res += list(PAUSE2)
				elif randomizer > 50 and randomizer <= 75:
					Res += list(DURA3)
				else:
					Res += list(DURA7)
			elif(self.QuarterIndex(index) == 2):
				randomizer = random.randint(1, 100)
				if randomizer <= 70:
					Res += list(DOT1)
				elif randomizer > 70 and randomizer <= 90:
					Res += list(MIX1)
				else:
					Res += list(EVEN2)
		return Res

	def bassBallad(self):
		randomizer = random.randint(1, 100)
		if randomizer <= 57:
			return list(EVEN2)
		elif randomizer > 57 and randomizer <= 62:
			return list(EVEN3)
		elif randomizer > 62 and randomizer <= 67:
			return list(MIX1)
		elif randomizer > 67 and randomizer <= 80:
			return list(TRIP1)
		elif randomizer > 80 and randomizer <= 85:
			return list(DURA2)
		elif randomizer > 85 and randomizer <= 90:
			return list(DURA3)
		else:
			return list(DURA6)
	def bassBop(self):
		randomizer = random.randint(1, 100)
		if randomizer <= 57:
			return list(EVEN2)
		elif randomizer > 57 and randomizer <= 62:
			return list(EVEN3)
		elif randomizer > 62 and randomizer <= 67:
			return list(MIX1)
		elif randomizer > 67 and randomizer <= 80:
			return list(DOT1)
		elif randomizer > 80 and randomizer <= 90:
			return list(DURA2)
		elif randomizer > 90 and randomizer <= 95:
			return list(DURA3)
		else:
			return list(DURA7)
	def bassBlues(self):
		Result = []
		randomizer = random.randint(1, 100)
		if randomizer <= 70:
			#return [list(EVEN2)]
			Result += list(EVEN2)
		elif randomizer > 70 and randomizer <= 80:
			#return [list(EVEN3)]
			Result += list(EVEN3)
		elif randomizer > 80 and randomizer <= 85:
			#return [list(MIX1)]
			Result += list(MIX1)
		elif randomizer > 85 and randomizer <= 90:
			#return [list(DURA1)]
			Result += list(DURA1)
		elif randomizer > 90 and randomizer <= 95:
			#return [list(DURA2)]
			Result += list(DURA2)
		else:
			#return [list(PAUSE2)]
			Result += list(PAUSE2)
		return Result

	def generateBass(self):
		Result = []
		if(GenDic[self.genre] == 4): #Bossa Nova
			Result.append(self.bassBossa())
		else:
			n = int(round(self.duration * 4, 0))

			for index in range(1, n + 1): 
				if (self.QuarterIndex(index) == 0):
					#this quarternote is the first quarternote of this chord
					randomizer = random.randint(1, 100)
					if randomizer <= 65:
						Result.append(list(EVEN2))
					elif randomizer > 65 and randomizer <= 95:
						Result.append(list(EVEN3))
					else:
						Result.append(list(MIX1))
				elif (self.QuarterIndex(index) == 1):
					#this quarternote is the 3rd/5th/7th quarternote of this chord
					randomizer = random.randint(1,100)
					if randomizer <= 80:
						Result.append(list(EVEN2))
					elif randomizer > 80 and randomizer <= 90:
						Result.append(list(EVEN3))
					else:
						Result.append(list(MIX1))
				else:
					#not downbeat
					if (GenDic[self.genre] == 1): #Ballad
						Result.append(self.bassBallad())
					elif (GenDic[self.genre] == 2): #Bebop
						Result.append(self.bassBop())
					elif (GenDic[self.genre] == 3): #Blues
						Result.append(self.bassBlues())
		return Result 

	def generateRhythmWrapper(self):
		if (self.line == 1):
			return self.assignDynamix(self.generateBass())
		elif(self.line == 0):
			return self.assignDynamix(self.generatePiano())

	def generateRhythm(self, Duration, Genre, Line, Dynamix, BR):
		# Line: True-Bass; False-Piano
		self.genre = Genre  # string
		self.dynamix = Dynamix  # int
		self.duration = Duration  # double
		self.br = BR  # boolean
		self.line = Line  # boolean
		if(not self.hasInit):
			self.cor = list(Correlation)
		if(BR):
			self.cor = list(Correlation)
		return self.generateRhythmWrapper()