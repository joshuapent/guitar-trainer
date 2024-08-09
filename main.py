import random
import time

class Chord:
  def __init__ (self, name, scale, difficulty):
    self.name = name
    self.scale = scale
    self.difficulty = difficulty

chords = []

chords.append(Chord("A", "Standard", "Easy"))
chords.append(Chord("C", "Standard", "Easy"))
chords.append(Chord("D", "Standard", "Easy"))
chords.append(Chord("G", "Standard", "Easy"))

metronome_state = True
metronome_speed = 1

if metronome_state == True:
  start_time = round(time.time())
  cycle_num = 0
  while metronome_state == True and cycle_num < 5:
    time.sleep(metronome_speed)

    
    print(chords[random.randint(0, len(chords)-1)].name)
    cycle_num += 1
  end_time = round(time.time())
  print("Total time elapsed was", end_time - start_time, "seconds.")



random_Generator = random.randint(0, len(chords)-1)

print(chords[random_Generator].name)
