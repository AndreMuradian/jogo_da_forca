# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.letras_certas = []
		self.letras_erradas = []

	# Método para adivinhar a letra
	def guess(self, letras):
		if letras in self.word and letras not in self.letras_certas:
			self.letras_certas.append(letras)
		elif letras not in self.word and letras not in self.letras_erradas:
			self.letras_erradas.append(letras)
		else:
			return False
		return True


	# Método para verificar se o jogo terminou
	def hangman_over(self):
		return self.hangman_won() or (len(self.letras_erradas) == 6)
		
	# Método para verificar se o jogador venceu
	def hangman_won(self):
		if "_" not in self.hide_word():
			return True
		return False

	# Método para não mostrar a letra no board
	def hide_word(self):
		rtn = ""
		for letras in self.word:
			if letras not in self.letras_certas:
				rtn += "_"
			else:
				rtn += letras
		return rtn
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(board[len(self.letras_erradas)])
		print("Palavra: " + self.hide_word())
		print("Letras erradas: ")
		for letras in self.letras_erradas:
			print(letras)
		print()
		print("Letras corretas: ")
		for letras in self.letras_certas:
			print(letras)
		print()

# Função para ler uma palavra de forma aleatória do banco de palavras, esta pronta
def rand_word():
    with open("palavras.txt", "rt") as f:
            bank = f.readlines()
    return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while not game.hangman_over():
		game.print_game_status()
		letra = input("Digite uma letra: ")
		game.guess(letra)

	# Verifica o status do jogo
	game.print_game_status()	

	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()

