"""Fonte única para ajuda da CLI e página didática do painel."""
COMANDOS = [
    {"tema": "Preparação", "comando": "ambiente", "descricao": "Confere Python, executáveis, INIs, ODBC, serviços e bancos sem escrita.", "exemplo": "automatiza ambiente", "opcoes": "--perfil NOME: seleciona o perfil."},
    {"tema": "Auditorias", "comando": "auditorias", "descricao": "Mapeia e testa históricos e filtros, registrando cada passo.", "exemplo": "automatiza auditorias --modulo refeitorio --perfil auditorias", "opcoes": "--modulo todos|nome; --extremo; --filtro TEXTO; --pular 1,2; --saida PASTA; --pid N."},
    {"tema": "Sequências", "comando": "sequencias", "descricao": "Executa cenário YAML ou sequência gerada por semente.", "exemplo": "automatiza sequencias --arquivo tests/sequencias/checagem_leitura.yaml", "opcoes": "--arquivo YAML ou --seed N; --passos N; --massa N."},
    {"tema": "Sequências", "comando": "robot", "descricao": "Executa casos Robot selecionados por tag.", "exemplo": "automatiza robot --tag smoke", "opcoes": "--tag NOME."},
    {"tema": "Banco", "comando": "observar", "descricao": "Acompanha mudanças SQL e registra notas manuais.", "exemplo": "automatiza observar iniciar --duracao 1800 --intervalo 15", "opcoes": "iniciar|anotar|status|parar; --nota TEXTO; --duracao SEG; --intervalo SEG."},
    {"tema": "Banco", "comando": "conferir", "descricao": "Captura consulta filtrada ou compara dois arquivos locais.", "exemplo": "automatiza conferir comparar --antes reports/antes.json --depois reports/depois.json --saida reports/diff.json", "opcoes": "consultar|comparar; --filtros JSON; --antes; --depois; --saida."},
    {"tema": "RH/SIRH", "comando": "ciclos", "descricao": "Planeja ou executa ciclos; escrita requer confirmação e DB_NAME seguro.", "exemplo": "automatiza ciclos planejar --arquivo examples/ciclos-sirh.json --saida reports/plano.json", "opcoes": "planejar|executar|suite; --arquivo; --saida; --semente; --rodadas; --confirmo-escrita."},
    {"tema": "Resultados", "comando": "comparar-rodadas", "descricao": "Compara falhas entre duas rodadas de auditoria.", "exemplo": "automatiza comparar-rodadas resultados/antes resultados/depois", "opcoes": "ANTERIOR ATUAL."},
    {"tema": "Projeto", "comando": "testes-unitarios", "descricao": "Executa a suíte Python isolada.", "exemplo": "automatiza testes-unitarios", "opcoes": "Sem opções."},
    {"tema": "Projeto", "comando": "comandos", "descricao": "Mostra esta lista completa de comandos.", "exemplo": "automatiza comandos", "opcoes": "Sem opções."},
]

POWERSHELL = [
    {"tema": "PowerShell útil", "comando": "Get-CimInstance Win32_Process", "descricao": "Acha o PID pelo caminho do executável.", "exemplo": "Get-CimInstance Win32_Process | Where-Object ExecutablePath -like 'C:\\AcessusHostFisico\\*' | Select-Object ProcessId,ExecutablePath", "opcoes": "Leitura somente."},
    {"tema": "PowerShell útil", "comando": "Get-Item", "descricao": "Lê a versão do executável.", "exemplo": "(Get-Item 'C:\\acesso\\Acessus.exe').VersionInfo.FileVersion", "opcoes": "Leitura somente."},
    {"tema": "PowerShell útil", "comando": "Get-Service", "descricao": "Lista o estado dos serviços Acessus.", "exemplo": "Get-Service FrmSyncImpViewsPrincipal,FrmViewsPrincipalService,SrvAcessusCom", "opcoes": "Leitura somente."},
]
