# -*- coding: utf-8 -*-


def get_digits(text):
    """
    Accept an parameter string.
    Return only numerical characters
    """
    text = str(text)
    digits = ''
    for i in text:
        if i.isdigit():
            digits += i
    return digits


def valid_br_cpf(cpf):
    """
    Accept an string parameter cpf and
    Check if is brasilian CPF valid.
    Return True or False
    """
    # if cpf is string
    if not isinstance(cpf, basestring):
        return False

    cpf = cpf.replace('.', '')  # extract dots
    cpf = cpf.replace('-', '')  # extract stroke

    # if does not contain numerical characters
    for i in cpf:
        if not i.isdigit():
            return False
            break

    #  check if length == 11
    if len(cpf) != 11:
        return False

    # checks if all digits are equal
    for i in range(10):
        text = str(i) * 11
        if text == cpf:
            return False
            break

    # first checksum
    multi = 10
    result = 0

    for i in cpf[:9]:
        result = result + (int(i) * multi)
        multi = multi - 1

    remainder = result % 11

    if remainder < 2:
        checksum1 = 0
    else:
        checksum1 = 11 - remainder

    assemble_cpf = cpf[:9] + str(checksum1)

    # secound checksum
    multi = 11
    result = 0

    for i in assemble_cpf:
        result = result + (int(i) * multi)
        multi = multi - 1

    remainder = result % 11

    if remainder < 2:
        checksum2 = 0
    else:
        checksum2 = 11 - remainder

    assemble_cpf += str(checksum2)

    return True if cpf == assemble_cpf else False
