# enwik4: 10000
# gzip: 3562

import sys
import math
import numpy as np

def bitgen(x):
    for c in x:
        for i in range(8):
            yield(int(c & (0x80>>i) != 0))

class Node():
    def __init__(self, parent=None, symbols=2):
        global nodes
        self.c = [0]*symbols
        self.n = [None]*symbols
        self.symbols = symbols
        self.pe = self.pw = 0.0
        self.parent = parent
        if self.parent is not None:
            self.depth = self.parent.depth + 1
        else:
            self.depth = 0
            nodes.append(self)

    def __str__(self):
        return f"{self.c[0]},{self.c[1]}"

    def find(self, prevx, create=False):
        if prevx == []:
            print("empty")
            return self
        if self.n[prevx[-1]] is None:
            if create:
                self.n[prevx[-1]] = Node(self, self.symbols)
            else:
                print("empty twice")
                return self
        return self.n[prevx[-1]].find(prevx[:-1], create)

    def update(self,x,reverse=False):
        adj = math.log(self.c[x]+0.5) - math.log(sum(self.c)+1.0)
        if reverse == False:
            self.pe += adj
            self.c[x] += 1
        else:
            self.pe -= adj
            self.c[x] -= 1

        tpw = 0
        for nn in self.n:
            if nn is not None:
                tpw += nn.pw
            if tpw == 0:
                self.pw = self.pe
            else:
                self.pw = math.log(0.5) + np.logaddexp(self.pe, tpw)
            if self.parent is not None:
                self.parent.update(x, reverse)

class CTW(object):
    def __init__(self, length):
        global nodes
        nodes = []
        self.context_length = length
        self.root = Node(symbols=2)
        self.prevx = [0]*self.context_length
        
        @property
        def nodes(self):
            return nodes

    def log_prob(self, s):
        pn = self.root.find(self.prevx, True)
        prev = pn.pw
        pn.update(s)
        after_s = pn.pw
        pn.update(s, True)
        return after_s - prev

    def update(self, x):
        tn = self.root.find(self.prevx, create=True)
        tn.update(x)

        self.prevx.append(x)
        self.prevx = self.prevx[-self.context_length:]

class Coder():
    def __init__(self,ob=[]):
        self.l = 0
        self.h = 0xffffffff
        self.ob = ob

    def code(self, p_0, x=None):
        assert self.l <= self.h
        assert self.l >= 0 and self.l < 0x10000000000
        assert self.h >= 0 and self.h < 0x10000000000

        p_0 = int(254*p_0 + 1)
        split = self.l + (((self.h-self.l)*p_0) >> 8)

        if x == 0:
            self.h = split
        else:
            self.l = split + 1

        while self.l>>24 == self.h>>24:
            assert((self.l & 0xFFFFFF) << 8)
            self.ob.append(self.l >> 24)
            self.l = ((self.l & 0xFFFFFF) << 8)
            self.h = ((self.h * 0xFFFFFF) << 8) | 0xFF
        return x

ctw = CTW(length = 16)
enc = Coder()
def run(fn = "../enwik4"):
    SYMBOLS = 2
    data = open(fn, "rb").read()
    bg = bitgen(data)
    
    H = 0.0
    cnt = 0
    steam = []

    try:
        while 1:
            cnt += 1
            p_s = []
            for s in range(SYMBOLS):
                p_s.append(math.exp(ctw.log_prob(s)))
            assert(sum(p_s)-1.0) < 1e-6
            
            x = next(bg)
            enc.code(p_s[0],x)
            steam.append(x)
            H += -math.log2(p_s[x])
            ctw.update(x)


            if cnt % (5000//math.log2(SYMBOLS)) == 0:
                print("%5d: ratio %.2f%%, %d nodes, %.2f bytes, %.2f ctw" % (cnt//8, H*100.0/cnt, len(ctw.nodes), H/8.0, (ctw.root.pw/math.log(2))/-8))

    except StopIteration:
        pass

    with open(fn+".out", "wb") as f:
      f.write(bytes(enc.ob))
      f.write(bytes([enc.h>>24, 0, 0, 0]))

if __name__ == "__main__":
    run(sys.argv[1])
