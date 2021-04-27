from typing import Dict


def profile_most_probable_kmer(text: str, k: int, profile: list):
    """Find a profile-most probable kmer in a string.

    i.e. the kmer that is most likely to be generated in text, given the profile
    """
    profile: Dict[str, int] = parse_profile_input_to_list(profile)
    # find all possible kmers in text of size k
    kmers: set = find_all_possible_kmers(text, k)
    # find the probability of each kmer given profile
    for kmer in kmers:
        for i in range(k):
            base_at_i: str = kmer[i]
            probability_of_base_given_profile = profile[base_at_i][i]

    # return the most probable kmer

    return None


def find_all_possible_kmers(text: str, k: int) -> set:
    from chapter1_and_chapter2.findclumps import frequencytable

    kmers_in_text = set()
    for line in text:
        kmers_in_line: List[str] = [key for key in frequencytable(line, k).keys()]
        for kmer in kmers_in_line:
            kmers_in_text.add(kmer)

    return kmers_in_text


def parse_profile_input_to_list(prof_split: str) -> dict[str, list[float]]:
    prof_split = prof_split.splitlines()
    prof_split = [i.split(' ') for i in prof_split]
    alanine, guanine = {'A': [float(i) for i in prof_split[0]]}, {'G': [float(i) for i in prof_split[1]]}
    cytosine, thymine = {'C': [float(i) for i in prof_split[2]]}, {'T': [float(i) for i in prof_split[3]]}

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
    print(parse_profile_input_to_list(prof))
