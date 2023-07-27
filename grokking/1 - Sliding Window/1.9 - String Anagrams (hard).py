# Question: Given a string and a pattern, find all anagrams of the pattern in the given string.
# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:
#     abc
#     acb
#     bac
#     bca
#     cab
#     cba

# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Example 1:
# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".

# Example 2:
# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".


def find_string_anagrams(s, pattern):
    window_start, matched = 0, 0
    char_frequency = {}

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    # Try to extend the range [window_start, window_end]
    for window_end in range(len(s)):
        right_char = s[window_end]
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1

        if matched == len(char_frequency):
            result = []
            for i in range(window_start, window_end + 1):
                result.append(i)
            return result

        # Shrink the window by one character
        if window_end >= len(pattern) - 1:
            left_char = s[window_start]
            window_start += 1
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1

    return []


def main():
    print(find_string_anagrams("ppqp", "pq"))
    print(find_string_anagrams("abbcabc", "abc"))


main()
