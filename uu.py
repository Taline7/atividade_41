# Validação de Login com While
# Permite que o usuário tente fazer login até digitar a senha correta ("1234").
# Mostra uma mensagem de erro a cada tentativa incorreta.

# Validação de Login com While
senha_correta = 1234
senha = int(input("Digite a senha: "))

while senha != senha_correta:
    print("ERRO. Tente novamente.")
    senha = int(input("Digite a senha: "))

print("Acesso permitido.")