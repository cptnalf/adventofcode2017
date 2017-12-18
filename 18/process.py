#!/usr/bin/python
import sys

regs = {}
freq_played = None
ptr = 0

def getvalue(x):
  if x.isalpha():
    res = regs.get(x,0)
  else:
    res = int(x)
    
  return res

def ins_set(x):
  regs[x[0]] = getvalue(x[1])

def ins_add(x):
  regs[x[0]] = regs.get(x[0],0) + getvalue(x[1])

def ins_mul(x):
  regs[x[0]] = regs.get(x[0],0) * getvalue(x[1])

def ins_mod(x):
  regs[x[0]] = regs.get(x[0],0) % getvalue(x[1])

def ins_snd(x):
  global freq_played
  print('Play freq ' + str(regs.get(x[0], 0))) 
  freq_played = regs.get(x[0],0)

def ins_rcv(x):
  global freq_played
  if getvalue(x[0]) != 0:
    print('last played ' + str(freq_played)) 

def ins_jump(x):
  global ptr
  if regs.get(x[0], 0) > 0:
    ptr += getvalue(x[1])
  else:
    ptr += 1

def process(filename):
  global ptr

  instrdic = {
    'set': ins_set
    ,'add': ins_add
    ,'mul': ins_mul
    ,'mod' : ins_mod
    ,'snd' : ins_snd
    ,'rcv' : ins_rcv
    ,'jgz' : ins_jump
  }
  instrs = list()

  with open(filename, 'r') as inf:
    for l in inf:
      args = l.split()
      for j in range(len(args)):
        args[j] = args[j].rstrip().lstrip()
      instrs.append((args[0],args[1:]))
  
  while ptr >= 0 and ptr < len(instrs):
    (n, args) = instrs[ptr]
    print(n + ' ' + str(args))
    fx = instrdic.get(n)
    if fx == None:
      break
    
    fx(args)
    if n != 'jgz':
      ptr += 1

if __name__ == "__main__":
  process(sys.argv[1])