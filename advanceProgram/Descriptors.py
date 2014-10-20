import weakref

class Celsius(object):
    def __init__(self, value=0.0):
        self.value = float(value)
        print("I'm working!")
    def __get__(self, instance, owner):
         print("I'm working two!")
         return self.value
    def __set__(self, instance, value):
        print("I'm working finally!")
        self.value = float(value)
        
class Temperature(object):
    celsius = Celsius()

temp = Temperature()
temp.celsius

class lazyattribute(object):
    def __init__(self, f):
        self.data = weakref.WeakKeyDictionary()
        self.f = f
    def __get__(self, obj, cls):
        if obj not in self.data:
            self.data[obj] = self.f(obj)
        return self.data[obj]

class Foo(object):
    @lazyattribute
    def bar(self):
        print "Being lazy"
        return 42

f = Foo()
print f.bar

print "after set the value, not execute bar() function "

print f.bar        
