import random
from pianoSegment import PianoSegment
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

  def __init__(self, chords, banks, rhythmBank, dynamics, genre, dur, register):
    self.chords = chords
    self.banks = banks
    self.rhythmBank = rhythmBank
    self.dynamics = dynamics
    self.genre = genre
    self.dur = dur
    self.setBasicHarmony()
    self.setPitchTypePiano()
    self.setPostPiano()
    self.setSegmentsPiano()
    self.connectSegments()
    self.register = register

  """
  Set the basic rhythms of piano and bass, used by the first segment
  Set the unit length
  """
  def setBasicHarmony(self):
    shortest = 0
    for chord in self.chords:
      shortest = min(shortest, chord.dur)
    self.unitLength = shortest ## The number of bar
    self.basicPianoRhythm = self.rhythmBank.generateRhythm(shortest, self.genre, False, self.dynamics, True)
    self.basicBassRhythm = self.rhythmBank.generateRhythm(shortest, self.genre,
                                                          True, self.dynamics * BASS_VOLUMN_RATIO, True)

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
  def setPostPiano(self):
    pianoSegments = []
    typeOption1 = ["root", "third"]
    typeOption2 = ["fifth", "seventh"]
    typeOption3 = ["second"]
    typeOption = typeOption1 * 3 + typeOption2 * 2 + typeOption3
    num = random.randint(0, len(typeOption) - 1)
    for chord in self.chords:
      pianoSegments.append(PianoSegment((chord.getPost(typeOption[num]) + chord.degree) % 12,
                                        self.pianoPitchType, self.rhythmBank, self.unitLength,
                                        self.genre, self.dynamics, self.banks, chord))
      # Mod 12 to make things standard
    self.pianoSegments = pianoSegments


  """
  For the piano part
  Create a list of segments object using the field Harmony
  Set the nodes of all segments using harmony
  """
  def setSegmentsPiano(self):
    pianoSegments = self.pianoSegments
    pianoSegments[0].finalize(None, pianoSegments[1].post)
    for i in range(1, self.dur // self.unitLength):
      nextNote = pianoSegments[i + 1].post if i != self.dur//self.unitLength - 1 else -1
      pianoSegments[i].finalize(pianoSegments[i - 1], nextNote)

  """
  Connect all segments together into a tuple of
  pitch, relative time, duration and volume
  """
  def connectSegments(self):
    return 42