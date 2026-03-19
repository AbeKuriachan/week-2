array = [-10,-5,1,10,3,25,7,11,0]

#function for returning max and min value from a list
def min_max(arr:list):
    min_value=arr[0]
    max_value=arr[0]
    for i in arr:
        if i < min_value:
            min_value=i
        if i > max_value:
            max_value=i
    return min_value,max_value

#function demo
minimum,maximum=min_max(array)
print(f"min: {minimum}, max: {maximum}")


def reverse(num:int):
    rev=0
    while num>0:
        digit=num%10
        num=num//10
        rev=rev*10+digit
    return rev

#palindrome checking
number=121
reversed_num=reverse(number)
if number==reversed_num:
    print(f"number: {number} is palindrome")
else:
    print(f"number: {number} is not palindrome")


def tuples_to_dict(tuples_list):
    result = {}

    for item in tuples_list:
        key = item[0]
        value = item[1]
        result[key] = value

    return result

#function demo
data = [("a", 1), ("b", 2), ("c", 3)]
print("dictionary created from tuple: ",tuples_to_dict(data))


def max_key(d):
    max_k = None
    max_v = None

    for key in d:
        if max_v is None or d[key] > max_v:
            max_v = d[key]
            max_k = key

    return max_k


# Example usage
d = {"a": 10, "b": 25, "c": 15}
print("max key is: ",max_key(d))


def calc_stats(*args):
    total = 0
    count = 0

    for num in args:
        total += num
        count += 1

    if count == 0:
        return (0, 0)

    avg = total / count
    return (f"sum:{total},avg:{avg}")


# Example usage
print(calc_stats(10, 20, 30, 40))


def top_student(**kwargs):
    max_name = None
    max_marks = None

    for name in kwargs:
        if max_marks is None or kwargs[name] > max_marks:
            max_marks = kwargs[name]
            max_name = name

    return max_name, max_marks


# Example usage
print(top_student(Alice=85, Bob=92, Charlie=88))




