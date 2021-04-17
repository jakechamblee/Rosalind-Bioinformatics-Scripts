def neighbors(pattern: str, d: int) -> set:
    """Return all combinations which match a given pattern with < d mismatches"""
    from hammingdistance import hammingdistance
    if d == 0:
        return len(pattern)

    # base case which is returned at bottom of recursion
    if len(pattern) == 1:
        return {'A', 'T', 'C', 'G'}

    neighborhood = set()
    suffixneighbors = neighbors(pattern[1:], d)

    for neighbor in suffixneighbors:
        if hammingdistance(pattern[1:], neighbor) < d:
            # If they are a match, add all possible combinations
            for base in {'A', 'G', 'C', 'T'}:
                neighborhood.add(base+neighbor)
        else:
            # If they are not a match, then only one possible combination
            neighborhood.add(pattern[0]+neighbor)

    return neighborhood


if __name__ == '__main__':
    text = 'TTA'
    d = 1
    x = neighbors(text, d)
    print(neighbors(text, d))
    print(' '.join([i for i in x]))