import pytest
from ControleAcesso import Funcionalidades, Usuarios, SistemaGerenciamentoAcesso

@pytest.fixture
def sistema():
    sistema = SistemaGerenciamentoAcesso()

    # Adicionar algumas funcionalidades para teste
    funcionalidade1 = Funcionalidades(id=1, nome="Funcionalidade Nível 1", nivel=1)
    funcionalidade2 = Funcionalidades(id=2, nome="Funcionalidade Nível 2", nivel=2)
    funcionalidade3 = Funcionalidades(id=3, nome="Funcionalidade Nível 3", nivel=3)
    sistema.funcionalidades.append(funcionalidade1)
    sistema.funcionalidades.append(funcionalidade2)
    sistema.funcionalidades.append(funcionalidade3)

    return sistema