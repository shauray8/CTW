# enwiktest: 1000000
# gzip: 356274

import sys
import math

def bitgen(x):
    for c in x:
        for i in range(8):
            yield(int(c & (0x80>>i) != 0))

def run(fn = "enwik4"):
    enw = open(fn, "rb").read()
    bg = bitgen(enw)
    SYMBOLS = 2
    enc = Coder()
    ctw = CTW(context_length=16)

    H = 0.0
    cnt = 0
    stream = []
    try:
        while 1:
            cnt += 1

            p_s = []
            for s in range(SYMBOLS):
                p_s.append(math.exp(ctw.log_prob(s)))
            assert (sum(p_s)-1.0) < 1e-6


run()
