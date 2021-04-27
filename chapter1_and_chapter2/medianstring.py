from findclumps import frequencytable
from distancebetweenpatternandstrings import distance_between_pattern_and_multiple_strings


def median_string(k: int, seqs: str) -> str:
    """Find kmer that minimizes summed hamming distances among all possible kmers, across all passed seqs.

    O(4**k *n*k*t) complexity
    """

    dna = split_string_on_newline(seqs)  # because of input format
    kmers_in_dna = set()

    # Generates all possible kmers in passed seqs of size k
    for line in dna:
        kmers_in_line: List[str] = [key for key in frequencytable(line, k).keys()]
        for kmer in kmers_in_line:
            kmers_in_dna.add(kmer)

    distance = float('inf')
    # Finds kmer with smallest hamming distance across passed seqs
    for kmer in kmers_in_dna:
        minimized_summation_of_kmer_distances: int = distance_between_pattern_and_multiple_strings(kmer, dna)
        if distance > minimized_summation_of_kmer_distances:
            distance = minimized_summation_of_kmer_distances
            median = kmer

    return median


def split_string_on_newline(seqs: str):
    return seqs.split('\n')


if __name__ == '__main__':
    k = 3
    text = '''AAATTGACGCAT
            GACGACCACGTT
            CGTCAGCGCCTG
            GCTGAGCACCGG
            AGTTCGGGACAG'''
    print(median_string(k, text))