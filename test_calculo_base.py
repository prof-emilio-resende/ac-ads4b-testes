#Teste utilizando o retorno de uma função chamada CalculaInss

from DeduzirDependentes import deduzir_dependentes

@pytest.mark.parametrize('salario, qntd_dependentes, expected', [(3000, 2, 2290.82)])
def test_calcula(salario, qntd_dependentes, expected):
    assert deduzir_dependentes(salario, qntd_dependentes) == expected