from art import *
print('''      \033[1;31mATENCAO ASSIM QUE VOCE ESCOLHE UMA OPCAO
          NAO PODE VOLTAR AO MENU INICIAL\033[m''')

#VARIAVEIS:
aceleracao = tempo = velocidade = distancia = result = times_for_game = 0
option = ' '
while option not in 'Ss':
	print('='*45)
	tprint('''    FISICA''', font="cybermedium")
	print('''\033[1;32m
	[1]CALCULO DE VELOCIDADE
	[2]CALCULO DE DISTANCIA PECORRIDA
	[3]CALCULAR O TEMPO
	[4]CALCULAR ACELERACAO\033[m
	\033[1;31m[S]SAIR DO JOGO \033[m''')
	print('='*45)
	option = str(input('>>>> Digite uma opção: ')).strip().upper()[0]
	if option == '1':#VELOCIDADE
		times_for_game = int(input('Determine um limite de jogo: '))
		for a in range(1,times_for_game +1):
			print('#'*45)
			tempo = float(input('Digite o intervalo de tempo pecorrido: '))
			distancia = float(input('Digite a distancia pecorrida: '))
			velocidade = distancia / tempo
			option = str(input('Metros ou quilometros?[M/K]: ')).strip().upper()[0]
			print('#'*45)
			if option in 'Mm':
				print(f'\033[1;33m>>>>A velocidade percorrida foi de {velocidade} m\033[m')
			else:
				if option in 'Kk':
					print(f'\033[1;33m>>>>A velocidade percorrida foi de {velocidade} Km/h\033[m')
						
	if option == '2':#DISTANCIA
		times_for_game = int(input('Determine um limite de jogo: '))
		for a in range(1,times_for_game +1):
			print('='*45)
			tempo = float(input('Digite o intervalo de tempo pecorrido: '))
			velocidade = float(input('Digite a velocidade pecorrida: '))
			distancia = velocidade * tempo
			option = str(input('Metros ou quilometros?[M/K]: ')).strip().upper()[0]
			print('='*45)
			if option in 'Mm':
				print(f'\033[1;32m>>>>A distancia percorrida foi de {distancia} M/s\033[m')
			else:
				if option in 'Kk':
					print(f'\033[1;32m>>>>A distancia percorrida foi de {distancia} Km/h\033[m')
	
		
	if option == '3':#TEMPO
		times_for_game = int(input('Determine um limite de jogo: '))
		for a in range(1,times_for_game +1):
			print('#'*45)
			velocidade = float(input('Digite a velocidade pecorrida: '))
			distancia = float(input('Digite a distancia pecorrida: '))
			tempo = distancia / velocidade
			print('#'*45)
			print(f'\033[1;34m>>>>O tempo gasto foi de {tempo} S \033[m')

	if option == '4':#ACELERACAO
		times_for_game = int(input('Determine um limite de jogo: '))
		for a in range(1,times_for_game +2):
			print('#'*45)
			print('''
	\033[1;36m[1]APENAS ACELERACAO
	[2]VELOCIDADE POR TEMPO
	[3]TEMPO POR ACELERACAO\033[m''')
			print('#'*45)
			option = str(input('>>>> Digite uma opção: '))
			if option == '1':
				print('#'*45)
				tempo = float(input('Digite o tempo final apos sua aceleracao: '))
				velocidade = float(input('Digite a velocidade atingida em sua aceleracao: '))
				aceleracao = velocidade / tempo
				print('#'*45)
				print(f'\033[1;35m>>>>Portanto a cada segundo a velocidade aumenta {aceleracao} M/s° \033[m')
			if option == '2':
				print('#'*45)
				aceleracao = float(input('Qual foi a  taxa de aceleracao?: '))
				tempo = float(input('Digite o tempo final apos sua aceleracao: '))
				velocidade = aceleracao * tempo
				print('#'*45)
				print(f'\033[1;32m>>>>Portanto apos {tempo} segundos a velocidade e de  {velocidade} M/s \033[m')
			if option == '3':
				print('#'*45)
				aceleracao = float(input('Qual foi a taxa de aceleracao?: '))
				velocidade = float(input('Qual a taxa de velocidade?: '))
				tempo = velocidade / aceleracao
				print('#'*45)
				print(f'\033[1;33m>>>>A velocidade de {velocidade} Km/h foi alcancada em {tempo} S \033[m')
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
				
