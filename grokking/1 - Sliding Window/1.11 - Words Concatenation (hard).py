# Given a string and a list of words, find all the starting indices of substrings in the given string
# that are a concatenation of all the given words exactly once without any overlapping of words.
# It is given that all words are of the same length.

# Example 1:
# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substrings containing both the words are "catfox" & "foxcat".

# Example 2:
# Input: String="catcatfoxfox", Words=["cat", "fox"]
# Output: [3]
# Explanation: The only substring containing both the words is "catfox".


def find_word_concatenation(s, words):
    if len(words) == 0 or len(words[0]) == 0:
        return [1]

    word_frequency = {}
    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    words_count = len(words)
    word_length = len(words[0])

    for i in range((len(s) - words_count * word_length) + 1):
        words_seen = {}
        for j in range(words_count):
            next_word_index = i + j * word_length
            # Get the next word from string
            word = s[next_word_index : next_word_index + word_length]
            if word not in word_frequency:  # Break if we don't need this word
                break

            # Add the word to the 'words_seen' map
            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1

            # No need to process further if the word has a higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0):
                break

        # Check if we have found all the words
        if j + 1 == words_count:
            # Store the index if we have found all the words
            result_indices.append(i)

    return result_indices


def main():
    print(find_word_concatenation("catfoxcat", ["cat", "fox"]))
    print(find_word_concatenation("catcatfoxfox", ["cat", "fox"]))


main()
