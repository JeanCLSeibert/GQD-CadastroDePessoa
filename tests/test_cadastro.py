import copy
import pytest

from cadastro import CadastroPessoa
from pessoa import Pessoa
from repositorio_pessoas_memoria import (
    RepositorioPessoasMemoria,
)

def testCadastrarPessoa():
    cadastro = CadastroPessoa()
    cadastro.cadastrar("Jean", 23, "jean@seibert.moe")

    pessoas = cadastro.listar()
    assert len(pessoas) == 1
    assert pessoas[0].getNome() == "Jean"
    assert pessoas[0].getIdade() == 23
    assert pessoas[0].getEmail() == "jean@seibert.moe"

def testBuscarPorNome():
    cadastro = CadastroPessoa()
    cadastro.cadastrar("Jean", 23, "jean@seibert.moe")

    encontrada = cadastro.buscarPorNome("Jean")

    assert encontrada is not None
    assert encontrada.getNome() == "Jean"
    assert encontrada.getIdade() == 23
    assert encontrada.getEmail() == "jean@seibert.moe"

class RepositorioDeCopias(RepositorioPessoasMemoria):
    """Devolve cópias, simulando objetos reconstruídos."""

    def buscar(self, nome):
        pessoa = super().buscar(nome)
        if pessoa is None:
            return None

        return copy.copy(pessoa)

@pytest.mark.parametrize(
    "fabrica",
    [RepositorioPessoasMemoria, RepositorioDeCopias]
)
def testAlterarPersiste(fabrica):
    repositorio = fabrica()
    repositorio.cadastrar(
        Pessoa("Ana Souza", 30, "ana@example.com")
    )
    cadastro = CadastroPessoa(repositorio)
    cadastro.alterar(
        "Ana Souza",
        "Ana Souza",
        31,
        "ana.s@example.com"
    )
    pessoa = repositorio.buscar("Ana Souza")

    assert pessoa is not None
    assert pessoa.getIdade() == 31
    assert pessoa.getEmail() == "ana.s@example.com"
