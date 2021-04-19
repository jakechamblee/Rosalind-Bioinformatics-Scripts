from distancebetweenpatternandstrings import distancebetweenpatternandstrings, split_dna
from neighbors import neighbors
from findclumps import frequencytable
from distancebetweenpatternandstrings import distancebetweenpatternandstrings


def medianstring(k: int, dna: str) -> str:
    """Find kmer that minimizes summed hamming distances among all possible kmers, across all passed seqs."""

    dna = dna.split('\n')  # because of input format
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


if __name__ == '__main__':
    k = 3
    dna = '''AAATTGACGCAT
GACGACCACGTT
CGTCAGCGCCTG
GCTGAGCACCGG
AGTTCGGGACAG'''
    print(medianstring(k, dna))