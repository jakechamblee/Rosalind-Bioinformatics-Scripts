import pytest
from patterncount import patterncount
from frequentwords import frequentwords


class TestPatternCount:

    def test_patterncount_beginning_middle_and_end_of_string_cases(self):
        text = 'ATACATAGATA'
        pattern = 'ATA'
        assert patterncount(text, pattern) == 3

    def test_patterncount_finds_overlapping_occurrences(self):
        text = 'ATAATATATCCATA'
        pattern = 'ATA'
        assert patterncount(text, pattern) == 4


class TestFrequentWords:

    def test_frequent_words_finds_max_kmers(self):
        text = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'
        size = 4
        assert frequentwords(text, size) == 'GCAT CATG'
