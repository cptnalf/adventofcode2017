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
    
if __name__ == "__main__":
  kh = KnotHash()

  # for verification.
  #kh.load('AoC 2017')
  #kh.run()
  #print(kh.gethex())
  instr = 'flqrgnkx'
  used = 0
  for x in range(0,128):
    kh.reset()
    kh.load(instr + '-'+str(x))
    kh.run()
    #print(kh.gethex())
    kh.populateHex()
    for x in kh.hexsrc:
      l = ''
      for b in format(x,'08b'):
        #if b == '0':
        #  l += '.'
        if b == '1':
          used += 1
          #l += '#'
      #print(l)
  
  print(used)
