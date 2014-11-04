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

    # Check if brazilian CNPJ is valid
    # Return True or False
    utilplus.valid_br_cnpj('12525951000163')
