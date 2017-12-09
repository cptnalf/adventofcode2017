#!/usr/bin/python
import sys

def process(fname):
  data = None
  with open(fname, 'r') as inf:
    data = inf.read()
  
  esc = False
  gstart = False
  score = 0
  tot = 0
  garbage = 0
  for c in data:
    if esc:
      esc = False
      continue
    
    if c == '!':
      esc = True
      continue
    
    if gstart:
      if c == '>':
        gstart = False
      else:
        garbage += 1
      continue
          
    if c == '<':
      gstart = True
      continue
    
    if c == '{':
      score += 1
      tot += score
    
    if c == '}':
      score -= 1

    print(c,end='')
  
  print("tot = {0} score={1}".format(tot, score))
  print("garbage chars: {0}".format(garbage))

if __name__ == "__main__":
  process(sys.argv[1])