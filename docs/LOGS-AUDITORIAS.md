# Logs automáticos de Auditorias/Históricos

O script `scripts/testar_auditorias_cronologico.py` alimenta **dois arquivos permanentes** na raiz de `resultados/` durante a execução:

| Arquivo | Uso |
| --- | --- |
| `resultados/passo-a-passo.log` | Leitura humana, uma linha por ação, em ordem cronológica. |
| `resultados/passo-a-passo-detalhado.jsonl` | Uma linha JSON por ação, outra por tentativa finalizada e uma por fim de execução. Contém horário local com milissegundos, horário UTC, ID da execução, sequência, tempo decorrido, build, executável, PID, janela, servidor e banco confirmados, módulo, histórico, filtro, valores planejados e exibidos, período, mensagens, contagem, status, duração, caminhos das evidências e traceback de falhas de automação quando disponíveis. |

Ambos são abertos **somente em modo de acréscimo** e sincronizados no disco a cada ação. Cada rodada continua criando sua própria pasta com `tentativas.jsonl` e screenshots. O arquivo detalhado começa a registrar as execuções feitas após sua implantação; os passos antigos permanecem no log humano, sem inventar metadados que não foram capturados na época.

O código que grava os dois arquivos fica em `src/automatiza/diario_auditorias.py`. O executor o chama diretamente; não depende do Codex. Os registros compartilham `execucao_id`. Cada ação no JSONL possui `linha_passo_a_passo` idêntica à linha do log humano; cada `tentativa_finalizada` contém `registro_completo` e `tentativa_id`.

Para executar, abra Auditorias/Históricos no módulo desejado e obtenha o PID do processo. Na venv Python 32 bits, rode:

```powershell
$env:PYTHONPATH = 'C:\AutomatizaTestes\src'
& 'C:\python32b\venv32\Scripts\python.exe' `
  'C:\AutomatizaTestes\scripts\testar_auditorias_cronologico.py' `
  <PID> <modulo> 'C:\AutomatizaTestes\resultados\nome-da-rodada'
```

`<modulo>` aceita `acesso`, `refeitorio`, `portaria`, `estacionamento`, `escola` e `administracao`. O script apenas consulta a interface e usa SQL de leitura para selecionar amostras. O JSONL não inclui usuário, senha ou string de conexão.
