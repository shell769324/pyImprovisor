import random
"""
  Create a phrase
  @param chords: a list of Chord objects
  @param banks: the dictionary between a chord and a note
  @param rhythmBank: a rhythmBank
"""
BASE_VOLUMN_RATIO = 0.8
class Phrase:

  def __init__(self, chords, banks, rhythmBank, dynamics, genre):
    self.chords = chords
    self.segments = [] # A list of list of note, where a note is a tuple
    self.setPost()
    self.banks = banks
    self.rhythmBank = rhythmBank
    self.dynamics = dynamics
    self.genre = genre

  """
  Set the basic rhythms of piano and bass, used by the first segment
  """
  def setBasicHarmony(self):
    shortest = 0
    for chord in self.chords:
      shortest = min(shortest, chord.dur)
    self.basicPianoRhythm = self.rhythmBank.generateRhythm(shortest, self.genre, False, self.dynamics)
    self.basicBaseRhythm = self.rhythmBank.generateRhythm(shortest, self.genre, True, self.dynamics * BASE_VOLUMN_RATIO)

  """
  Send back some variation of a certain rhythm pattern
  """
  def getVariation(selfs, original):
    int = random.randint(1, 2)
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
    return original

  # {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
  """
  Set the rhythm of all segments as in harmony
  """
  def setHarmony(self):
    return 42

  """
  Set the first note of each segment
  TODOOOOOO: finish the bass line
  """
  def setPost(self):
    for chord in self.chords:
      self.segments.append([()])