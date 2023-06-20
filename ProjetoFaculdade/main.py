# IMPORTANDO BIBLIOTECAS
from datetime import date, time, datetime

# Listas/Dicionários
pessoas = []
livros = []
emprest = []
devol = []


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
    if cpf in pessoas:
        while cpf in pessoas:
            print('CPF já cadastrado!')
            cpf = int(input('Digite outro CPF: '))
            if cpf not in pessoas:
                continue
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
        arq.readlines()
        print(arq)

    print('Pessoa casdastrada com sucesso!')


# LISTA DE PESSOAS CADASTRADAS
def listar_pessoa():
    for p in pessoas:
        nome, email, cpf = p
        print(p)


# BUSCANDO PESSOAS
def buscar_pessoa():
    cpf = int(input('CPF: '))
    for b in pessoas:
        nome, email, cpf = b
        print(b)
        print(f'Pessoa com o CPF {cpf} está cadastrada no sistema!')
        if b not in pessoas:
            print(f'Pessoa com CPF {cpf} não encontrada')


# REMOVER PESSOA
def remover_pessoa():
    cpf = int(input('CPF: '))
    for rp in pessoas:
        nome, email, cpf = rp
        print(rp)
        r = input('Deseja remover essa pessoa? ')
        if r == 'Ss':
            pessoas.remove(pessoas['nome': nome, 'cpf': cpf, 'email': email])
        print('Pessoa removida com sucesso!')
    if cpf not in pessoas:
        print(f'Pessoa com CPF {cpf} não encontrada.')


# ALTERAR PESSOA
def alterar_pessoa():
    cpf = int(input('Digite o CPF que deseja alterar: '))
    for at in pessoas:
        nome, email, cpf = at
        print(at)
        alt = input('Deseja fazer a alteração desse cadastro? ').upper()
        if alt == 'Ss' or alt == 'SIM' or alt == 'sim':
            pessoas.remove(pessoas['nome': nome, 'email': email, 'cpf': cpf])
            print('Começando a alteração...')
            nome = input('Novo nome: ')
            email = input('Novo email: ')
            cpf = int(input('Novo cpf: '))
            pessoas.append({'nome': nome, 'email': email, 'cpf': cpf})
    print('Alterações feitas com sucesso!')


# CONSULTAR PESSOA
def consulta_pessoa():
    print('''Escolha um tipo de consulta:
    [ 1 ] Consultar pelo nome
    [ 2 ] Consultar por parte do nome
    [ 3 ] Consultar pelo CPF''')
    consult = int(input('Por onde deseja consultar: '))
    if consult == 1:
        nome = input('Nome: ')
        if nome in pessoas:
            print(f'O nome {nome} se encontra no sistema!')
        else:
            print(f'O nome {nome} não se encontra no nosso sistema')
    elif consult == 2:
        parte_nome = input('Parte do nome que deseja consultar: ')
        if parte_nome in pessoas:
            posicao = pessoas.find(parte_nome)
            print(f'A parte do nome {parte_nome} se encontra em {posicao}')
        else:
            print('Este nome não está cadastrado no nosso sistema! Tente novamente.')
    elif consult == 3:
        cpf = int(input('CPF: '))
        if cpf in pessoas:
            print(f'O CPF {cpf} se encontra no nosso sistema!')
        else:
            print('O CPF não se encontra no nosso sistema!')
    else:
        while consult < 1 and consult > 3:
            consult = int(input('ERRO! Digite um número entre 1 e 3: '))
    print()


# MENU LIVROS
def exibir_menu_livros():
    print('''Escolha uma opção:
    [ 1 ] Cadastrar um livro
    [ 2 ] Listar os livros cadastrados
    [ 3 ] Procurar os livros
    [ 4 ] Remover
    [ 5 ] Alterar
    [ 6 ] Consultar (pelo título ou parte do título, pelo autor ou pela editora)
    [ 7 ] Encerrar/Sair''')


