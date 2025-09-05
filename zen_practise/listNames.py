l1 = ['orange', 'apple', 'banana', 'kiwi', 'mango']

for index, value in enumerate(l1, start=1):
    l1[3] = 'grape'
    print(f'{index}. {value}')

# mem usage understanding of python 
import sys 
print(sys.getsizeof(l1))
print(sys.getsizeof(l1[0]))
print(sys.getsizeof(l1[1]))
print(sys.getsizeof(l1[2]))
print(sys.getsizeof(l1[3]))

#memory address of the list and its elements
print(id(l1))   
print(id(l1[0]))
print(id(l1[1]))
print(id(l1[2]))
print(id(l1[3]))