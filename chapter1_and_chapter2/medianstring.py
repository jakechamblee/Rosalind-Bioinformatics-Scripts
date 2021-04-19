from findclumps import frequencytable
from distancebetweenpatternandstrings import distancebetweenpatternandstrings


def median_string(k: int, seqs: str) -> str:
    """Find kmer that minimizes summed hamming distances among all possible kmers, across all passed seqs."""

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
        minimized_summation_of_kmer_distances: int = distancebetweenpatternandstrings(kmer, dna)
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