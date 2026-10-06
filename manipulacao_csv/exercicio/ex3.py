import csv

# Ler o arquivo de treinadores
with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
    treinadores = list(csv.DictReader(arquivo))

# Ler o arquivo de pokémons
with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
    pokemons = list(csv.DictReader(arquivo))


while True:
    print("\n===== RELATÓRIOS =====")
    print("1 - Relatório de um treinador")
    print("2 - Média de nível dos Pokémon de um treinador")
    print("3 - Média de nível dos Pokémon por tipo")
    print("4 - Quantidade de Pokémon por treinador")
    print("5 - Quantidade de Pokémon por tipo")
    print("6 - Treinadores com nível acima de um valor")
    print("7 - Sair")

    opcao = input("Escolha uma opção: ")

    # OPÇÃO 1
    if opcao == "1":
        nome = input("Digite o nome do treinador: ")

        treinador_encontrado = None

        for treinador in treinadores:
            if treinador["nome"].lower() == nome.lower():
                treinador_encontrado = treinador

        if treinador_encontrado != None:
            print("\n===== RELATÓRIO =====")
            print(f"Treinador: {treinador_encontrado['nome']}")
            print(f"Região: {treinador_encontrado['regiao']}")
            print(f"Nível do treinador: {treinador_encontrado['nivel']}")

            print("\nPokémon:")

            for pokemon in pokemons:
                if pokemon["treinador"].lower() == nome.lower():
                    print(f"- {pokemon['nome']} - {pokemon['tipo']} - Nível {pokemon['nivel']}")

        else:
            print("Treinador não encontrado.")

    # OPÇÃO 2
    elif opcao == "2":
        nome = input("Digite o nome do treinador: ")

        treinador_existe = False

        for treinador in treinadores:
            if treinador["nome"].lower() == nome.lower():
                treinador_existe = True

        if treinador_existe:
            soma = 0
            quantidade = 0

            for pokemon in pokemons:
                if pokemon["treinador"].lower() == nome.lower():
                    nivel = int(pokemon["nivel"])
                    soma += nivel
                    quantidade += 1

            if quantidade > 0:
                media = soma / quantidade
                print(f"Média de nível dos Pokémon de {nome}: {media:.2f}")
            else:
                print("Esse treinador não possui Pokémon.")

        else:
            print("Treinador não encontrado.")

    # OPÇÃO 3
    elif opcao == "3":
        tipo = input("Digite o tipo do Pokémon: ")

        soma = 0
        quantidade = 0

        for pokemon in pokemons:
            if pokemon["tipo"].lower() == tipo.lower():
                nivel = int(pokemon["nivel"])
                soma += nivel
                quantidade += 1

        if quantidade > 0:
            media = soma / quantidade
            print(f"Média de nível dos Pokémon do tipo {tipo}: {media:.2f}")
        else:
            print("Nenhum Pokémon desse tipo foi encontrado.")

    # OPÇÃO 4
    elif opcao == "4":
        quantidade_treinadores = {}

        for pokemon in pokemons:
            treinador = pokemon["treinador"]

            if treinador in quantidade_treinadores:
                quantidade_treinadores[treinador] += 1
            else:
                quantidade_treinadores[treinador] = 1

        print("\n===== QUANTIDADE DE POKÉMON POR TREINADOR =====")

        # Ordenar do maior para o menor
        resultado = sorted(
            quantidade_treinadores.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for treinador, quantidade in resultado:
            print(f"{treinador}: {quantidade}")

    # OPÇÃO 5
    elif opcao == "5":
        quantidade_tipos = {}

        for pokemon in pokemons:
            tipo = pokemon["tipo"]

            if tipo in quantidade_tipos:
                quantidade_tipos[tipo] += 1
            else:
                quantidade_tipos[tipo] = 1

        print("\n===== QUANTIDADE DE POKÉMON POR TIPO =====")

        # Ordenar do maior para o menor
        resultado = sorted(
            quantidade_tipos.items(),
            key=lambda item: item[1],
            reverse=True
        )

        for tipo, quantidade in resultado:
            print(f"{tipo}: {quantidade}")

    # OPÇÃO 6
    elif opcao == "6":
        nivel = int(input("Digite o nível mínimo: "))

        print(f"\nTreinadores com nível acima de {nivel}:")

        encontrou = False

        for treinador in treinadores:
            if int(treinador["nivel"]) > nivel:
                print(f"- {treinador['nome']} - Nível {treinador['nivel']}")
                encontrou = True

        if encontrou == False:
            print("Nenhum treinador encontrado.")

    # OPÇÃO 7
    elif opcao == "7":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")