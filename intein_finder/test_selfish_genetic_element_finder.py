import pytest
import requests


class TestSelfishGeneticElementFinder:
    request = requests.get('https://www.ebi.ac.uk/interpro/wwwapi/entry/InterPro/')
    intein_request = requests.get(
        'https://www.ebi.ac.uk/interpro/wwwapi/entry/InterPro/?search=intein&page_size=100'
    ).json()
    transposase_request = requests.get(
        'https://www.ebi.ac.uk/interpro/wwwapi/entry/InterPro/?search=transposase&page_size=100'
    ).json()
    homing_endonuclease_request = requests.get(
        'https://www.ebi.ac.uk/interpro/wwwapi/entry/InterPro/?search=homing%20endonuclease&page_size=100'
    ).json()

    def test_basic_request_is_valid(self):
        assert self.request.status_code == 200

    def test_intein_pulling_limited_by_pagination(self):
        # If true, then need to add pagination logic to get all IPR domains b/c > 100 IPRs present
        intein_count = self.intein_request['count']
        assert intein_count <= 100

    def test_transposase_pulling_limited_by_pagination(self):
        transposase_count = self.transposase_request['count']
        assert transposase_count <= 100

    def test_homing_endonuclease_pulling_limited_by_pagination(self):
        homing_endonuclease_count = self.homing_endonuclease_request['count']
        assert homing_endonuclease_count <= 100
