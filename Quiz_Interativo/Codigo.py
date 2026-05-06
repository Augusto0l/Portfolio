import os

New_Game = "sim"
while New_Game == "sim":
    score = 0
    print("\nBem-vindo ao Quiz de Conhecimentos Gerais\n")
    print("Começando...\n")
    print("1- Qual é a capital do Brasil?\n(A) São Paulo\n(B) Rio De Janeiro\n(C) Brasília\n(D) Minas Gerais\n(E) Bahia")
    answer_1 = input("Resposta: ").strip().upper()
    if answer_1 == "C":
        print("\nAcertou!!\n")
        score = score + 1
    else:
        print("\nErrou, Resposta Correta (C)\n")
    
    print("2- Qual é o nome do oceano que banha a costa oeste da América do Sul?\n(A) Pacífico\n(B) Atlântico\n(C) Índico\n(D) Ártico\n(E) Antártico")
    answer_2 = input("Resposta: ").strip().upper()
    if answer_2 == "A":
        print("\nAcertou!!\n")
        score = score + 1
    else:
        print("\nErrou!, Resposta Correta (A)\n")

    print("3- Qual é o nome da moeda oficial do Japão?\n(A) Real\n(B) Iene\n(C) Euro\n(D) Libra")
    answer_3 = input("Resposta: ").strip().upper()
    if answer_3 == "B":
        print("\nAcertou!!\n")
        score = score + 1
    else:
        print("\nErrou, Resposta Correta (C)\n")
    
    print("4- Qual é o nome do famoso museu de arte em Paris?\n(A) Museu do Vaticano\n(B) Museu Metropolitano de Arte\n(C) Museu Britânico\n(D) Museu Do Louvre")
    answer_4 = input("resposta: ").strip().upper()
    if answer_4 == "D":
        print("\nAcertou!!\n")
        score = score + 1
    else:
        print("\nErrou!, Resposta Correta (D)\n")

    print("5- Qual é o nome do famoso time de futebol inglês conhecido como The Gunners?\n(A) Arsenal\n(B) Manchester United\n(C) Chelsea\n(D) Liverpool")
    answer_5 = input("resposta: ").strip().upper()
    if answer_5 == "A":
        print("\nAcertou!!\n")
        score = score + 1
    else:
        print("\nErrou!, Resposta Correta (A)\n")

    print("6- Qual é o nome do famoso festival de música que acontece em Woodstock, nos Estados Unidos?\n(A) Coachella\n(B) Glastonbury\n(C) Lollapalooza\n(D) Woodstock ")
    answer_6 = input("resposta: ").strip().upper()
    if answer_6 == "D":
        print("\nAcertou!!\n")
        score = score + 1
    else:
        print("\nErrou!, Resposta Correta (D)\n")

    print("7- Qual é o nome do famoso escritor brasileiro autor de Dom Casmurro?\n(A) Jorge Amado\n(B) Machado de Assis\n(C) Carlos Drummond de Andrade\n(D) José de Alencar")
    answer_7 = input("resposta: ").strip().upper()
    if answer_7 == "B":
        print("\nAcertou!!\n")
        score = score + 1
    else:
        print("\nErrou!, Resposta Correta (B)\n")

    print("8- Qual é o nome do famoso personagem de desenho animado criado por Walt Disney?\n(A) Pato Donald\n(B) Mickey Mouse\n(C) Pernalonga\n(D) Bob Esponja")
    answer_8 = input("resposta: ").strip().upper()
    if answer_8 == "B":
        print("\nAcertou!!\n")
        score = score + 1
    else:
        print("\nErrou!, Resposta Correta (B)\n")

    print("9- Qual é o nome do famoso pintor espanhol autor de Guernica?\n(A) Salvador Dalí\n(B) Pablo Picasso\n(C) Diego Rivera\n(D) Joan Miró")
    answer_9 = input("resposta: ").strip().upper()
    if answer_9 == "B":
        print("\nAcertou!!\n")
        score = score + 1
    else:
        print("\nErrou!, Resposta Correta (B)\n")

    print("10- Qual é o nome da famosa ponte em São Francisco, nos Estados Unidos?\n(A) Brooklyn Bridge\n(B) Tower Bridge\n(C) Golden Gate Bridge\n(D) Sydney Harbour Bridge")
    answer_10 = input("resposta: ").strip().upper()
    if answer_10 == "C":
        print("\nAcertou!!\n")
        score = score + 1
    else:
        print("\nErrou!, Resposta Correta (C)\n")

    print("Quiz Finalizado!")
    print(f"Sua Pontuação foi de: {score}/10")

    New_Game = input("\nDeseja fazer o quiz novamente (sim/não)?: ")
    New_Game = New_Game

    os.system('cls')

    
    
    


    

