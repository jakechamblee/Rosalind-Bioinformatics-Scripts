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

    #listpatterns = [i for i in patterns]
    return patterns
    #return listpatterns

    # this needs to now check, for each window, if any of the kmers in the freqtable appear >= t times
    # If so, append them to patterns. This does NOT need to track the position in the genome where these clumps occur.

if __name__ == '__main__':
    text = 'CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA'
    k = 5
    print(frequencytable(text, k))
    print(findclumps(text, k, 50, 4))