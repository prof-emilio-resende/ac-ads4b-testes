import calculadora_ir as inss
from DeducaoDependente import DeducaoDependente


def deduzir_dependentes(salario_bruto, qtd_dependentes):
    dependentes = DeducaoDependente()
    return salario_bruto - inss.calcula_inss(salario_bruto) - dependentes.deducao_dependente(qtd_dependentes)
