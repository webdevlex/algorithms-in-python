def powerSet(set, result=[[]]):
    if len(set) != 0:
        firstItem = set.pop(0)
        powerSet(set, result)
        for i in range(len(result)):
            newItem = result[i].copy()
            newItem.append(firstItem)
            result.append(newItem)
    return result


set = ["a", "b", "c"]
print(powerSet(set))
