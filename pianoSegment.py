import random
import bank

TRIAL = 3
class PianoSegment:
  def __init__(self, post, pitchType, rhythmBank, unitLength, genre, dyna, banks, chord):
    self.post = post
    self.pitchType = "BLOCK"
    self.rhythmBank = rhythmBank
    self.rhythms = []
    self.attacks = []
    self.unitLength = unitLength
    self.genre = genre
    self.dynamics = dyna
    self.banks = banks
    self.chord = chord

  """
  Calculate the density of a rhythm pattern
  @return: the density of a rhythm
  """
  def calculateDensity(self, rhythm):
    count = 0
    for i in range(len(rhythm)):
      if (rhythm[i] > 0):
        count += 1
    return count

  """
  Calculate interval similarity
  """
  def calculateIntvSim(self, intv):
    return 42

  """
  Calculate rhythm similarity
  """
  def calculateRhySim(self, rhy):
    attack = [0] * self.unitLength * 96 * 4
    prevMag = 0
    currMag  = 0
    for i in range(len(rhy)):
      if(rhy[i] > 0):
        attack[i] = 1
        currMag +=1
      if(self.prev.rhythm[i] > 0):
        prevMag += 1
    top = 0
    for i in range(len(self.prev.attack)):
      top += attack[i] * self.prev.attack[i]
    self.attacks.append(attack)
    return top / (prevMag * currMag) ** 0.5

  """
  Check stable notes and key notes in downbeats
  """
  def countDownBeatsNotes(self, pit):
    return 42


  """
  Score the new phrase based on
  1) The similarity of rhythmic pattern with the previous phrase
  2) The similarity of interval with the previous phrase
  3) The number of stables notes and key nodes on the down beat
  4) Connection with the starting pitch of the next phrase
  @param prev: the previous segment
  @param new: the next phrase
  @param nextNote: the post of the next segment
  @return: the score of the new phrase
  """
  def calculateScore(self, intv, rhy, pit):
    return self.calculateIntvSim(intv) + self.calculateRhySim(rhy) + self.countDownBeatsNotes(pit)

  """
  Get the nth note time and its duration
  @param rhythm: the rhythm int list
  @return a list of tuple (time, duration) where 1/4 note = 120
  """
  def getAllNoteTime(self, rhythm):
    res = []
    i = 0
    while(i < len(rhythm)):
      if(rhythm[i] > 0):
        start = i
        i += 1
        while(i < len(rhythm) and rhythm[i - 1] == rhythm[i]):
          i += 1
        res.append((start * 120 / 96, (i - start) * 120 / 96, rhythm[start]))
        i -= 1
      i += 1
    return res

  """
  return a list of notes of block chords type
  """
  def blockChordNotes(self, rhythm):
    chord = self.chord
    register = ((self.post - 12) // 12) * 12 # the register at least one octave lower than the top
    block = []
    block.append((chord.getPost("third") + chord.degree()) % 12 + register)
    block.append((chord.getPost("fifth") + chord.degree()) % 12 + register)
    res = []
    if("7" in chord.quality):
      block.append((chord.getPost("seventh") + chord.degree()) % 12 + register)
    noteTime = self.getAllNoteTime(rhythm)
    for i in range(len(noteTime)):
      for j in range(len(block)):
        res.append((block[i], noteTime[i][0], noteTime[i][1], noteTime[i][2]))
    return res

  """
  return a list of notes of chordal notes type
  @param rhythm: the rhythm
  """
  def chordalNotes(self, rhythm):
    chord = self.chord
    canUse = self.banks[chord.name]
    rightLength = []
    noteTime = self.getAllNoteTime(rhythm)
    for i in range(len(canUse.chords)):
      if(len(canUse.chords[i]) == len(noteTime)):
        rightLength.append(i)


  """
  return a list of notes of line notes type
  """

  def lineNotes(self,rhythm):
    a=self.nextNote
    b=self.post
    canUse = self.banks[self.chord.name]
    notes=getAllNoteTime(rhythm)

    listTemp=[]
    for i in [-2,-1,0,1,2]:
      for item in canUse: 
        listTemp.append(item+i*12)
    if b not in listTemp:
      if b-1 in listTemp:
        b=b-1
      else: b=b+1
    aLoc,bLoc=listTemp.index(a),listTemp.index(b)
    DNCU=bLoc-aLoc

    if DNCU > 0: GG=1
    else: GG=-1 
    
    if abs(DNCU) >= len(notes):
        for i in range(len(notes)):
            notes[i]=(listTemp[aLoc+GG*i],notes[i][0],notes[i][1],notes[i][2])
        return notes
        
    else:
        if len(notes)-abs(DNCU) ==1:
            for i in range(len(notes)-1):
                notes[i]=(listTemp[aLoc+GG*i],notes[i][0],notes[i][1],notes[i][2])
            notes[-1]=(listTemp[bLoc+GG*1],notes[-1][0],notes[-1][1],notes[-1][2])
            return notes
            
        elif len(notes)-abs(DNCU)==2:
            for i in range(len(notes)-1):
                notes[i]=(listTemp[aLoc+GG*i],notes[i][0],notes[i][1],notes[i][2])
            notes[-1]=(listTemp[bLoc+GG*1],notes[-1][0],notes[-1][1],notes[-1][2])
            return notes
            
        elif len(notes)-abs(DNCU)==3:
            for i in range(len(notes)-2):
                notes[i]=(listTemp[aLoc+GG*i],notes[i][0],notes[i][1],notes[i][2])
            notes[-1]=(listTemp[bLoc-GG*1],notes[-1][0],notes[-1][1],notes[-1][2])
            notes[-2]=(listTemp[bLoc+GG*1],notes[-1][0],notes[-2][1],notes[-2][2])
            return notes
        
        elif len(notes)-abs(DNCU)==4:
            for i in range(len(notes)-3):
                notes[i]=(listTemp[aLoc+GG*i],notes[i][0],notes[i][1],notes[i][2])
            notes[-1]=(listTemp[bLoc-GG*1],notes[-1][0],notes[-1][1],notes[-1][2])
            notes[-2]=(listTemp[bLoc],notes[-1][0],notes[-2][1],notes[-2][2])
            notes[-3]=(listTemp[bLoc+GG*1],notes[-3][0],notes[-3][1],notes[-3][2])
            return notes
            
        elif len(notes)-abs(DNCU)==5:
            for i in range(len(notes)-3):
                notes[i]=(listTemp[aLoc+GG*i],notes[i][0],notes[i][1],notes[i][2])
            notes[-1]=(listTemp[bLoc-GG*1],notes[-1][0],notes[-1][1],notes[-1][2])
            notes[-2]=(listTemp[bLoc],notes[-1][0],notes[-2][1],notes[-2][2])
            notes[-3]=(listTemp[bLoc+GG*1],notes[-3][0],notes[-3][1],notes[-3][2])
            notes[-4]=(listTemp[bLoc+GG*1],notes[-4][0],notes[-4][1],notes[-4][2])
            return notes
        
        elif len(notes)-abs(DNCU)==6:
            for i in range(len(notes)-3):
                notes[i]=(listTemp[aLoc+GG*i],notes[i][0],notes[i][1],notes[i][2])
            notes[-1]=(listTemp[bLoc-GG*1],notes[-1][0],notes[-1][1],notes[-1][2])
            notes[-2]=(listTemp[bLoc],notes[-1][0],notes[-2][1],notes[-2][2])
            notes[-3]=(listTemp[bLoc+GG*1],notes[-3][0],notes[-3][1],notes[-3][2])
            notes[-4]=(listTemp[bLoc+GG*1],notes[-4][0],notes[-4][1],notes[-4][2])
            notes[-5]=(listTemp[bLoc+GG*1],notes[-5][0],notes[-5][1],notes[-5][2])
            return notes
            
        elif len(notes)-abs(DNCU)==7:
            for i in range(len(notes)-3):
                notes[i]=(listTemp[aLoc+GG*i],notes[i][0],notes[i][1],notes[i][2])
            notes[-1]=(listTemp[bLoc-GG*1],notes[-1][0],notes[-1][1],notes[-1][2])
            notes[-2]=(listTemp[bLoc],notes[-1][0],notes[-2][1],notes[-2][2])
            notes[-3]=(listTemp[bLoc+GG*1],notes[-3][0],notes[-3][1],notes[-3][2])
            notes[-4]=(listTemp[bLoc+GG*1],notes[-4][0],notes[-4][1],notes[-4][2])
            notes[-5]=(listTemp[bLoc+GG*1],notes[-5][0],notes[-5][1],notes[-5][2])
            notes[-6]=(listTemp[bLoc+GG*1],notes[-6][0],notes[-6][1],notes[-6][2])  
            return notes
        
        else:
            for i in range(len(notes)):
                notes[i]=(listTemp[aLoc+GG*i],notes[i][0],notes[i][1],notes[i][2])
            return notes




  """
  Set the notes of this segment
  """
  def setNotes(self, rhythm):
    count = 0
    self.rhythm = rhythm
    self.pitch = []
    self.interval = []
    if(self.prev == None): # The first segment in a phrase
      if(self.pitchType == "BLOCK"):
        return 42
    else: # The second or other segment in a phrase
      return 42
  """
  Finalize decisions
  """
  def finalize(self, prev=None, nextNote=-1):
    self.prev = prev
    self.nextNote = nextNote
    if(self.pitchType == "BLOCK"):
      self.res = self.blockChordNotes(self.rhythmBank(self.unitLength, self.genre, False,
                                                      self.dynamics, True))