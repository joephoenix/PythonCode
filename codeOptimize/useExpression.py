from time import time

t = time()

slist = ['a','b','is','python','jason','hello','hill','with','phone','test', 
'dfdf','apple','pddf','ind','basic','none','baecr','var','bana','dd','wrd'] 

total = []

for i in range(1000000):
    for w in slist:
        total.append(w)
        
print("total run time in normal mode:")
print(time() - t)

t = time()

for i in range(1000000):
    a = [w for w in slist]

print("total run time in list comprehension mode:")
print(time() - t)

t = time()

for i in range(1000000):
    a = (w for w in slist)
    
print("total run time in generator expression mode:")
print(time() - t)


