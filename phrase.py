class Phrase:
  def __init__(self, chords):
    self.chords = chords
    self.setEndNotes()

  def setEndNotes(self):
    chords = self.chords
