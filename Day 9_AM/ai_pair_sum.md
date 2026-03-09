# AI Pair Sum Analysis

## 1️ Prompt Used

"Write a Python function that finds all pairs in a list that sum to a target number using list comprehensions."

---

# 2️ AI Generated Code

def pair_sum(nums, target):
    return [(a, b) for a in nums for b in nums if a + b == target]

# 3 Issues

Problems Observed after test 1: print(pair_sum([1,2,3,4,5], 6))

Duplicate pairs

(1,5) and (5,1)
(2,4) and (4,2)

Invalid pair

(3,3)

But there is only one 3 in the list, so this pair should not exist.

# 4 Corrected code

def pair_sum(nums, target):
    pairs = [(nums[i], nums[j])
             for i in range(len(nums))
             for j in range(i+1, len(nums))
             if nums[i] + nums[j] == target]

    return pairs


#more efficient solution using set

def pair_sum(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num

        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))

        seen.add(num)

    return list(pairs)