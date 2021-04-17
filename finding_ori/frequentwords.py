def frequentwords(text: str, k: int) -> str:
    """Find the most frequent kmers of length k in a string"""
    kmers = {}

    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        if kmer in kmers:
            kmers[kmer] += 1
        else:
            kmers[kmer] = 1

    keys, values = kmers.keys(), kmers.values()
    max_value = max(values)
    max_keys = [key for key, v in kmers.items() if v == max_value]

    return ' '.join(max_keys)

if __name__ == '__main__':
    text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    k = 4
    print(frequentwords(text, k))
