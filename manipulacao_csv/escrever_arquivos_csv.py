import csv

def criar_csv():
    with open("alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerow(["Maria", 16, "DEV"])
        escritor.writerow(["Larissa", 16, "DEV"])
        escritor.writerow(["Luiz", 16, "DEV"])

#criar_csv()


def salvar_alunos():
    alunos = [
        ["Maria", 16, "DEV"],
        ["Larissa", 16, "DEV"],
        ["Luiz", 16, "DEV"],
        ["Rosolem", 16, "DEV"],
        ["Jaison", 18, "DEV"],
        ["Renan", 40, "Python"]
    ]

    with open("novos-alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)

        escritor.writerow(["Nome", "Idade", "Curso"])

        escritor.writerows(alunos)

#salvar_alunos()

def ler_csv():
    with open("novos-alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)

        next(leitor)

        for linha in leitor:
            print(linha[0])

#ler_csv()

def exibir_alunos():
    with open("novos-alunos.csv", "r", encoding="utf-8") as arquivo:
        alunos = csv.DictReader(arquivo)

        for aluno in alunos:
            print(aluno["Curso"])

#exibir_alunos()


def cadastrar_aluno():
    with open("novos-alunos.csv", "a+", encoding="utf-8") as arquivo:
        arquivo.seek(0,2)
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        curso = input("Digite o curso do aluno: ")

        escritor = csv.writer(arquivo)
        escritor.writerow([nome, idade, curso])

        arquivo.seek(0)
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            print(linha)

#cadastrar_aluno()


def deletar_aluno():
    with open("novos_alunos.csv", "r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        alunos = list(leitor)

        with open("novos_alunos.csv", "w", newline="", encoding="utf-8") as arquivo:
            cabecalho = ["Nome", "Idade", "Curso"]
            escritor = csv.DictWriter(arquivo, fieldnames=cabecalho)

            escritor.writeheader()

            aluno_apagar = input("Digite o nome do aluno(a) que deseja apagar: ")

            for aluno in alunos:
                if alunos["Nome"] != aluno_apagar:
                    escritor.writerow(aluno)


deletar_aluno()