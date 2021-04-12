def frequencytable(text, k):
    kmers = {}

    for i in range(len(text) - (k + 1)):
        kmer = text[i:i + k]
        if kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1

    return kmers


def findclumps(text, k, L, t):
    patterns = set()

    for i in range(len(text) - L + 1):  # parse entire genome minus L
        window = text[i:i+L]
        freqmap = frequencytable(window, k)  # freq table of kmers of size k in that window
        for kmer in freqmap:
            if freqmap[kmer] >= t:
                patterns.add(kmer)

    return patterns


if __name__ == '__main__':
    text = 'CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC'
    k = 5
    #print(frequencytable(text, k))
    x = findclumps(text, k, 75, 4)
    print(' '.join([x for x in x]))