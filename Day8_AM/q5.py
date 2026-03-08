
'''The bug is that multiple if statements are used instead of an if-elif chain.
Because of this, every condition is checked independently,
and the variable grade keeps getting overwritten.'''


#Fix

score = 85

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(grade)