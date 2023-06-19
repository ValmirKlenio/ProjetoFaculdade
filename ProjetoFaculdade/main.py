from datetime import date, datetime

# Listas para armazenar as pessoas, livros, empréstimos e devoluções
pessoas = []
livros = []
emprestimos = []
devolucoes = []

# Função para exibir o menu de opções relacionadas a pessoas
def exibir_menu_pessoa():
  print('''Escolha uma opção:
    [ 1 ] Cadastrar uma pessoa
    [ 2 ] Listar pessoas cadastradas
    [ 3 ] Procurar dados de uma pessoa
    [ 4 ] Remover uma pessoa
    [ 5 ] Alterar dados de uma pessoa
    [ 6 ] Consultar pessoa
    [ 7 ] Sair/Encerrar''')

# Função para cadastrar uma pessoa
def cadastro_pessoa():
  nome = input('Nome: ')
  cpf = int(input('CPF: '))
  # Verificar se o CPF já está cadastrado
  if any(p['cpf'] == cpf for p in pessoas):
    print('CPF já cadastrado!')
    return
  email = input('Email: ')
  pessoas.append({'nome': nome, 'cpf': cpf, 'email': email})
  print('Pessoa cadastrada com sucesso!')

# Função para listar as pessoas cadastradas
def listar_pessoa():
  if len(pessoas) == 0:
    print('Nenhuma pessoa cadastrada.')
  else:
    for p in pessoas:
      print(p)

# Função para buscar dados de uma pessoa
def buscar_pessoa():
  cpf = int(input('CPF: '))
  for p in pessoas:
    if p['cpf'] == cpf:
      print(f'Pessoa com o CPF {cpf} está cadastrada no sistema!')
      return
  print(f'Pessoa com CPF {cpf} não encontrada')

# Função para remover uma pessoa
def remover_pessoa():
  cpf = int(input('CPF: '))
  for p in pessoas:
    if p['cpf'] == cpf:
      pessoas.remove(p)
      print('Pessoa removida com sucesso!')
      return
  print(f'Pessoa com CPF {cpf} não encontrada.')

# Função para alterar dados de uma pessoa
def alterar_pessoa():
  cpf = int(input('Digite o CPF que deseja alterar: '))
  for p in pessoas:
    if p['cpf'] == cpf:
      print(p)
      alterar = input(
        'Deseja fazer a alteração desse cadastro? (S/N) ').upper()
      if alterar == 'S':
        pessoas.remove(p)
        print('Começando a alteração...')
        nome = input('Novo nome: ')
        email = input('Novo email: ')
        cpf = int(input('Novo CPF: '))
        pessoas.append({'nome': nome, 'cpf': cpf, 'email': email})
        print('Alterações feitas com sucesso!')
      return
  print('Pessoa não encontrada.')

# Função para consultar uma pessoa
def consulta_pessoa():
  print('''Escolha um tipo de consulta:
    [ 1 ] Consultar pelo nome
    [ 2 ] Consultar por parte do nome
    [ 3 ] Consultar pelo CPF''')
  consult = int(input('Por onde deseja consultar: '))
  if consult == 1:
    nome = input('Nome: ')
    for p in pessoas:
      if p['nome'] == nome:
        print(f'O nome {nome} está cadastrado no sistema!')
        return
    print(f'O nome {nome} não está cadastrado no nosso sistema')
  elif consult == 2:
    parte_nome = input('Parte do nome que deseja consultar: ')
    for p in pessoas:
      if parte_nome in p['nome']:
        print(f'A parte do nome {parte_nome} se encontra no nome {p["nome"]}')
        return
    print('Este nome não está cadastrado no nosso sistema! Tente novamente.')
  elif consult == 3:
    cpf = int(input('CPF: '))
    for p in pessoas:
      if p['cpf'] == cpf:
        print(f'O CPF {cpf} está cadastrado no nosso sistema!')
        return
    print('O CPF não está cadastrado no nosso sistema!')
  else:
    print('Opção inválida.')

# Função para exibir o menu de opções relacionadas a livros
def exibir_menu_livros():
  print('''Escolha uma opção:
    [ 1 ] Cadastrar um livro
    [ 2 ] Listar os livros cadastrados
    [ 3 ] Procurar os livros
    [ 4 ] Remover um livro
    [ 5 ] Alterar dados de um livro
    [ 6 ] Consultar livro
    [ 7 ] Encerrar/Sair''')

