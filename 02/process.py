#!/usr/bin/python

import sys

def process(args):
  """process the advent spreadsheet"""

  inf = open(args[0], 'r')

  lines = []
  lines1 = []

  for l in inf:
    lw = None
    up = None
    v = 0
    lst1 = []
    for c in l.split('\t'):
      v = int(c)
      lst1.append(v)
      if lw == None or lw > v:
        lw = v
      if up == None or up < v:
        up = v
    lines.append([lw, up])

    lst1.sort()
    print(lst1)
    for x in range(len(lst1)):
      y = len(lst1) -1
      while y >= 0:
        if y == x:
          y -= 1
          continue
        else:
          if lst1[y] % lst1[x] == 0:
            lines1.append(lst1[y] // lst1[x])
            break
        y -= 1

    
  inf.close()
  inf = None
  print(lines)
  print(lines1)

  tot = 0
  for sl in lines:
    tot += sl[1] - sl[0]
  print(tot)
  tot = 0
  for ls in lines1:
    tot += ls
  print(tot)

if __name__ == '__main__':
  process(sys.argv[1:])
