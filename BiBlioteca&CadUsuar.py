import datetime 

livros_ficçao_cientifica = {'Kindred – laços de sangue': {"emprestados": 0, "disponiveis": 3},'Neuromancer':{"emprestados": 0, "disponiveis": 3},'Eu, robo':{"emprestados": 0, "disponiveis": 3}, 'O fim da infancia':{"emprestados": 0, "disponiveis": 2}, 'O Homem do castelo alto':{"emprestados": 0, "disponiveis": 5}, 'A paixão da nova eva':{"emprestados": 0, "disponiveis": 5}, 'A maquina do tempo':{"emprestados": 0, "disponiveis": 5}, 'O guia do mochileiro das galaxias':{"emprestados": 0, "disponiveis": 5},'As cronicas marcianas':{"emprestados": 0, "disponiveis": 4}, 'Fundação – trilogia':{"emprestados": 0, "disponiveis": 1}}

livros_fantasia = {'A sociedade do anel':{"emprestados": 0, "disponiveis": 6}, 'A guerra dos tronos':{"emprestados": 0, "disponiveis": 5}, 'Deuses americanos':{"emprestados": 0, "disponiveis": 5},'As brumas de avalon':{"emprestados": 0, "disponiveis": 5},'O Nnome do vento':{"emprestados": 0, "disponiveis": 5},'O leão':{"emprestados": 0, "disponiveis": 5},' A feiticeira e o guarda-roupa':{"emprestados": 0, "disponiveis": 5},'O maravilhoso mágico de oz':{"emprestados": 0, "disponiveis": 3},'Eragon':{"emprestados": 0, "disponiveis": 2}, 'Harry potter e a pedra filosofal':{"emprestados": 0, "disponiveis": 4},'A cor da magia ':{"emprestados": 0, "disponiveis": 1}}

livros_romance = {'Orgulho e preconceito':{"emprestados": 0, "disponiveis": 4}, 'Os miseráveis':{"emprestados": 0, "disponiveis": 6},'Dom casmurro':{"emprestados": 0, "disponiveis": 8},'Anna karenina':{"emprestados": 0, "disponiveis": 8},'Os catadores de conchas':{"emprestados": 0, "disponiveis": 3},'O morro dos ventos uivantes':{"emprestados": 0, "disponiveis": 5},'O amor nos tempos de cólera':{"emprestados": 0, "disponiveis": 3},'O retrato de dorian Gray':{"emprestados": 0, "disponiveis": 1}, 'Cem anos de solidão':{"emprestados": 0, "disponiveis": 3},'Crime e castigo':{"emprestados": 0, "disponiveis": 7}}

livros_terror = {'O exorcista':{"emprestados": 0, "disponiveis": 2},'It-a coisa ':{"emprestados": 0, "disponiveis": 4},'Cemiterio':{"emprestados": 0, "disponiveis": 2},'Dracula':{"emprestados": 0, "disponiveis": 3},'O iluminado':{"emprestados": 0, "disponiveis": 3},'A casa infernal':{"emprestados": 0, "disponiveis": 4},'o desfiladeiro do medo':{"emprestados": 0, "disponiveis": 4},'A noiva fantasma':{"emprestados": 0, "disponiveis": 2},'As ruinas':{"emprestados": 0, "disponiveis": 3},'O bebe de rosimery':{"emprestados": 0, "disponiveis": 2}}

livros_psicologia = {'Introdução à psicologia':{"emprestados": 0, "disponiveis": 4},'O poder do habito':{"emprestados": 0, "disponiveis": 2},'O mal-estar na civilização':{"emprestados": 0, "disponiveis": 2},'O animal social':{"emprestados": 0, "disponiveis": 3},'Inteligência emocional':{"emprestados": 0, "disponiveis": 1},'O homem que confundiu sua esposa com um chapéu':{"emprestados": 0, "disponiveis": 3},'Mulheres que amam demais':{"emprestados": 0, "disponiveis": 2},'Teoria das personalidades':{"emprestados": 0, "disponiveis": 3},'O livro vermelho':{"emprestados": 0, "disponiveis": 2},'Poderosa mente':{"emprestados": 0, "disponiveis": 4}}

#poderia criar um dicionario para guarda todos os tipos de literaturas


