MAJOR_PENTA = [0, 2, 4, 7, 9, 12]
MAJOR = [0, 2, 4, 5, 7, 9, 11, 12]
NAT_MINOR = [0, 2, 3, 5, 7, 8, 10, 12]
BLUES = [0, 3, 5, 6, 7, 10, 12]
ALTERED_DOM = [0, 1, 3, 4, 6, 8, 10, 12]
DIM = [0, 1, 3, 4, 6, 7, 9, 10, 12]

MAJOR_T = [0, 4, 7]
MINOR_T = [0, 3, 7]
DIM_T = [0, 3, 6]
AUG_T = [0, 4, 8]
F4_T = [0, 4, 6]
MAJOR_SEV = MAJOR_T + [11]
MINOR_SEV = MINOR_T + [10]
DOM_SEV = MAJOR_T + [10]
HALF_DIM = DIM_T + [10]
FULL_DIM = DIM_T + [9]
MAJOR_SEV_AUG = AUG_T + [11]
DOM_SEV_F4 = F4_T + [10]
MINOR_MAJ_SEV = MINOR_T + [11]

ITV = {"m2":1, "M2":2, "m3":3, "M3":4, "P4":5, "T":6, "P5":7,
       "m6":8, "M6":9, "m7":10, "M7":11}

class Bank:
  def __init__(self, chord):
    self.chord = chord
    self.createScales()
    self.createChords()

  def transpose(self, notes, interval, up = True):
    interval %= 12
    result = [0] * len(notes)
    for i in range(len(notes)):
      result[i] = notes[i] + interval * (1 if up else -1)
    return result

  def createScales(self):
    chord = self.chord
    quality = chord.quality
    degree = chord.degree
    scales = []
    if(quality in ["M", "M7"]):
      scales.append(self.transpose(MAJOR_PENTA, degree))
      scales.append(self.transpose(MAJOR, degree))
      scales.append(self.transpose(BLUES, degree + ITV["M6"]))
    elif(quality == "m7"):
      scales.append(self.transpose(BLUES, degree))
      scales.append(self.transpose(MAJOR, degree + ITV["m7"]))
    elif(quality == "m7b5"):
      scales.append(self.transpose(DIM, degree))
      scales.append(self.transpose(ALTERED_DOM, degree + ITV["P4"]))
    else:
      scales.append(self.transpose(MAJOR, degree + ITV["P4"]))
      scales.append(self.transpose(DIM, degree))
      scales.append(self.transpose(ALTERED_DOM, degree))
      scales.append(self.transpose(BLUES, degree + ITV["P5"]))
      scales.append(self.transpose(BLUES, degree + ITV["M6"]))
    self.scales = scales

  def createChords(self):
    chord = self.chord
    quality = chord.quality
    degree = chord.degree
    chords = []
    if(quality in ["M", "M7", "7"]):
      chords.append(self.transpose(MAJOR_T, degree))
    elif(quality == "M7"):
      chords.append(self.transpose(MAJOR_SEV, degree))
      chords.append(self.transpose(MINOR_T, degree + ITV["M3"]))
      chords.append(self.transpose(MINOR_SEV, degree + ITV["M3"]))
      chords.append(self.transpose(MAJOR_T, degree + ITV["P5"]))
    elif(quality == "m7"):
      chords.append(self.transpose(MINOR_T, degree))
      chords.append(self.transpose(MINOR_SEV, degree))
      chords.append(self.transpose(MAJOR_T, degree + ITV["m3"]))
      chords.append(self.transpose(MAJOR_SEV, degree + ITV["m3"]))
      chords.append(self.transpose(MINOR_T, degree + ITV["P5"]))
    elif(quality == "m7b5"):
      chords.append(self.transpose(DIM, degree))
      chords.append(self.transpose(HALF_DIM, degree))
      chords.append(self.transpose(MINOR_T, degree + ITV["m3"]))
      chords.append(self.transpose(MINOR_SEV, degree + ITV["m3"]))
    else:
      chords.append(self.transpose(DOM_SEV, degree))
      chords.append(self.transpose(DIM, degree + ITV["M3"]))
      chords.append(self.transpose(HALF_DIM, degree + ITV["M3"]))
      chords.append(self.transpose(MAJOR_SEV_AUG, degree + ITV["m6"]))
      chords.append(self.transpose(DOM_SEV_F4, degree + ITV["T"]))
      chords.append(self.transpose(MINOR_MAJ_SEV, degree + ITV["P4"]))
    self.chords = chords

  def createLicks(self):
    chord = self.chord
    quality = chord.quality
    degree = chord.degree
    licks = []