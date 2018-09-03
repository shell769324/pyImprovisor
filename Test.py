#!/usr/bin/env python
from midiutil import MIDIFile
degrees = [60, 63, 65, 66, 67, 70, 72] # MIDI note number
track = 0
channel = 0
time = 0 # In beats
full = 120
duration = 80 # In beats
tempo = 120  # In BPM
volume = 100 # 0-127, as per the MIDI standard
MyMIDI = MIDIFile(1, True, True, False, 1, 120, True)
MyMIDI.addTempo(track, time, tempo)
for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + duration
    duration = full - duration

with open("minor-blues-scale.mid", "wb") as output_file: MyMIDI.writeFile(output_file)