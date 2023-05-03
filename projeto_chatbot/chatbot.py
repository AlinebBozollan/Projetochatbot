def area_do_aluno():
    print("Bem-vindo à Área do Aluno.  Digite o número referente a sua opcao abaixo")
    resposta = input("\n1. Meu Curso\n2. Dicas e utilidades \n3. Comunicados\n4. Voltar\n")
    
    try:
            int(resposta)  # tenta converter a resposta para um número inteiro
    except ValueError:  # se a conversão falhar, significa que o usuário não inseriu um número
            print("Desculpe, digite um número de 1 a 4. Por favor, tente novamente.")
            area_do_aluno()
            
    if resposta == "1":
            print("https://aluno.resilia.work/dashboard , seu atendimento sera automaticamente reiniciado, aperte 4 no menu principal se deseja sair")
    elif resposta == "2":
            print("www.discord.com/turmavamoai/dicaseutilidades , seu atendimento sera automaticamente reiniciado, aperte 4 no menu principal se deseja sair")
    elif resposta == "3":
            print("www.discord.com/turmavamoai/comunicados , seu atendimento sera automaticamente reiniciado, aperte 4 no menu principal se deseja sair")
    elif resposta == "4":
            return #retorna ao menu principal 
    else:
            print("Desculpe, não entendi sua resposta. Por favor, tente novamente.")
            
