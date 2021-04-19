from typing import List


def bruteforce_motif_find(dna: str, k: int, d: int) -> str:
    """Find all (k, d) motifs that appear in all passed strings, of length k, with <= d mismatches."""
    from neighbors import neighbors
    from findclumps import frequencytable
    from approximatepatternmatching import approximatepatternmatching

    dna: List[str] = dna.split('\n')  # needed because of the weird form of the input
    patterns = set()

    all_possible_kmers_of_length_k: List[str] = list(frequencytable(dna[0], k))
    for kmer in all_possible_kmers_of_length_k:
        kmer_neighbors: List[str] = list(neighbors(kmer, d))
        for motif in kmer_neighbors:
            # Adds only if motif matches all lines in dna (with up to d mismatches)
            if all([approximatepatternmatching(motif, line, d) for line in dna]):
                patterns.add(motif)

    return patterns


if __name__ == '__main__':
    text = '''ATTTGGC
TGCCTTA
CGGTATC
GAAAATT'''
    print(' '.join(bruteforce_motif_find(text, k=3, d=1)))
