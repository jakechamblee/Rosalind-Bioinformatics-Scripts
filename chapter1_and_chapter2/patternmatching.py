from typing import List


def patternmatching(text: str, pattern: str) -> str:
    '''Find the indexes where a pattern appears in a text'''
    from reverse_complement import reverse_complement

    pattern_rev_complement: str = reverse_complement(pattern)
    k: int = len(pattern)
    indexes_of_matches: List[str] = [str(i) for i in range(len(text)) if (text[i:i + k] == pattern or text[i:i + k] == pattern_rev_complement)]
    # indexes_of_matches: List[str] = [str(i) for i in range(len(text)) if text[i:i + k] == pattern]
    return ' '.join(indexes_of_matches)


if __name__ == '__main__':
    text = 'GATATATGCATATACTTTATAGATATC'
    pattern = 'GAT'
    print(patternmatching(text, pattern))
