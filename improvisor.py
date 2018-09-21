import math
#from midiutil import MIDIFile
from bank import Bank
from chord import Chord
from phrase import Phrase

OCTAVE = 12

class Improvisor:

  def __init__(self):
    self.letters = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    #self.MyMIDI = MIDIFile(1, True, True, False, 1, 120, True)
    self.banks = {}
    self.chords = []
    self.phrases = []
    self.patterns = []
    self.createPatterns()
    self.tempo = 100

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
  Create a bank of rhythmic patterns
  """
  def createPatterns(self):
    return 42

  """
  Convert a list of chord symbols to a a list of Chord objects
  Store the list of Chords as chords
  @param chords: a list of chord symbols
  """
  def sheetIntepretor(self, chords):
    temp = []
    for (chord, dur) in chords:
      temp.append(Chord(chord, dur))
    self.chords = temp

  """
  Find out where each phrase begins and end
  Set phrases as a list of list of chords
  """
  def deconstructor(self):
    # Determine the content of each phrase
    chords = self.chords
    phrases = []
    sum = 0 # Once sum hits 2, append the phrase to phrases
    phrase = []
    for chord in chords:
      phrase.append(chord)
      sum += chord.dur
      if(math.isclose(sum, 2)):
        phrases.append(phrase)
        phrase = []
        sum = 0
      elif(math.isclose(sum, 4)):
        phrases.append(phrase)
        phrase = []
        sum = 0
      self.phrases = phrases

  """
  Expand the bank that maps chord name to an object that stores
  all chords, scales and licks that may be useful for improvisation
  """
  def expandBanks(self):
    for chord in self.chords:
      if(chord.name in self.banks):
        continue
      self.banks[chord.name] = Bank(chord)

  """
  Called after phrases are set.
  Add the posts of a phrase: the start and the end.
  Posts will be used to guide the generation of notes between them
  """
  def setPosts(self):
    return 42

  """
  Generate notes between posts
  """
  def fillPosts(selfs):
    return 42

  """
  Generate the midi file that only contains the chord
  """
  def pureChordsFile(self):
    return 42

  """
  Generate 1) a midi file that only contains the chords
           2) a midi file that solos over the chords
  @param chords: a list of tuples of chord name and duration
  @param tempo: tempo of the solo
  """
  def generator(self, chords, tempo = 100):
    self.tempo = tempo
    self.sheetIntepretor(chords)
    self.deconstructor()
    self.expandBanks()
    self.setPosts()

  def printChords(self):
    for chord in self.chords:
      print(chord.quality, end = " ")
    print("\n")

  def printPhrases(self):
    for phrase in self.phrases:
      for chord in phrase:
        print(chord.name, end = " ")
      print("")

def merge(chords, durs):
  res = []
  if(len(chords) != len(durs)):
    print(len(chords), len(durs))
    return None
  for i in range(len(chords)):
    res.append((chords[i], durs[i]))
  return res

improvisor = Improvisor()
chords1 = ["Am7", "D7", "GM7", "CM7", "F#m7b5"]
durs1 = [1, 1, 1, 1, 1]
chords2 = ["B7", "Em"]
durs2 = [1, 2]
chords3 = ["B7", "Em", "F#m7b5", "B7b9", "Em", "Am7", "D7", "GM7",
           "F#m7b5", "B7b9", "Em7", "A7", "Dm7", "G7", "F#m7b5", "B79", "Em"]
durs3 = [1, 2, 1, 1, 2, 1, 1, 2,
         1, 1, 0.5, 0.5, 0.5, 0.5, 1, 1, 2]
feed = merge(chords1 + chords2 + chords1 + chords3, durs1 + durs2 + durs1 + durs3)
improvisor.generator(feed, 100)
improvisor.printPhrases()