# CADASTRANDO LIVROS
def cadastro_livros():
    id_livro = int(input('Id: '))
    if id_livro in livros:
        print('Livro já cadastrado!')
    else:
        titulo = input('Título: ')
        resumo = input('Resumo: ')
        autor = input('Autor: ')
        editora = input('Editora: ')
        ano_publicacao = int(input('Ano de publicação: '))
        edicao = int(input('Edição: '))
        livros.append({'Id do Livro': id_livro, 'titulo': titulo, 'resumo': resumo, 'autor': autor,
                       'editora': editora, 'ano de publicação': ano_publicacao, 'edição': edicao})
        print(livros)
        # arquivo de escrita
        with open('livrosCadastrados.txt', 'a') as arq_l:
            for liv in livros:
                id_livro, titulo, resumo, autor = liv['Id do Livro'], liv['titulo'], liv['resumo'], liv['autor']
                editora, ano_publicacao, edicao = liv['editora'], liv['ano de publicação'], liv['edição']
                salva_l = f'{id_livro}, {resumo}, {autor}, {editora}, {ano_publicacao}, {edicao}, \n'
                arq_l.write(salva_l)
        # arquivo de leitura
        with open('livrosCadastrados.txt', 'r') as arq_l:
            arq_l.readlines()
            print(arq_l)
            print()
        print('Livro cadastrado com sucesso!!')


# LISTAR LIVROS CADASTRADOS
def listar_livros():
    for livro in livros:
        id_livro, titulo, resumo, autor, editora, ano_publicacao, edicao = livro
        print(livro)


# BUSCANDO LIVROS
def buscar_livros():
    id_livro = int(input('Id: '))
    for i_d in livros:
        id_livro, titulo, resumo, autor, editora, ano_publicacao, edicao = i_d
        print(i_d)
        print(f'Livro com o ID {id_livro} está cadastrado no sistema! ')
        if i_d not in livros:
            print(f'Livro com id {id_livro} não foi encontrado')


# REMOVER LIVROS
def remover_livro():
    id_livro = int(input('Id do Livro: '))
    if id_livro in livros:
        print(livros[id_livro])
        rem = input('Deseja remover este livro? ')
        if rem == 'Ss':
            livros.remove(id_livro)
        print("Livro removido com sucesso!")
    else:
        print(f'Livro com id {id_livro} não encontrado.')


# ALTERAR LIVROS
def alterar_livros():
    id_livro = int(input('Digite o Id do livro que deseja alterar: '))
    for ad in livros:
        id_livro, titulo, resumo, autor, editora, ano_publicacao, edicao = ad
        print(ad)
        alterar_livro = input('Deseja fazer a alteração desse cadastro? ').upper()
        if alterar_livro == 'Ss' or alterar_livro == 'SIM' or alterar_livro == 'sim':
            livros.remove(livros['id do livro': id_livro, 'titulo': titulo, 'resumo': resumo,
                          'editora': editora, 'ano de publicação': ano_publicacao, 'edição': edicao])
            print('ALTERANDO OS DADOS')
            id_livro = int(input('Novo id: '))
            titulo = str(input('Novo título: '))
            resumo = input('Novo resumo: ')
            autor = input('Novo(s) autor(res): ')
            editora = str(input('Nova editora: '))
            ano_publicacao = int(input('Novo ano de publicação: '))
            edicao = int(input('Nova edição: '))
            livros.append({'id do livro': id_livro, 'titulo': titulo, 'resumo': resumo, 'autor': autor,
                           'editora': editora, 'ano de publicação': ano_publicacao, 'edição': edicao})
    print('Alterações feitas com sucesso')


# CONSULTAR LIVROS
def consulta_livros():
    print('''Escolha um tipo de consulta:
          [ 1 ] Consultar pelo Id do Livro
          [ 2 ] Consultar pelo Título
          [ 3 ] Consultar por parte do Título
          [ 4 ] Consultar pelo autor
          [ 5 ] Consultar pela editora''')
    consul = int(input('Por onde deseja consultar: '))
    if consul == 1:
        id_livro = int(input('Id: '))
        for i_l in livros:
            id_livro = i_l
            print(i_l)
            print(f'O livro com o ID {id_livro} está cadastrado')
            if i_l not in livros:
                print(f'O id {id_livro} não se encontra no sistema ou não está cadastrado')
    elif consul == 2:
        titulo = input('Título: ')
        for t in livros:
            titulo = t
            print(t)
            print(f'O livro com o título {titulo} está cadastrado')
            if t not in livros:
                print(f'O Título {titulo} não se encontra no nosso sistema ou não está cadastrado')
    elif consul == 3:
        parte_titulo = input('Parte do título que deseja consultar: ')
        if parte_titulo in livros:
            pos = livros.find(parte_titulo)
            print(f'A parte do Título {parte_titulo} se encontra em {pos}')
        else:
            print('Este Título não está cadastrado no nosso sistema! Tente novamente.')
    elif consul == 4:
        autor = input('Autor(es): ')
        for a in livros:
            autor = a
            print(a)
            print(f'O(s) Autor(es) {autor} se encontra no nosso sistema!')
        if autor not in livros:
            print('O(s) Autor(es) não se encontra no nosso sistema ou não foi cadastrado!')
    elif consul == 5:
        editora = input('Editora: ')
        for ed in livros:
            editora = ed
            print(ed)
            print(f'A Editora {editora} se encontra no nosso sistema!')
        if editora not in livros:
            print('A Editora não se encontra no nosso sistema ou não foi cadastrada!')

        while consul < 1 and consul > 5:
            consul = int(input('ERRO! Digite um número entre 1 e 5: '))
        print()


