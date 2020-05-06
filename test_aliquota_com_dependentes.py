import pytest
from DeducaoDependente import DeducaoDependente
from CalculadoraIRRF import CalculadoraIRRF
from calculadora import enquadramento_aliquota
from calculadora_ir import calcula_inss

@pytest.mark.parametrize('salario, dependentes, expected', [(3600, 2, 69.06)])
def teste_enquadramento_aliquota_01(salario, dependentes, expected):
    salario_descontado_inss = calcula_inss(salario)
    salario_base = salario - salario_descontado_inss
    deducao_dependente = DeducaoDependente().deducao_dependente(dependentes)
    salario_apos_reducao = CalculadoraIRRF().subtrair_base_irrf(salario_base - deducao_dependente)
    enquadramento_aliquota = enquadramento_aliquota(salario_apos_reducao)
    assert enquadramento_aliquota == expected

@pytest.mark.parametrize('salario, dependentes, expected', [(3000, 2, 29.01)])
def teste_enquadramento_aliquota_02(salario, dependentes, expected):
    salario_descontado_inss = calcula_inss(salario)
    salario_base = salario - salario_descontado_inss
    deducao_dependente = DeducaoDependente().deducao_dependente(dependentes)
    salario_apos_reducao = CalculadoraIRRF().subtrair_base_irrf(salario_base - deducao_dependente)
    enquadramento_aliquota = enquadramento_aliquota(salario_apos_reducao)
    assert enquadramento_aliquota == expected

@pytest.mark.parametrize('salario, dependentes, expected', [(3500, 2, 62.39)])
def teste_enquadramento_aliquota_03(salario, dependentes, expected):
    salario_descontado_inss = calcula_inss(salario)
    salario_base = salario - salario_descontado_inss
    deducao_dependente = DeducaoDependente().deducao_dependente(dependentes)
    salario_apos_reducao = CalculadoraIRRF().subtrair_base_irrf(salario_base - deducao_dependente)
    enquadramento_aliquota = enquadramento_aliquota(salario_apos_reducao)
    assert enquadramento_aliquota == expected