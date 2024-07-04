import os, random
from strings2 import *

# As the game is indeed to be played after a training, here's some hints for a code review purpose
# If you wanna fair play, at Level 1 the processes you can do is: 'Triagem', 'Contenção' and 'Erradicação'
# If you wanna skip level 1 and go to level 2, type 'defcon' at the level choice screen
# If you wanna see all the right answers, type 'respostas' at the level choice screen

n1Agente = False
checkInstall = 5
n1Isolado = False
iocs_bloqs = []
n2Desbloqueado = False
logs_maquinas = [0,0,0,0,0,0]
docDesbloqueado = False
ordemDocumentação = ["6","4","5","1","8","3","10","7","11","12","14","13","9","2"]

def Molde():
    os.system('cls & color B')
    print(banner)

def Validador(escolha,a,b):
    while escolha not in menus[b]:
        Molde()
        print("=== Por favor, digite uma opção válida!! ===\n")
        escolha = input(menus[a]).lower()
    return escolha

def N1():
    Molde()

    global n1Agente,checkInstall,n1Isolado,n2Desbloqueado

    if n1Agente:
        if n1Isolado:
            x = 0
            for i in iocs_n1:
                for y in iocs_bloqs:
                    if y == i:
                        x += 1
            if x >= len(iocs_n1):
                ação = input(menus[18]).lower()
                ação = Validador(ação,18,19)

            else:
                ação = input(menus[2]).lower()
                ação = Validador(ação,2,3)
        else:
            ação = input(menus[2]).lower()
            ação = Validador(ação,2,3)
    else:
        ação = input(menus[2]).lower()
        ação = Validador(ação,2,3)

    if ação in ["triagem"]:
        while True:
            Molde()
            tri = input(menus[4]).lower()
            tri = Validador(tri,4,5)

            if tri in ["1","instalar agentes","instalar","agentes"]:
                Molde()
                agente = input(menus[6]).lower()
                agente = Validador(agente,6,7)

                if agente in ["1","confirmar"]:
                    success = int(random.randrange(1,10))
                    if success > checkInstall:
                        n1Agente = True
                        if checkInstall == 5:
                            input("\n================================\nAgente instalado com sucesso.\n================================\n\n>> Pressione [Enter] para voltar ao menu!!")
                            N1()
                        else:
                            input("\n========================================================================\nParece que o troubleshooting deu certo! Agente instalado com sucesso.\n========================================================================\n\n>> Pressione [Enter] para voltar ao menu!!")
                            N1()
                    else:
                        if checkInstall == 5:
                            checkInstall = checkInstall - 2
                            input("\n**************************************************************\nHouve algum problema ao instalar o agente, tente novamente.\n**************************************************************\n\n>> Pressione [Enter] para voltar ao menu!!")
                            N1()
                        else:
                            checkInstall = checkInstall - 3
                            input("\n***************************************************************\nSeu troubleshooting ainda não trouxe resultados. Não desista!!\n***************************************************************\n\n>> Pressione [Enter] para voltar ao menu!!")
                            N1()
                elif agente in ["2","cancelar","voltar","cancelar e voltar"]:
                    pass

            elif tri in ["2","visualizar logs","visualizar", "logs"]:
                if not n1Agente:
                    input("\nVocê precisa instalar um agente na máquina para poder ver seus logs.\n>> Pressione [Enter] para voltar!!")
                else:
                    print(maquina_n1)
                    input("\n>> Pressione [Enter] para voltar!!")
                    N1()

            elif tri in ["3","voltar"]:
                N1()

    elif ação in ["contenção","contencao","contençao","contencão"]:
        while True:    
            Molde()
            conter = input(menus[8]).lower()
            conter = Validador(conter,8,9)

            if conter in ["1","isolar a máquina","isolar","máquina"]:
                Molde()
                isolar = input(menus[10]).lower()
                isolar = Validador(isolar,10,11)

                if isolar in ["1","confirmar"]:
                    n1Isolado = True
                    input("\n================================\nMáquina isolada com sucesso.\n================================\n\n>> Pressione [Enter] para voltar ao menu!!")
                    N1()

                elif isolar in ["2","cancelar","voltar","cancelar e voltar"]:
                    pass

            elif isolar in ["2","voltar"]:
                N1()

    elif ação in ["erradicação","erradicacao","erradicaçao","erradicacão"]:
        while True:
            Molde()
            erra = input(menus[12]).lower()
            erra = Validador(erra,12,13)

            if erra in ["1","bloquear iocs", "bloquear", "iocs"]:
                Molde()
                bloq = input(menus[14]).lower()
                bloq = Validador(bloq,14,15)

                if bloq in ["1","prosseguir"]:
                    escolha = 0
                    iocInput = []
                    while escolha not in ["2","concluir"]:
                        iocInput.append(input('\nDigite o IoC que deseja bloquear:\n\n>> '))
                        escolha = input(menus[16]).lower()
                        escolha = Validador(escolha,16,17)
                    print("\n")
                    for i in range(len(iocInput)):
                        print(" ¬",iocInput[i])
                        iocs_bloqs.append(iocInput[i])

                    input("\n================================\nIoCs bloqueados com sucesso.\n================================\n\n>> Pressione [Enter] para voltar ao menu!!")
                    N1()

                elif bloq in ["2","cancelar","voltar","cancelar evoltar"]:
                    pass

            elif erra in ["2","voltar"]:
                N1()

    elif ação in ["recuperação","recuperacao","recuperaçao","recuperacão"]:
        input("\nDe fato a Recuperação é uma etapa de IR, mas ela não é o foco do nosso jogo.\n>> Pressione [Enter] para voltar!!")
        N1()

    elif ação in ["documentação","documentacao","documentaçao","documentacão"]:
        input("\nDe fato a Documentação é uma etapa de IR, mas ela não é o foco deste nível.\n>> Pressione [Enter] para voltar!!")
        N1()

    elif ação in ["finalizar incidente", "finalizar", "incidente"]:
        Molde()
        final = input(menus[20]).lower()
        final = Validador(final,20,21)

        if final in ["1","finalizar"]:
            n2Desbloqueado = True
            Niveis()
        elif final in ["2","cancelar e voltar","cancelar","voltar"]:
            N1()

