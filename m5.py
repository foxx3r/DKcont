import wikipedia
wikipedia.set_lang('pt')

times_for_game = int(input('Voce que fazer quantas pesquisas: '))
for a in range(1,times_for_game +1):
	print('\033[1;32m#\033[m'*45)
			
	busca = input('Faca sua pesquisa: ')
	print('\033[1;34m#'*16,'PESQUISANDO','#'*16)
	print(wikipedia.summary(busca, sentences=15))




