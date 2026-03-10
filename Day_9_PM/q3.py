def unique_to_each(a, b):
    result = set(a) - set(b)
    return list(result)

'''The bug is that current result is computing only the elements which are exclusive to set a. set a - set b
will compute only elements which are present inside the set a'''

#fix

def new_unique_to_each(a, b):
    result_a = set(a) - set(b)
    result_b = set(b) - set(a)
    result= result_a.union(result_b)
    return list(result)


