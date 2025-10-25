# Validação de Login com While
# Permita que o usuário tente fazer login até digitar a senha correta ("1234"). 
# Mostre uma mensagem de erro a cada tentativa incorreta.
senha_correta = 1234
senha = int(input("Digite a senha:"))
while senha != senha_correta:
    input("ERRO. Tente novamente: ")
    senha = int(input("Digite sua senha"))

print("Acesso permitido!")
    

