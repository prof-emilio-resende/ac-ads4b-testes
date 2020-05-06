from DeducaoDependente import DeducaoDependente
import pytest

def test_01():
    calc = DeducaoDependente()
    p1 = calc.deducao_dependente(3)
    assert p1 == (189.59 * 3)

def test_02():
    calc = DeducaoDependente()
    p1 = calc.deducao_dependente(4)
    assert p1 == (189.59 * 4)

def test_03():
    calc = DeducaoDependente()
    p1 = calc.deducao_dependente(5)
    assert p1 == (189.59 * 5)

def test_04():
    calc = DeducaoDependente()
    p1 = calc.deducao_dependente(6)
    assert p1 == (189.59 * 6)