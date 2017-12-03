#!/usr/bin/python

import sys
import math

# polar distance to cartesian coordinates

def process(distance):
  """convert distance into cartesian coords and dump the length
     which is x + y
     (x,y) = (r,theta)
     r = sqrt(x2 + y2)
     """
  x = 0
  y = 0

  size = nextodd(float(distance))
  x = (size - 1) / 2
  y = distance - (size - 2) * (size - 2) - x

  print("s={2} {0} , {1}".format(x, y, size))

def nextodd(num):
  return math.ceil(math.sqrt(num)) // 2 * 2 + 1

if __name__ == "__main__":
  process(361527)