def N2():
    Molde()

    global docDesbloqueado

    if docDesbloqueado:
        ação = input(menus[30]).lower()
        ação = Validador(ação,30,31)
    else:
        ação = input(menus[24]).lower()
        ação = Validador(ação,24,25)

    if ação in ["1","triagem"]:
        while True:
            Molde()
            tri = input(menus[26]).lower()
            tri = Validador(tri,26,27)

            if tri in ["1","visualizar logs","visualizar", "logs"]:
                Molde()
                visu = input(menus[28]).lower()
                visu = Validador(visu,28,29)

                if visu in ["1","web server","web","server"]:
                    print(web)
                    input("\n>> Pressione [Enter] para voltar ao menu!!")
                    logs_maquinas[0] = 1
                elif visu in ["2","database","data base","db","banco"]:
                    print(db)
                    input("\n>> Pressione [Enter] para voltar ao menu!!")
                    logs_maquinas[1] = 1
                elif visu in ["3","workstation 1","ws 1","ws1"]:
                    print(ws1)
                    input("\n>> Pressione [Enter] para voltar ao menu!!")
                    logs_maquinas[2] = 1
                elif visu in ["4","workstation 2","ws 2","ws2"]:
                    print(ws2)
                    input("\n>> Pressione [Enter] para voltar ao menu!!")
                    logs_maquinas[3] = 1
                elif visu in ["5","workstation 3","ws 3","ws3"]:
                    print(ws3)
                    input("\n>> Pressione [Enter] para voltar ao menu!!")
                    logs_maquinas[4] = 1
                elif visu in ["6","domain controller","dc","domain","controller"]:
                    print(ad)
                    input("\n>> Pressione [Enter] para voltar ao menu!!")
                    logs_maquinas[5] = 1

                if logs_maquinas[0] == 1 and logs_maquinas[1] == 1 and logs_maquinas[2] == 1 and logs_maquinas[3] == 1 and logs_maquinas[4] == 1 and logs_maquinas[5] == 1:
                    docDesbloqueado = True 
                N2()

            elif tri in ["2","voltar"]:
                N2()

    elif ação in ["2","documentação"]:
        Molde()
        doc = input(menus[32]).lower()
        doc = Validador(doc,32,33)

        if doc in ["1","prosseguir"]:
            docInput = []
            for i in range(len(ordemDocumentação)):
                Molde()
                doc = input(menus[34]).lower()
                doc = Validador(doc,34,35)
                docInput.append(doc)
            if docInput == ordemDocumentação:
                input("Parabéns, você recriou todo o ataque!!!\n\n>> Pressione [Enter] para finalizar o jogo!!")
                exit()
            else:
                input("O ataque ainda não está correto... Porque não revê os logs e tenta de novo?\n\n>> Pressione [Enter] para voltar ao menu!!")
                N2()
        elif doc in ["2","voltar"]:
            N2()

def Niveis():
    Molde()

    if n2Desbloqueado:
        niv = input(menus[22]).lower()
        niv = Validador(niv,22,23)
    else:
        niv = input(menus[0]).lower()
        niv = Validador(niv,0,1)

    if niv in ["1", "nível 1", "nivel", "nivel 1"]:
        Molde()
        input(desc1)
        N1()
    
    elif niv in ["2","nível 2","nivel 2","defcon"]:
        Molde()
        input(desc2)
        N2()

    elif niv in ["respostas"]:
        input(respostas)

Niveis()