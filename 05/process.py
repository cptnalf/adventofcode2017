#!/usr/bin/python
import sys

def process(puzzle):

  lst = readin(puzzle)
  inscnt = 0
  idx = 0
  cur = 0
  print("items: {0:d}".format(len(lst)))

  while idx >=0 and idx <len(lst):
    cur = lst[idx]
    lst[idx] += 1
    print("idx {0} jump {1} locmod: {2}".format(idx, cur, lst[idx] ))

    idx += cur
    inscnt += 1
  
  print("took {0:d} instructions to exit".format(inscnt))

def process2(puzzle):

  lst = readin(puzzle)
  inscnt = 0
  idx = 0
  cur = 0
  print("items: {0:d}".format(len(lst)))

  while idx >=0 and idx <len(lst):
    cur = lst[idx]
    lst[idx] += (1 if cur < 3 else -1)
    print("idx {0} jump {1} locmod: {2}".format(idx, cur, lst[idx] ))

    idx += cur
    inscnt += 1
  
  print("took {0:d} instructions to exit".format(inscnt))

def readin(fname):
  inf = open(fname,'r')
  lst = []
  cur = 0
  for l in inf:
    cur = int(l)
    lst.append(cur)
  
  inf.close()
  inf = None

  return lst

if __name__ == '__main__':
  if len(sys.argv) > 2:
    process2(sys.argv[1])
  else:
    process(sys.argv[1])