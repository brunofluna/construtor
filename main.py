# NOTE: criar a classe
class Pessoa:
    # os atributos são SEMPRE definidos dentro do método construtor.
    # NOTE: Método construtor
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

# NOTE: Programa principal
if __name__ == '__main__':
    # entrada de dados
    nome = input("Digite o nome do usuário: ")
    idade = int(input('Digite a idade do usuário: '))
    cpf = input('Digite o CPF do usuário: ')
    email = input('Digite o e-mail do usuário: ')

    # instancia o objeto
    usuario = Pessoa(nome, idade, cpf, email)

    # saída de dados
    print(f'Nome: {usuario.nome}.')
    print(f'Idade: {usuario.idade}.')
    print(f'C P F: {usuario.cpf}.')
    print(f'E-mail: {usuario.email}.')