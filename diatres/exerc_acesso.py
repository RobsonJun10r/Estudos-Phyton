senha_input = "abcd1234"
senha_corect = "abcd1234"
user_block = True

acesso_concedido = (senha_input == senha_corect) and not user_block
print('Usuário pode acessar?', acesso_concedido)