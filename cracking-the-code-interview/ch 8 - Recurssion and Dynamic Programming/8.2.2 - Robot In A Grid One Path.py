def getAllPaths(maze):
    allPaths = []
    if maze and len(maze) != 0:
        getAllPathsHelper(maze, len(maze) - 1, len(maze[0]) - 1, allPaths)
    return allPaths


def getAllPathsHelper(maze, r, c, allPaths, currentPath=[]):
    if r >= 0 and c >= 0 and maze[r][c]:
        currentPath.append((r, c))

        atOrigin = r == 0 and c == 0
        if atOrigin:
            allPaths.append(currentPath)

        getAllPathsHelper(maze, r - 1, c, allPaths, currentPath.copy())
        getAllPathsHelper(maze, r, c - 1, allPaths, currentPath.copy())


maze = [[True, True], [True, True]]
for result in getAllPaths(maze):
    print(result)
