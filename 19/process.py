#!/usr/bin/python
import sys

def finddir(newdir, px, py, arr, dirc):
  if arr[py][px] is not '+':
    return None
  
  c1 = ''
  if newdir[0] != dirc[0] or newdir[1] != dirc[1]:
    if len(arr) <= (py + newdir[1]) or (py + newdir[1]) < 0:
      return False
    line = arr[py + newdir[1]]

    if len(line) <= (px + newdir[0]) or (px + newdir[0]) < 0:
      return False
    
    c1 = line[px + newdir[0]]
    if c1.isalpha() or (
        newdir[0] == 0 and (newdir[1] == 1 or newdir[1] == -1) and c1 == '|') or (
        (newdir[0] == 1 or newdir[0] == -1) and newdir[1] == 0 and c1 == '-'):
      return True
  
  return False

puzzle = []

with open(sys.argv[1],'r') as inf:
  for l in inf:
    puzzle.append(l.rstrip())

curd = (0,1)
x = 0
y = 0
x = puzzle[y].index('|')
steps = 1
chars = ''

done = False

while not done:
  x += curd[0]
  y += curd[1]

  steps += 1
  if puzzle[y][x] == '|':
    pass
  if puzzle[y][x] == '+':
    #figure out our next direction based on what's connected
    bdir = (0 - curd[0], 0 - curd[1])
    newd = next((d for d in [(0,1),(0,-1),(1,0),(-1,0)] if finddir(d,x, y,puzzle,bdir)), None)
    print('{0},{1} {2}'.format(x,y,newd))
    if newd is None:
      print("wut")
      break
    else:
      curd = newd

  if puzzle[y][x] == '-':
    pass
  if puzzle[y][x].isalpha():
    chars += puzzle[y][x]
  
  if puzzle[y][x].isspace():
    steps -= 1
    done = True

print("{0},{1} => stepped: {2} for {3}".format(x,y, steps, chars))
