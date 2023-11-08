# Valores fixos de variáveis para simular o índice de qualidade do ar em certos períodos do dia
indice_qualidade_ar_manha = 47
indice_qualidade_ar_tarde = 63
indice_qualidade_ar_noite = 109

# Lista para armazenar as operações realizadas pelo usuário
operacoes_realizadas = []

# Apresentação e boas-vindas
# Imprime uma mensagem de boas-vindas e as opções de escolha disponíveis
def menu_principal():
    print(' -'*30)
    print('Bem-vindo ao aplicativo "Solving O₂". Agradecemos o acesso!')
    print(' -'*30)
    print('Atualmente, possuímos algumas opções para te ajudar com a poluição de São Paulo:')
    print('1. Qual o nível de poluição em minha área e o que fazer para me proteger?')
    print('2. Qual a condição mais favorável para ir até o meu local de trabalho hoje?')
    print('3. Qual o espaço de co-working mais próximo de minha casa?')
    print('4. Salvar dicas de como me proteger da poluição do ar em um arquivo .txt')
    print('5. Sair')

# Função para adicionar uma operação à lista de operações realizadas
def adicionar_operacao(operacao):
    operacoes_realizadas.append(operacao)

# Função para caso seja selecionado a opção (1)
# Exibe informações sobre o nível de poluição e fornece medidas de segurança com base no período do dia escolhido
def nivel_poluicao():
    print('')
    print(' -'*30)
    print('Você acessou a página "Qual o nível de poluição em minha área e o que fazer para me proteger?"')
    print('')
    print('Percebemos que você está perto de Ibirapuera, São Paulo.')
    print('')
    while True:
        periodo = input('Por favor, informe o período atual ([manhã = M], [tarde = T] ou [noite = N]), ou digite "V" para voltar ao menu principal: ')
        if periodo.lower() == "v":
            print('Retornando ao menu principal...')
            return
        elif periodo.lower() not in ["m", "t", "n"]:
            print('')
            print('Opção inválida, por favor, digite "M" para manhã, "T" para tarde, "N" para noite ou "V" para voltar ao menu principal.')
            continue

        confirmacao = input(f'Você selecionou o período {periodo.upper()}. Isto está correto? Digite "S" para SIM e "N" para NÃO: ')
        if confirmacao.lower() == "s":
            if periodo.lower() == "m":
                print('')
                print(f'O índice de qualidade do ar, nesta região, pela manhã é: {indice_qualidade_ar_manha}')
                print('')
                adicionar_operacao('Verificou o nível de poluição pela manhã.')
            elif periodo.lower() == "t":
                print('')
                print(f'O índice de qualidade do ar, nesta região, pela tarde é: {indice_qualidade_ar_tarde}')
                print('')
                adicionar_operacao('Verificou o nível de poluição pela tarde.')
            elif periodo.lower() == "n":
                print('')
                print(f'O índice de qualidade do ar, nesta região, pela noite é: {indice_qualidade_ar_noite}')
                print('')
                adicionar_operacao('Verificou o nível de poluição pela noite.')

            medidas_seguranca = input('Você gostaria de saber quais são as medidas de segurança que deve tomar com base nisso? (Digite "S" para SIM e "N" para NÃO): ')
            if medidas_seguranca.lower() == "s":
                print('')
                print('Medidas de segurança contra poluição:')
                print('- Evite atividades ao ar livre em áreas muito poluídas (índice maior do que 100).')
                print('- Leve sempre um colírio e evite atividades físicas intensas em áreas muito poluídas (índice maior do que 100).')
                print('- Use máscara de proteção contra poluição quando necessário.')
                print('- Mantenha ambientes internos bem ventilados.')
                print('- Não deixe de praticar esportes ou até mesmo dar uma caminhada caso o índice esteja menor do que 60!')
                print('')
                adicionar_operacao('Visualizou medidas de segurança contra poluição.')

            voltar = input('Digite "V" para voltar ao menu principal ou pressione "Enter" para continuar nesta página: ')
            if voltar.lower() == "v":
                return
        elif confirmacao.lower() == "n":
            continue
        else:
            print('Opção inválida, digite "S" para SIM ou "N" para NÃO.')

# Função para caso seja selecionado a opção (2)
# Oferece recomendações sobre o meio de transporte com base na distância fornecida pelo usuário
def condicao_transporte():
    print('')
    print(' -'*30)
    print('Você acessou a página "Qual a condição mais favorável para ir até o meu local de trabalho hoje?"')
    print('')

    while True:
        try:
            distancia = float(input('Por favor, informe a distância aproximada (em km) de sua casa até seu local de trabalho: '))
        except ValueError:
            print('')
            print('Por favor, insira um valor numérico válido.')
            continue
        if distancia <= 0:
            print('')
            print('A distância deve ser maior que zero.')
        else:
            print('')
            print(f'Você inseriu uma distância de {distancia} km.')

            confirmacao = input('Isso está correto? Digite "S" para SIM e "N" para NÃO: ')
            if confirmacao.lower() == "s":
                if distancia <= 5:
                    print('')
                    print('Recomendamos caminhada ou transporte público.')
                    print('')
                    adicionar_operacao('Recebeu recomendação de transporte: caminhada ou transporte público.')
                elif distancia < 12:
                    print('')
                    print('Recomendamos transporte público ou carona.')
                    print('')
                    adicionar_operacao('Recebeu recomendação de transporte: transporte público ou carona.')
                else:
                    print('')
                    print('Recomendamos o uso de veículo próprio.')
                    print('')
                    adicionar_operacao('Recebeu recomendação de transporte: uso de veículo próprio.')

                voltar = input('Digite "V" para voltar ao menu principal ou pressione Enter para continuar: ')
                if voltar.lower() == "v":
                    return
            elif confirmacao.lower() == "n":
                continue
            else:
                print('Opção inválida, digite "S" para SIM ou "N" para NÃO.')

