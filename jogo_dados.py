import random

def lancar_dado():
return random.randint(1, 6)

def jogar():
print("=== Jogo de Dados Virtual ===")
while True:
comando = input("Digite 'l' para lançar os dados ou 's' para sair: ").lower()
if comando == 's':
print("Obrigado por jogar! Até a próxima.")
break
elif comando == 'l':
dado1 = lancar_dado()
dado2 = lancar_dado()
soma = dado1 + dado2
print(f"Você lançou: {dado1} e {dado2} (Soma: {soma})\n")
else:
print("Comando inválido. Use 'l' para lançar ou 's' para sair.\n")

if name == "main":
jogar()
