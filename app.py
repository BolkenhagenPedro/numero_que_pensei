from random import randint

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro válido.')
            continue
        except (KeyboardInterrupt):
            print('Usuário preferiu não digitar esse número.')
            return 0
        else:
            return n

def limpar_terminal():
    try:
        from os import system
        from platform import system as sys
        
        sistema_operacional = sys()
        
        if sistema_operacional == 'Windows': system('cls')
        elif sistema_operacional == 'Linux': system('clear')
        elif sistema_operacional == 'Darwin': system('clear')

    except:
        return False
    
input('Aperte enter para começar...')
while True:
    comp = randint(1,100)
    cont = 0
    print('Foi gerado um número entre 1 e 100...')
    jogador = leiaint('Chute um valor entre 1 e 100: ')
    cont += 1
    while jogador != comp:
        if jogador > comp:
            print('Chute um valor mais baixo...')
        else:
            print('Chute um valor mais alto...')
        cont += 1
        jogador = leiaint('Chute um valor entre 1 e 100: ')

    print(f'PARABÉNS! Você acertou o número que o computador pensou, que era: {comp}')
    print(f'Você acertou com {cont} tentativas')
    resp = input('Jogar novamente? (S/N) ').strip().upper()[0]
    while resp not in 'SN':
        print('Digite um resposta válida!')
        resp = input('Jogar novamente? (S/N) ').strip().upper()[0]
    if resp == 'N':
        limpar_terminal()
        break
    limpar_terminal()
