#Description: Create a function called concat_tuples that takes two tuples as input and returns a new tuple containing all elements from both input tuples.
# Ensure that the function works correctly with tuples of different lengths.

def concat_tuples(tuples1,tuples2):
    return tuples1 + tuples2

tuplea = (1,2,3)

tupleb = (4,5,6)

results = concat_tuples(tuplea,tupleb)
print('Concatented tuple: ',results)






