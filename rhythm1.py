import random
QUARTER = 24
COUNT = 14
## FULL
#4 * 1/16
FULL1 = [2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1]
#2 * 1/8
FULL2 = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
#1 * 1/4
FULL3 = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#1/8 1/16 1/16
FULL4  = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1]
#triplet
FULL5 = [2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]

## Have space
# 1/8 rest
ENDP1 = [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# rest 1/8
ENDP2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1]
# 1/12 1/12 rest
ENDP3 = [2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# rest 1/12 1/12
ENDP4 = [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
# rest 1/12 rest
ENDP5 = [0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# rest
ENDP6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

## Connecting
# 1/8 rest
CONN1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
# 1/8 1/8
CONN2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1]
# 1/4
CONN3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

class Rhythm1:
  def __init__(self):
    self.setDensity()
    self.setBlockPara()

  def normalizer(self, distribution):
    disSum = float(sum(distribution))
    for i in range(1, len(distribution)):
      distribution[i] += distribution[i - 1]
    for i in range(len(distribution)):
      distribution[i] /= disSum

  def normalizer2D(self, distribution):
    for i in range(len(distribution)):
      self.normalizer(distribution[i])

  def setDensity(self):
    return 42

  def setBlockPara(self):
    self.blockIdx = [FULL2, ENDP1, ENDP2, ENDP6, CONN1]
    blockFirstWeight = [4, 4, 0, 0, 0]
    blockTransition = [[0, 3, 5, 3, 3],
                       [3, 1, 4, 2, 0],
                       [0, 3, 4, 2, 2],
                       [4, 4, 2, 0, 0],
                       [3, 1, 4, 2, 0]]
    self.normalizer(blockFirstWeight)
    self.normalizer2D(blockTransition)
    self.blockFirstWeight = blockFirstWeight
    self.blockTransition = blockTransition


  def setGenre(self, genre):
    self.genre = genre

  def firstBlock(self):
    num = random.uniform(0, 1)
    for i in range(COUNT):
      if (self.blockFirstWeight[i] > num):
        return i
    raise ValueError("first method, impossible")

  def similarBlock(self, idx):
    num = random.uniform(0, 1)
    for i in range(COUNT):
      if (self.blockTransition[idx][i] > num):
        return i
    raise ValueError("similar method, impossible case")

  def generateRhythm(self, dur, dyna, type, BR):
    res = []
    quarterCount = int(round(dur * 4, 0))
    # If we want a basic rhythm, use first
    # Store the index of basic rhythm
    if(BR):
      quarterCount -= 1
      self.basicRhyIdx = self.firstBlock()
      res.extend(self.blockIdx[self.basicRhyIdx])
    # Try to mimic and grow from basic rhythm
    curr = self.basicRhyIdx
    while (quarterCount > 0):
      curr = self.similarBlock(curr) if quarterCount % 4 == 0 else self.firstBlock()
      res.extend(self.blockIdx[curr])
      quarterCount -= 1
    # Change 2 to volume, adjust volume and change 1 to -1
    for i in range(len(res)):
      if(res[i] == 2):
        # Set basic volume
        res[i] = dyna
        # eighth beat reinforce
        if(i % 12 == 0):
          res[i] += 3
        # quarter beat reinforce
        elif(i % 24 == 0):
          res[i] += 4
        # Prevent overflow
        if(res[i] >= 127):
          res[i] = 127
      elif(res[i] == 1): res[i] = -1
    return res