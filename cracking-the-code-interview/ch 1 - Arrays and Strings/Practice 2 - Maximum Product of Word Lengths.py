from itertools import combinations


def maxProduct(words):
    wordsMap = {}
    for word in words:
        bitVector = 0
        for char in word:
            charIdx = ord(char) - ord("a")
            bitVector |= 1 << charIdx
        wordsMap[word] = bitVector

    maxProduct = 0
    for word1, word2 in combinations(wordsMap.keys(), 2):
        bitVector1 = wordsMap[word1]
        bitVector2 = wordsMap[word2]
        if bitVector1 & bitVector2 == 0:
            maxProduct = max(maxProduct, len(word1) * len(word2))

    return maxProduct


input = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
output = maxProduct(input)
print(f"\ninput: {input}")
print(f"output: {output}")
