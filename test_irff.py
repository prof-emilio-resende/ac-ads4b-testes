from CalculadoraIRRF import CalculadoraIRRF
import pytest

def test_01_subtrair():
    calc = CalculadoraIRRF()
    p1 = calc.subtrair_base_irrf(3000)
    assert p1 == 1096.02

def test_02_subtrair():
    calc = CalculadoraIRRF()
    p1 = calc.subtrair_base_irrf(5000)
    assert p1 == 3096.02

def test_03_subtrair():
    calc = CalculadoraIRRF()
    p1 = calc.subtrair_base_irrf(7000)
    assert p1 == 5096.02

def test_04_subtrair():
    calc = CalculadoraIRRF()
    p1 = calc.subtrair_base_irrf(9000)
    assert p1 == 7096.02