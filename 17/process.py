#!/usr/bin/python

 # circular buffer.
def step(lst, cnt, idx):
  idx += cnt
  if idx > len(lst):
    idx = idx % len(lst)
  
  return idx

buf = list()
buf.append(0)

newidx = 0
stpcnt = 343
# 343
curidx = 0
for x in range(1,2018):
  newidx = step(buf,stpcnt, curidx)
  buf.insert(newidx,x)
  curidx = newidx + 1

print(buf)
newidx = buf.index(0)
print(newidx)

vafterzero = 0
curidx = 0
for x in range(1,50000000 + 1):
  curidx = (curidx + stpcnt) % x + 1
  if curidx == 1:
    vafterzero = x

print(vafterzero)