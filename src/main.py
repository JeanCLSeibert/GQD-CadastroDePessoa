"""Sistema de Cadastro de Pessoas."""

from cadastro import CadastroPessoa
from repositorio_pessoas_mysql import RepositorioPessoasMySQL
from repositorio_pessoas_memoria import RepositorioPessoasMemoria
USAR_MYSQL = True

def criarRepositorio():
    if USAR_MYSQL:
        return RepositorioPessoasMySQL.aPartirDoAmbiente()
    return RepositorioPessoasMemoria()

def printMenu():
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Analisar pessoa")
    print("6 - Sair")
    return int(input("Escolha uma opcao: "))

def exibirPessoa(pessoa):
    print("Nome: " + pessoa.getNome())
    print("Idade: " + str(pessoa.getIdade()))
    print("E-mail: " + pessoa.getEmail())
    print("-------------------------")
    if pessoa.getIdade() >= 18:
        print("Situação: Maior de idade")
    else:
        print("Situação: Menor de idade")



def cadastrarPessoa(cadastro):
    """Cadastra o Nome, Idade e E-mail de uma pessoa e informa se é de maior/menor"""
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    email = input("Informe o e-mail: ")

    cadastro.cadastrar(nome, idade, email)

    if idade >= 18:
        print("Situação: Maior de idade")
    else:
        print("Situação: Menor de idade")

def consultarPessoa(cadastro):
    """Pesquisa uma pessoa nos cadastro e a apresenta se encontrado"""
    busca = input("Nome para consultar: ")
    pessoa = cadastro.buscarPorNome(busca)
    if pessoa is None:
        print("Não encontrado")
    else:
        exibirPessoa(pessoa)

def alterarPessoa(cadastro):
    """Altera as informações de uma pessoa"""

    busca = input("Nome para alterar: ")

    pessoa = cadastro.buscarPorNome(busca)

    if pessoa is None:
        print("Não encontrado")
        return

    exibirPessoa(pessoa)

    nome = input("Novo nome: ")
    idade = int(input("Nova idade: "))
    email = input("Novo e-mail: ")

    pessoaAlterada = cadastro.alterar(busca, nome, idade, email)
    if pessoaAlterada is None:
        print("Não foi possível alterar a pessoa")
    else:
        print("Pessoa alterada")
        exibirPessoa(pessoa)

def listarPessoas(cadastro):
    """Lista todos os cadastros do sistema"""
    pessoas = cadastro.listar()
    if len(pessoas)==0:
        print("Nenhum cadastro")
    else:
        for pessoa in pessoas:
            exibirPessoa(pessoa)
        print("Total: " + str(len(pessoas)))

def analisarIdade(idade):
    """Apresenta a faixa etária a partir de uma idade"""
    if idade < 12:
        print("Faixa etária: Criança")
    elif idade < 18:
        print("Faixa etária: Adolescente")
    elif idade < 30:
        print("Faixa etária: Adulto jovem")
    elif idade < 60:
        print("Faixa etária: Adulto")
    else:
        print("Faixa etária: Idoso")

def analisarEmail(email):
    """Valida se o e-mail informado é válido"""
    if email == "":
        print("Cadastro incompleto: sem o e-mail")
        return -1
    if "@" not in email:
        print("E-mail invalido")
        return -1
    print("E-mail utilizável")
    return 1

def analisarProvedorEmail(email):
    if email.endswith("@gmail.com"):
        print("Provedor: Gmail")
    elif email.endswith("@outlook.com"):
        print("Provedor: Outlook")
    elif email.endswith("@hotmail.com"):
        print("Provedor: Hotmail")
    elif email.endswith("@utfpr.edu.br"):
        print("Provedor: UTFPR")
    else:
        print("Provedor: Outro")


def analisarIdadeEEmail(idade, email):
    if idade >= 18 and email != "":
        print("Cadastro apto para contato")
    elif idade >= 18 and email == "":
        print("Maior de idade sem contato")
    elif idade < 18 and email != "":
        print("Menor de idade com contato")
    else:
        print("Menor de idade sem contato")

def analisarPessoa(cadastro):
    """Busca uma pessoa e valida seu cadastro pela sua faixa etária, validade do e-mail e se é possível contactar"""
    busca = input("Nome para analisar: ")
    pessoa = cadastro.buscarPorNome(busca)

    if pessoa is None:
        print("Pessoa não encontrada")
    else:
        idade = pessoa.getIdade()
        email = pessoa.getEmail()

        analisarIdade(idade)
        emailOk = analisarEmail(email)
        if emailOk>0:
            analisarProvedorEmail(email)
        analisarIdadeEEmail(idade, email)


def main():
    """Executa o loop de menu do programa"""
    cadastro = CadastroPessoa(criarRepositorio())

    op = 0

    while op != 6:
        op = printMenu()
        if op == 1:
            cadastrarPessoa(cadastro)
        elif op == 2:
            consultarPessoa(cadastro)
        elif op == 3:
            alterarPessoa(cadastro)
        elif op == 4:
            listarPessoas(cadastro)
        elif op == 5:
            analisarPessoa(cadastro)
        elif op == 6:
            print("Saindo...")

        else:
            print("Opcao invalida")

if __name__ == "__main__":
    main()
    print("Fim do programa")
