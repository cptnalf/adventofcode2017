#!/usr/bin/python
import sys
import itertools

class Scanner:
  def __init__(self, index, length):
    self.index = index
    self.length = length
    self.pos = 0
    self.dir = 1

  def move(self):
    self.pos += self.dir
    if self.pos < 0:
      self.dir = 1
      self.pos = 0

    if self.pos >= self.length:
      self.dir = -1
      self.pos = self.length -1
    
    self.pos 

def process(fname):
  """
  pull file contents which will be:
  index -> length
  order of movement: you move, then scanners move.
  caught = scanner in destination location.
  """
  pos = -1
  score = 0
  (maxscan, scanners) = loadscanners(fname)

  while pos <= maxscan:
    pos += 1
    score += scoresneak(pos, scanners)
    movescanners(scanners)
  
  print("score: " + str(score))
  score = 0
  for pos in scanners:
    if ss(scanners[pos].length, pos) == 0:
      print("caught: {0} {1}".format(pos,pos * scanners[pos].length))
  scores = [pos * scanners[pos].length for pos in scanners if ss(scanners[pos].length, pos) == 0]

  score = sum(scores)
  print("alt: {0} = {1}".format(score, scores))

  offset = 0
  score = 1
  while score > 0:
    # this needs to take into account the zero position.
    score = 1 if any(ss(scanners[pos].length, pos + offset) == 0 for pos in scanners ) else 0
    offset += 1
  
  print(offset - 1)

  offset = next(wait for wait in itertools.count() if not any(ss(scanners[pos].length, wait + pos) == 0 for pos in scanners))
  print(offset)

def ss(height, time):
  """
  """
  offset = time % ((height - 1) * 2)
  return 2 * (height -1) - offset if offset > height -1 else offset

def scoresneak(pos, scandic):
  res = 0
  caught = False

  if pos in scandic:
    if scandic[pos].pos == 0:
      res = pos * scandic[pos].length
      caught = True
    
    print("@{0} -> l{1} {2} = {3} {4}".format(pos, scandic[pos].length, scandic[pos].pos, res, caught))

  return res

def movescanners(scanners):
  for x in scanners:
    scanners[x].move()

def loadscanners(filename):
  dic = {}
  midx = 0

  with open(filename, 'r') as inf:
    for l in inf:
      parts = l.split(':')
      s = Scanner(int(parts[0]), int(parts[1]))
      dic[s.index] = s
      if s.index > midx:
        midx = s.index
  
  return (midx, dic)

if __name__ == "__main__":
  process(sys.argv[1])