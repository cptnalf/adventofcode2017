#!/usr/bin/python
import sys
import re

class Node:
  def __init__(self,name):
    self.name = name
    self.links = list()
  
  def __contains__(self,name):
    if name is None:
      return False

    return name in [x.name for x in self.links]

def process(fname):
  root = Node('0')

  nodeDic = {}
  nodeDic[root.name] = root

  with open(fname, 'r') as inf:
    for l in inf:
      idx = l.find('<->')
      n = Node(l[0:idx].rstrip())
      lst = (l[idx+4:].lstrip().rstrip()).split(',')

      for nn in lst:
        nn = nn.lstrip().rstrip()
        nl = None
        if nn in nodeDic:
          nl =  nodeDic[nn]
        else:
          nl = Node(nn)
          nodeDic[nl.name] = nl
        
        if n.name not in nl:
          nl.links.append(n)
        
        if nl.name not in n:
          n.links.append(nl)

  cnt = 0
  cnt = printTree(root, nodeDic)
  print("links: " + str(cnt))

def printTree(node, nodeDic):
  q = list()
  visited = list()
  n = 0

  while node is not None:
    n += 1
    print(node.name)
    visited.append(node.name)
    for x in node.links:
      if x.name not in visited:
        q.append(x)

    #print (node.name + " <" + str(len(visited)))
    if len(q) < 1:
      node = None
    else:
      while node.name in visited and len(q) > 0:
        node = q.pop(0)
  
  return n

if __name__ == "__main__":
  process(sys.argv[1])
