# Question: Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

# Example 1:
# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"

# Example 2:
# Input: String="abdabca", Pattern="abc"
# Output: "abc"
# Explanation: The smallest substring having all characters of the pattern is "abc".

# Example 3:
# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.


def find_substring(str, pattern):
    matched = 0
    window_start = 0
    substr_start = 0
    min_length = len(str) + 1
    char_freq = {}

    for char in pattern:
        if char not in char_freq:
            char_freq[char] = 0
        char_freq[char] += 1

    for window_end in range(len(str)):
        right_char = str[window_end]
        if right_char in char_freq:
            char_freq[right_char] -= 1
            if char_freq[right_char] == 0:
                matched += 1

        while matched == len(char_freq):
            subStringLength = window_end - window_start + 1
            if subStringLength < min_length:
                min_length = subStringLength
                substr_start = window_start

            left_char = str[window_start]
            window_start += 1
            if left_char in char_freq:
                if char_freq[left_char] == 0:
                    matched -= 1
                char_freq[left_char] += 1
    if min_length > len(str):
        return ""
    return str[substr_start : substr_start + min_length]


print(find_substring("aabdec", "abc"))
print(find_substring("abdabca", "abc"))
print(find_substring("adcad", "abc"))