class pattern:
  def __init__(self, durs):
    self.durs = durs
    self.setTotal()
    self.avg = self.total / len(durs)

  def setTotal(self):
    total = 0
    for dur in self.durs:
      total += dur
    self.total = total