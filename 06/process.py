#!/usr/bin/python
import sys

def process(infile):
  prevs = []
  cycle = 0
  infc = 0
  cycleseen = False

  lst = slurp(infile)
  while True:
    prevs.append(lst)
    print(lst)
    
    newlst = level_lst(lst)
    cycle +=1

    if newlst in prevs:
      break
    lst = newlst
  
  print("{0:d} cycles for :{1}".format(cycle, newlst))

  targetlst = newlst
  lst = newlst
  while True:
    newlst = level_lst(lst)
    infc += 1 
    if newlst == targetlst:
      break
    lst = newlst
  print("{0:d} cycles for again.".format(infc))


def slurp(fname):
  lst = []
  inf = open(fname,'r')
  for l in inf:
    for w in l.split():
      i = int(w)
      lst.append(i)
  
  return lst

def level_lst(inlst):
  outlst = []

  # start point
  idxm = 0
  for x in range(len(inlst)):
    if inlst[idxm] < inlst[x]:
      idxm = x
  
  amt = inlst[idxm]
  outlst = inlst.copy()
  outlst[idxm] = 0
  idxr = idxm + 1
  while amt > 0 and idxr != idxm:
    if idxr >= len(inlst):
      idxr = 0
    
    outlst[idxr] += 1
    amt -=1
    idxr +=1
  
  return outlst

if __name__ == "__main__":
  process(sys.argv[1])
