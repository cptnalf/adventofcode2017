#!/usr/bin/python
import sys

def process(args):
  """pull in the file, and look at the first line for numbers"""
  inf = open(args[1],'r')
  
  delta = 1

  p = None
  cur = 0
  tot = 0
  cnt = 0
  lst = []
  while True:
    c = inf.read(1)
    if not c:
      break

    lst.append(int(c))
  inf.close()
  inf = None

  if (len(args) > 2):
    delta = int(len(lst) / 2)

  x=0
  while x < len(lst):
    cnt = x + delta
    if cnt > (len(lst) -1):
      cnt = cnt - len(lst)
    
    cur = lst[x]
    p = lst[cnt]
    if cur == p:
      tot += cur
      print("{0:s} {1:d} {2:d}".format(c, cur, tot))
    x+=1
  
  print("sum is: {0:d} {1:d}".format(tot, cnt))

if __name__ == "__main__":
  process(sys.argv)
