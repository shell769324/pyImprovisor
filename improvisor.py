import math
#from midiutil import MIDIFile
from bank import Bank
from chord import Chord
from phrase import Phrase
import numpy
from Rhythm import rhythm

OCTAVE = 12

class Improvisor:

  def __init__(self):
    self.letters = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    #self.MyMIDI = MIDIFile(1, True, True, False, 1, 120, True)
    self.banks = {} # The bank of notes corresponding to a specific chord
    self.rhythmBank = rhythm()
    self.chords = []
    self.phrases = []
    self.patterns = []
    self.tempo = 100
    self.genre = "Bebop"

  """
  Return the pitch of a note symbol
  @param s: the note symbol
  @return: the pitch represented by an integer in [0, 128)
  """
  def GN(self, s):
    letter = s[0]
    num = s[1] if len(s) == 2 else s[2]
    tweak = 0 if len(s) == 2 else (-1 if s[1] == 'b' else 1)
    return self.letters[letter] + (int(num) + 1) * OCTAVE + tweak

  """
  Return a list of pitches after transposition
  @param notes: the list of pitches
  @param interval: transpose by that number of semitone
  @param up: tranpose upward
  @return: the list of notes after tranposition
  """
  def transpose(self, notes, interval, up=True):
    result = [0] * len(notes)
    for i in range(len(notes)):
      result[i] = notes[i] + interval * (1 if up else -1)
    return result

  """
  Convert a list of chord symbols to a a list of Chord objects
  Store the list of chords as chords
  @param chords: a list of chord symbols
  """
  def sheetIntepretor(self, chords):
    print(chords)
    temp = []
    for i in range(len(chords)):
      (chord, dur) = chords[i]
      temp.append(Chord(chord, dur))
    self.chords = temp

  """
  Find out where each phrase begins and end
  Set phrases as a list of list of chords
  @param dynamics: the average dynamics value
  """
  def deconstructor(self, dynamics=90):
    # Determine the content of each phrase
    chords = self.chords
    phrases = []
    sum = 0 # Once sum hits 2, append the phrase to phrases
    chordsInPhrase = []
    prevPost = 60
    for i in range(len(chords)):
      chrd = chords[i]
      chordsInPhrase.append(chrd)
      sum += chrd.dur
      print(sum)
      if(numpy.isclose(sum, 1) and len(chordsInPhrase) >= 3):
        print("here1")
        phrases.append(Phrase(chordsInPhrase, self.banks, self.rhythmBank,
                              dynamics, self.genre, 1, prevPost))
        prevPost = phrases[-1].lastEnd
        chordsInPhrase = []
        sum = 0
      elif(numpy.isclose(sum, 2) and len(chordsInPhrase) >= 2):
        phrases.append(Phrase(chordsInPhrase, self.banks, self.rhythmBank,
                              dynamics, self.genre, 2, prevPost))
        prevPost = phrases[-1].lastEnd
        chordsInPhrase = []
        sum = 0
      elif(numpy.isclose(sum, 4)):
        phrases.append(Phrase(chordsInPhrase, self.banks, self.rhythmBank,
                              dynamics, self.genre, 4, prevPost))
        prevPost = phrases[-1].lastEnd
        chordsInPhrase = []
        sum = 0
    self.phrases = phrases

  """
  Connect all phrases into one list of tuple
  @return the list of tuple
  """
  def connect(self):
    connected = []
    currT = 0
    for phrase in self.phrases:
      temp = phrase.res
      local = 0
      for i in range(len(temp)):
        connected.append([temp[i][0], temp[i][1] + currT, temp[i][2], temp[i][3]])
      currT += temp[-1][1] + temp[-1][2]
    print(connected)
    return connected

  """
  Expand the bank that maps chord name to an object that stores
  all chords, scales and licks that may be useful for improvisation
  """
  def expandBanks(self):
    for chrd in self.chords:
      if(chrd.name in self.banks):
        continue
      self.banks[chrd.name] = Bank(chrd)

  """
  Generate the midi file that only contains the chord
  """
  def purechordsFile(self):
    return 42

  """
  Generate 1) a midi file that only contains the chords
           2) a midi file that solos over the chords
  @param chords: a list of tuples of chord name and duration
  @param tempo: tempo of the solo
  @param genre: a string specifying the genre
  """
  def generator(self, chords, tempo=100, genre="bebop"):
    print(type(chords))
    self.tempo = tempo
    self.genre = genre
    self.sheetIntepretor(chords)
    self.expandBanks()
    self.deconstructor()
    self.connect()

  def printchords(self):
    for chrd in self.chords:
      print(chrd.quality + " ")
    print("\n")

  def printPhrases(self):
    for phrase in self.phrases:
      for chrd in phrase:
        print(chrd.name + " ")
      print("")

def merge(chords, durs):
  res = []
  if(len(chords) != len(durs)):
    print(len(chords), len(durs))
    return None
  for i in range(len(chords)):
    res.append((chords[i], durs[i]))
  return res