# IMPORTANDO BIBLIOTECAS
from datetime import datetime

# Listas/Dicionários
pessoas = []
livros = []
emprest = []
devol = []
# contabilizador do relatório
livros_mais_emprest = 0

def exibir_menu_bibliot():
    print('''O que deseja fazer:
    [ 1 ] Cadastramento de usuários
    [ 2 ] Cadastramento de livros
    [ 3 ] Empréstimo de livros
    [ 4 ] Devolução de livros
    [ 5 ] Relatórios
    [ 6 ] Sair/Encerrar''')

def exibir_menu_pessoa():
    print('''Escolha uma opção:
    [ 1 ] Cadastrar uma pessoa
    [ 2 ] Listar pessoas cadastradas
    [ 3 ] Procurar dados de uma pessoa
    [ 4 ] Remover
    [ 5 ] Alterar
    [ 6 ] Consultar (pelo nome, ou parte do nome, ou pelo CPF)
    [ 7 ] Sair/Encerrar''')

# CADASTRANDO O USUÁRIO
def cadastro_pessoa():
    nome = input('Nome: ')
    cpf = int(input('CPF: '))
    if any(pessoa['cpf'] == cpf for pessoa in pessoas):
        print('CPF já cadastrado!')
        return

    email = input('Email: ')
    pessoas.append({'nome': nome, 'cpf': cpf, 'email': email})
    print(pessoas)

    # arquivo de escrita
    with open('pessoasCadastradas.txt', 'a') as arq:
        for pes in pessoas:
            nome, cpf, email = pes['nome'], str(pes['cpf']), pes['email']
            salva = f'{nome}, {cpf}, {email}, \n'
            arq.write(salva)
        print()

    # arquivo de leitura
    with open('pessoasCadastradas.txt', 'r') as arq:
        print(arq.readlines())

    print('Pessoa cadastrada com sucesso!')

# LISTA DE PESSOAS CADASTRADAS
def listar_pessoa():
    for pessoa in pessoas:
        print(pessoa)

# BUSCANDO PESSOAS
def buscar_pessoa():
    cpf = int(input('CPF: '))
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            print(f'Pessoa com o CPF {cpf} está cadastrada no sistema!')
            print(pessoa)
            return
    print(f'Pessoa com CPF {cpf} não encontrada')

# REMOVER PESSOA
def remover_pessoa():
    cpf = int(input('CPF: '))
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            print(pessoa)
            r = input('Deseja remover essa pessoa? (S/N) ')
            if r.upper() == 'S':
                pessoas.remove(pessoa)
                print('Pessoa removida com sucesso!')
                return
    print(f'Pessoa com CPF {cpf} não encontrada.')

# ALTERAR PESSOA
def alterar_pessoa():
    cpf = int(input('Digite o CPF que deseja alterar: '))
    for pessoa in pessoas:
        if pessoa['cpf'] == cpf:
            print(pessoa)
            alt = input('Deseja fazer a alteração desse cadastro? (S/N) ').upper()
            if alt == 'S':
                nome = input('Digite o novo nome: ')
                email = input('Digite o novo email: ')
                pessoa['nome'] = nome
                pessoa['email'] = email
                print('Cadastro alterado com sucesso!')
                return
    print(f'Pessoa com CPF {cpf} não encontrada.')

# CONSULTAR PESSOA
def consulta_pessoa():
    valor = input('Digite o nome, parte do nome ou CPF para consultar: ')
    encontrado = False
    for pessoa in pessoas:
        if valor in pessoa['nome'] or str(valor) == str(pessoa['cpf']):
            print(pessoa)
            encontrado = True
    if not encontrado:
        print('Nenhum registro encontrado.')

# CADASTRANDO LIVROS
def cadastro_livros():
    id_livro = input('ID do Livro: ')
    if any(livro['id_livro'] == id_livro for livro in livros):
        print('ID do livro já cadastrado!')
        return

    titulo = input('Título: ')
    resumo = input('Resumo: ')
    autor = input('Autor: ')
    editora = input('Editora: ')
    ano_publicacao = input('Ano de Publicação: ')
    edicao = input('Edição: ')

    livros.append({
        'id_livro': id_livro,
        'titulo': titulo,
        'resumo': resumo,
        'autor': autor,
        'editora': editora,
        'ano_publicacao': ano_publicacao,
        'edicao': edicao
    })

    print('Livro cadastrado com sucesso!')

