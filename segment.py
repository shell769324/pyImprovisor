class Segment:
  def __init__(self, rhythm, notes):
    self.rhythm = rhythm
    self.notes = notes

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
