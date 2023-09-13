def hackerTeam(team_a, team_b):
    result = 0
    for i in range(len(team_a)):
        currentResult = 0
        currentValue = 0
        for j in range(i, len(team_a)):
            if team_a[j] >= currentValue and team_a[j] <= team_b[j]:
                currentResult += 1
                currentValue = team_a[j]
            elif team_b[j] >= currentValue:
                currentResult += 1
                currentValue = team_b[j]
            else:
                break
        if currentResult > result:
            result = currentResult
    return result


print(hackerTeam([5, 2, 4, 1], [3, 5, 2, 2]))
print(hackerTeam([2, 7, 3], [4, 2, 6]))
print(hackerTeam([9, 7], [10, 8]))
