class Node():

    def __init__(self, parent=None, symbols=2):
        global nodes
        self.c = [0]*symbols
        self.n = [None]*symbols
        self.symbols = symbols
        self.pe = self.pw = 0.0
        self.parent = parent
#        if self.parent is not None:
#          self.depth = self.parent.depth + 1
#        else:
#          self.depth = 0
#        nodes.append(self)
    
    def __str__(self):
      return "[%d,%d]" % (self.c[0], self.c[1])
  
    def find(self, prevx, create=False):
      if prevx == []:
        return self
      if self.n[prevx[-1]] is None:
        if create:
          self.n[prevx[-1]] = Node(self, self.symbols)
        else:
          return self
      return self.n[prevx[-1]].find(prevx[:-1], create)
  
    def update(self, x, reverse=False):
      peadj = math.log(self.c[x]+0.5) - math.log(sum(self.c)+1.0)
      if reverse == False:
        self.pe += peadj
        self.c[x] += 1
      else:
        self.c[x] -= 1
        self.pe -= peadj
  
      # propagate
      tpw = 0
      for nn in self.n:
        if nn is not None:
          tpw += nn.pw
      if tpw == 0:
        self.pw = self.pe
      else:
        self.pw = math.log(0.5) + logaddexp(self.pe, tpw)
      if self.parent is not None:
        self.parent.update(x, reverse)

import math
root = Node(symbols=2)
a = root.find([0]*8)
print(a.pw)
a.update(0)
print(a.pw)
