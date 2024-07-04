banner = ('''\n
▄█    ▄   ▄█▄    ▄█ ██▄   ▄███▄      ▄      ▄▄▄▄▀       ▄▀  ██   █▀▄▀█ ▄███▄   
██     █  █▀ ▀▄  ██ █  █  █▀   ▀      █  ▀▀▀ █        ▄▀    █ █  █ █ █ █▀   ▀  
██ ██   █ █   ▀  ██ █   █ ██▄▄    ██   █     █        █ ▀▄  █▄▄█ █ ▄ █ ██▄▄    
▐█ █ █  █ █▄  ▄▀ ▐█ █  █  █▄   ▄▀ █ █  █    █         █   █ █  █ █   █ █▄   ▄▀ 
 ▐ █  █ █ ▀███▀   ▐ ███▀  ▀███▀   █  █ █   ▀           ███     █    █  ▀███▀   
   █   ██                         █   ██                      █    ▀           
\n''')

menus = [
    ('''Que nível deseja jogar?
 ¬ Nível 1
\n>> '''),
    ["1", "nível 1", "nivel 1","defcon","respostas"],
    ('''Que etapa do processo de IR você deseja realizar?
\n>> '''),
    ["triagem",
    "contenção","contencao","contençao","contencão",
    "erradicação","erradicacao","erradicaçao","erradicacão",
    "recuperação","recuperacao","recuperaçao","recuperacão",
    "documentação","documentacao","documentaçao","documentacão"],
    ('''~~~ Triagem ~~~
 ¬ 1: Instalar agentes
 ¬ 2: Visualizar logs
 ¬ 3: Voltar
\n>> '''),
    ["1","instalar agentes","instalar","agentes",
    "2","visualizar logs","visualizar", "logs",
    "3","voltar"],
    ('''~~~ Triagem ¬ Instalar agentes ~~~
    \nDeseja instalar um agente na máquina comprometida?
Com o agente, você vai poder visualizar os logs da mesma!
 ¬ 1: Confirmar
 ¬ 2: Cancelar e voltar
\n>> '''),
    ["1","2","confirmar","cancelar","voltar","cancelar e voltar"],
    ('''~~ Contenção ~~\n
 ¬ 1: Isolar a máquina
 ¬ 2: Voltar
\n>> '''),
    ["1","isolar a máquina","isolar","máquina",
    "2","voltar"],
    ('''~~~ Contenção ¬ Isolar a máquina ~~~
    \nDeseja cortar todas as conexões de rede da máquina?
 ¬ 1: Confirmar
 ¬ 2:Cancelar e voltar
\n>> '''),
    ["1","confirmar",
    "2","cancelar","voltar","cancelar e voltar"],
    ('''~~~ Erradicação ~~~
 ¬ 1: Bloquear IoCs
 ¬ 2: Voltar
\n>> '''),
    ["1","bloquear iocs", "bloquear", "iocs",
    "2","voltar"],
    ('''~~~ Erradicação ¬ Bloquear IoCs ~~~
    \nDeseja bloquear algum IoC no ambiente?
 ¬ 1: Prosseguir
 ¬ 2: Cancelar e voltar
\n>> '''),
    ["1","prosseguir",
    "2","cancelar","voltar","cancelar evoltar"],
    ('''\n ¬ 1: Bloquear outro
 ¬ 2: Concluir
\n>> '''),
    ["1","bloquear","outro","bloquear outro",
    "2","concluir"],
    ('''Que etapa do processo de IR você deseja realizar?
\nFinalizar Incidente (Novo)
\n>> '''),
    ["finalizar incidente", "finalizar", "incidente"],
    ('''~~~ Finalizar Incidente ~~~
    \nVocê já fez tudo possível e recomendado no Nível 1.
Deseja finalizar o mesmo e se aventurar no Nível 2?
 ¬ 1: Finalizar
 ¬ 2: Cancelar e voltar
\n>> '''),
    ["1","finalizar",
    "2","cancelar e voltar","cancelar","voltar"],
    ('''Que nível deseja jogar?
 ¬ Nível 1
 ¬ Nível 2 (Novo)
\n>> '''),
    ["1","nível 1","nivel 1",
    "2","nível 2","nivel 2",
    "respostas"],
    ('''O que deseja fazer?
 ¬ 1: Triagem
\n>> '''),
    ["1","triagem"],
    ('''~~~ Triagem ~~~
 ¬ 1: Visualizar logs
 ¬ 2: Voltar
\n>> '''),
    ["1","visualizar logs","visualizar", "logs",
    "2","voltar"],
    ('''~~~ Triagem ¬ Visualizar Logs ~~~
     \nQual máquina você deseja visualizar?
 ¬ 1: Web Server
 ¬ 2: Database
 ¬ 3: Workstation 1
 ¬ 4: Workstation 2
 ¬ 5: Workstation 3
 ¬ 6: Domain Controller
\n>> '''),
    ["1","web server","web","server",
    "2","database","data base","db","banco",
    "3","workstation 1","ws 1","ws1",
    "4","workstation 2","ws 2","ws2",
    "5","workstation 3","ws 3","ws3",
    "6","domain controller","dc","domain","controller"],  
    ('''O que deseja fazer?
 ¬ 1: Triagem
 ¬ 2: Documentação (Novo)   
\n>> '''),
    ["1","triagem",
    "2","documentação","documentacao","documentaçao","documentacão"],
    ('''~~~ Documentação ~~~
\nDeseja documentar toda a linha do tempo do ataque?
Insira todos os acontecimentos na ordem correta para completar o jogo!\n
 ¬ 1: Prosseguir
 ¬ 2: Voltar
\n>> '''),
    ["1","prosseguir",
    "2","voltar"],
    (''' ¬ 1: Netcat foi executado para um scan de rede
 ¬ 2: MySQLDump foi executado
 ¬ 3: Workstation 2 foi comprometida
 ¬ 4: Dump de credenciais foi feito para conseguir acesso Administrativo
 ¬ 5: Banco de Dados foi comprometido
 ¬ 6: Web Server foi comprometido
 ¬ 7: Persistência foi criada nas máquinas comprometidas
 ¬ 8: Workstation 1 foi comprometida
 ¬ 9: Nishang foi executado
 ¬ 10: Mais um Netcat foi executado para encontrar outras redes internas
 ¬ 11: Workstation 3 foi comprometida via e-mail infectado
 ¬ 12: Rubeus foi executado em uma máquina
 ¬ 13: Persistência foi criada nas outras máquinas comprometidas
 ¬ 14: Domain Controller foi comprometido
\nQual a primeira/próxima etapa?
\n>> '''),
    ["1","netcat foi executado para um scan de rede",
    "2","mysqldump foi executado",
    "3","workstation 2 foi comprometida",
    "4","dump de credenciais foi feito para conseguir acesso administrativo",
    "5","banco de dados foi comprometido",
    "6","web server foi comprometido",
    "7","persistência foi criada nas máquinas comprometidas",
    "8","workstation 1 foi comprometida",
    "9","nishang foi executado",
    "10","mais um netcat foi executado para encontrar outras redes internas",
    "11","workstation 3 foi comprometida via e-mail infectado",
    "12","rubeus foi executado em uma máquina",
    "13","persistência foi criada nas outras máquinas comprometidas",
    "14","domain controller foi comprometido"],
]

