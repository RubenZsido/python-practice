from math import factorial, floor
import math


def countHomogenous(s):
    #dictionary of how many substrings are there and of what length
    map = {}
    prev_char = s[0]
    string_length = 0
    words = []
    curr_word = ""
    #count them
    for i in s:
        print(i)
        #continue
        if prev_char == i:
            string_length += 1
            curr_word = curr_word + i
            print("--added")
        #word is ended
        else:
            #end
            words.append(curr_word)
            curr_word = ""
            map[string_length] = map.get(string_length, 0) + 1
            print("--ended")
            #start new
            string_length = 1
            prev_char = i
            curr_word = i
    words.append(curr_word)
    curr_word = ""
    map[string_length] = map.get(string_length, 0) + 1
    print(map)
    print(words)
    sum = 0
    for key, value in map.items():
        sum += nCr(key, value)
    return floor(sum) 

def nCr(n, r):
    return factorial(n) / factorial(r) * factorial(n - r)

print(countHomogenous("abbcccaa"))
# 1: 1
# 2: 2
# 3: 1