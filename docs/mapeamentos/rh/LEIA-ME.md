# Mapeamento do RH sem controlar a tela

Os mapas desta pasta foram extraídos **diretamente dos recursos TPF0 dos
arquivos instalados**, sem carregar bibliotecas, executar o RH ou alterar as
suas janelas. Os binários originais foram apenas lidos. O SHA-256 de cada
origem está no JSON correspondente.

| Mapa | Formulário | Componentes declarados |
|---|---|---:|
| login | TFrm_Login | 22 |
| aviso-configuracoes | TFrm_ConfiguracoesInvalidas | 9 |
| frequencia-principal | TFrm_RHPA0010 | 228 |
| registro-ocorrencias | TFrm_RH0540RegOcorrencias | 159 |
| ocorrencias-coletiva-inclusao | TFrm_RH0541ProgColetivaInclusao | 80 |
| ocorrencias-coletiva-exclusao | TFrm_RH0543ProgColetivaExclusao | 34 |
| ferias-cedidas | TFrm_RHPA5130 | 53 |
| ferias-cedidas-detalhe | TFrm_RHPA5131 | 30 |
| ferias-coletiva-exclusao | TFrm_RHPA5133 | 25 |

Os nomes `registro-ocorrencias` e `ferias-cedidas` correspondem aos menus:

- `Programações → Registro de Ocorrências...`
- `Programações → Férias Cedidas...`

O mapa `ferias-cedidas-detalhe` é especificamente **Programação Coletiva de
Férias Cedidas — Inclusão**. Não representa automaticamente todo o fluxo de
inclusão individual. Seu botão foi declarado como `Iniciar Processo`.

Cada mapa tem uma árvore JSON e uma tabela Markdown. São preservados nomes,
classes, legendas, campos de dados declarados, ordem de tabulação e alguns
eventos. Textos de campos, conexões, SQL interno e imagens binárias são omitidos.

**Não são seletores de execução já validados.** O nome Delphi de um componente
não é automaticamente `automation_id`, e componentes herdados podem ter
propriedades no formulário ancestral. A visibilidade/habilitação pode ser
alterada pelo código do sistema. As posições são as do recurso, não coordenadas
para clicar numa tela atual.

## Pistas para a próxima validação real

- Ocorrências: `Edt_Contrato`, `Edt_Ocorrencia`, `Edt_DataInicio`,
  `Edt_HoraInicio` e os controles de término. Há ações coletivas separadas.
- Férias: seleção de contrato, início, término, dias de gozo e autorização;
  abas/controles de programação coletiva aparecem no recurso.
- O rótulo de afastamento para INSS no formulário de ocorrências não comprova
  qual tipo é importado pelo serviço para o Acessus. Essa regra continua pendente.
- As rotas em `src/automatiza/rh.py` usam os menus e classes declarados aqui;
  ainda não foram executadas nas janelas reais.

## Reextrair depois de uma atualização

```powershell
.\.venv\Scripts\automatiza.exe mapear-delphi --arquivo C:\meta\rhsis\RHForms.bpl --classe TFrm_RH0540RegOcorrencias --saida .\docs\mapeamentos\rh\registro-ocorrencias.json
```

O leitor aceita os tipos encontrados nesta instalação e recusa dados truncados
ou tipos desconhecidos. Não é um descompilador de regras de negócio.

Referência do formato de flags: [Embarcadero — TFilerFlag](https://docwiki.embarcadero.com/Libraries/Athens/en/System.Classes.TFilerFlag).
