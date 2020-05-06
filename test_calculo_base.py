#Teste utilizando o retorno de uma função chamada CalculaInss

from DeduzirDependentes.py import deduzir_dependentes
from calculadora_ir import calcula_inss
import pytest

@pytest.mark.parametrize('salario, qntd_dependentes, expected', [(3000, 2, 2290.82)])
def test_calcula(salario, qntd_dependentes, expected):
    assert deduzir_dependentes(salario, qntd_dependentes) == expected