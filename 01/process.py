#!/usr/bin/python
import sys

def process(args):
  """pull in the file, and look at the first line for numbers"""
  inf = open(args[1],'r')
  
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

  x=0
  while x < len(lst):
    if (x == (len(lst) -1)):
      cnt = 0
    else:
      cnt = x + 1
    
    cur = lst[x]
    p = lst[cnt]
    if cur == p:
      tot += cur
      print("{0:s} {1:d} {2:d}".format(c, cur, tot))
    x+=1
  
  print("sum is: {0:d} {1:d}".format(tot, cnt))

if __name__ == "__main__":
  process(sys.argv)
