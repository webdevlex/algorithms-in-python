def insertion(n, m, i, j):
    mask = 0b1 << ((j - i) + 1)
    mask -= 1
    mask <<= i
    n &= ~mask
    m <<= i
    n |= m


insertion(0b111111, 0b00, 2, 3)
