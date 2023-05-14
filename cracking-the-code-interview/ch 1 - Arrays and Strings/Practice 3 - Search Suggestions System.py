def searchSuggestionSystem(products, searchWord):
    products.sort()
    lenOfSubstring = 0
    substring = ""
    result = []
    for char in searchWord:
        lenOfSubstring += 1
        substring += char
        wordMatches = []

        i = 0
        while len(wordMatches) < 3 and i < len(products):
            currentProduct = products[i]
            if currentProduct[0:lenOfSubstring] == substring:
                wordMatches.append(currentProduct)
                i += 1
            else:
                products.remove(currentProduct)

        result.append(wordMatches)

    return result


# products = ["mobile", "mouse", "moneypot", "montior", "mousepad"]
# searchWord = "mouse"

# products = ["havana", "mouse", "moneypot", "montior", "mousepad"]
# searchWord = "havana"

print(f"\ninput: products = {products}, searchWord = '{searchWord}'")
output = searchSuggestionSystem(products, searchWord)
print(f"output: {output}")
