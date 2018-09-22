OCTAVE = 12
class Chord:
  def __init__(self, name, dur):
    self.name = name
    self.dur = dur
    self.setQuality()
    self.setDegree()
    self.setKeyNotes()

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
    if(len(self.name) == 1): return letters[self.name[0]]
    name = self.name
    letter = name[0]
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
  Get a random post 
  @param type: must be either root, third, fifth, seventh or second
  """
  def getPost(self, type):
    if(type == "third"):
      if(self.quality in ["M", "M6", "M7"]):
        return 4
      else:
        return 3
    elif(type == "fifth"):
      if(self.quality == "m7b5" or 6 in self.keyNotes):
        return 6
      elif(8 in self.keyNotes):
        return 8
      else:
        return 7
    elif(type == "seventh"):
      if(self.quality in ["M", "M6", "M7"]):
        return 11
      else:
        return 10
    elif(type == "root"):
      return 0
    elif(type == "second"):
      return 2
    else:
      raise ValueError("invalid post type!")