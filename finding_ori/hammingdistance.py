def hammingdistance(text1: str, text2: str) -> int:
    '''Finds the total character difference between two strings'''
    difference = 0
    if len(text1) != len(text2):
        return 10000  # arbitrarily large number

    for i, base in enumerate(text1):
        if not text2[i] == base:
            difference += 1
    return difference


if __name__ == '__main__':
    text1 = 'GGGCCGTTGGT'
    text2 = 'GGACCGTTGAC'
    print(hammingdistance(text1, text2))