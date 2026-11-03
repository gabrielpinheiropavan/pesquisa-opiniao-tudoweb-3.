
# Pesquisa de Opiniao - Empresa TudoWeb

TOTAL_ENTREVISTADOS = 50

# Contadores das respostas
quantidade_excelente = 0
quantidade_bom = 0
quantidade_ruim = 0

print("======================================")
print("   PESQUISA DE SATISFACAO - TUDOWEB")
print("======================================")

# Repeticao para entrevistar 50 pessoas
for entrevistado in range(1, TOTAL_ENTREVISTADOS + 1):

    print(f"\n--- Entrevistado {entrevistado} de {TOTAL_ENTREVISTADOS} ---")

    # Coleta do nome
    nome = input("Digite seu nome: ").strip()

    while nome == "":
        print("O nome nao pode ficar vazio.")
        nome = input("Digite seu nome: ").strip()

    # Coleta e validacao da idade
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade > 0:
                break
            else:
                print("Digite uma idade maior que zero.")
        except ValueError:
            print("Digite uma idade valida usando numeros.")

    # Coleta e validacao da opiniao
    print("\nComo voce avalia nosso atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    while True:
        try:
            opiniao = int(input("Digite sua opiniao (1, 2 ou 3): "))

            if opiniao in (1, 2, 3):
                break
            else:
                print("Opcao invalida. Escolha 1, 2 ou 3.")
        except ValueError:
            print("Digite apenas numeros.")

    # Estrutura de decisao para contabilizar as respostas
    if opiniao == 1:
        quantidade_excelente += 1
        print("Obrigado pela avaliacao, EXCELENTE!")

    elif opiniao == 2:
        quantidade_bom += 1
        print("Obrigado pela avaliacao, BOM!")

    else:
        quantidade_ruim += 1
        print("Obrigado pela avaliacao, RUIM!")

# Resultado final da pesquisa
print("\n======================================")
print("       RESULTADO DA PESQUISA")
print("======================================")
print(f"Total de entrevistados: {TOTAL_ENTREVISTADOS}")
print(f"Respostas EXCELENTE: {quantidade_excelente}")
print(f"Respostas BOM: {quantidade_bom}")
print(f"Respostas RUIM: {quantidade_ruim}")
print("======================================")
print("Obrigado por participar da pesquisa!")