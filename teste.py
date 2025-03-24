# import os

def menu():
    while True:
        print("Escolha a temperatura base para conversão:\n")
        print("1 - Celsius\n")
        print("2 - Farenheit\n")
        print("3 - Kelvin\n")
        print("4 - Sair\n")
    
        opcao_base = int(input("\nDigite a opção desejada: "))

        if opcao_base == 1:
            temp = float(input("\nDigite a temperatura em Celsius: "))
            converter_temperatura(temp, "C")
        elif opcao_base == 2:
            temp = float(input("\nDigite a temperatura em Fahrenheit: "))
            converter_temperatura(temp, "F")
        elif opcao_base == 3:
            temp = float(input("\nDigite a temperatura em Kelvin: "))
            converter_temperatura(temp, "K")
        elif opcao_base == 4:
            print("Saindo... Até mais!")
            break
        else:
            print("Opção inválida! Escolha uma opção do menu.")
            
        input("\nPressione Enter para continuar...") # Aguarda o usuário pressionar Enter antes de voltar ao menu
        # os.system("cls" if os.name == "nt" else "clear")  # Limpa o terminal
            
def converter_temperatura(valor, unidade):
    print("\nEscolha para qual unidade deseja converter:")
    if unidade == "C":
        print("1 - Fahrenheit")
        print("2 - Kelvin")
        print("3 - Ambas")
    elif unidade == "F":
        print("1 - Celsius")
        print("2 - Kelvin")
        print("3 - Ambas")
    elif unidade == "K":
        print("1 - Celsius")
        print("2 - Fahrenheit")
        print("3 - Ambas")

    opcao = input("\nDigite a opção desejada: ")

    if unidade == "C":
        f = (valor * 9/5) + 32
        k = valor + 273.15
        if opcao == "1":
            print(f"\n{valor}°C = {f:.2f}°F")
        elif opcao == "2":
            print(f"\n{valor}°C = {k:.2f}K")
        elif opcao == "3":
            print(f"\n{valor}°C = {f:.2f}°F e {k:.2f}K")
        else:
            print("Opção inválida!")

    elif unidade == "F":
        c = (valor - 32) * 5/9
        k = (valor - 32) * 5/9 + 273.15
        if opcao == "1":
            print(f"\n{valor}°F = {c:.2f}°C\n")
        elif opcao == "2":
            print(f"\n{valor}°F = {k:.2f}K\n")
        elif opcao == "3":
            print(f"\n{valor}°F = {c:.2f}°C e {k:.2f}K\n")
        else:
            print("Opção inválida!")

    elif unidade == "K":
        c = valor - 273.15
        f = (valor - 273.15) * 9/5 + 32
        if opcao == "1":
            print(f"\n{valor}K = {c:.2f}°C\n")
        elif opcao == "2":
            print(f"\n{valor}K = {f:.2f}°F\n")
        elif opcao == "3":
            print(f"\n{valor}K = {c:.2f}°C e {f:.2f}°F\n")
        else:
            print("Opção inválida!")
            
# Inicia o programa
menu()