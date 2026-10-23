# Perguntas abertas

| Nº | Pergunta | Impacto | Quem provavelmente sabe |
|---|---|---|---|
| 1 | As configurações reais de Sync (`novo123`) e Comunicação (`sm`) apontam para qual servidor/banco nesta instalação? | Impede iniciar/reiniciar serviços com segurança. | Administrador SQL / dev |
| 2 | Quais campos e estados definem pessoa, crachá, ocorrência, férias e unidade válidos no build atual? | Oráculo de negócio e casos de borda ficam em aviso. | Dev / usuário |
| 3 | Ao deletar e recriar igual cada entidade, qual deve ser o efeito em vínculos, histórico e exclusão lógica? | Não é possível afirmar esperado vs obtido. | Dev / usuário |
| 4 | Qual rota e quais seletores de cada formulário foram validados no Acessus 2.11.1 e no RH atual? | CRUD e importação ficam BLOQUEADOS. | Dev / usuário de automação |
| 5 | Qual evento dispara a importação de cada entidade e como se reconhece o término? | Checkpoint de importação fica BLOQUEADO. | Dev dos serviços |
| 6 | Qual estratégia aprovada de limpeza dos dados AUTOTEST_ em RH e Acessus, inclusive relações? | Impede mutações reais repetíveis. | Administrador SQL / dev |
| 7 | Qual é o briefing da próxima mudança e os cadastros prioritários? | Define o primeiro cenário completo. | Gabriel / dev |
| 8 | Quais são as tabelas e chaves de vínculo entre origem e destino para cada entidade? | Comparação completa de importação depende disso. | Dev / administrador SQL |

