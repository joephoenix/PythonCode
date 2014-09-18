from time import time

t = time()

abbreviations = ['cf.', 'e.g.', 'ex.', 'etc.', 'fig.', 'i.e.', 'Mr.', 'vs.']

#1
for i in range(1000000):
    for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
        if w in abbreviations:
            if w[-1] == '.' and w in abbreviations:
                pass

print "total run time in normal mode:"
print time()- t

#2
t = time()
for i in range(1000000):
    for w in ('Mr.', 'Hat', 'is', 'chasing', 'the', 'black', 'cat', '.'):
        if w in abbreviations:
            pass
         
print "total run time in lazy if mode:"
print time() - t


#3
t = time()
s = ""
lists = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']

for i in range(10000):
    for substr in lists:
        s += substr
        
print("total run time:")
print(time() - t)
