#!/usr/bin/python
import sys

def load(filename):
  acts = []

  with open(filename,'r') as inf:
    for l in inf:
      parts = l.split(',')
      for p in parts:
        if p[0] == 's':
          acts.append(('s',int(p[1:])))
        if p[0] == 'x':
          ss = (p[1:]).split('/')

          acts.append(('x',int(ss[0]), int(ss[1])))
        if p[0] == 'p':
          ss = (p[1:]).split('/')
          acts.append(('p',ss[0], ss[1].rstrip()))
  
  return acts

def lstMove(lst, one,two):
  tmp = None
  pos = one
  pos2 = two

  tmp = lst[pos]
  lst[pos] = lst[pos2]
  lst[pos2] = tmp

  #print("{0} <=> {1} == {2}".format(pos, pos2,lst))

def spin(lst,cnt):
  tmp = None
  idx = None
  lstsrc = lst.copy()

  for x in range(0,len(lst)):
    idx = x + cnt
    if idx >= len(lst):
      idx -= len(lst)
    
    lst[idx] = lstsrc[x]

def ptnr(lst,s):
  idxa = lst.index(s[1])
  idxb = lst.index(s[2])

  #print("p {0} {1}".format(s[1],s[2]))
  lstMove(lst,idxa, idxb)

locs = []
c = 'a'
while c <= 'p':
  locs.append(str(c))
  c = chr(ord(c) + 1)

#print(locs)

actions = load(sys.argv[1])

adic = {
  's': lambda s:spin(locs,s[1])
  ,'x': lambda s:lstMove(locs, s[1],s[2])
  ,'p': lambda s:ptnr(locs,s)
}

for x in actions:
  act = adic[x[0]]
  act(x)

ans = ''
for x in locs:
  ans += x

print(ans)