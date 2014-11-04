# -*- coding: utf-8 -*-
from nose.tools import assert_equal
from domplus import utilplus


def test_get_digits():
    """
    Test get_digits
    """
    assert_equal("0123", utilplus.get_digits("a0b1c2d3"))
    assert_equal("0123", utilplus.get_digits("-0+1=2/3"))
    assert_equal("", utilplus.get_digits(""))
    assert_equal("123", utilplus.get_digits(12.3))


def test_valid_br_cpf():
    """
    Test valid_br_cpf
    """
    # True
    assert_equal(True, utilplus.valid_br_cpf('03167158590'))
    assert_equal(True, utilplus.valid_br_cpf('467.368.255-63'))

    # False
    for i in range(10):
        text = str(i) * 11
        yield check_br_cpf_False, text

    yield check_br_cpf_False, 46736825563  # no string
    yield check_br_cpf_False, '467.368.255/63'  # special character =! . or -
    yield check_br_cpf_False, '467368255638'  # > 11 digits
    yield check_br_cpf_False, '4673682556'  # < 11 digits


def check_br_cpf_False(cpf):
    assert_equal(False, utilplus.valid_br_cpf(cpf))
