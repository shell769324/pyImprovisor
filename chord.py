OCTAVE = 12
class Chord:
  def __init__(self, name, dur):
    self.name = name
    self.dur = dur
    self.setQuality()
    self.setDegree()
    self.setKeyNotes()
    self.setDegDict()

  """
  Set the quality of the chord by its name
  """
  def setQuality(self):
    name = self.name # Save typing
    if("m7b5" in name):
      self.quality = "m7b5" # half diminished seventh chord
    elif("m" in name):
      self.quality = "m7" # Minor seventh chord
    elif("M6" in name):
      self.quality = "M" # Major sixth chord
    elif("M" in name):
      self.quality = "M7" # Major seventh chord
    elif(len(name) == 1 or len(name) == 2 and name[1] in ['#', 'b']):
      self.quality = "M" # Major chord
    else:
      self.quality = "7" # Dominant seventh chord

  """
  Set the degree of the chord by its name
  The degree ranges in [0, 12)
  """
  def setDegree(self):
    letters = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
    if(len(self.name) == 1):
      self.degree = letters[self.name[0]]
      return
    name = self.name
    letter = name[0]
    tweak = 0
    if(name[1] in ['b', '#']):
      tweak = -1 if name[1] == 'b' else 1
    # Roundabout
    self.degree = (letters[letter] + tweak) % 12

  """
  Set key notes (extensional notes)
  """
  def setKeyNotes(self):
    quality = self.quality
    name = self.name
    self.keyNotes = []
    if(quality == "m"):
      if(name[-1] == '6'):
        self.keyNotes.append(9)
      if("11" in name):
        self.keyNotes.append(5)
    elif(quality == "M7"):
      if("#11" in name):
        self.keyNotes.append(6)
    elif(quality == "7"):
      if("b9" in name):
        self.keyNotes.append(1)
      if("#9" in name):
        self.keyNotes.append(3)
      if("b5" in name):
        self.keyNotes.append(6)
      if("#5" in name):
        self.keyNotes.append(8)
      if("13" in name):
        self.keyNotes.append(9)

  """
  Create a dictionary that maps degree in English to degree in midiutil
  """
  def setDegDict(self):
    degDict = {}
    quality = self.quality
    degDict["third"] = 4 if quality in ["M", "M6", "M7", "7"] else 3
    degDict["fifth"] = (6 if quality == "m7b5" or 6 in self.keyNotes
                          else 8 if 8 in self.keyNotes else 7)
    degDict["seventh"] = 11 if quality in ["M", "M6", "M7"] else 10
    degDict["root"] = 0
    degDict["second"] = 2
    self.degDict = degDict

  """
  Get the absolute pitch of a note specified by the type
  @param type: either third, seventh, fifth, root or second
  @param post: the return will be a note of type nearest to post
  @param up: true if looking for note below post
  @return the desired note
  """
  def getNote(self, type, post, down):
    res = self.degDict[type] + self.degree
    while(res < post):
      res += 12
    return res - 12 if down else res

  """
  Get the closest third, seventh or second
  """
  def getClosestStable(self, post):
    notes = []
    for name in list(self.degDict.keys()):
      notes.append(self.getNote(name, post, False))
      notes.append(self.getNote(name, post, True))
    good = []
    for note in notes:
      if note <= post:
        good.append(note)
    return max(good)