#!/usr/bin/python

class KnotHash:
  """calculate a knot hash of a given string input."""
  def __init__(self):
    self.reset()

  def reset(self):
    self.pos = 0
    self.step = 0
    self.round = 0
    self.arr = list(range(0,256))
    self.srclens = []
    self.hexsrc = list()

  def load(self,srcstr):
    """load a string into the hash, using the default 'salt'"""
    strs = self.pull(srcstr)
    staticset = [17,31,73,47,23]
    strs.extend(staticset)
    self.setsrc(strs)

  def run(self):
    """run 64 rounds of the hash function."""
    while self.round < 64:
      self.doround()
  
  def setsrc(self,src):
    self.srclens = src

  def populateHex(self):
    """condense the hash into a 16byte list"""
    self.hexsrc = list()
    idx = 0
    while idx < 16:
      v = 0
      for x in range(idx * 16, (idx +1) * 16):
        v ^= self.arr[x]
      self.hexsrc.append(v)
      idx +=1
  
  def gethex(self):
    """dump a hex representation of the 16byte list"""
    res = ''
    self.populateHex()

    for v in self.hexsrc:
      res += format(v, "02x")

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

seen = set()
rows = list()

def search(i,j):
  """search the array for stuff close to the given coords."""
  if (i,j) in seen:
    return

  if not rows[i][j]:
    return
  
  seen.add((i,j))
  if i > 0:
    search(i -1, j)
  if j > 0:
    search(i,j -1)
  if i < 127:
    search(i + 1,j)
  if j < 127:
    search(i,j + 1)

if __name__ == "__main__":
  kh = KnotHash()

  # for verification.
  #kh.load('AoC 2017')
  #kh.run()
  #print(kh.gethex())
  instr = 'uugsqrei'
  #'uugsqrei'
  #'flqrgnkx'
  used = 0
  for x in range(0,128):
    kh.reset()
    kh.load(instr + '-'+str(x))
    kh.run()
    h = kh.gethex()
    v = '{:0128b}'.format(int(h,16))
    used += sum(map(int,v))
    rows.append(list(map(int,v)))
  
  print(used)

  used = 0
  for x in range(0,128):
    for y in range(0,128):
      if (x,y) in seen:
        continue

      if rows[x][y]:
        used += 1
        search(x,y)
  
  print(used)




