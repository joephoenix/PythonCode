import time
#python3
#from ContextLib import contextmanager

# normal execute
class demo1:
    def __init__(self, label):
        self.label = label
        
    def __enter__(self):
        self.start = time.time()
        
    def __exit__(self, exc_ty, exc_val, exc_tb):
        end = time.time()
        print('{}: {}'.format(self.label, end - self.start))
        
with demo1('counting'):
    n = 1000000
    while n > 0:
        n -= 1
        
# ContextLib execute
#@contextmanager
#def demo2(label):
#    start = time.time()
#    try:
#        yield
#    finally:
#        end = time.time()
#        print('{}: {}'.format(label, end - start))
#        
#with demo2("counting"):
#    n = 1000000
#    while n > 0:
#        n -= 1
    
