from art import *
from time import sleep
import math
print('''      \033[1;31mATENCAO ASSIM QUE VOCE ESCOLHE UMA OPCAO
          NAO PODE VOLTAR AO MENU INICIAL\033[m''')
catetoOposto = hipotenusa = adjacente = raizQ = raizC = result = capital = taxaJuros = juro = tempo = montante = sum1 = sum2 = sum3 = delta = X1 = X2 = baskara = option_int = times_for_game = 0
question = option = ' '

while True:
	print('='*45)
	tprint('''Matematica''', font="cybermedium")
	print('''\033[1;32m
	[1]ADIÇÃO
	[2]SUBTRAÇÃO
	[3]MULTIPLICAÇÃO
	[4]DIVISÃO	
	[5]PORCENTAGEM
	[6]RADICIAÇÃO
	[7]FATORIAL 
	[8]TRIGONOMETRIA BASICA
	[9]TEOREMA DE PITAGORAS
	[10]EQUACAO SEGUNDO GRAU\033[m
	\033[1;31m[S]SAIR DO JOGO \033[m''')
	print()
	print('='*45)
	option = str(input('>>>> Digite uma opção: ')).strip().upper()[0]
	if option in 'Ss':
		break
	if option == '1':#CONDICAO 1
		print('''
	\033[1;36m[1]SOMA COM VARIOS VALORES
	[2]SOMA COM 2 VALORES\033[m
	\033[1;31m[3]SAIR\033[m''')
		option_int = int(input('>>>> Escolha uma opcao: '))
		
		if option_int == 1:#SOMA VARIOS VALORES
			sum2 = int(input('>>>> Digite o um numero: '))								
			while question not in 'Nn':
				print()
				question = str(input('Quer continuar?[S/N]: '))
				print()
				if question in 'Ss':
					sum1 = int(input('>>>> Digite o um numero: '))
					result += sum1			
			print(f'A soma de todos os numeros é igual a  = {result+sum2}')			
	
		if option_int == 2:#SOMA COM 2 VALORES
			times_for_game = int(input('Determine um limite de jogo: '))
			for a in range(1,times_for_game +1):
				sum1 = int(input('\033[1;34m>>>>> Digite o primeiro numero: '))
				sum2 = int(input('>>>>> Digite o segundo numero: \033[m'))	
				print(f'\033[1;33m A soma de {sum1} + {sum2} = {sum1+sum2} \033[m')									
				question = str(input('Quer continuar?[S/N]: '))								
				if question in 'Nn':
					print('\033[1;31m VOLTANDO AO MENU..')
					sleep(2)
					break
					 
	if option == '2':#SUBTRAÇÃO
		times_for_game = int(input('>>>> Determine um limite de jogo: '))
		for a in range(1,times_for_game +1):
			sum1 = int(input('\033[1;36m>>>>> Digite o primeiro numero: '))
			sum2 = int(input('>>>>> Digite o segundo numero: \033[m'))
			print(f'\033[1;33mO numero {sum1} menos o numero {sum2} = {sum1-sum2} \033[m')		
			question = str(input('Quer continuar?[S/N]: '))								
			if question in 'Nn':
				print('\033[1;31m VOLTANDO AO MENU...\033[m')
				sleep(2)
				break
						
	if option == '3':#MULTIPLICACAO
		times_for_game = int(input('>>>> Determine um limite de jogo: '))
		for a in range(1,times_for_game +1):	
			sum1 = int(input('\033[1;36m>>>>> Digite o primeiro numero: '))
			sum2 = int(input('>>>>> Digite o segundo numero: \033[m'))
			print(f'\033[1;33mO numero {sum1} multiplicado por {sum2} = {sum1*sum2} \033[m')
			question = str(input('Quer continuar?[S/N]: '))
			if question in 'Nn':
				print('\033[1;31m VOLTANDO AO MENU...\033[m')
				sleep(2)
				break											
	
	if option == '4':#DIVISÃO
		times_for_game = int(input('>>>> Determine um limite de jogo: '))
		for a in range(1,times_for_game +1):			
			sum1 = int(input('\033[1;33m>>>>> Digite o primeiro numero: '))
			sum2 = int(input('>>>>> Digite o segundo numero: \033[m'))
			print(f'\033[1;35mO numero {sum1} dividido por {sum2} = {sum1/sum2} \033[m')			
			question = str(input('Quer continuar?[S/N]: '))
			if question in 'Nn':
				print('\033[1;31m VOLTANDO AO MENU...\033[m')
				sleep(2)
				break							 								
		
	if option == '5':#PORCENTAGEM
		times_for_game = int(input('Determine um limite de jogo: '))
		for c in range(1,times_for_game +1):
			print('<>'*23)
			print('''		
	\033[1;34m[1]PORCENTAGEM DE UM VALOR
	[2]JUROS SIMPLES
	[3]JUROS COMPOSTO
	[4]DESCONTO DE CAPITAL
	[5]ACRESCIMO DE CAPITAL\033[m
	\033[1;31m[6]SAIR \033[m''')
			print('<>'*23)				
			option_int = int(input('>>>>> Escolha uma opcao: '))
			if option_int == 1:
				sum1 = float(input('\033[1;33m>>>>> Digite o valor em porcentagem: '))
				sum2 = int(input('>>>>> Digite o valor para retirar sua porcentagem: \033[m'))
				result = sum1 *(sum2/100)
				print(f'\033[1;35m{sum1}% porcentos de R${sum2:.2f} reais equivale a R${result:.2f} reais\033[m')
			if option_int == 2:
				capital = int(input('>>>> Digite o valor do capital: '))
				taxaJuros = float(input('>>>> Digite o valor do juros aplicado ao capital: '))
				tempo = int(input('>>>> Digite o periodo o qual o juros foi posto: '))
				result = taxaJuros *(capital/100)
				juro = result * tempo
				montante = capital + juro
				print('<>'*23)
				print(f'''\033[1;36m
O montante no final deste periodo para quitar a fatura 
sera de R${montante:.2f} reais
sendo R${capital:.2f} reias de emprestimo e 
{juro:.2f} reais do juros de {taxaJuros}% de taxa de juros aplicado!\033[m''')
			if option_int == 3:
				capital = int(input('>>>> Digite o valor do capital: '))
				taxaJuros = float(input('>>>> Digite o valor da taxa de juros: '))
				tempo = int(input('>>>> Digite o tempo que o capital foi aplicado: '))
				montante = capital *(1 + (taxaJuros/100))**tempo
				print('<>'*23)
				print(f'\033[1;32mPortanto,o valor obtido no fim do tempo sera de R${montante:.2f} reais sendo R${montante - capital:.2f} reiais de juros de uma taxa de {taxaJuros/100}% \033[m')
			if option_int == 4:
				capital = int(input('Digite o valor do capital inicial: '))
				taxaJuros = float(input('Digite a taxa de desconto aplicada ao capital: '))
				montante = capital*(taxaJuros/100)
				print('<>'*23)
				print(f'\033[1;32mPortanto, o valor apos o desconto sera de R${capital-montante:.2f} reias sendo R${montante:.2f} reais conrrespondente a taxa de {taxaJuros}% \033[m')
			if option_int == 5:
				capital = int(input('Digite o valor do capital inicial: '))
				taxaJuros = float(input('Digite a taxa de desconto aplicada ao capital: '))
				montante = capital*(taxaJuros/100)
				print('<>'*23)
				print(f'\033[1;32mPortanto, o valor apos o acrescimo sera de R${capital+montante:.2f} reias sendo R${montante:.2f} reais conrrespondente a taxa de {taxaJuros}% \033[m')			
			if option_int == 6:
				print('\033[1;31m VOLTANDO AO MENU...\033[m')
				sleep(2)
				break		
	if option == '6':#RADICIACAO
		times_for_game = int(input('Determine um limite de jogo: '))
		for c in range(1,times_for_game +1):
			print('='*45)
			print('''
	\033[1;36m[1]RAIZ QUADRADA
	[2]RAIZ CUBICA
	[3]OUTRAS RAIZES \033[m
	\033[1;31m[4]SAIR \033[m''')
			print('='*45)
			option_int = int(input('>>>> Escolha uma opcao: '))
			if option_int == 1:
				sum1 = int(input('Qual numero voce deseja saber sua raiz?: '))
				raizQ = sum1 **(1/2)
				print('='*45)
				print(f'\033[1;35mA raiz quadrada de {sum1} e {raizQ:.1f}\033[m')
			
			if option_int == 2:
				sum1 = int(input('Qual numero voce deseja saber sua raiz?: '))
				raizC = sum1 **(1/3)
				print('='*45)
				print(f'\033[1;35mA raiz cubica de {sum1} e {raizC:.1f}\033[m')
			
			if option_int == 3:
				sum1 = int(input('Qual o numero que voce deseja saber sua raiz: '))				
				sum2 = int(input('Informe qual indice voce quer: '))
				raizQ = sum1 **(1/sum2)
				print('='*45)
				print(f'\033[1;35mA raiz de {sum1} com indice {sum2} e {raizQ:.1f}\033[m')
			if option_int == 6:
				print('\033[1;31m VOLTANDO AO MENU...\033[m')
				sleep(2)
				break
				
	if option == '7':#FATORIAL
		times_for_game = int(input('Determine um limite de jogo: '))
		for c in range(1,times_for_game +1):
			print('='*45)
			sum1 = int(input('\033[1;35mDigite um numero: \033[m'))
			print('='*45)
			sum2 = sum1 + 1
			result = 1
			print(f'\033[1;34mCalculando Fatorial de !{sum1} =\033[m',end=' ')
			while sum2 > 0:		
				sum2 -= 1		
				if sum2 != 0:
					print(f'{sum2}',end=' ')
					print(f'x ' if result > 1 else 'x ',end='')
					result *= sum2
			print(result)

	if option == '8':#TRIGONOMETRIA
		times_for_game = int(input('Determine um limite de jogo: '))
		for c in range(1,times_for_game +1):		
			print('''
	\033[1;33m[1]SENO
	[2]COSSENO
	[3]TANGENTE \033[m
	\033[1;31m[4]SAIR\033[m''')
			option_int = int(input('>>>> Escolha uma opcao: '))
			if option_int == 1:
				catetoOposto = float(input('Digite o valor do cateto oposto: '))
				hipotenusa = float(input('Digite o valor da hipotenusa: '))
				result = catetoOposto / hipotenusa
				if result > 1:
					print('~'*40)
					print(f'>>>> O valor do seno e de {result}')
					print('~'*40)
				elif result < 1:
					print('~'*40)
					print(f'>>>> O valor do seno e de {result:.3f}')
					print('~'*40)
			if option_int == 2:
				adjacente = float(input('Digite o valor do cateto adjacente: '))
				hipotenusa = float(input('Digite o valod da hipotenusa: '))
				result = adjacente / hipotenusa
				if result > 1:
					print('~'*40)
					print(f'>>>> O valor do cosseno e de {result}')
					print('~'*40)
				elif result < 1:
					print('~'*40)
					print(f'>>>> O valor do cosseno e de {result:.3f}')
					print('~'*40)
			if option_int == 3:
				catetoOposto = float(input('Digite o valor do cateto oposto: '))
				adjacente = float(input('Digite o valor do cateto adjacente: '))
				result = catetoOposto / adjacente 
				if result > 1:
					print('~'*40)
					print(f'>>>> O valor da tangente e de {result}')
					print('~'*40)
				elif result < 1:
					print('~'*40)
					print(f'>>>> O valor da tangente e de {result:.3f}')
					print('~'*40)
	
	if option == '9':
		times_for_game = int(input('Determine um limite de jogo: '))
		for c in range(1,times_for_game +1):
			print('#'*45)	
			sum1 = int(input('\033[1;33m Digite o valor do primeiro cateto: '))
			sum2 = int(input('Digits o valor do segundo cateto: \033[m'))
			hipotenusa = (sum1**2) + (sum2 **2) 
			print('#'*45)	
			print(f'\033[1;35m>>>>O valor da hipotenusa e igual a {math.sqrt(hipotenusa)}\033[m')
				
	if option == '10':#EQUACAO 
		times_for_game = int(input('Determine um limite de jogo: '))
		for c in range(1,times_for_game +1):				
				sum1 = int(input('Digite o valor de Ax: '))
				sum2 = int(input('Digite o valor de Bx: '))
				sum3 = int(input('Digite o valor de C: '))				
				delta = (sum2**2)-4*sum1*sum3			
				X1 = (sum2 + (delta**(1/2))) / (2*sum1) 
				X2 = (sum2 - (delta**(1/2))) / (2*sum1) 			
				print('='*45)
				print(f'\033[1;32mO Resultado do X1 e: {X1:.3f}')
				print(f'O Resultado do X2 e: {X2:.3f}\033[m')
	if option in 'Ss':
		break				
											
		










