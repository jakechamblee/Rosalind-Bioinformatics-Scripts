from typing import List
from hammingdistance import hammingdistance


def approximatepatterncount(pattern: str, text: str, d: int):
    '''Finds the starting positions where a given pattern appears as a substring with up to d mismatches'''
    # d refers to the maximum allowable hamming distance
    matches: List[str] = []
    patternlength: int = len(pattern)

    for i, _ in enumerate(text[:(len(text) - patternlength + 1)]):
        if hammingdistance(text[i:patternlength + i], pattern) <= d:
            matches.append(str(i))

    return len(matches)

if __name__ == '__main__':
    text1 = 'AAAAA'
    text2 = 'AACAAGCTGATAAACATTTAAAGAG'
    print(approximatepatterncount(text1, text2, 2))