def printWordsVertically(s):
    words = s.split(" ")
    mx = max(len(word) for word in words)
    ans = []
    for i in range(mx):
        l = []
        for word in words:
            l.append(word[i] if i < len(word) else " ")
        ans.append("".join(l).rstrip())
    return ans


input = "CONTEST IS COMING"
output = printWordsVertically(input)
print(f"\ninput: {input}")
print(f"output: {output}")
