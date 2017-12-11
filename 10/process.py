#!/usr/bin/python
import sys

def process(lenlst):
  arr = list(range(0,256))
  pos = 0
  step = 0
  vals = []
  idxs = []

  for x in lenlst:
    vals.clear()
    idxs.clear()

    cnt = x
    idx = pos
    while cnt > 0:
      if idx >= len(arr):
        idx = 0
      
      vals.append(arr[idx])
      idxs.append(idx)
      idx += 1
      cnt -= 1

    idxs.reverse()
    for y in range(0,len(idxs)):
      arr[idxs[y]] = vals[y]
    
    print("{0} {1} {2}  {3} => {4}".format(pos, step, x, idxs, vals))

    pos += x + step
    if pos >= len(arr):
      pos -= len(arr)
    step += 1

  print(str(arr[0]) + " " + str(arr[1]) + " = " + str(arr[0] * arr[1]))

def load(fname):
  res = []
  with open(fname, 'r') as inf:
    data = inf.read()
    lens = data.rstrip().split(',')
    for x in lens:
      v = int(x)
      if v is not None:
        res.append(v)
  
  return res

if __name__ == "__main__":
  lst = load(sys.argv[1])
  process(lst)

      
