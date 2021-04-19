def frequentwords_with_mismatches(text: str, k: int, d: int):
    """Finds all most frequent k-mers with up to d mismatches"""
    from neighbors import neighbors

    freqmap = dict()
    textlength = len(text)

    # Generates freqmap for all neighbors in all windows in text
    for i in range(textlength - k):
        window = text[i:k+i]
        neighborhood = neighbors(window, d)
        for neighbor in neighborhood:
            if neighbor in freqmap:
                freqmap[neighbor] += 1
            else:
                freqmap[neighbor] = 1

    # gets the most frequent keys from freqmap
    keys, values = freqmap.keys(), freqmap.values()
    maxvalue = max(values)
    maxpatterns = [key for key, value in freqmap.items() if value == maxvalue]

    return maxpatterns


if __name__ == '__main__':
    text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
    k = 4
    d = 1
    print(' '.join(frequentwords_with_mismatches(text, k, d)))