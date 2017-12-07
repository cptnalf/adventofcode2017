#!/usr/bin/python
import sys
import re

nodeDic = {}
leaves = {}

class Node:
  def __init__(self,name,weight,childnames=list()):
    self.name = name
    self.weight = weight
    self.children = list()
    self.childrennames = childnames
  
  def add(self,n):
    self.children.append(n)

  def __str__(self):
    lst = [x.name for x in self.children]
    return "{0} ({1}) => {2}".format(self.name,self.weight, lst )

  def __unicode__(self):
    return "{0} ({1}) => {2}".format(self.name,self.weight, [x.name for x in self.children])

  def __contains__(self,item):
    """determine if the node is contained in this tree"""
    if item is None:
      return False

    if type(item) is Node:
      for n in self.children:
        if n.name == item.name:
          #print("found! {0}".format(item.name))
          return True
        else:
          if item in n:
            return True
    
    return False

def process(filename):
  inf = open(filename, 'r')
  for l in inf:
    parse_line(l)
  
  inf.close()
  root = None

  print("{0} -> {1}".format(len(nodeDic), len(leaves)))

  for k in nodeDic:
    n = nodeDic[k]

    assemble(n)

  for cn in nodeDic:
    n = nodeDic[cn]
    if root is None or root in n:
      root = n
  
  print("root: {0}".format(root))

def assemble(node):
  """finds the direct children of the supplied node"""
  #print(node.childrennames)
  for ch in node.childrennames:
    newnode = None
    if ch in nodeDic:
      newnode = nodeDic[ch]
    if ch in leaves:
      newnode = leaves[ch]
    
    if newnode is not None:
      node.add(newnode)
      #print("{0} => {1} {2}".format(node.name, ch, node.children))
  
  print(node)

def parse_line(line):
  """ parse one line of the input file.
  this is a line:
usevgds (44) -> aydmhhv, kkftjia
  it contains a program name (usevgds), a weight (44) and the names of sub programs (aydmhhv, kkftjia)
  """
  name = ''
  weight = ''
  children = []

  linere = re.compile("([\w]+)[\s]+[(]([\d]+)[)]")
  linkre = re.compile("[\s]+[-][>][\s]+([a-zA-Z, \t]+)")
  res = linere.search(line,0)
  if res:
    node = None
    name = res.group(1)
    weight = int(res.group(2))

    idx= len(res.group(0))
    res = linkre.search(line,idx)
    if res:
      children = res.group(1).split(', ')
      node = Node(name,weight,children)
      nodeDic[name] = node
    else:
      node = Node(name,weight)
      leaves[name] = node
    
    #print("{0} {1} => {2}".format(name, weight, children))
    #if node is not None:
      #print(node)
  

if __name__ == "__main__":
  process(sys.argv[1])
