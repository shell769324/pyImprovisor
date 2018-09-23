from __future__ import division
import random
import math
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
BLOCK_BASIC = {1:10, 2:7, 3:3, 4:0}
BLOCK_FREQ = lambda x : BLOCK_BASIC[x] + random.randint(-2, 2)

class Phrase:

  def __init__(self, chords, banks, rhythmBank, dynamics, genre, dur, lastEnd):
    self.chords = chords
    self.banks = banks
    self.rhythmBank = rhythmBank
    self.dynamics = dynamics
    self.genre = genre
    self.dur = dur
    self.lastEnd = lastEnd
    self.setBasicRhythm()
    self.setPitchTypePiano()
    self.setPostPiano()
    self.setSegmentsPiano()
    self.connectSegments()

  """
  Set the basic rhythms of piano and bass, used by the first segment
  Set the unit length
  """
  def setBasicRhythm(self):
    shortest = 100
    sum = 0
    for chord in self.chords:
      shortest = min(shortest, chord.dur)
      sum += chord.dur
    self.unitLength = shortest ## The smallest unit
    self.unitCount = int(round(sum / shortest, 0)) ## The number of units
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
    return int(round(count / (len(rhythm) / 24), 0))

  """
  Set the basic pitch type to use
  including line, chordal notes and block chords
  line should have the highest frequency overall, followed by chordal notes
  and block chords should occur from time to time
  Decision is based on the density of the basic rhythm field
  """
  def setPitchTypePiano(self):
    rou = self.calculateDensity(self.basicPianoRhythm)
    # Calculate the bid of each pitch type
    blockBid = BLOCK_FREQ(rou)
    chordalBid = CHORDAL_FREQ(rou)
    lineBid = LINE_FREQ(rou)
    # Determine the pitch type to use
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
    # Determine which relative degree will be the post
    typeOption1 = ["root", "third"]
    typeOption2 = ["fifth", "seventh"]
    typeOption3 = ["second"]
    typeOption = typeOption1 * 3 + typeOption2 * 2 + typeOption3
    num = random.randint(0, len(typeOption) - 1)
    # Relative degree of the [0, 12) of the previous chord
    prevDeg = self.chords[0].degree
    # The absolute degree of the previous chord
    prevPost = self.chords[0].getNote(typeOption[num], self.lastEnd, False)
    res = 0
    for chord in self.chords:
      # Two options for the next post
      higher = chord.getNote(typeOption[num], prevPost, False)
      lower = chord.getNote(typeOption[num], prevPost, True)
      res = 0 # The actual absolute degree of the post of the current segment
      if(higher >= 84):
        res = lower
      elif(self.pianoPitchType == "BLOCK" and lower <= 60 or lower <= 48):
        res = higher
      else:
        res = higher if (random.randint(0, 1) == 1) else lower
      # Create a new segment with a post
      pianoSegments.append(PianoSegment(res, self.pianoPitchType, self.rhythmBank, self.unitLength,
                                        self.genre, self.dynamics, self.banks, chord))
      # Prep for the next iteration
      prevDeg = chord.degree
      prevPost = res
    self.pianoSegments = pianoSegments
    self.lastEnd = res

  """
  For the piano part
  Create a list of segments object using the field Harmony
  Set the nodes of all segments using harmony
  """
  def setSegmentsPiano(self):
    pianoSegments = self.pianoSegments
    pianoSegments[0].finalize(None, pianoSegments[1].post)
    for i in range(1, self.unitCount):
      nextNote = pianoSegments[i + 1].post if i != self.unitCount - 1 else -1
      pianoSegments[i].finalize(pianoSegments[i - 1], nextNote)

  """
  Connect all segments together into a tuple of
  pitch, relative time, duration and volume
  """
  def connectSegments(self):
    connected = []
    currT = 0
    for seg in self.pianoSegments:
      temp = seg.res
      local = 0
      for i in range(len(temp)):
        connected.append([temp[i][0], temp[i][1] + currT, temp[i][2], temp[i][3]])
      currT += int(round(self.unitLength * 480, 0))
    self.res = connected