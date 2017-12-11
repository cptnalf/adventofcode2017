#!/usr/bin/python
import sys

class HexCoord:
  """
  http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
  """
  def __init__(self):
    self.x = 0
    self.y = 0
    self.z = 0

  def calcz(self):
    self.z = 0 - self.x - self.y

  def dist(self):
    return (abs(self.x) + abs(self.y) + abs(self.z)) / 2
  
  def __str__(self):
    return "({0},{1},{2})".format(self.x, self.y, self.z)


def moveN(hc):
  """ (0,+)"""
  hc.y += 1
  hc.z -= 1

def moveS(hc):
  """(0,-)"""
  hc.y -= 1
  hc.z += 1

def moveNE(hc):
  """(+,0)"""
  hc.x += 1
  hc.z -= 1

def moveSW(hc):
  """(-,0)"""
  hc.x -= 1
  hc.z += 1

def moveNW(hc):
  """(-,0)"""
  hc.x -= 1 
  hc.y += 1

def moveSE(hc):
  """(+,0)"""
  hc.x += 1
  hc.y -= 1

def process(dirs):
  #    \ n  /
  #  nw +--+ ne
  #    /    \
  #  -+      +-
  #    \    /
  #  sw +--+ se
  #    / s  \

  coords = HexCoord()
  dirFX = {
    'n': moveN
    ,'s': moveS
    ,'ne':moveNE
    ,'se':moveSE
    ,'nw':moveNW
    ,'sw': moveSW
  }

  maxd = 0
  for d in dirs:
    if d in dirFX:
      dirFX[d](coords)
    
    curd = coords.dist()
    print(d + ' => ' + str(curd) + ' :' +str( coords))
    if curd > maxd:
      maxd = curd
  
  print(maxd)
  print(coords)

if __name__ == "__main__":
  lst = list()
  with open(sys.argv[1],'r') as inf:
    slrp = inf.read().rstrip()
    lst = slrp.split(',')
  process(lst)
