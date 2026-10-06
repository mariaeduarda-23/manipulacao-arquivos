import csv

# Ler o arquivo
with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
    treinadores = list(csv.DictReader(arquivo))


while True:
    print("\n===== TREINADORES POKÉMON =====")
    print("1 - Listar todos os treinadores")
    print("2 - Buscar treinador pelo nome")
    print("3 - Listar treinadores de uma região")
    print("4 - Mostrar treinador com maior nível")
    print("5 - Mostrar treinador com menor nível")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    # Opção 1
    if opcao == "1":
        for treinador in treinadores:
            print(f"Nome: {treinador['nome']}")
            print(f"Região: {treinador['regiao']}")
            print(f"Nível: {treinador['nivel']}")
            print()

    # Opção 2
    elif opcao == "2":
        nome = input("Digite o nome do treinador: ")

        encontrado = False

        for treinador in treinadores:
            if treinador["nome"].lower() == nome.lower():
                print(f"Nome: {treinador['nome']}")
                print(f"Região: {treinador['regiao']}")
                print(f"Nível: {treinador['nivel']}")
                encontrado = True

        if not encontrado:
            print("Treinador não encontrado.")

    # Opção 3
    elif opcao == "3":
        regiao = input("Digite a região: ")

        encontrado = False

        for treinador in treinadores:
            if treinador["regiao"].lower() == regiao.lower():
                print(f"Nome: {treinador['nome']}")
                print(f"Região: {treinador['regiao']}")
                print(f"Nível: {treinador['nivel']}")
                print()
                encontrado = True

        if not encontrado:
            print("Nenhum treinador encontrado nessa região.")

    # Opção 4
    elif opcao == "4":
        maior = treinadores[0]

        for treinador in treinadores:
            if int(treinador["nivel"]) > int(maior["nivel"]):
                maior = treinador

        print("Treinador com maior nível:")
        print(f"Nome: {maior['nome']}")
        print(f"Região: {maior['regiao']}")
        print(f"Nível: {maior['nivel']}")

    # Opção 5
    elif opcao == "5":
        menor = treinadores[0]

        for treinador in treinadores:
            if int(treinador["nivel"]) < int(menor["nivel"]):
                menor = treinador

        print("Treinador com menor nível:")
        print(f"Nome: {menor['nome']}")
        print(f"Região: {menor['regiao']}")
        print(f"Nível: {menor['nivel']}")

    # Opção 6
    elif opcao == "6":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")