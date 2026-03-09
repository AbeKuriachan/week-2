def rotate_list(lst, k):
    if not lst:
        return lst

    k = k % len(lst)   # Handle k > len(lst)

    return lst[-k:] + lst[:-k]


# Example
print(rotate_list([1,2,3,4,5], 10))