# Função para caso seja selecionado a opção (3)
# Informa o usuário sobre o espaço de co-working mais próximo de sua casa, com base na escolha do bairro
def co_working():
    print('')
    print(' -'*30)
    print('Você acessou a página "Qual o espaço de co-working mais próximo de minha casa?"')
    print('')

    while True:
        print('Escolha uma das opções de bairro:')
        print('1. Bela Vista')
        print('2. Santana')
        print('3. Barra Funda')
        print('')

        escolha = input('Digite o número correspondente (1, 2 ou 3), ou digite "V" para voltar ao menu principal: ')
        if escolha.lower() == "v":
            print('Retornando ao menu principal...')
            return
        if escolha not in ["1", "2", "3"]:
            print('')
            print('Opção inválida, por favor, digite "1", "2" ou "3", ou "V" para voltar ao menu principal.')
            continue

        confirmacao = input(f'Você selecionou o bairro {escolha}. Isto está correto? Digite S para SIM e N para NÃO: ')
        if confirmacao.lower() == "s":
            if escolha == "1":
                print('O co-working 2 é o mais próximo! Endereço: Av. Paulista, 1106')
                adicionar_operacao('Encontrou espaço de co-working mais próximo: Bela Vista, Av. Paulista, 1106')
            elif escolha == "2":
                print('O co-working 2 é o mais próximo! Endereço: R. Alfredo Guedes, 91')
                adicionar_operacao('Encontrou espaço de co-working mais próximo: Santana, R. Alfredo Guedes, 91')
            elif escolha == "3":
                print('O co-working 3 é o mais próximo! Endereço: R. Palestra Itália, 200')
                adicionar_operacao('Encontrou espaço de co-working mais próximo: Barra Funda, R. Palestra Itália, 200')

            voltar = input('Digite "V" para voltar ao menu principal ou pressione Enter para continuar: ')
            if voltar.lower() == "v":
                return
        elif confirmacao.lower() == "n":
            continue
        else:
            print('Opção inválida, digite "S" para SIM ou "N" para NÃO.')

# Função para salvar as dicas em um arquivo de texto
def salvar_dicas_em_arquivo():
    dicas = [
        '- Evite atividades ao ar livre em areas muito poluidas (indice maior do que 100).',
        '- Leve sempre um colirio e evite atividades fisicas intensas em areas muito poluidas (indice maior do que 100).',
        '- Use mascara de protecao contra poluicao quando necessario.',
        '- Mantenha ambientes internos bem ventilados.',
        '- Nao deixe de praticar esportes ou ate mesmo dar uma caminhada caso o indice esteja menor do que 60!'
    ]
    with open('dicas_poluição.txt', 'w') as arquivo:
        for dica in dicas:
            arquivo.write(dica + '\n')
    operacoes_realizadas.append('Salvou as dicas de como se cuidar em arquivo .txt')  # Adiciona uma entrada especial ao resumo
    print('')
    print(' -'*30)
    print('Você acessou a página "Salvar dicas de como me proteger da poluição do ar em um arquivo .txt"')
    print('')
    print('As dicas de como se cuidar foram salvas em "dicas_poluição.txt".')
    print('Você será redirecionado para o menu principal agora.')
    print('Tenha um ótimo dia e não se esqueça de seguir as dicas corretamente!')
    print('')

# Função principal que mantém o programa em execução
while True:
    menu_principal()
    print('')
    try:
        escolha = int(input('Digite o número da opção desejada: '))
    except ValueError:
        print('Por favor, insira um número válido como escolha.')
        continue

    if escolha == 1:
        nivel_poluicao()
    elif escolha == 2:
        condicao_transporte()
    elif escolha == 3:
        co_working()
    elif escolha == 4:
        salvar_dicas_em_arquivo()  # Opção para salvar as dicas em um arquivo .txt (nova opção)
    elif escolha == 5:
        print('Resumo das operações realizadas:')
        for operacao in operacoes_realizadas:
            print(f'- {operacao}')
        confirmacao = input('Você tem certeza que deseja sair? (Digite "S" para SIM ou "N" para NÃO): ')
        if confirmacao.lower() == "s":
            print("Saiu do programa. Volte Sempre!")
            break
        else:
            print("Cancelou saída do programa. Sendo direcionado para o menu principal...")
    else:
        print('Opção inválida, tente novamente.')