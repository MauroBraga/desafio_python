
def addContato(contatos,nome,telefone,email):
    contato ={"nome":nome,"telefone":telefone,"email":email,"favorito":False}
    contatos.append(contato)
    print(f"Conato {nome} foi adicionada com sucesso!")
    return

def updateContato(contatos,indice,nome,telefone,email):
    indice_ajustado = int(indice) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contatos[indice_ajustado]["nome"]=nome
        contatos[indice_ajustado]["telefone"]=telefone
        contatos[indice_ajustado]["email"]=email
        print(f"Conato {nome}  foi alterado!")
    else:
        print(f"Conato {nome}  não foi alterado!")
    return

def marcareContato(contatos,indice):
    indice_ajustado = int(indice) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        nome = contatos[indice_ajustado]["nome"]
        contatos[indice_ajustado]["favorito"] =  False if contatos[indice_ajustado]["favorito"] else True
        print(f"Conato {nome}  foi alterado!")
    else:
        print(f"Conato não foi alterado!")
    return

def findAll(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{status}] Nome:{nome} telefone: {telefone} e-mail: {email}")
    return

def findAllFavoritos(contatos):
    print("\nLista de contatos favoritos:")
    for indice, contato in enumerate(contatos, start=1):
        if(contato["favorito"]):
            status = "✓" if contato["favorito"] else " "
            nome = contato["nome"]
            telefone = contato["telefone"]
            email = contato["email"]
            print(f"{indice}. [{status}] Nome:{nome} telefone: {telefone} e-mail: {email}")
    return

def deleteContato(contatos,indice):
    indice_ajustado = int(indice) - 1
    if indice_ajustado >= 0 and indice_ajustado < len(contatos):
        contato = contatos[indice_ajustado]
        nome = contatos[indice_ajustado]["nome"]
        contatos.remove(contato)
        print(f"Conato {nome}  foi deletado!")
    else:
        print(f"Conato não foi deletado!")
    return

contatos=[]

while True:
  print("\nMinha Agenda:")
  print("1. Adicionar contato")
  print("2. Ver contatos")
  print("3. Atualizar contato")
  print("4. Marcar/desmarcar um contato como favorito")
  print("5. Ver contatos Favorito")
  print("6. Deletar contato")
  print("7. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
      nome = input("Digite o nome : ")
      telefone = input("Digite o telefone : ")
      email = input("Digite o email : ")
      addContato(contatos, nome,telefone,email)
  elif escolha == "2":
      findAll(contatos)
  elif escolha == "3":
      indice = int(input("Digite o indice : "))
      nome = input("Digite o nome : ")
      telefone = input("Digite o telefone : ")
      email = input("Digite o email : ")
      updateContato(contatos,indice, nome,telefone,email)
  elif escolha == "4":
      indice = int(input("Digite o indice : "))
      marcareContato(contatos,indice)
  elif escolha == "5":
      findAllFavoritos(contatos)
  elif escolha == "6":
      indice = int(input("Digite o indice : "))
      deleteContato(contatos,indice)
  elif escolha == "7":
      break