def paintFill(screen, r, c, newColor):
    currentColor = screen[r][c]
    if currentColor == newColor:
        return False
    return fill(screen, r, c, currentColor, newColor)


def fill(screen, r, c, replaceColor, newColor):
    if pointOutOfBounds(screen, r, c):
        return False

    currentColor = screen[r][c]
    if currentColor == replaceColor:
        screen[r][c] = newColor
        fill(screen, r - 1, c, replaceColor, newColor)
        fill(screen, r, c - 1, replaceColor, newColor)
        fill(screen, r + 1, c, replaceColor, newColor)
        fill(screen, r, c + 1, replaceColor, newColor)
    return True


def pointOutOfBounds(screen, r, c):
    return r < 0 or r >= len(screen) or c < 0 or c >= len(screen[0])


screen = [
    ["green", "red", "green"],
    ["red", "green", "green"],
    ["green", "green", "green"],
]

r = 1
c = 1
color = "blue"
paintFill(screen, r, c, color)

print(screen)
