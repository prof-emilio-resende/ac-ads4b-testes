def enquadramento_aliquota(salario_base):

    if salario_base <= 1903.98:
        return 'Isento'

    elif salario_base >= 1903.99 and salario_base <= 2826.65:
        aliquota = 7.5

    elif salario_base >= 2826.66 and salario_base <= 3751.05:
        aliquota = 15

    elif salario_base >= 3751.06 and salario_base <= 4664.68:
        aliquota = 22.5    

    else:
        aliquota = 27.5

    return aliquota