# Função para cadastrar um livro
def cadastro_livros():
  id_livro = int(input('Id: '))
  # Verificar se o livro já está cadastrado
  if any(l['Id do Livro'] == id_livro for l in livros):
    print('Livro já cadastrado!')
    return
  titulo = input('Título: ')
  resumo = input('Resumo: ')
  autor = input('Autor: ')
  editora = input('Editora: ')
  ano_publicacao = int(input('Ano de publicação: '))
  edicao = int(input('Edição: '))
  # Adicionar o livro à lista de livros
  livros.append({
    'Id do Livro': id_livro,
    'titulo': titulo,
    'resumo': resumo,
    'autor': autor,
    'editora': editora,
    'ano de publicação': ano_publicacao,
    'edição': edicao
  })
  print('Livro cadastrado com sucesso!!')

# Função para listar os livros cadastrados
def listar_livros():
  if len(livros) == 0:
    print('Nenhum livro cadastrado.')
  else:
    for l in livros:
      print(l)

# Função para buscar dados de um livro
def buscar_livros():
  id_livro = int(input('Id: '))
  for l in livros:
    if l['Id do Livro'] == id_livro:
      print(l)
      return
  print(f'Livro com id {id_livro} não foi encontrado')

# Função para remover um livro
def remover_livro():
  id_livro = int(input('Id do Livro: '))
  for l in livros:
    if l['Id do Livro'] == id_livro:
      livros.remove(l)
      print("Livro removido com sucesso!")
      return
  print(f'Livro com id {id_livro} não encontrado.')

# Função para alterar dados de um livro
def alterar_livros():
  id_livro = int(input('Digite o Id do livro que deseja alterar: '))
  for l in livros:
    if l['Id do Livro'] == id_livro:
      print(l)
      alterar_livro = input(
        'Deseja fazer a alteração desse cadastro? (S/N) ').upper()
      if alterar_livro == 'S':
        livros.remove(l)
        print('Começando a alteração...')
        id_livro = int(input('Novo id: '))
        titulo = str(input('Novo título: '))
        resumo = input('Novo resumo: ')
        autor = input('Novo(s) autor(res): ')
        editora = str(input('Nova editora: '))
        ano_publicacao = int(input('Novo ano de publicação: '))
        edicao = int(input('Nova edição: '))
        # Adicionar o livro com os novos dados à lista de livros
        livros.append({
          'Id do Livro': id_livro,
          'titulo': titulo,
          'resumo': resumo,
          'autor': autor,
          'editora': editora,
          'ano de publicação': ano_publicacao,
          'edição': edicao
        })
        print('Alterações feitas com sucesso!')
      return
  print('Livro não encontrado.')

# Função para consultar um livro
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
    for l in livros:
      if l['Id do Livro'] == id_livro:
        print(l)
        return
    print(f'O livro com o ID {id_livro} não está cadastrado')
  elif consul == 2:
    titulo = input('Título: ')
    for l in livros:
      if l['titulo'] == titulo:
        print(l)
        return
    print(f'O Título {titulo} não está cadastrado')
  elif consul == 3:
    parte_titulo = input('Parte do título que deseja consultar: ')
    for l in livros:
      if parte_titulo in l['titulo']:
        print(
          f'A parte do Título {parte_titulo} se encontra no título {l["titulo"]}'
        )
        return
    print('Este Título não está cadastrado no nosso sistema! Tente novamente.')
  elif consul == 4:
    autor = input('Autor(es): ')
    for l in livros:
      if autor in l['autor']:
        print(
          f'O(s) Autor(es) {autor} está(ão) cadastrado(s) no nosso sistema!')
        return
    print('O(s) Autor(es) não está(ão) cadastrado(s) no nosso sistema!')
  elif consul == 5:
    editora = input('Editora: ')
    for l in livros:
      if editora == l['editora']:
        print(f'A Editora {editora} está cadastrada no nosso sistema!')
        return
    print('A Editora não está cadastrada no nosso sistema!')
  else:
    print('Opção inválida.')

# Função para realizar um empréstimo de livro
def emprestimo():
  id_livro = int(input('Id: '))
  # Verificar se o livro já está emprestado
  for e in emprestimos:
    if e['Id do livro'] == id_livro:
      print('Livro já emprestado!')
      return
    # Verificar se o livro existe na lista de livros
  for l in livros:
    if l['Id do Livro'] == id_livro:
      pessoa = input('Nome da pessoa: ')
      titulo = l['titulo']
      data = date.today()
      hora = datetime.now().time()
      # Adicionar o empréstimo à lista de empréstimos
      emprestimos.append({
        'Id do livro': id_livro,
        'Título': titulo,
        'Pessoa': pessoa,
        'Data de saída': data,
        'Hora de saída': hora
      })
      print('Empréstimo realizado com sucesso!')
      return
  print(f'Livro com id {id_livro} não encontrado.')

