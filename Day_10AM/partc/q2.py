from collections import defaultdict

def group_anagrams(words: list[str]) -> dict[str, list[str]]:
    groups = defaultdict(list)

    for word in words:
        key = ''.join(sorted(word))   # create anagram signature
        groups[key].append(word)

    return dict(groups)


# Example
print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))
