#!/usr/bin/python

import sys

def process(infile):
  """process file full of clear-text passphrases
     check that each passphrase contains unique words
  """

  valids = 0
  valid2s = 0
  cnt = 0
  inf = open(infile, 'r')
  for l in inf:
    cnt += 1
    d1 = []
    isok = True
    hasana = False
    llst = l.split()
    for w in llst:
      if w in d1:
        isok = False
        break
      else:
        d1.append(w)
    
    if isok:
      valids += 1

      z = 0
      for w in range(len(llst)):
        z = w + 1
        while z < len(llst):
          hasana = checkanagram(llst[w], llst[z])
          if hasana:
            break
          
          z +=1
        if hasana:
          break
      
      if not hasana:
        print (str(hasana) + ' ' + str(llst))
        valid2s += 1
  
  print("have {0} valids of {1}".format(valids, cnt))
  print("2: have {0} valids of {1}".format(valid2s, cnt))

def checkanagram(w1, w2):
  
  isana = True
  l1 = []
  for c in w1:
    l1.append(c)

  for c in w2:
    if c in l1:
      l1.remove(c)
    else:
      isana = False
      break
    
  if isana:
    isana = len(l1) == 0

  return isana

if __name__ == "__main__":
  process(sys.argv[1])
