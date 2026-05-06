import random
import os

novo_jogo = 'sim'
while novo_jogo == 'sim':

    user_points = 0 
    computer_points = 0

    options = ["r","t","p"]

    while True:
        user_choice = input("\nEscolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair: ").lower()

        if user_choice == 'q':
            break

        computer_choice = random.randint(0, 2)

        computer_option = options[computer_choice]

        print("O computador escolheu: " + computer_option)

        if user_choice == computer_option:
            print("Empate!")
        elif user_choice == "r" and computer_option == "t":
            print("Você Ganhou!")
            user_points = user_points + 1

        elif user_choice == "p" and computer_option == "r":
            print("Você Ganhou!")
            user_points = user_points + 1

        elif user_choice == "t" and computer_option == "p":
            print("Você Ganhou!")
            user_points = user_points + 1

        else:
            print("Você Perdeu!")
            computer_points = computer_points + 1

    print("\nSua pontução foi: " + str(user_points))
    print("Pontuação do computador foi: " + str(computer_points))

    if computer_points > user_points:
        print('\nComputador Ganhouu!!')
    elif computer_points == user_points:
        print("\nVocês Empataram o jogo")
    else:
        print("\nVocê Ganhouu!!")

    novo_jogo = input("\nVocê deseja jogar novamente (sim/não)?: ").lower()
    novo_jogo = novo_jogo
    os.system("cls")