usuarios = {}
while True:
 inicio = input('Digite (C) para cadastro ou (L) para loguin: ')
 match inicio:
    case 'c':
     print('CADASTRO')
     print('_'*60)
     cadastro_usuario = input('Cadastre seu usuario: ')
     senha_cadastrada = input('Cadastre uma senha: ')
     senha_confirmacao = input('Digite a senha novamente para confirmar: ')

     while len(senha_cadastrada) <=3 or senha_cadastrada != senha_confirmacao:
      print('A senha deve conter mais de 3 caracteres')
      senha_cadastrada = input('Cadastre uma senha: ')
      senha_confirmacao = input('Confirme a senha: ')
       
      if senha_confirmacao == senha_cadastrada and len(senha_cadastrada) >=3:
         print(f'{cadastro_usuario} senha cadastrada')   
       
     else:
        usuarios[cadastro_usuario] = senha_cadastrada  
        # print('senha cadastrada')
        print(usuarios)
        continue
           
    case 'l':
     print('_'*60)
     print('LOGIN')
   #   print(usuarios)
     usuario = input('Usuario: ')
     senha_digitada = input('Senha: ')
     buscar_usuario = [usuario for x in usuarios if usuario == x]
     while buscar_usuario != [usuario]:
      print('Usuario incorreto')
      usuario = input('Digite novamente, Usuario: ')
      senha_digitada = input('Senha: ')
      buscar_usuario = [usuario for x in usuarios if usuario == x]
     if senha_digitada == usuarios[cadastro_usuario]:
      print('BEM-VINDO')
     elif senha_digitada != usuarios[cadastro_usuario]:
        print('3 tentativas')
        for numero_tentativa in range(1, 4):
         senha_digitada2 = input(f'Senha incorreta, tentativa {numero_tentativa}, tente novamente: ')
         if senha_digitada2 == usuarios[cadastro_usuario]:
            print('BEM-VINDO')
            break
     else:
      print('Bloqueado')

     livros_devolvidos = {}
     livros_emprestados = {}
     genero = str
     while genero != 'fechar':
      genero = input(f"""Temos de: 
      Terror
      Psicologia
      Ficção cientifica
      Fantasia                       
      Romance
      fechar                         
      : """).lower()  
      match genero:
       case 'terror':
        print(livros_terror)
        nome = input('Digite o nome do livro: ').capitalize()
        buscar = [nome for x in livros_terror if nome == x]
        if buscar:
               print(f'Digite (e) para pegar emprestado ou (d) para devolver: {nome}')
               emprestimo = input(f'Registar emprestimo(e) do livro {nome} ou devolver (d):  ')
               match emprestimo:        
                case 'e':
                 if nome in livros_terror:
                  if livros_terror[nome]["disponiveis"] > 0:
                   livros_terror[nome]["disponiveis"] -= 1
                   livros_terror[nome]["emprestados"] += 1
                   data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                   livros_emprestados[nome] = data_hora_emprestimo
                  print(f"O livro {nome} foi emprestado com sucesso!")
                  print(livros_emprestados)
                  continue 
                 elif livros_terror[nome]["disponiveis"] == 0:
                  print(f"Desculpe, o livro {nome} não está disponível no momento.")
                case 'd':
                 if nome in livros_terror:
                  if livros_terror[nome]["emprestados"] > 0:
                   livros_terror[nome]["emprestados"] -= 1
                   livros_terror[nome]["disponiveis"] += 1
                   data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                   livros_devolvidos[nome] = data_hora_emprestimo
                  print(f"O livro {nome} foi devolvido com sucesso!")
                  print(livros_devolvidos)
                 print('menu principal')
                 continue         
        else:
          print('livro nao encontrado')
       case 'psicologia':
        print(livros_psicologia)
        nome = input('Digite o nome do livro: ').capitalize()
        buscar = [nome for x in livros_psicologia if nome == x]
        if buscar:
               print(f'Digite (e) para pegar emprestado ou (d) para devolver: {nome}')
               emprestimo = input(f'Registar emprestimo(e) do livro {nome} ou devolver (d):  ')
               match emprestimo:        
                case 'e':
                 if nome in livros_psicologia:
                  if livros_psicologia[nome]["disponiveis"] > 0:
                   livros_psicologia[nome]["disponiveis"] -= 1
                   livros_psicologia[nome]["emprestados"] += 1
                   data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                   livros_emprestados[nome] = data_hora_emprestimo
                   print(f"{nome}: Emprestimo realizado com sucesso!")
                   print(livros_emprestados)
                   print('-'*50)
                   
                  elif livros_psicologia[nome]["disponiveis"] == 0:
                   print(f"Desculpe, o livro {nome} não está disponível no momento.")
                case 'd':
                  if nome in livros_psicologia:
                   if livros_psicologia[nome]["emprestados"] > 0:
                      livros_psicologia[nome]["emprestados"] -= 1
                      livros_psicologia[nome]["disponiveis"] += 1
                   data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                   livros_devolvidos[nome] = data_hora_emprestimo
                  print(f"O livro {nome} foi devolvido com sucesso!")
                  print(livros_devolvidos)
                  print('-'*50)                  
        else:
          print('livro nao encontrado')
       case 'ficção cientifica':
        print(livros_ficçao_cientifica)
        nome = input('Digite o nome do livro: ').capitalize()
        buscar = [nome for x in livros_ficçao_cientifica if nome == x]
        if buscar:
               print(f'Digite (e) para pegar emprestado ou (d) para devolver: {nome}')
               emprestimo = input(f'Registar emprestimo(e) do livro {nome} ou devolver (d):  ')
               match emprestimo:        
                case 'e':
                 if nome in livros_ficçao_cientifica:
                  if livros_ficçao_cientifica[nome]["disponiveis"] > 0:
                   livros_ficçao_cientifica[nome]["disponiveis"] -= 1
                   livros_ficçao_cientifica[nome]["emprestados"] += 1
                   data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                   livros_emprestados[nome] = data_hora_emprestimo
                  print(f"{nome}: Emprestimo realizado com sucesso!")
                  print(livros_emprestados)
                  print('-'*50)
                  
                 elif livros_ficçao_cientifica[nome]["disponiveis"] == 0:
                  print(f"Desculpe, o livro {nome} não está disponível no momento.")
                case 'd':
                 if nome in livros_ficçao_cientifica:
                  if livros_ficçao_cientifica[nome]["emprestados"] > 0:
                   livros_ficçao_cientifica[nome]["emprestados"] -= 1
                   livros_ficçao_cientifica[nome]["disponiveis"] += 1
                   data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                   livros_devolvidos[nome] = data_hora_emprestimo
                  print(f"O livro {nome} foi devolvido com sucesso!")
                  print(livros_devolvidos)
                  print('-'*50)
                           
        else:
          print('livro nao encontrado')    
       case 'fantasia':
        print(livros_fantasia)
        nome = input('Digite o nome do livro: ').capitalize()
        buscar = [nome for x in livros_fantasia if nome == x]
        if buscar:
               print(f'Digite (e) para pegar emprestado ou (d) para devolver: {nome}')
               emprestimo = input(f'Registar emprestimo(e) do livro {nome} ou devolver (d):  ')
               match emprestimo:        
                case 'e':
                 if nome in livros_fantasia:
                  if livros_fantasia[nome]["disponiveis"] > 0:
                   livros_fantasia[nome]["disponiveis"] -= 1
                   livros_fantasia[nome]["emprestados"] += 1
                   data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                   livros_emprestados[nome] = data_hora_emprestimo
                  print(f"{nome}: Emprestimo realizado com sucesso!")
                  print(livros_emprestados)
                  print('-'*50)
                  
                 elif livros_fantasia[nome]["disponiveis"] == 0:
                  print(f"Desculpe, o livro {nome} não está disponível no momento.")
                case 'd':
                 if nome in livros_fantasia:
                  if livros_fantasia[nome]["emprestados"] > 0:
                   livros_fantasia[nome]["emprestados"] -= 1
                   livros_fantasia[nome]["disponiveis"] += 1
                   data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                   livros_devolvidos[nome] = data_hora_emprestimo
                  print(f"O livro {nome} foi devolvido com sucesso!")
                  print(livros_devolvidos)
                  print('-'*50)
                           
        else:
          print('livro nao encontrado')    
       case 'romance':
        print(livros_romance)
        nome = input('Digite o nome do livro: ').capitalize()
        buscar = [nome for x in livros_romance if nome == x]
        if buscar:
               print(f'Digite (e) para pegar emprestado ou (d) para devolver: {nome}')
               emprestimo = input(f'Registar emprestimo(e) do livro {nome} ou devolver (d):  ')
               match emprestimo:        
                case 'e':
                 if nome in livros_romance:
                  if livros_romance[nome]["disponiveis"] > 0:
                   livros_romance[nome]["disponiveis"] -= 1
                   livros_romance[nome]["emprestados"] += 1
                   data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                   livros_emprestados[nome] = data_hora_emprestimo
                  print(f"{nome}: Emprestimo realizado com sucesso!")
                  print(livros_emprestados)
                  print('-'*50)
                  
                 elif livros_romance[nome]["disponiveis"] == 0:
                  print(f"Desculpe, o livro {nome} não está disponível no momento.")
                case 'd':
                 if nome in livros_romance:
                  if livros_romance[nome]["emprestados"] > 0:
                   livros_romance[nome]["emprestados"] -= 1
                   livros_romance[nome]["disponiveis"] += 1
                   data_hora_emprestimo = datetime.datetime.now().strftime("%d-%m-%Y %H:%M")
                   livros_devolvidos[nome] = data_hora_emprestimo
                  print(f"O livro {nome} foi devolvido com sucesso!")
                  print(livros_devolvidos)
                  print('-'*50)
                           
        else:
          print('Livro não encontrado')
      
