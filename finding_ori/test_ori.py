import pytest
from patterncount import patterncount
from frequentwords import frequentwords
from reverse_complement import reverse_complement
from patternmatching import patternmatching


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


class TestPatternMatching:

    def test_patternmatching_finds_template_pattern_matches(self):
        text = 'GATACGATGAT'
        pattern = 'GAT'
        assert patternmatching(text, pattern) == '0 5 8'

    def test_patternmatching_finds_rev_complement_pattern_matches(self):
        text = 'GATAAAATCGAT'
        # rev complement of GAT is ATC
        pattern = 'GAT'
        assert patternmatching(text, pattern) == '0 6 9'

class TestBruteForceMotifFind:

    def test_(self):