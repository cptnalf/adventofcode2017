#!/usr/bin/python

#p=<-13053,-6894,1942>, v=<14,39,-11>, a=<16,7,-2>
# kinematics equation:
# xn = xp + v*t + 1/2 * a * t^2

import re
import sys

class Particle:
  def __init__(self,id,p,v,a):
    self.id = id
    self.p = p
    self.v = v
    self.a = a
  
  def step(self):
    for i in range(0,3):
      self.v[i] += self.a[i]
      self.p[i] += self.v[i]

  def dist(self,step):
    #res = 0
    #for i in range(0,3):
    #  res += abs(self.p[i] + step * (self.v[i] + self.a[i]))
    #return res
    return sum([abs(x) for x in self.p])

  def __str__(self):
    return str(self.id)

lre = re.compile("[apv][=][<]([0-9-]+),([0-9-]+),([0-9-]+)[>]")

particles = []
x = 0
with open(sys.argv[1], 'r') as inf:
  for l in inf:
    parts = []
    for m in lre.finditer(l):
      groups = []
      for g in m.groups():
        groups.append(int(g))
      parts.append(groups)
    
    p = Particle(x,parts[0], parts[1], parts[2])
    particles.append(p)
    x += 1
    #particles.append(parts[0])
    #velocities.append(parts[1])
    #accels.append(parts[2])

x = 0
done = False
while x < 10000:
  smalls = None
  for p in particles:
    #d = sum(abs(p) for p in [particles[i][h] + velocities[i][h] + x * accels[i][h] for h in range(0,3)])
    p.step()
    d = p.dist(x)

    if smalls is None or smalls[1] > d:
      smalls = (p,d)
    #smalls.sort(key=lambda e: e[0],reverse=True)
  print(str(x) + " smalls " + str(smalls[0]) + ', ' + str(smalls[1]))
  x += 1

