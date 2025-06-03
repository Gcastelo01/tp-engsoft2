import pytest

from CalculadoraBhaskara import calcular_raizes, calcular_raiz_linear, calcular_raizes_quadraticas

def test_calcular_raizes_imaginarias():
    assert calcular_raizes(1, 1, 1) == "A equação não possui raízes reais"

def test_calcular_raiz_unica():
    assert calcular_raizes(1, -2, 1) == "A equação possui uma raiz real: 1.0"
    
def test_calcula_duas_raizes():
    assert calcular_raizes(1, -3, 2) == "A equação possui duas raízes reais: 2.0 e 1.0"

def test_calcular_raizes_a_zero():
    with pytest.raises(ZeroDivisionError):
        calcular_raizes(0, 2, 1)

def test_calcular_raiz_linear():
    assert calcular_raiz_linear(2, -4) == "A raiz da equação é: 2.0"

def test_equacao_impossivel():
    assert calcular_raiz_linear(0, 4) == "A equação é impossível (0 ≠ 0) e não tem solução."

def test_identidade():
    assert calcular_raiz_linear(0, 0) == "A equação é uma identidade (0 = 0) e tem infinitas soluções."

def test_calcular_raiz_linear_negativa():
    assert calcular_raiz_linear(3, 9) == "A raiz da equação é: -3.0"

def test_calcular_raiz_linear_fracionaria():
    assert calcular_raiz_linear(3, -2) == "A raiz da equação é: 0.6666666666666666"

def test_calcular_raizes_quadraticas_duas_raizes(monkeypatch, capsys):
    inputs = iter(["1", "-5", "6"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calcular_raizes_quadraticas()
    captured = capsys.readouterr()
    assert "A equação possui duas raízes reais: 3.0 e 2.0" in captured.out

def test_calcular_raizes_quadraticas_uma_raiz(monkeypatch, capsys):
    inputs = iter(["1", "-2", "1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calcular_raizes_quadraticas()
    captured = capsys.readouterr()
    assert "A equação possui uma raiz real: 1.0" in captured.out

def test_calcular_raizes_quadraticas_sem_raizes_reais(monkeypatch, capsys):
    inputs = iter(["1", "1", "1"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    calcular_raizes_quadraticas()
    captured = capsys.readouterr()
    assert "A equação não possui raízes reais" in captured.out