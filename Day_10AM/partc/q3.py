from collections import defaultdict

def char_freq(text):
    freq = defaultdict(int) #fix for key error

    for char in text:
        freq[char] += 1


    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return sorted_freq


print(char_freq("banana"))
