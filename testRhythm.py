from Rhythm import rhythm

R = rhythm()
"""
print(R.line)
print(R.duration)
print(R.genre)
print(R.dynamix)
print(R.br)
"""
L = R.generateRhythm(1, "Ballad", 1, 125, 1)
#print(len(L))
for i in range(len(L)):
	print(L[i])