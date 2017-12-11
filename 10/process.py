#!/usr/bin/python
import sys

class KnotHash:
  def __init__(self):
    self.pos = 0
    self.step = 0
    self.round = 0
    self.arr = list(range(0,256))
    self.srclens = []
  
  def setsrc(self,src):
    self.srclens = src

  def gethex(self):
    idx = 0
    res = ''

    while idx < 16:
      v = 0
      for x in range(idx *16,(idx +1) * 16):
        v ^= self.arr[x]
      res += format(v, "02x")
      idx += 1

    return res

  def pull(self, stringochars):
    lst = list()
    for x in stringochars:
      lst.append(ord(x))

    return lst

  def doround(self):
    self.round += 1

    vals = []
    idxs = []

    for x in self.srclens:
      vals.clear()
      idxs.clear()

      cnt = x
      idx = self.pos
      while cnt > 0:
        idx = idx % 256
        
        vals.append(self.arr[idx])
        idxs.append(idx)
        idx += 1
        cnt -= 1
      
      idxs.reverse()
      for y in range(0, len(idxs)):
        self.arr[idxs[y]] = vals[y]

      # print("{0} {1} {2}  {3} => {4}".format(self.pos, self.step, x, idxs, vals))

      self.pos += x + self.step
      self.pos = self.pos % 256
      self.step += 1
    

def process(lenlst):
  hasher = KnotHash()
  hasher.setsrc(lenlst)
  hasher.doround()

  print(str(hasher.arr[0]) + " " + str(hasher.arr[1]) + " = " + str(hasher.arr[0] * hasher.arr[1]))

def part2(instr):
  hasher = KnotHash()
  staticset = [17,31,73,47,23]

  inchars = hasher.pull(instr)
  inchars.extend(staticset)
  hasher.setsrc(inchars)
  while hasher.round < 64:
    #print("round: {0} {1} {2}".format(hasher.round, hasher.pos, hasher.step ))
    hasher.doround()
    #print(hasher.gethex())
  
  print(hasher.gethex())

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

  str1 = ''
  with open(sys.argv[1]) as f1:
    str1 = f1.read().rstrip()
  
  part2('')
  part2('AoC 2017')
  part2('1,2,3')
  part2('1,2,4')
  part2(str1)


      
