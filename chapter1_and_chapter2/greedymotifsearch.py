from scipy.stats import entropy


def greedy_motif_search(text: str, k: int, t: int):
    """
    text = DNA strings to parse
    k = size of kmer
    t = number of strings in text
    """
    from profile_most_probable_kmer import find_profile_most_probable_kmer
    from findclumps import frequencytable
    from hammingdistance import hammingdistance
    # split text string into list
    text_strings: List[str] = split_string_on_newline(text)

    # find first motif in each string in dna of length k
    first_motifs = [string[:k] for string in text_strings]
    best_motifs = first_motifs

    all_kmers_in_first_dna_string: List[str] = list(frequencytable(text_strings[0], k))

    best_motifs = []
    best_score = k*t
    for kmer in all_kmers_in_first_dna_string:
        motif1 = kmer
        for i in range(1, t):
            i + 0
            # profile = from motif1 ... motif i-1
            # motifi = find_profile_most_probable_kmer(text[i], k, profile)
        #motifs = from motif1 ... motif t
        #motifs_score = calculate score(motifs), the total hammingdistance
        motifs_score = 0
        if motifs_score < best_score:
            best_motifs = best_motifs
            best_score = motifs_score

    return best_motifs


    # if profile_most_probable_kmer returns None (because probability of match is zero)
    # then select first kmer (could this loop endlessly?)
    # repeat for all strings in dna
    # after finishing a loop selecting all profile_most_probable_kmers, score the set of motifs and save
    # Lastly , re-calculate the profile
    # then repeat the loop

    # After finishing all loops, select the set of motifs with the best (lowest) score (entropy)
    # entropy(list[floats], base=2) to run entropy

    return all_kmers_in_first_dna_string


def create_profile(text: str, k: int):
    """Create probability profile for a string"""
    from findclumps import frequencytable
    # where i is each position in the consensus string profile
    string_counts = {i: {'A': 0, 'C': 0, 'G': 0, 'T': 0} for i in range(k)}
    probability_profile = string_counts
    for i, base in enumerate(text):
        if base in string_counts[i]:
            string_counts[i][base] += 1

    # calculate profile at each position
    # count each base at each position. Calculate the probability of each base by taking (count_each_base / t)
    #

    # count all

    return string_counts


def split_string_on_newline(seqs: str):
    return seqs.split('\n')


if __name__ == '__main__':
    text = '''GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG'''
    #print(greedy_motif_search(text, 3, 5))
    #print(split_string_on_newline(text))
    print(create_profile('GGC', 3))