import pytest
from calculadora import enquadramento_aliquota

@pytest.mark.parametrize('salario,expected', [(1000, 'Isento')])
def test_enquadramento_01(salario, expected):
    assert enquadramento_aliquota(salario) == expected

@pytest.mark.parametrize('salario,expected', [(2000, 7.5)])
def test_enquadramento_02(salario, expected):
    assert enquadramento_aliquota(salario) == expected

@pytest.mark.parametrize('salario,expected', [(3000, 15)])
def test_enquadramento_03(salario, expected):
    assert enquadramento_aliquota(salario) == expected

@pytest.mark.parametrize('salario,expected', [(4000, 22.5)])
def test_enquadramento_04(salario, expected):
    assert enquadramento_aliquota(salario) == expected

@pytest.mark.parametrize('salario,expected', [(5000, 27.5)])
def test_enquadramento_05(salario, expected):
    assert enquadramento_aliquota(salario) == expected

