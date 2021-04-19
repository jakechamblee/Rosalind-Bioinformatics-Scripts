def reverse_complement(text: str) -> str:
    reverse = text[::-1]
    # Must replace with lowercase letters to avoid reverting the previous method's replacements
    return reverse.replace('G', 'c').replace('C', 'g').replace('T', 'a').replace('A', 't').upper()


if __name__ == '__main__':
    text = 'ATGGCCTA'
    print(reverse_complement(text))