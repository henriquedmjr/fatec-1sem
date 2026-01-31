from Aula12import import cadastrar_aluno, login_aluno, turma
print("Ola seja bem vindo!")

while True:
    esc = str(input('você é novo aqui ou ja tem algum cadastro? (n ou c) '))
    if esc == 'n':
        cadastrar_aluno()
    else:
        login_aluno()
    cont = str(input("deseja continuar? (s ou n) "))
    if cont == 'n':
        break  
    for i in range(len(turma)):
            print(turma[i])
