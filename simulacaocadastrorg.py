# Criando sistema que simula como funcionaria o sistema de RG 
# Agr adaptar o sistema de maneira a ler o numero RG verificar e gerar um novo
# Possibilidade de criar um doc para cada cadastro ou ir enfileirando em um doc só
# criar funcao que le o maior numero no doc e soma mais um pra atribuir ao proximo, executar antes da funcao de atribuicao 

contador = 1
infinito = 2
rg = 1
registro_geral = "registrogeral.txt"

class registrogeral:
	def __init__ (self, rg, nome, idade, estadocivil, rua, numero, complemento):
		
		self.id = rg
		self.nome = nome
		self.idade = idade
		self.estadocivil = estadocivil 
		self.rua = rua
		self.numero = numero
		self.complemento = complemento


def salvardados():
	arquivo = open(registro_geral, 'a')
	text = list()
	text.append('\n RG: {}\n Nome: {}\n Idade: {}\n Estado Civil: {}\n Rua: {}\n Numero: {}\n Complemento: {}\n'.format(novoregistro.id, novoregistro.nome, novoregistro.idade, novoregistro.estadocivil, novoregistro.rua, novoregistro.numero, novoregistro.complemento))
	arquivo.writelines(text)
	arquivo.close()
        


while contador < infinito:
	nome = input('Digite seu nome: ')
	idade = input('Digite sua idade: ')
	estadocivil = input('Digite seu estado civil: ')
	rua = input('Digite o nome da sua rua: ')
	numero = input('Digite o numero da sua casa: ')
	complemento = input('Digite o se for necessario complemento: ')
	novoregistro = registrogeral(rg,nome, idade, estadocivil, rua, numero, complemento)
	salvardados()
	print('\n\nDeseja cadastrar outra pessoa? \n1 - Sim \n2 - Não')
	opcao = int(input())
	if opcao == 2:
		break
	else:
		contador += 1
		infinito += 1
		rg += 1
		
