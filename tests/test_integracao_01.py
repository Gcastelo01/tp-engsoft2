import pytest
from ControleAcesso import Funcionalidades, Usuarios, SistemaGerenciamentoAcesso

@pytest.fixture
def sistema():
    sistema = SistemaGerenciamentoAcesso()
    
    # Configurar funcionalidades
    funcionalidades = [
        Funcionalidades(id=1, nome="Cadastrar Usuário", nivel=5),
        Funcionalidades(id=2, nome="Remover Usuário", nivel=5),
        Funcionalidades(id=3, nome="Editar Usuário", nivel=1),
        Funcionalidades(id=4, nome="Calculadora", nivel=2),
        Funcionalidades(id=5, nome="Calculadora de Equações", nivel=2),
        Funcionalidades(id=6, nome="Calculadora Física", nivel=3),
    ]
    
    sistema.funcionalidades.extend(funcionalidades)
    return sistema

def test_cadastro_usuario_associacao_funcionalidades(sistema):
    # Cadastrar um novo usuário com nível 3
    novo_usuario = Usuarios(id=2, nome="Maria", username="maria", email="maria@example.com", setor="TI", cargo="Dev", nivel=3)
    sistema.cadastrarUsuario(novo_usuario)
    
    # Verificar se as funcionalidades com nível <= 3 foram associadas corretamente ao usuário
    funcionalidades_esperadas = [3, 4, 5, 6]  # IDs das funcionalidades que devem ser liberadas
    
    funcionalidades_associadas = sistema.mostrarFuncionalidadesLiberadas(novo_usuario.id)
    
    assert set(funcionalidades_esperadas) == set(funcionalidades_associadas)
