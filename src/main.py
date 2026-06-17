lista = []


cont = int(input("Digite quantos nomes deseja inserir: "))
for i in range(cont):
    nome = input(f"Digite o {i + 1} nome: ")
    lista.append(nome)
print(lista)