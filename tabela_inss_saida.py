def mostrar(ano, faixa_contribuicao):
    if ano == 2022:
        if faixa_contribuicao == 1:
            print("|--------------------------------------------|")
            print("| Salário de Contribuição (R$)  |  Alíquota  |")
            print("|-------------------------------|------------|")
            print("| \033[31mAté 1.212,00\033[m                  |    \033[31m7,5%\033[m    |")
            print("| De  1.212,01 até 2.247,35     |    9%      |")
            print("| De  2.427,36 até 3.641,03     |    12%     |")
            print("| De  3.641,04 até 7.087,22     |    14%     |")
            print("|--------------------------------------------|")
        elif faixa_contribuicao == 2:
            print("|--------------------------------------------|")
            print("| Salário de Contribuição (R$)  |  Alíquota  |")
            print("|-------------------------------|------------|")
            print("| Até 1.212,00                  |    7,5%    |")
            print("| \033[31mDe  1.212,01 até 2.247,35\033[m     |    \033[31m9%\033[m      |")
            print("| De  2.427,36 até 3.641,03     |    12%     |")
            print("| De  3.641,04 até 7.087,22     |    14%     |")
            print("|--------------------------------------------|")
        elif faixa_contribuicao == 3:
            print("|--------------------------------------------|")
            print("| Salário de Contribuição (R$)  |  Alíquota  |")
            print("|-------------------------------|------------|")
            print("| Até 1.212,00                  |    7,5%    |")
            print("| De  1.212,01 até 2.247,35     |    9%      |")
            print("| \033[31mDe  2.427,36 até 3.641,03\033[m     |    \033[31m12%\033[m     |")
            print("| De  3.641,04 até 7.087,22     |    14%     |")
            print("|--------------------------------------------|")
        elif faixa_contribuicao == 4:
            print("|--------------------------------------------|")
            print("| Salário de Contribuição (R$)  |  Alíquota  |")
            print("|-------------------------------|------------|")
            print("| Até 1.212,00                  |    7,5%    |")
            print("| De  1.212,01 até 2.247,35     |    9%      |")
            print("| De  2.427,36 até 3.641,03     |    12%     |")
            print("| \033[31mDe  3.641,04 até 7.087,22\033[m     |    \033[31m14%\033[m     |")
            print("|--------------------------------------------|")
    elif ano == 2021:
        if faixa_contribuicao == 1:
            print("|--------------------------------------------|")
            print("| Salário de Contribuição (R$)  |  Alíquota  |")
            print("|-------------------------------|------------|")
            print("| \033[31mAté 1.100,00\033[m                  |    \033[31m7,5%\033[m    |")
            print("| De  1.100,01 até 2.203,48     |    9%      |")
            print("| De  2.203,49 até 3.305,22     |    12%     |")
            print("| De  3.305,23 até 6.433,57     |    14%     |")
            print("|--------------------------------------------|")
        elif faixa_contribuicao == 2:
            print("|--------------------------------------------|")
            print("| Salário de Contribuição (R$)  |  Alíquota  |")
            print("|-------------------------------|------------|")
            print("| Até 1.100,00                  |    7,5%    |")
            print("| \033[31mDe  1.100,01 até 2.203,48\033[m     |    \033[31m9%\033[m      |")
            print("| De  2.203,49 até 3.305,22     |    12%     |")
            print("| De  3.305,23 até 6.433,57     |    14%     |")
            print("|--------------------------------------------|")
        elif faixa_contribuicao == 3:
            print("|--------------------------------------------|")
            print("| Salário de Contribuição (R$)  |  Alíquota  |")
            print("|-------------------------------|------------|")
            print("| Até 1.100,00                  |    7,5%    |")
            print("| De  1.100,01 até 2.203,48     |    9%      |")
            print("| \033[31mDe  2.203,49 até 3.305,22\033[m     |    \033[31m12%\033[m     |")
            print("| De  3.305,23 até 6.433,57     |    14%     |")
            print("|--------------------------------------------|")
        elif faixa_contribuicao == 4:
            print("|--------------------------------------------|")
            print("| Salário de Contribuição (R$)  |  Alíquota  |")
            print("|-------------------------------|------------|")
            print("| Até 1.100,00                  |    7,5%    |")
            print("| De  1.100,01 até 2.203,48     |    9%      |")
            print("| De  2.203,49 até 3.305,22     |    12%     |")
            print("| \033[31mDe  3.305,23 até 6.433,57\033[m     |    \033[31m14%\033[m     |")
            print("|--------------------------------------------|")