desc1 = ('''Vamos treinar um pouco o que aprendemos até agora?
\nVamos começar de forma simples.
Preciso que você responda um Incidente que aconteceu em X máquina.
Faça os passos necessários e avançe ao próximo nível!
\n>> Pressione [Enter] para continuar!! ''')

desc2 = ('''Agora que já deu para aquecer, vamos para o verdadeiro desafio!
\nPrecisamos de sua ajuda para entender o que aconteceu em um Incidente.
Foi detectado atividade suspeita no Banco de Dados deles.
Agentes ja foram instalados em todas máquinas.
Precisamos de sua ajuda para ler os logs e criar uma linha do tempo do ataque.
Recrie o ataque corretamente e zere o Incident Game!
\nEste é o ambiente alvo:\n
Database  ______________ Workstation 1 _________
10.0.2.10       |        10.0.3.22              |
    |           |                               |
    |           |_______ Workstation 2 _________|__ Domain Controller
    |           |        10.0.3.23              |   10.0.4.10
    |           |                               |
Web Server      |_______ Workstation 3 _________|
10.0.2.9                 10.0.3.24
\n>> Pressione [Enter] para continuar!! ''')

maquina_n1 = ('''\n ===  Conexões de rede  ==
¬ 31/02/23 20h07 INBOUND 3.44.29.109:443
¬ 31/02/23 20h15 OUTBOUND 172.253.122.102:443
\n ===  Processos da máquina  ===
¬ 31/02/23 20h13 evil_seed
¬ 31/02/23 20h15 gdrive
\n ===  Últimos logons  ===
¬ 31/02/23 20h07 jorge
\n ===  Arquivos suspeitos  ===
¬ 31/02/23 20h13 database.sql''')

