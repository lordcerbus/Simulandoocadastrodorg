# Implementar programa de busca de dados pelo numero do RG

def gerarrg(): # Função que localiza o rg mais recente e gera o proximo
	doc = open(registro_geral, 'r')
	maior_numero = 0
	for linha in doc:
		if "RG:" in linha:
			  numeroo = int(linha.split("RG: ")[1].strip())
			  if numeroo > maior_numero:
			  	 maior_numero = numeroo
	rg = maior_numero + 1
	doc.close()
	return rg

		
class registrogeral: # Classe que recebe as variaveis e cria o cadastro
	def __init__ (self, rg, nome, idade, estadocivil, rua, numero, complemento):
		
		self.id = rg2
		self.nome = nome
		self.idade = idade
		self.estadocivil = estadocivil 
		self.rua = rua
		self.numero = numero
		self.complemento = complemento

def salvardados():# Função que recebe as variaveis e as aplica ao documento
	arquivo = open(registro_geral, 'a')
	text = list()
	text.append('\n RG: {} \n Nome: {} \n Idade: {} anos \n Estado Civil: {} \n Rua: {} \n Numero: {} \n Complemento: {} \n'.format(novoregistro.id, novoregistro.nome, novoregistro.idade, novoregistro.estadocivil, novoregistro.rua, novoregistro.numero, novoregistro.complemento))
	arquivo.writelines(text)
	arquivo.close()
        
def encontrar_linha_com_rg(arquivo, numero_rg):# Funcão de pesquisa do rg
    try:
        with open(arquivo, 'r') as arquivo_texto: # Abre o arquivo no modo leitura
            linhas = arquivo_texto.readlines() # Captura o numero de linhas

            for numero_linha, linha in enumerate(linhas):
                if 'RG:' in linha and numero_rg in linha:# Pesquisa e retorna a linha do rg requerido
                    print(f'{linha.strip()}')
                    for i in range(numero_linha + 1, min(numero_linha + 7, len(linhas))):# Imprime as outras linhas refrentes ao rg
                        print(f'{linhas[i].strip()}')
                    break
            else: # Caso o numero de rg n exista
                print(f"Não foi encontrada nenhuma linha com 'RG:' e o número '{numero_rg}'.")

    except FileNotFoundError: # Caso o documento não exista
        print(f"O arquivo '{arquivo}' não foi encontrado.")
        
def apagar_linhas_com_rg(arquivo, numero_rg):
    try:
        with open(arquivo, 'r') as arquivo_texto:
            linhas = arquivo_texto.readlines()

            for numero_linha, linha in enumerate(linhas):
                if 'RG:' in linha and numero_rg in linha:
                    # Encontrou a linha com 'RG:' e o número especificado
                    del linhas[numero_linha:numero_linha + 8]
                    break
            else:
                print(f"Não foi encontrada nenhuma linha com 'RG:' e o número '{numero_rg}'.")

        # Reescreve o arquivo com as linhas atualizadas
        with open(arquivo, 'w') as arquivo_atualizado:
            arquivo_atualizado.writelines(linhas)

    except FileNotFoundError:
        print(f"O arquivo '{arquivo}' não foi encontrado.")
              
escolha = input("O que gostaria de fazer?\n 1 - Cadastrar novo RG \n 2 - Pesquisar RG \n 3 - Deletar RG \n 4 - Fechar Programa ")

contador = 1
infinito = 2

while contador < infinito:
	if escolha == "2":
		nome_arquivo = "registrogeral.txt"
		numero_rg_procurado = input("Digite o número de RG que deseja buscar: ")
		numero_rg_procurado_tratado = numero_rg_procurado.zfill(8)
		encontrar_linha_com_rg(nome_arquivo, numero_rg_procurado_tratado)
		escolha = input("O que gostaria de fazer?\n 1 - Cadastrar novo RG \n 2 - Pesquisar RG \n 3 - Deletar RG \n 4 - Fechar Programa ")
	elif escolha == "1":
		rg = 0
		registro_geral = "registrogeral.txt"
		open(registro_geral, "a")
		nome = input('Digite seu nome: ')
		idade = input('Digite sua idade: ')
		estadocivil = input('Digite seu estado civil: ')
		rua = input('Digite o nome da sua rua: ')
		numero = input('Digite o numero da sua casa: ')
		complemento = input('Digite o se for necessario complemento: ')
		rg = gerarrg()
		rg1 = str(rg)
		rg2 = rg1.zfill(8)
		novoregistro = registrogeral(rg2,nome, idade, estadocivil, rua, numero, complemento)
		salvardados()
		print('\n\nDeseja cadastrar outra pessoa? \n1 - Sim \n2 - Não')
		opcao = int(input())
		if opcao == 2:
	 		escolha = input("O que gostaria de fazer?\n 1 - Cadastrar novo RG \n 2 - Pesquisar RG \n 3 - Deletar RG \n 4 - Fechar Programa ")
		else:
			contador += 1
			infinito += 1
	elif escolha == "3":
		nome_arquivo = "registrogeral.txt"
		numero_rg_procurado = input("Digite o número de RG que deseja buscar: ")
		apagar_linhas_com_rg(nome_arquivo, numero_rg_procurado)
		escolha = input("O que gostaria de fazer?\n 1 - Cadastrar novo RG \n 2 - Pesquisar RG \n 3 - Deletar RG \n 4 - Fechar Programa ")
	else: 
		print("Programa Finalizado")
		contador = infinito