from typing import Dict


def profile_most_probable_kmer(text: str, k: int, profile: list):
    """Find a profile-most probable kmer in a string.

    i.e. the kmer that is most likely to be generated in text, given the profile
    """
    from math import prod

    profile: Dict[str, int] = parse_profile_input_to_list(profile)
    # find all possible kmers in text of size k
    kmers: set = find_all_possible_kmers(text, k)
    # find the probability of each kmer given profile
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

    return most_likely_kmer


def find_all_possible_kmers(text: str, k: int) -> set:
    from findclumps import frequencytable
    kmers_in_text: dict = frequencytable(text, k)

    return kmers_in_text


def parse_profile_input_to_list(prof_split: str) -> dict:
    prof_split = prof_split.splitlines()
    prof_split = [i.split(' ') for i in prof_split]
    alanine, cytosine = {'A': [float(i) for i in prof_split[0]]}, {'C': [float(i) for i in prof_split[1]]}
    guanine, thymine = {'G': [float(i) for i in prof_split[2]]}, {'T': [float(i) for i in prof_split[3]]}

    # merge the dictionaries
    new_profile = {**alanine, **guanine, **cytosine, **thymine}

    return new_profile


if __name__ == '__main__':
    txt = 'ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT'
    prof = '''0.2 0.2 0.3 0.2 0.3
0.4 0.3 0.1 0.5 0.1
0.3 0.3 0.5 0.2 0.4
0.1 0.2 0.1 0.1 0.2'''
    print(profile_most_probable_kmer(txt, 5, prof))
    #print(parse_profile_input_to_list(prof))
    #print(find_all_possible_kmers(txt, 5))