# LISTA DE LIVROS CADASTRADOS
def listar_livros():
    for livro in livros:
        print(livro)

# BUSCANDO LIVROS
def buscar_livros():
    id_livro = input('ID do livro: ')
    for livro in livros:
        if livro['id_livro'] == id_livro:
            print(f'Livro com o ID {id_livro} está cadastrado no sistema!')
            print(livro)
            return
    print(f'Livro com ID {id_livro} não encontrado')

# EMPRÉSTIMO DE LIVROS
def emprestimo_livros():
    cpf = int(input('CPF do usuário: '))
    id_livro = input('ID do livro: ')
    data_emprestimo = datetime.now()

    pessoa = None
    for p in pessoas:
        if p['cpf'] == cpf:
            pessoa = p
            break

    livro = None
    for l in livros:
        if l['id_livro'] == id_livro:
            livro = l
            break

    if pessoa is None:
        print(f'Usuário com CPF {cpf} não encontrado.')
        return

    if livro is None:
        print(f'Livro com ID {id_livro} não encontrado.')
        return

    emprest.append({
        'pessoa': pessoa,
        'livro': livro,
        'data_emprestimo': data_emprestimo
    })

    print('Empréstimo realizado com sucesso!')

# DEVOLUÇÃO DE LIVROS
def devolucao_livros():
    cpf = int(input('CPF do usuário: '))
    id_livro = input('ID do livro: ')
    data_devolucao = datetime.now()

    emprestimo = None
    for em in emprest:
        if em['pessoa']['cpf'] == cpf and em['livro']['id_livro'] == id_livro:
            emprestimo = em
            break

    if emprestimo is None:
        print('Empréstimo não encontrado.')
        return

    devol.append({
        'pessoa': emprestimo['pessoa'],
        'livro': emprestimo['livro'],
        'data_emprestimo': emprestimo['data_emprestimo'],
        'data_devolucao': data_devolucao
    })

    emprest.remove(emprestimo)

    print('Devolução realizada com sucesso!')

# RELATÓRIOS
def relatorios():
    print('1 - Livros mais emprestados')
    print('2 - Livros emprestados')
    print('3 - Livros devolvidos')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        livro_emprestado = {}
        for em in emprest:
            id_livro = em['livro']['id_livro']
            if id_livro in livro_emprestado:
                livro_emprestado[id_livro] += 1
            else:
                livro_emprestado[id_livro] = 1

        if not livro_emprestado:
            print('Nenhum livro foi emprestado.')
            return

        livros_mais_emprest = max(livro_emprestado.values())
        print('Os livros mais emprestados são:')
        for livro, quantidade in livro_emprestado.items():
            if quantidade == livros_mais_emprest:
                print(f'ID: {livro}, Quantidade: {quantidade}')

    elif opcao == 2:
        if not emprest:
            print('Nenhum livro emprestado.')
            return

        print('Livros emprestados:')
        for em in emprest:
            print(f"CPF: {em['pessoa']['cpf']}, ID: {em['livro']['id_livro']}, Data do empréstimo: {em['data_emprestimo']}")

    elif opcao == 3:
        if not devol:
            print('Nenhum livro devolvido.')
            return

        print('Livros devolvidos:')
        for dev in devol:
            print(f"CPF: {dev['pessoa']['cpf']}, ID: {dev['livro']['id_livro']}, Data do empréstimo: {dev['data_emprestimo']}, Data da devolução: {dev['data_devolucao']}")

    else:
        print('Opção inválida.')

# PROGRAMA PRINCIPAL
while True:
    exibir_menu_bibliot()
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        while True:
            exibir_menu_pessoa()
            opcao_pessoa = int(input('Escolha uma opção: '))

            if opcao_pessoa == 1:
                cadastro_pessoa()
            elif opcao_pessoa == 2:
                listar_pessoa()
            elif opcao_pessoa == 3:
                buscar_pessoa()
            elif opcao_pessoa == 4:
                remover_pessoa()
            elif opcao_pessoa == 5:
                alterar_pessoa()
            elif opcao_pessoa == 6:
                consulta_pessoa()
            elif opcao_pessoa == 7:
                break
            else:
                print('Opção inválida!')

    elif opcao == 2:
        cadastro_livros()

    elif opcao == 3:
        emprestimo_livros()

    elif opcao == 4:
        devolucao_livros()

    elif opcao == 5:
        relatorios()

    elif opcao == 6:
        print('Encerrando o programa...')
        break

    else:
        print('Opção inválida!')
