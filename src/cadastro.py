from typing import List, Optional
from pessoa import Pessoa
from repositorio_pessoas import RepositorioPessoas
from repositorio_pessoas_memoria import RepositorioPessoasMemoria
class CadastroPessoa:
    """Gerencia as operações de cadastro de pessoas."""
    def __init__(
    self, repositorio: Optional[RepositorioPessoas] = None
    ) -> None:
        if repositorio is None:
            repositorio = RepositorioPessoasMemoria()
        self.__repositorio = repositorio
    def cadastrar(self, nome, idade, email):
        pessoa = Pessoa(nome, idade, email)
        self.__repositorio.cadastrar(pessoa)
        return pessoa
    def buscarPorNome(self, nome):
        return self.__repositorio.buscar(nome)
    def listar(self) -> List[Pessoa]:
        return self.__repositorio.listar()
    def alterar(self, nome, novoNome, novaIdade, novoEmail):
        pessoa = self.buscarPorNome(nome)
        if pessoa is None:
            return None
        pessoa.setNome(novoNome)
        pessoa.setIdade(novaIdade)
        pessoa.setEmail(novoEmail)
        return pessoa