iocs_n1 = ["3.44.29.109","172.253.122.102","evil_seed","gdrive","database.sql"]

web = (''' ===  Conexões de rede  ===
¬ 31/02/23 19h23 INBOUND 3.44.29.109:443
¬ 31/02/23 19h25 INBOUND 19.16.105.35:443
¬ 31/02/23 19h23 INBOUND 100.58.29.68:443
¬ 31/02/23 19h24 INBOUND 13.44.17.233:443
¬ 31/02/23 19h22 INBOUND 20.04.21.77:443
¬ 31/02/23 19h27 INBOUND 80.76.99.167:443
¬ 31/02/23 19h30 INBOUND 25.50.75.100:443
¬ 31/02/23 19h22 OUTBOUND 10.0.2.10:3306
¬ 31/02/23 19h27 OUTBOUND 10.0.2.10:5985 
\n ===  Processos da máquina  ===
¬ 31/02/23 19h25 dump.cpp
¬ 31/02/23 19h27 winrm
¬ 31/02/23 19h45 regedit
¬ 31/02/23 19h46 powersheIl
\n ===  Últimos logons  ===
¬ 31/02/23 19h22 sv_acc
\n ===  Arquivos suspeitos  ===
¬ 31/02/23 19h25 webserver_02_31_2023.txt''')

db = (''' ===  Conexões de rede  ===
¬ 31/02/23 19h22 INBOUND 10.0.2.10:3306
¬ 31/02/23 19h27 INBOUND 10.0.2.9:5985
¬ 31/02/23 19h32 OUTBOUND 10.0.3.22:5985
¬ 31/02/23 19h33 OUTBOUND 10.0.3.23:5985
¬ 31/02/23 19h34 OUTBOUND 10.0.3.24:5985
¬ 31/02/23 20h45 OUTBOUND [2a0b:e40:3::11:]:443
\n ===  Processos da máquina  ===
¬ 31/02/23 19h29 nc
¬ 31/02/23 19h32 winrm
¬ 31/02/23 19h45 regedit
¬ 31/02/23 19h46 powersheIl
¬ 31/02/23 20h43 mysqldump
¬ 31/02/23 20h44 megacmd
\n ===  Últimos logons  ===
¬ 31/02/23 19h27 adm
\n ===  Arquivos suspeitos  ===
¬ 31/02/23 20h43 legit.sql''')

