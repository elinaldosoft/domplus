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
    Check if is brazilian CPF valid.
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
        result += int(i) * multi
        multi -= 1

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
        result += int(i) * multi
        multi -= 1

    remainder = result % 11

    if remainder < 2:
        checksum2 = 0
    else:
        checksum2 = 11 - remainder

    assemble_cpf += str(checksum2)

    return True if cpf == assemble_cpf else False


def valid_br_cnpj(cnpj):
    """
    Accept an string parameter CNPJ and
    Check if is brazilian CNPJ valid.
    Return True or False
    """
     # if cnpj is string
    if not isinstance(cnpj, basestring):
        return False

    cnpj = cnpj.replace('.', '')  # extract dots
    cnpj = cnpj.replace('-', '')  # extract stroke
    cnpj = cnpj.replace('/', '')  # extract slash

     # if does not contain numerical characters
    for i in cnpj:
        if not i.isdigit():
            return False
            break

    #  check if length == 14
    if len(cnpj) != 14:
        return False

    # checks if all digits are equal
    for i in range(10):
        text = str(i) * 14
        if text == cnpj:
            return False
            break

    # first checksum1
    multi = 5
    result = 0
    for i in cnpj[:12]:
        result += int(i) * multi
        multi -= 1
        if multi < 2:
            multi = 9

    remainder = result % 11

    if remainder < 2:
        checksum1 = 0
    else:
        checksum1 = 11 - remainder

    assemble_cnpj = cnpj[:12] + str(checksum1)

    # secound checksum
    multi = 6
    result = 0

    for i in assemble_cnpj:
        result += int(i) * multi
        multi -= 1
        if multi < 2:
            multi = 9

    remainder = result % 11

    if remainder < 2:
        checksum2 = 0
    else:
        checksum2 = 11 - remainder

    assemble_cnpj += str(checksum2)

    return True if cnpj == assemble_cnpj else False
