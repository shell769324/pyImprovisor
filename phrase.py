from __future__ import division
import random
import numpy
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
    self.setUnitLength()
    self.setPitchTypePiano()
    self.setPostPiano()
    self.setSegmentsPiano()
    self.connectSegments()

  """
  Set the unit length and unit count
  """
  def setUnitLength(self):
    shortest = 100
    sum = 0
    for chord in self.chords:
      shortest = min(shortest, chord.dur)
      sum += chord.dur
    self.unitLength = shortest ## The smallest unit
    self.unitCount = int(round(sum / shortest, 0)) ## The number of units

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
    num = random.uniform(0, 1)
    # Determine the pitch type to use
    if(num < 0.2):
      self.pianoPitchType = "BLOCK"
    elif(num < 0.55):
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
    i = 0
    currDur = 0
    while(i < len(self.chords)):
      chord = self.chords[i]
      res = chord.getClosestStable(prevPost)
      # Create a new segment with a post
      pianoSegments.append(PianoSegment(res, self.pianoPitchType, self.rhythmBank, self.unitLength,
                                        self.genre, self.dynamics, self.banks, chord))
      # Prep for the next iteration
      prevDeg = chord.degree
      prevPost = res
      currDur += self.unitLength
      if(numpy.isclose(currDur, chord.dur)):
        currDur = 0
        i = i + 1
    self.pianoSegments = pianoSegments
    self.lastEnd = res + 12 if res <= 60 else res

  """
  For the piano part
  Create a list of segments object using the field Harmony
  Set the nodes of all segments using harmony
  """
  def setSegmentsPiano(self):
    pianoSegments = self.pianoSegments
    pianoSegments[0].finalize(None, pianoSegments[1].post)
    print(self.unitCount)
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