# Função para realizar uma devolução de livro
def devolucao():
  id_livro = int(input('Id: '))
  # Verificar se o livro já foi devolvido
  for d in devolucoes:
    if d['Id do livro'] == id_livro:
      print('Livro já devolvido!')
      return
    # Verificar se o livro está emprestado
  for e in emprestimos:
    if e['Id do livro'] == id_livro:
      pessoa = e['Pessoa']
      titulo = e['Título']
      data = date.today()
      hora = datetime.now().time()
      # Adicionar a devolução à lista de devoluções
      devolucoes.append({
        'Id do livro': id_livro,
        'Título': titulo,
        'Pessoa': pessoa,
        'Data de devolução': data,
        'Hora de devolução': hora
      })
      emprestimos.remove(e)
      print('Devolução realizada com sucesso!')
      return
  print(f'Livro com id {id_livro} não encontrado.')

# Função para listar os empréstimos realizados
def listar_emprestimos():
  if len(emprestimos) == 0:
    print('Nenhum livro emprestado.')
  else:
    for e in emprestimos:
      print(e)

# Função para listar as devoluções realizadas
def listar_devolucoes():
  if len(devolucoes) == 0:
    print('Nenhum livro devolvido.')
  else:
    for d in devolucoes:
      print(d)

# Função para exibir o menu principal
def menu_principal():
  print('Bem-vindo(a) à Biblioteca!')
  while True:
    print('Escolha uma opção:')
    print('[ 1 ] Menu Pessoa')
    print('[ 2 ] Menu Livros')
    print('[ 3 ] Empréstimos')
    print('[ 4 ] Relatórios')
    print('[ 5 ] Encerrar/Sair')
    opcao = int(input('Opção: '))
    if opcao == 1:
      # Opções relacionadas a pessoas
      exibir_menu_pessoa()
      opcao_pessoa = int(input('Opção: '))
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
        continue
      else:
        print('Opção inválida!')
    elif opcao == 2:
      # Opções relacionadas a livros
      exibir_menu_livros()
      opcao_livros = int(input('Opção: '))
      if opcao_livros == 1:
        cadastro_livros()
      elif opcao_livros == 2:
        listar_livros()
      elif opcao_livros == 3:
        buscar_livros()
      elif opcao_livros == 4:
        remover_livro()
      elif opcao_livros == 5:
        alterar_livros()
      elif opcao_livros == 6:
        consulta_livros()
      elif opcao_livros == 7:
        continue
      else:
        print('Opção inválida!')
    elif opcao == 3:
      # Opções relacionadas a empréstimos
      print('[ 1 ] Empréstimo de livro')
      print('[ 2 ] Devolução de livro')
      print('[ 3 ] Listar empréstimos')
      print('[ 4 ] Listar devoluções')
      print('[ 5 ] Encerrar/Sair')
      opcao_emprestimo = int(input('Opção: '))
      if opcao_emprestimo == 1:
        emprestimo()
      elif opcao_emprestimo == 2:
        devolucao()
      elif opcao_emprestimo == 3:
        listar_emprestimos()
      elif opcao_emprestimo == 4:
        listar_devolucoes()
      elif opcao_emprestimo == 5:
        continue
      else:
        print('Opção inválida!')
    elif opcao == 4:
      # Opções relacionadas a relatórios
      print('---Relatórios---')
      print('[ 1 ] Relatório de empréstimos')
      print('[ 2 ] Relatório de devoluções')
      print('[ 3 ] Encerrar/Sair')
      opcao_relatorio = int(input('Opção: '))
      if opcao_relatorio == 1:
        print('---Relatório de Empréstimos---')
        if len(emprestimos) == 0:
          print('Nenhum livro emprestado.')
        else:
          for e in emprestimos:
            print(f"Id do livro: {e['Id do livro']}")
            print(f"Título: {e['Título']}")
            print(f"Pessoa: {e['Pessoa']}")
            print(f"Data de saída: {e['Data de saída']}")
            print(f"Hora de saída: {e['Hora de saída']}")
            print('---')
      elif opcao_relatorio == 2:
        print('---Relatório de Devoluções---')
        if len(devolucoes) == 0:
          print('Nenhum livro devolvido.')
        else:
          for d in devolucoes:
            print(f"Id do livro: {d['Id do livro']}")
            print(f"Título: {d['Título']}")
            print(f"Pessoa: {d['Pessoa']}")
            print(f"Data de devolução: {d['Data de devolução']}")
            print(f"Hora de devolução: {d['Hora de devolução']}")
            print('---')
      elif opcao_relatorio == 3:
        continue
      else:
        print('Opção inválida!')
    elif opcao == 5:
      print('Saindo...')
      break
    else:
      print('Opção inválida!')

# Executar o menu principal
menu_principal()
