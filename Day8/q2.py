def find_pairs(numbers, target):
    seen = set()
    pairs = []

    for num in numbers:
        complement = target - num

        if complement in seen:
            pairs.append((complement, num))

        seen.add(num)

    return pairs

print(find_pairs([1, 2, 3, 4, 5], 6))