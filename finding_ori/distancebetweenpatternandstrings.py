from typing import Dict


def distancebetweenpatternandstrings(pattern: str, dna: str) -> int:
    '''Calculate minimized summation of hamming distances between a pattern and all DNA strings'''
    from hammingdistance import hammingdistance
    from findclumps import frequencytable

    kmer_length: int = len(pattern)
    distance: int = 0
    for line in dna:
        hamm_distance = float('inf')
        # Find every kmer in each line, then find minimum hamming distance in that line
        kmers_in_line: Dict[str, int] = frequencytable(line, kmer_length)
        for kmer in kmers_in_line:
            if hamm_distance > hammingdistance(pattern, kmer):
                hamm_distance = hammingdistance(pattern, kmer)
        distance += hamm_distance

    return distance


def split_dna(dna: str):
    '''Splits a whitespace separated string into a list'''
    return dna.split(' ')


def all_strings(k):
    return None


if __name__ == '__main__':
    p = 'AAA'
    d = 'TTACCTTAAC GATATCTGTC ACGGCGTTCG CCCTAAAGAG CGTCAGAGGT'
    print(distancebetweenpatternandstrings(p, split_dna(d)))
