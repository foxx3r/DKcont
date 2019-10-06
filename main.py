# -*- coding: utf-8 -*-
from art import tprint

print('×' * 50)
tprint('D4RK')

print('\033[1;32m[*]Criador: D4RK SYST3M\n\
[*]Canal Do Youtube: https://www.youtube.com/channel/UCUKyY5rDaAGKdNKAd8XXbwQ\n\
\n\
[*]Grupo Do Telegran: https://t.me/joinchat/KpcuPFRwrDINubprpTATAA\n\
\n\
[*]Finalidade: Resolver calculos e problemas matematicos\n\
\n\
[*]Versão: 1.0 Criada em 18/09/2019\n\
\033[m')

print('×' * 50)
print(f'{"▬" * 15} \033[1;34m MATEMATICA\033[m {"▬" * 13}')
print(f'{"<" * 8} \033[1;32mESCOLHA UMA QUANTIDADE DE FICHAS\033[m {">" * 7}')

try:
    quantidade_fichas = int(input('Digite quantas fichas voce quer: '))
except ValueError:
    print("Digite apenas inteiros!!!")
    exit()
except KeyboardInterrupt:
    exit()

print(f'{"<" * 13} \033[1;32mESCOLHA UMA OPÇÃO\033[m{"<" * 13}')

for x in range(1, quantidade_fichas + 1):
    print('''
	\033[1;32m[1] MATEMATICA\033[m
	\033[1;33m[2] FISICA\033[m
	\033[1;36m[3] FAZER PESQUISA NO WIKIPEDIA
	\033[1;34m[4] PARA CONTINUAR\033[m
	\033[1;35m[5] REGRAS E INFORMACOES DO JOGO
	\033[1;31m[6] PARA SAIR\033[m''')

    try:
        opcao = int(input('\033[1;33mDigite a Opção Desejada: \033[m'))
    except ValueError:
        print('Digite um inteiro apenas!')
        exit()
    except KeyboardInterrupt:
        exit()

    if opcao == 1:
        import m1
    elif opcao == 2:
        import m2
    elif opcao == 3:
        import m5
    elif opcao == 5:
        import m4
    elif opcao == 6:
        break
    elif opcao < 1 or opcao > 6:
        print("Opcao invalida!")
