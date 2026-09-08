def hidenp(small: str, big: str) -> bool:
    i = 0
    j = 0

    while i < len(small) and j < len(big):
        if small[i] == big[j]:
            i += 1
        j += 1

    return i == len(small)