#Teste utilizando o retorno de uma função chamada CalculaInss

from calculadora_ir import calcula_inss
import pytest

@pytest.mark.parametrize('salario, deducao_dependentes, expected', [(3000, 379.18, 2290.82)])
def test_calcula(salario, deducao_dependentes, expected):
    assert calcula_inss(salario) == expected