import random

jogo = input(" Você quer adivinhar o número do computador(opção1), ou quer que o computador adivinhe o seu número(opção 2)? Escolha entre as opções 1 e 2. ")

if jogo == "1":
    print("Ok, vamos começar, boa sorte para adivinhar o número do computador.")
    min = "1"
    max = input(" A escolha do computador será de 1 até o número máximo que você escolher. Defina esse valor máximo agora. ")
    print(f"Ok, você fixou o range entre 1 e {max}, e o computador já escolheu." )
    num_cpu = random.randint(int(min), int(max))
    print(num_cpu)
    chute = 0
    tentativas = 0
    novomin=1
    novomax=int(max)
    while chute != num_cpu:
        tentativas += 1
        chute = int(input(f'Adivinhe agora, lembre que o número está entre {novomin} e {novomax}, boa sorte.' ))
        if chute >= novomax or chute <= novomin:
            print("Preste atenção nos números" )
        elif chute < num_cpu:
            print('Tente novamente um número mais alto, Seu chute foi muito baixo.')
            novomin = int(chute)
        elif chute > num_cpu:
            print('Tente novamente um número mais baixo, Seu chute foi muito alto.')
            novomax = int(chute)

    print(f'Parabéns, você acertou em {tentativas} tentativas, o número {num_cpu}!! ')

elif jogo == "2":
    print("Ok, vamos começar, boa sorte!.")
    min = "1"
    max = input(" Defina agora o valor máximo para fazer o range entre 1 e esse valor. ")
    print(f"Ok, você fixou o range entre 1 e {max}. " )
    meunum = input(" Agora escolha o seu número e boa sorte. ")
    print(f"O seu número é {meunum}. ")
    low = 1
    high = max
    feedback = ''
    tentativas = 0
    while feedback != 'c':
        tentativas += 1
        if low != high:
            guess = random.randint(int(low), int(high))
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Seu número é {guess}?  Responda (H) se o {guess} é muito alto, responda (L) se o {guess} for muito baixo, ou responda (C) se estiver correto?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'O computador acetou seu número {meunum}, em {tentativas} tentativas !')
    

else:
    print("Da próxima vez escolha um número entre as opções disponíveis")


    