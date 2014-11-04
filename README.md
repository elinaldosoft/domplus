domplus
=======
domplus is a python package with common functions in commercial applications.

Installation
------------
    pip install domplus

Usage
-----
    from domplus import utilplus
    
    # Check if brazilian CPF is valid
    # Return True or False
    utilplus.valid_br_cpf('03167158590')

    # OR
    utilplus.valid_br_cpf('031.671.585-90')


    # Check if brazilian CNPJ is valid
    # Return True or False
    utilplus.valid_br_cnpj('75317134000130')

    # OR
    utilplus.valid_br_cnpj('75.317.134/0001-30')