ws1 = (''' ===  Conexões de rede  ===
¬ 31/02/23 19h27 INBOUND 10.0.4.10:389
¬ 31/02/23 19h32 INBOUND 10.0.2.10:5985
¬ 31/02/23 19h30 OUTBOUND 92.27.65.40:443
¬ 31/02/23 19h35 OUTBOUND 10.0.4.10:5985
\n ===  Processos da máquina  ===
¬ 31/02/23 19h33 nc
¬ 31/02/23 19h20 powershell
¬ 31/02/23 19h35 wimrm
¬ 31/02/23 19h45 regedit
¬ 31/02/23 19h46 powersheIl
¬ 31/02/23 19h50 outlook
\n ===  Últimos logons  ===
¬ 31/02/23 19h32 adm
\n ===  Arquivos suspeitos  ===
¬ ''')

ws2 = (''' ===  Conexões de rede  ===
¬ 31/02/23 19h27 INBOUND 10.0.4.10:389
¬ 31/02/23 19h33 INBOUND 10.0.2.10:5985
¬ 31/02/23 19h30 OUTBOUND 29.88.15.67:443
\n ===  Processos da máquina  ===
¬ 31/02/23 19h25 cmd
¬ 31/02/23 19h45 regedit
¬ 31/02/23 19h46 powersheIl
\n ===  Últimos logons  ===
¬ 31/02/23 19h32 adm
\n ===  Arquivos suspeitos  ===
¬ ''')

ws3 = (''' ===  Conexões de rede  ===
¬ 31/02/23 19h27 INBOUND 10.0.4.10:389
¬ 31/02/23 19h27 INBOUND 10.0.4.10:88
¬ 31/02/23 19h35 OUTBOUND 12.53.98.53:443
¬ 31/02/23 20h22 OUTBOUND 10.0.4.10:5985
\n ===  Processos da máquina  ===
¬ 31/02/23 20h04 powersheIl
¬ 31/02/23 20h06 regedit
¬ 31/02/23 20h09 rubeus
\n ===  Últimos logons  ===
¬ 31/02/23 20h04 felipe
\n ===  Arquivos suspeitos  ===
¬ 31/02/23 20h19 rub_out.txt''')

ad = (''' ===  Conexões de rede  ===
¬ 31/02/23 20h22 INBOUND 10.0.3.22:5985
¬ 31/02/23 19h27 OUTBOUND 10.0.3.22:389
¬ 31/02/23 19h27 OUTBOUND 10.0.3.23:389
¬ 31/02/23 19h27 OUTBOUND 10.0.3.24:389
¬ 31/02/23 20h25 OUTBOUND 20.04.21.77:443
¬ 31/02/23 20h40 OUTBOUND [2a0b:e40:3::11:]:443
\n ===  Processos da máquina  ===
¬ 31/02/23 20h24 cmd
¬ 31/02/23 20h37 nishang
¬ 31/02/23 20h40 megacmd
\n ===  Últimos logons  ===
¬ 31/02/23 20h22 d_a
¬ 31/02/23 20h27 d-a
\n ===  Arquivos suspeitos  ===
¬ 31/02/23 20h38 ntds.dit.cpy
¬ 31/02/23 20h38 sam.cpy
¬ 31/02/23 20h38 system.cpy''')

respostas = ('''A resposta do Nível 1 é simples
 ¬ Instale os agentes
 ¬ Isole a máquina
 ¬ Bloqueie todos os IoCs (3.44.29.109 | 172.253.122.102 | evil_seed | gdrive | database.sql)
\nNo Nível 2, a linha do tempo do ataque é:
 ¬ Web Server foi comprometido
 ¬ Dump de credenciais foi feito para conseguir acesso Administrativo
 ¬ Banco de Dados foi comprometido
 ¬ Netcat foi executado para um scan de rede
 ¬ Workstation 1 foi comprometido
 ¬ Workstation 2 foi comprometido
 ¬ Mais um Netcat foi executado para encontrar outras redes internas
 ¬ Persistência foi criada nas máquinas comprometidas
 ¬ Workstation 3 foi comprometida via e-mail infectado
 ¬ Rubeus foi executado em uma máquina
 ¬ Domain Controller foi comprometido
 ¬ Persistência foi criada nas outras máquinas comprometidas
 ¬ Nishang foi executado
 ¬ MySQLDump foi executado
''')