#!/usr/bin/python

cnt = 40 * 1000 * 1000
gam = 16807
gbm = 48271
ga = lambda p: (p * gam) % 2147483647
gb = lambda p: (p * gbm) % 2147483647

judged = 0
pa = 65
pb = 8921
x = 0
while x < cnt:
  ra = ga(pa)
  rb = gb(pb)

  if x < 5:
    print(format(ra,'10d') + '  ' + format(rb,'10d'))

  if ra & 65535 == rb & 65535:
    judged += 1

  pa = ra
  pb = rb
  x += 1

print(judged)