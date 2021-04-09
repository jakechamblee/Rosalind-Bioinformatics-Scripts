def hammingdistance(text1: str, text2: str) -> int:
    difference = 0
    if len(text1) != len(text2):
        return None
        #raise ValueError('Strings must have equal length to compute Hamming distance')

    for i, base in enumerate(text1):
        if not text2[i] == base:
            difference += 1
    return difference


if __name__ == '__main__':
    text1 = 'GGGCCGTTGGT'
    text2 = 'GGACCGTTGAC'
    print(hammingdistance(text1, text2))