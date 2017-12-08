#!/usr/bin/python
import sys
import re

# 1 = register name
# 2 = inc|dec
# 3 = inc/dec amount
# 4 = reg name again
# 5 = comparison
# 6 = number to compare to
regline = re.compile("([a-z]+)[\s]+(inc|dec)[\s]+([0-9-]+)[\s]+if[\s]+([a-z]+)[\s]+(==|!=|>=|<=|<|>)[\s]+([0-9-]+)")

class Instr:

  def __init__(self, reg, act, amt, cmpreg, cmp, cmpamt):
    self.name = reg
    if act == 'dec':
      amt = 0 - amt
    self.amt = amt
    self.cmpreg = cmpreg
    self.cmp = cmp
    self.cmpamt = cmpamt

def parse(infile):
  inf = open(infile,'r')

  lst = []
  for l in inf:
    res = regline.match(l)
    if res:
      #print("{0} ? {1} {2} {3} : {4} {5}".format(res.group(1), res.group(4), res.group(5), res.group(6), res.group(2), res.group(3)))
      lst.append(Instr(res.group(1), res.group(2), int(res.group(3))
        , res.group(4), res.group(5), int(res.group(6)) ) )

  inf.close()
  inf = None

  return lst

def initRegs(rd, name):
  if name not in rd:
    rd[name] = 0

def process(filename):
  instrs = parse(filename)
  regs = {}

  cmpdic = {
    '==': lambda x,y: x == y
    ,'!=': lambda x,y: x != y
    ,'>=': lambda x,y: x >= y
    ,'<=': lambda x,y: x <= y
    ,'>': lambda x,y: x > y
    ,'<': lambda x,y: x < y
  }

  m = None
  for i in instrs:
    initRegs(regs, i.name)
    initRegs(regs, i.cmpreg)
    
    act = cmpdic.get(i.cmp, None)
    if act is not None:
      if act(regs[i.cmpreg], i.cmpamt):
        regs[i.name] += i.amt
    else:
      print("{0} {1}".format(i.name, i.cmp))
    
    for r in regs:
      if m is None or m < regs[r]:
        m = regs[r]
    
  print(regs)
  print("max during process " + str(m))
  
  m = None
  for r in regs:
    if m is None or m < regs[r]:
      m = regs[r]
  
  print("max {0}".format(m))

if __name__ == "__main__":
  process(sys.argv[1])
