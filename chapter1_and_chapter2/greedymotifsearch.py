from scipy.stats import entropy


def greedy_motif_search(text: str, k: int, t: int):
    """
    text = DNA strings to parse
    k = size of kmer
    t = number of strings in text
    """
    from findclumps import frequencytable
    from hammingdistance import hammingdistance
    # split text string into list
    text_strings: List[str] = split_string_on_newline(text)

    # find first motif in each string in dna of length k
    first_motifs = [string[:k] for string in text_strings]
    # best_motifs = first_motifs

    all_kmers_in_first_dna_string: List[str] = list(frequencytable(text_strings[0], k))

    best_motifs = []
    best_score = k*t
    for kmer in all_kmers_in_first_dna_string:
        motif1 = kmer
        motifs = []
        motifs.append(kmer)
        profile = create_profile(kmer, k, t)  # list comprehension here?
        # find most probable kmer in the next string in dna
        for i in range(1, t):
            # using the profile made from dna1's kmer, find profile_most_probably_kmer for all dna strings (dnai...dnat)
            # find_profile_most_probable_kmer expects profile in the format of a string..
            # need to recode a form that expects the output of create_profile()
            motifs.append(find_profile_most_probable_kmer(text[i], k, profile))
            profile = create_profile(text[i], k, t)
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


def create_profile(text: str, k: int, t: int):
    """Create probability profile for a string"""
    from findclumps import frequencytable
    # where i is each position in the consensus string profile
    string_counts = [{'A': 0, 'C': 0, 'G': 0, 'T': 0} for i in range(k)]
    probability_profile = string_counts
    for i, base in enumerate(text):
        if base in string_counts[i]:
            string_counts[i][base] += 1
        # To get probability of each base at each position i
        string_counts[i][base] = string_counts[i][base]/t

    return string_counts


def calculate_score(motif1, motifs):
    from hammingdistance import hammingdistance

    return hammingdistance(motif1, motifs)


def find_profile_most_probable_kmer(text: str, k: int, profile: list):
    """Find a profile-most probable kmer in a string.

    i.e. the kmer that is most likely to be generated in text, given the profile
    """
    from math import prod

    profile = profile
    kmers: set = find_all_possible_kmers(text, k)
    lowest_kmer_probability = 0
    most_likely_kmer = None

    for kmer in kmers:
        kmer_probabilities = []

        for i in range(k):
            base_at_i: str = kmer[i]
            probability_of_base_at_position_i_given_profile = profile[base_at_i][i]
            kmer_probabilities.append(probability_of_base_at_position_i_given_profile)

        kmer_probability: float = prod(kmer_probabilities)

        if kmer_probability > lowest_kmer_probability:
            lowest_kmer_probability = kmer_probability
            most_likely_kmer = kmer

    # necessary to handle cases where there is no match
    if most_likely_kmer is None:
        return kmers[0]

    return most_likely_kmer


def find_all_possible_kmers(text: str, k: int) -> set:
    from findclumps import frequencytable
    kmers_in_text: dict = frequencytable(text, k)

    return kmers_in_text


def split_string_on_newline(seqs: str):
    return seqs.split('\n')


if __name__ == '__main__':
    text = '''GGCGTTCAGGCA
AAGAATCAGTCA
CAAGGAGTTCGC
CACGTCAATCAC
CAATAATATTCG'''
    print(greedy_motif_search(text, 3, 5))
    #print(split_string_on_newline(text))
    print(create_profile('GGC', 3, 1))