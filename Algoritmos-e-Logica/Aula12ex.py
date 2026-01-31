class Cadastro:
    def __str__(self):
        return f"{self.nome} ({self.matricula})[{self.senha}]"
    def __init__(self, a, b, c):
        self.nome = str(a)
        self.matricula = int(b)
        self.senha = str(c)
        
    
print("Ola seja bem vindo!")
turma = []
while True:
    esc = str(input('você é novo aqui ou ja tem algum cadastro? (n ou c) '))
    if esc == 'n':
        while True:
            n = input("digite o seu nome: " )
            m = int(input("digite sua matricula: "))
            matricula_existe = False            
            for aluno_existente in turma:
                if aluno_existente.matricula == m:
                    matricula_existe = True
                    break
            if matricula_existe:
                print("Matrícula já existente!")
            else:
                while True:    
                    sn = str(input("digite a sua senha: "))
                    sn2 = str(input("digite a sua senha denovo: "))
                    if sn == sn2:
                        print("Senhas conferem! ")
                        break
                    else:
                        print("Senhas não conferem! tente novamente. ")
                aluno_novo = Cadastro(n, m, sn)
                turma.append(aluno_novo)
                print("cadastro concluido!")
                print(f"sua matricula é {aluno_novo.matricula} ")
                break
    else:
            m2 = int(input("digite sua matricula: "))
            aluno_logado = None
            matricula_existe = True
            for aluno_existente in turma:
                if aluno_existente.matricula == m2:
                    aluno_logado = aluno_existente
                    print("Matricula identificada! ")
                    break
            if aluno_logado is None:
                print("Matrícula não encontrada!")
                matricula_existe = False
            else:
                print(f"Ola {aluno_logado.nome}, seja bem vindo de volta! ")
                while True:
                    sn3 = str(input("digite a sua senha: "))
                    if sn3 == aluno_logado.senha:
                        print("senha correta! ")
                        print("login concluido! ")
                        break      
                    else:
                        print("senha incorreta! ")
                        break
    cont = str(input("deseja continuar? (s ou n) "))
    if cont == 'n':
        break   

    for i in range(len(turma)):
        print(turma[i])