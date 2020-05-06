#Teste utilizando o retorno de uma funç~~ao chamada CalculaInss

from calculadora_ir import calcula_inss
import pytest

@pytest.mark.parametrize('salario,expected', [(3000, 330)])
def test_calcula(salario, expected):
    assert calcula_inss(salario) == expected