# LIVROS DISPONÍVEIS
def livros_disponiveis():
    for ld in livros:
        if ld not in emprest:
            print(f'Os livros disponíveis são {ld}')
            print(ld)


# EMPRÉSTIMO DE LIVROS
def emprestimo():
    # verificar se o livro está disponível
    id_livro = int(input('Id: '))
    for idl in emprest:
        id_livro = idl
        print(idl)
        print('Livro já emprestado!')
    # fazer o empréstimo
    if livros not in emprest:
        id_livro = int(input('Id: '))
        pessoa = input('Nome da pessoa: ')
        titulo = input('Título do livro: ')
        # registrar a data de saída do livro
        hora_e_data = datetime.now()
        print(f'Hora e Data do empréstimo: {hora_e_data}')
        emprest.append({'Pessoa': pessoa, 'Id do livro': id_livro, 'titulo': titulo, 'hora/data': hora_e_data})
    # arquivos do empréstimo
    with open('livrosEmprestados.txt', 'a') as arq_e:
        for e in livros:
            id_livro, titulo, resumo, autor = e['Id do Livro'], e['titulo'], e['resumo'], e['autor']
            editora, ano_publicacao, edicao = e['editora'], e['ano de publicação'], e['edição']
            salva_e = f'{id_livro}, {resumo}, {autor}, {editora}, {ano_publicacao}, {edicao}, \n'
            arq_e.write(salva_e)
            if e in emprest:
                print('Livro não disponível para empréstimo.')
        print()
    # arquivo de leitura do empréstimo
    with open('livrosEmprestados.txt', 'r') as arq_l:
        print(arq_l.readlines())
        print()
    print('Empréstimo realizado com sucesso!')


# DEVOLUÇÃO DO LIVRO
def devolucao():
    # Verificar se o livro está emprestado e fazer a devolução
    id_livro = int(input('Id do livro que deseja devolver: '))
    for d in emprest:
        id_livro, titulo, nome = d
        print(d)
        # tornar o livro disponível
        opc_d = input('Deseja devolver esse livro? ').upper()
        if opc_d == 'Ss':
            emprest.remove({'ID do livro': id_livro, 'Título': titulo, 'Pessoa': nome})
        # registrar a data de devolução
        hora_e_data = datetime.now()
        print(f'Hora e data da devolução: {hora_e_data}')
        devol.append({'Id do livro': id_livro, 'Título': titulo, 'Pessoa': nome, 'Hora e data': hora_e_data})
    # fazendo a leitura dos livros emprestados
    with open('livrosEmprestados.txt', 'r') as arq_l:
            print(arq_l.readlines())
            print()
    # escrevendo no arquivo de livros devolvidos
    with open('livrosDevolvidos.txt', 'a') as devolv_l:
        for dev in emprest:
            id_livro, titulo, resumo, autor = dev['Id do Livro'], dev['titulo'], dev['resumo'], dev['autor']
            editora, ano_publicacao, edicao = dev['editora'], dev['ano de publicação'], dev['edição']
            salva_d = f'{id_livro}, {resumo}, {autor}, {editora}, {ano_publicacao}, {edicao}, \n'
            devolv_l.write(salva_d)
            print()
    print('Livro devolvido com sucesso!')


