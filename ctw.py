# enwiktest: 1000000
# gzip: 356274


x = open("enwiktest","rb").read()
print(x[0:10])
def bit(x):
    for i in x:
        yield(i)

bg = bit(x)
for i in range(10):
    print(i, next(bg))
