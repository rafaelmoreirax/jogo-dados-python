
3. Siga as instruções no terminal para lançar os dados ou sair do jogo.

---

## 🛠️ Tecnologias

- Python 3 (biblioteca padrão)

---

## 📋 Funcionalidades

- Simula o lançamento de dois dados de 6 faces.
- Mostra o valor de cada dado e a soma.
- Permite jogar repetidamente até o usuário decidir sair.
- Interface simples e amigável no terminal.

---
```
## jogo_dados.py

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
```


---

## 📋 Exemplo de uso

```
=== Jogo de Dados Virtual ===
Digite 'l' para lançar os dados ou 's' para sair: l
Você lançou: 3 e 5 (Soma: 8)

Digite 'l' para lançar os dados ou 's' para sair: l
Você lançou: 6 e 1 (Soma: 7)

Digite 'l' para lançar os dados ou 's' para sair: s
Obrigado por jogar! Até a próxima.
```


---

## 🏷️ Tags

`python` `jogo` `dados` `terminal` `simples` `iniciante` `diversão`

---

## 📜 Licença

MIT

---

## 🤝 Contribuição

Pull requests e issues são bem-vindos!

---

## 📞 Contato

Desenvolvido por [rafael moreira](https://github.com/rafaelmoreirax)

