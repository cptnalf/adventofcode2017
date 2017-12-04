#!/usr/bin/python

import sys

def process(infile):
  """process file full of clear-text passphrases
     check that each passphrase contains unique words
  """

  valids = 0
  cnt = 0
  inf = open(infile, 'r')
  for l in inf:
    cnt += 1
    d1 = []
    isok = True
    for w in l.split():
      if w in d1:
        isok = False
        break
      else:
        d1.append(w)
    
    if isok:
      valids += 1
  
  print("have {0} valids of {1}".format(valids, cnt))

if __name__ == "__main__":
  process(sys.argv[1])
