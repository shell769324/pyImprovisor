import random
"""
  Create a phrase
  @param chords: a list of Chord objects
  @param banks: the dictionary between a chord and a note
  @param rhythmBank: a rhythmBank
"""
BASS_VOLUMN_RATIO = 0.8
class Phrase:

  def __init__(self, chords, banks, rhythmBank, dynamics, genre, dur):
    self.chords = chords
    self.segments = [] # A list of list of note, where a note is a tuple
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
  Create a list of segments object using the field Harmony
  Set the nodes of all segments using harmony
  """
  def setSegments(self):
    # The first segment should generate notes based on the next note
    
    # The other segment should generate notes based on the previous segment and the next note

  """
  Set the first note of each segment
  TODOOOOOO: finish the bass line
  """
  def setPost(self):
    for chord in self.chords:
      self.segments.append([()])