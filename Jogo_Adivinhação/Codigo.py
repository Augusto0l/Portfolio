import random
import os

new_game = "sim" 

while new_game == "sim":

    print("Seja muito Bem-vindo ao Guess number do Pedro!")
    choice_number = input("Digite o numero teto do desafio: ")

    if choice_number.isdigit():
        choice_number = int(choice_number)
    else:
        print("ERRO: O valor informado não é numérico. Favor execute novamente e informe um número!")
        quit()

    random_number = random.randint(0, choice_number)

    attempts = 0

    while True:
        answer_user = input("Adivinhe o número: ")
        if answer_user.isdigit():
            answer_user = int(answer_user)
        else:
            print("ERRO: O valor informado não é numérico. Favor execute novamente e informe um número!")
            continue

        attempts = attempts + 1
        if answer_user == random_number:
            print("Acertou!!")
            break
        elif answer_user > random_number:
            print("Chutou alto, o número randomico é menor que isso...")
        else:
            print("Chutou baixo, o número randomico é maior que isso...")
    print("Número de tentivas: "+ str(attempts))     

    new_game = input("\nDeseja jogar novamente (sim/não)?: ")   
    new_game = new_game
    os.system("cls")
