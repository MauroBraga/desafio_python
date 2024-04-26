
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

def findAll(contatos):
    print("\nLista de contatos:")
    for indice, contato in enumerate(contatos, start=1):
        status = "✓" if contato["favorito"] else " "
        nome = contato["nome"]
        telefone = contato["telefone"]
        email = contato["email"]
        print(f"{indice}. [{status}] Nome:{nome} telefone: {telefone} e-mail: {email}")
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
  elif escolha == "7":
      break