def minimumskew(genome) -> str:
    # This works but is quite slow. Could be optimized such that you only parse O(n) times rather than O(2n).
    skew_total: int = 0
    skew_map = []

    for i, base in enumerate(genome):
        skew_map.append(skew_total)   # This needs to be at the start so that the skew starts at zero
        if base == 'G':
            skew_total += 1
        elif base == 'C':
            skew_total += -1

    # This section is to catch multiple minimums of the same value. May be useful later.
    minimum = min(skew_map)
    minimum_positions = [str(i) for i, v in enumerate(skew_map) if v == minimum]

    return ' '.join(minimum_positions)



if __name__ == '__main__':
    text = ''

    print(minimumskew(text))