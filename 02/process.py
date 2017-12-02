#!/usr/bin/python

import sys

def process(args):
  """process the advent spreadsheet"""

  inf = open(args[0], 'r')

  lines = []

  for l in inf:
    lw = None
    up = None
    v = 0
    for c in l.split('\t'):
      v = int(c)
      if lw == None or lw > v:
        lw = v
      if up == None or up < v:
        up = v
    lines.append([lw, up])
  
  inf.close()
  inf = None
  print(lines)

  tot = 0
  for sl in lines:
    tot += sl[1] - sl[0]

  print(tot)

if __name__ == '__main__':
  process(sys.argv[1:])
