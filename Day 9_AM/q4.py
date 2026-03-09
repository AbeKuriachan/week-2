'''The problem occurs because you are modifying the list while iterating over it. This will create a
list index error'''

#fix


nums = [2,4,6,8]
nums = [n for n in nums if n % 2 != 0]
print(nums)