""" Tests for howdy.py """

import os
from subprocess import getstatusoutput

PRG = './salutations.py'


# --------------------------------------------------
def test_exists():
    """ Program exists """

    assert os.path.isfile(PRG)


# --------------------------------------------------
def test_usage():
    """ Prints usage """

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{PRG} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_defaults():
    """ Prints expected default values """

    rv, out = getstatusoutput(f'{PRG}')
    assert rv == 0
    assert out.strip() == 'Howdy, Stranger.'