# RELATÓRIOS
def relatorio():
    print('''Escolha a opção que deseja:
    [ 1 ] Lista dos usuários com livros emprestados e não devolvidos
    [ 2 ] Lista dos livros emprestados e não devolvidos até o momento
    [ 3 ] Lista dos 10 livros mais emprestados no mês''')
    opcao = int(input('O que deseja ver primeiro? '))

    if opcao == 1:
        if not emprest:
            print('Nenhum livro emprestado.')
            return
        for pde in emprest: # pessoa e livro emprestado
            nome, id_livro, titulo = pde
            print(pde)
            print()
    elif opcao == 2:
        if not devol:
            print('Nenhum livro devolvido.')
            return
        for le in emprest: # livros emprestados e n devolvidos
            id_livro, titulo, resumo, autor, editora, ano_publicacao = le
            print(le)
            print()
    elif opcao == 3:
        livros_mais_emprestados = sorted(emprest, key=lambda x: x[1], reverse=True)
        # Obtenha os 10 livros mais emprestados no mês
        top_10_emprestados = livros_mais_emprestados[:10]
        # Imprima a lista dos 10 livros mais emprestados no mês
        print("Lista dos 10 livros mais emprestados no mês:")
        for livro, quantidade in top_10_emprestados:
            print(f"{livro}: {quantidade} retiradas")


print('-*' * 20)
print('BEM VINDO AO SISTEMA DE BIBLIOTECA')
print('-*' * 20)
print()


def menu_principal():
    while True:
        exibir_menu_bibliot()
        print()
        opcao = int(input('Opção: '))
        if opcao == 1:
            exibir_menu_pessoa()
            # CADASTRO DE PESSOAS
            opcao_pessoa = int(input('Opção: '))
            if opcao_pessoa == 1:
                print('-*' * 20)
                print('...::: Cadastro de Pessoas :::...')
                cadastro_pessoa()
                print('-*' * 20)
                print()
            elif opcao_pessoa == 2:
                print('-*' * 20)
                print('...::: Lista de Pessoas Cadastradas :::...')
                listar_pessoa()
                print('-*' * 20)
                print()
            elif opcao_pessoa == 3:
                print('-*' * 20)
                print('...::: Buscar Pessoa Cadastradas :::...')
                buscar_pessoa()
                print('-*' * 20)
                print()
            elif opcao_pessoa == 4:
                print('-*' * 20)
                print('...::: Remover Pessoa Cadastradas :::...')
                remover_pessoa()
                print('-*' * 20)
                print()
            elif opcao_pessoa == 5:
                print('-*' * 20)
                print('...::: Alterar Dados de Pessoas Cadastradas :::...')
                alterar_pessoa()
                print('-*' * 20)
                print()
            elif opcao_pessoa == 6:
                print('-*' * 20)
                print('...::: Consultar Pessoas Cadastradas :::...')
                consulta_pessoa()
                print('-*' * 20)
                print()
            elif opcao_pessoa == 7:
                print('...::: ENCERRANDO :::...')
                print()
                break
            else:
                print('Opção inválida!')
        # CADASTRO DE LIVROS
        elif opcao == 2:
            exibir_menu_livros()
            opcao_livros = int(input('Opção: '))
            if opcao_livros == 1:
                print('-*' * 20)
                print('...::: Cadastro de Livros :::...')
                cadastro_livros()
                print('-*' * 20)
                print()
            elif opcao_livros == 2:
                print('-*' * 20)
                print('...::: Listar Livros Cadastrados :::...')
                listar_livros()
                print('-*' * 20)
                print()
            elif opcao_livros == 3:
                print('-*' * 20)
                print('...::: Buscar Livros Cadastrados :::...')
                buscar_livros()
                print('-*' * 20)
                print()
            elif opcao_livros == 4:
                print('-*' * 20)
                print('...::: Remover Livros Cadastrados :::...')
                remover_livro()
                print('-*' * 20)
                print()
            elif opcao_livros == 5:
                print('-*' * 20)
                print('...::: Alterar Livros Cadastrados :::...')
                alterar_livros()
                print('-*' * 20)
                print()
            elif opcao_livros == 6:
                print('-*' * 20)
                print('...::: Consultar Livros Cadastrados :::...')
                consulta_livros()
                print('-*' * 20)
                print()
            elif opcao_livros == 7:
                print('...::: ENCERRANDO :::...')
                print()
                break
            else:
                print('Opção inválida!')
        elif opcao == 3:
            print('-*' * 20)
            print('...::: Empréstimo :::...')
            emprestimo()
            print('-*' * 20)
            print()
        # devolução
        elif opcao == 4:
            print('-*' * 20)
            print('...::: Devolução de Livros :::...')
            devolucao()
            print('-*' * 20)
        # relatório
        elif opcao == 5:
            print('-*' * 20)
            print('...::: Relatórios :::...')
            relatorio()
            print('-*' * 20)
        # encerrando
        elif opcao == 6:
            print('-*' * 20)
            print('...::: ENCERRANDO :::...')
            print('-*' * 20)
            break


menu_principal()