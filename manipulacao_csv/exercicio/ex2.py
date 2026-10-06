import csv

# Ler o arquivo de treinadores
with open("treinadores.csv", "r", encoding="utf-8") as arquivo:
    treinadores = list(csv.DictReader(arquivo))

# Ler o arquivo de pokémons
with open("pokemons.csv", "r", encoding="utf-8") as arquivo:
    pokemons = list(csv.DictReader(arquivo))


while True:
    print("\n===== POKÉMON DOS TREINADORES =====")
    print("1 - Listar Pokémon de um treinador")
    print("2 - Contar Pokémon de um treinador")
    print("3 - Mostrar Pokémon de maior nível")
    print("4 - Mostrar Pokémon de menor nível")
    print("5 - Listar Pokémon de determinado tipo")
    print("6 - Voltar ao menu")

    opcao = input("Escolha uma opção: ")

    # Opção 1
    if opcao == "1":
        nome = input("Digite o nome do treinador: ")

        treinador_existe = False

        # Procurar o treinador
        for treinador in treinadores:
            if treinador["nome"].lower() == nome.lower():
                treinador_existe = True

        if treinador_existe:
            lista_pokemons = []

            # Procurar os pokémons desse treinador
            for pokemon in pokemons:
                if pokemon["treinador"].lower() == nome.lower():
                    lista_pokemons.append(pokemon)

            print("\nPokémon do treinador:")

            for pokemon in lista_pokemons:
                print(f"Nome: {pokemon['nome']}")
                print(f"Tipo: {pokemon['tipo']}")
                print(f"Nível: {pokemon['nivel']}")
                print()

        else:
            print("Treinador não encontrado.")

    # Opção 2
    elif opcao == "2":
        nome = input("Digite o nome do treinador: ")

        treinador_existe = False

        for treinador in treinadores:
            if treinador["nome"].lower() == nome.lower():
                treinador_existe = True

        if treinador_existe:
            quantidade = 0

            for pokemon in pokemons:
                if pokemon["treinador"].lower() == nome.lower():
                    quantidade += 1

            print(f"{nome} possui {quantidade} Pokémon.")

        else:
            print("Treinador não encontrado.")

    # Opção 3
    elif opcao == "3":
        nome = input("Digite o nome do treinador: ")

        treinador_existe = False

        for treinador in treinadores:
            if treinador["nome"].lower() == nome.lower():
                treinador_existe = True

        if treinador_existe:
            lista_pokemons = []

            for pokemon in pokemons:
                if pokemon["treinador"].lower() == nome.lower():
                    lista_pokemons.append(pokemon)

            if len(lista_pokemons) > 0:
                maior = lista_pokemons[0]

                for pokemon in lista_pokemons:
                    if int(pokemon["nivel"]) > int(maior["nivel"]):
                        maior = pokemon

                print("\nPokémon de maior nível:")
                print(f"Nome: {maior['nome']}")
                print(f"Tipo: {maior['tipo']}")
                print(f"Nível: {maior['nivel']}")

            else:
                print("Esse treinador não possui Pokémon.")

        else:
            print("Treinador não encontrado.")

    # Opção 4
    elif opcao == "4":
        nome = input("Digite o nome do treinador: ")

        treinador_existe = False

        for treinador in treinadores:
            if treinador["nome"].lower() == nome.lower():
                treinador_existe = True

        if treinador_existe:
            lista_pokemons = []

            for pokemon in pokemons:
                if pokemon["treinador"].lower() == nome.lower():
                    lista_pokemons.append(pokemon)

            if len(lista_pokemons) > 0:
                menor = lista_pokemons[0]

                for pokemon in lista_pokemons:
                    if int(pokemon["nivel"]) < int(menor["nivel"]):
                        menor = pokemon

                print("\nPokémon de menor nível:")
                print(f"Nome: {menor['nome']}")
                print(f"Tipo: {menor['tipo']}")
                print(f"Nível: {menor['nivel']}")

            else:
                print("Esse treinador não possui Pokémon.")

        else:
            print("Treinador não encontrado.")

    # Opção 5
    elif opcao == "5":
        tipo = input("Digite o tipo do Pokémon: ")

        lista_pokemons = []

        for pokemon in pokemons:
            if pokemon["tipo"].lower() == tipo.lower():
                lista_pokemons.append(pokemon)

        if len(lista_pokemons) > 0:
            print(f"\nPokémon do tipo {tipo}:")

            for pokemon in lista_pokemons:
                print(f"Nome: {pokemon['nome']}")
                print(f"Tipo: {pokemon['tipo']}")
                print(f"Nível: {pokemon['nivel']}")
                print(f"Treinador: {pokemon['treinador']}")
                print()

        else:
            print("Nenhum Pokémon desse tipo foi encontrado.")

    # Opção 6
    elif opcao == "6":
        print("Voltando ao menu...")
        break

    else:
        print("Opção inválida.")