num = [1, 4, -5, 10, -7, 2, 3, -1]
filtered_and_squared = []

# normal expression with if 
for number in num:
    if number > 0:
        filtered_and_squared.append(number ** 2)
        
print filtered_and_squared

# optimistic with lambda expression
filtered_and_squared = map(lambda x: x ** 2, filter(lambda x:x > 0, num))
print filtered_and_squared

# more optimistic with comprehension expression
filtered_and_squared = [x ** 2 for x in num if x > 0]
print filtered_and_squared

# best optimistic with generator objector
def square_generator(optional_parameter):
    return (x ** 2 for x in num if x > optional_parameter)

g = list(square_generator(0))
print g


alist = ['a1', 'a2', 'a3']
blist = [1, 2, 3]

for a, b in zip(alist, blist):
    print a, b
    
