import random
from segment import Segment
"""
  Create a phrase
  @param chords: a list of Chord objects
  @param banks: the dictionary between a chord and a note
  @param rhythmBank: a rhythmBank
"""
BASS_VOLUMN_RATIO = 0.8
LINE_BASIC = {1:5, 2:7, 3:8, 4:10}
LINE_FREQ = lambda x : LINE_BASIC[x] + random.randint(-2, 2)
CHORDAL_BASIC = {1:7, 2:8, 3:8, 4:7}
CHORDAL_FREQ = lambda x : CHORDAL_BASIC[x] + random.randint(-2, 2)
BLOCK_BASIC = {1:10, 2:7, 3:3, 4:2}
BLOCK_FREQ = lambda x : BLOCK_BASIC[x] + random.randint(-2, 2)

class Phrase:

  def __init__(self, chords, banks, rhythmBank, dynamics, genre, dur):
    self.chords = chords
    self.setPost()
    self.banks = banks
    self.rhythmBank = rhythmBank
    self.dynamics = dynamics
    self.genre = genre
    self.dur = dur

  """
  Set the basic rhythms of piano and bass, used by the first segment
  Set the unit length
  """
  def setBasicHarmony(self):
    shortest = 0
    for chord in self.chords:
      shortest = min(shortest, chord.dur)
    self.unitLength = shortest
    self.basicPianoRhythm = self.rhythmBank.generateRhythm(shortest, self.genre, False, self.dynamics)
    self.basicBassRhythm = self.rhythmBank.generateRhythm(shortest, self.genre, True, self.dynamics * BASS_VOLUMN_RATIO)

  """
  Send back some variation of a certain rhythm pattern
  TODO: to increase randomness
  """
  def getVariation(selfs, original):
    int = random.randint(1, 6)
    if(int == 1):
      # Delte one note
      for i in range(len(original)):
        if(original[i] > 0):
          for j in range(i, len(original)):
            original[i] = 0 # Set all trailing suspending cell to zero
    elif(int == 2):
      # Merge two adjacent notes
      found = False
      for i in range(len(original)):
        if(original[i] > 0):
          if(found): # If attach has been found, this is the second one
            original[i] = -1 # Change it to a connected line
            break
          else:
            found = True
    elif(int == 3):
      # Shift left by one eight note
      temp = [0] * len(original)
      for i in range(48, len(original)):
        temp[i] = original[i - 48]
      original = temp
    elif(int == 4):
      # Shift right by one eight note
      temp = [0] * len(original)
      for i in range(0, len(original) - 48):
        temp[i] = original[i + 48]
      original = temp
    return original

  # {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
  """
  Set the rhythm of all segments as in harmony
  """
  def setHarmony(self):
    pianoHarmony = []
    bassHarmony = []
    for i in range(self.dur // self.unitLength):
      pianoHarmony.append(self.getVariation(self.basicPianoRhythm))
      bassHarmony.append(self.getVariation(self.basicBassRhythm))
    self.pianoHarmony = pianoHarmony
    self.bassHarmony = bassHarmony

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
  Set the basic pitch type to use
  including line, chordal notes and block chords
  line should have the highest frequency overall, followed by chordal notes
  and block chords should occur from time to time
  Decision is based on the density of the basic rhythm field
  """
  def setPitchTypePiano(self):
    rou = self.calculateDensity(self.basicPianoRhythm)
    blockBid = BLOCK_FREQ(rou)
    chordalBid = CHORDAL_FREQ(rou)
    lineBid = LINE_FREQ(rou)
    if(blockBid > chordalBid and blockBid > lineBid):
      self.pianoPitchType = "BLOCK"
    elif(chordalBid > lineBid):
      self.pianoPitchType = "CHORDAL"
    else:
      self.pianoPitchType = "LINE"

  """
  Set the first note of each segment
  TODOOOOOO: finish the bass line
  """
  def setPost(self):
    segments = []
    typeOption1 = ["root", "third"]
    typeOption2 = ["fifth", "seventh"]
    typeOption3 = ["second"]
    typeOption = typeOption1 * 3 + typeOption2 * 2 + typeOption3
    num = random.randint(0, len(typeOption) - 1)
    for chord in self.chords:
      segments.append(Segment(chord.getPost(typeOption[num])))
    self.segments = segments

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
  def scorePhrase(self, prev, new, nextNote):
    return 42

  """
  For the piano part
  Create a list of segments object using the field Harmony
  Set the nodes of all segments using harmony
  """
  def setSegmentsPiano(self):
    segments = self.segments
    if(self.pianoPitchType == "BLOCK"):
      segments.append(Segment())
      a = 42
    elif(self.pianoPitchType == "CHORDAL"):
      a = 42
    else:
      a = 42
    return 42