import random

TRIAL = 3
class PianoSegment:
  def __init__(self, post, pitchType, rhythmBank, unitLength, genre, dyna, banks, chord):
    self.post = post
    self.pitchType = pitchType
    self.rhythmBank = rhythmBank
    self.rhythms = []
    self.intervals = []
    self.pitches = []
    self.attacks = []
    self.unitLength = unitLength
    self.genre = genre
    self.dynamics = dyna
    self.banks = banks
    self.chord = chord
    self.register = 60 # Default

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
  return a list of notes of block chords type
  """
  def blockChordNotes(self):
    return 42

  """
  return a list of notes of chordal notes type
  """
  def chordalNotes(self):
    return 42

  """
  return a list of notes of line notes type
  """
  def lineNotes(self):
    return 42

  """
  Set the notes of this segment
  """
  def setNotes(self, rhythm):
    count = 0
    self.rhythm = []
    self.pitch = []
    self.interval = []
    if(self.prev == None): # The first segment in a phrase

    else: # The second or other segment in a phrase

  """
  Finalize decisions
  """
  def finalize(self, prev=None, nextNote=-1):
    self.prev = prev
    self.nextNote = nextNote
    register =
    for i in range(TRIAL):
      self.setNotes(self.rhythmBank(self.unitLength, self.genre,
                                    False, self.dynamics, prev == None))
    scoreToIndex = []
    for i in range(len(self.intervals)):
      score = self.calculateScore(self.intervals[i], self.rhythms[i], self.pitches[i])
      scoreToIndex.append((score, i))
    scoreToIndex.sort(reverse=True)
    distribution = [0, 0, 0, 1, 1, 2]
    num = random.randint(0, 4)
    self.rhythm = self.rhythms[num]
    self.pitch = self.pitches[num]
    self.interval = self.intervals[num]
    self.attacks = self.attacks[num]