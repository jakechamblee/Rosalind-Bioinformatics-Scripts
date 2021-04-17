def patterncount(txt:str, pattern: str) -> int:
    """Count the number of occurences of a pattern in a string."""
    count = 0
    txt_length = len(txt)
    pattern_length = len(pattern)

    # Must add +1 to scan up to the last nucleotide in txt as the second index is non-inclusive in Python indexing
    for i in range(txt_length - pattern_length + 1):
        if txt[i:(i+pattern_length)] == pattern:
            count += 1
    return count

if __name__ == '__main__':
    text = 'GTTACTCCTAATTACTCCGATTACTCCTATTACTCCAATCGGGTTACTCCTTTGTTTACTCCTTACTCCTTACTCCTTACTCCCGTTACTCCATCGAATTACTCCGTTACTCCGCTTACTCCCCTGTTTATTACTCCTCTGGCTTTACTCCATTACTCCGTTACTCCCAGTTACTCCCCTCCCGAGTTACTCCGTTACTCCTTACTCCCGAGTTACTCCAAAGTTTACTCCGAGCGTTTACTCCAAGGTTACTCCGATTACTCCCGAACTTACTCCATTTTACTCCTTACTCCGAGCCTTACTCCTCTTACTCCTTACTCCCTTACTCCTTTACTCCTTACTCCTGATACTTACTCCCCCGTTACTCCCTTACTCCGAAATATTTTACTCCAGGTTACTCCACGTTACTCCACCCCTTACTCCATTCTCGAATTCGTCTTACTCCTTCATTACTCCAGTTACTCCTTACTCCGAGCGCTTACTCCATTACTCCTGTTACTCCCTGACGATATGAGTTACTCCTTTACTCCGTTTACTCCTCTTACTCCGGCTTACTCCGGTTACTCCTGTTTTACTCCGATTACTCCATGGTTTACTCCATTACTCCGCGAGGTTACTCCATTACTCCCATTACTCCTATTACTCCATTACTCCGCGGTTACTCCCTATTACTCCTTTACTCCGTTACTCCTTTACTCCTTACTCCTTACTCCACTTACTCCTAATTACTCCTTACTCCTTACTCCGAATTACTCCACCCGTTACTCCTATTACTCCCATTACTCCTTTTACTCCCTTACTCCCTTACTCCTATTACTCCGATTACTCCAATTTAGTCTTACTCCCGCCGTTACTCCCCTTACTCCTTACTCCGTTACTCCGCTTTACTCCATTACTCCTTACTCCCTTACTCCGGTTACTCCCGGGTCTTACTCCTAAAACCAGA'
    pattern = 'TTACTCCTT'
    print(patterncount(text, pattern))