# Portaria: TFrmConfigEtiqueta

> Inventário estático do commit 28074dd. O comportamento atual e os seletores precisam de validação na UI. Rota: Ferramentas > Etiqueta.

- DFM: `Acesso/UFrmConfigEtiqueta.dfm`
- PAS: `Acesso/UFrmConfigEtiqueta.pas`
- Handler de abertura: `acConfEtiquetaExecute`

## Controles

| Nome | Classe | Tipo | Caption | TabOrder | Máscara | MaxLength | Padrão |
|---|---|---|---|---:|---|---:|---|
| FrmConfigEtiqueta | TFrmConfigEtiqueta | outro | Configuração de Etiqueta | — | — | — | Visible=True |
| PageControl | TPageControl | contêiner | — | 0 | — | — | — |
| TabGeral | TTabSheet | contêiner | Geral | — | — | — | — |
| gbConfiguracao | TGroupBox | contêiner | Configurações da Impressora | 0 | — | — | — |
| lbModelo | TLabel | rótulo | Modelo: | — | — | — | — |
| lbPorta | TLabel | rótulo | Porta: | — | — | — | — |
| lbAvanco | TLabel | rótulo | Avanço Etq: | — | — | — | — |
| lbDPI | TLabel | rótulo | DPI Impressora: | — | — | — | — |
| lbTemperatura | TLabel | rótulo | Temperatura: | — | — | — | — |
| lbBackFeed | TLabel | rótulo | BackFeed: | — | — | — | — |
| lbMargem | TLabel | rótulo | Margem Esquerda: | — | — | — | — |
| lbTemperatura2 | TLabel | rótulo | Velocidade: | — | — | — | — |
| lbBackFeed1 | TLabel | rótulo | Origem: | — | — | — | — |
| Label5 | TLabel | rótulo | Pag.codigo | — | — | — | — |
| cbModelo | TComboBox | seleção | — | 1 | — | — | — |
| cbPorta | TComboBox | seleção | — | 0 | — | — | Text=\\LOCALHOST\L42 |
| edAvanco | TEdit | campo de texto/data | — | 6 | — | — | — |
| cbDPI | TComboBox | seleção | — | 3 | — | — | — |
| edTemperatura | TEdit | campo de texto/data | — | 2 | — | — | Text=10 |
| cbBackFeed | TComboBox | seleção | — | 7 | — | — | — |
| edMargemEsquerda | TEdit | campo de texto/data | — | 4 | — | — | Text=10 |
| ckMemoria | TCheckBox | seleção | Limpar Memória | 10 | — | — | Checked=True |
| edVelocidade | TEdit | campo de texto/data | — | 5 | — | — | Text=-1 |
| cbOrigem | TComboBox | seleção | — | 9 | — | — | — |
| cbPagCodigo | TComboBox | seleção | — | 8 | — | — | — |
| bConfSalvar | TButton | ação | Salvar | 11 | — | — | — |
| bConfLer | TButton | ação | Ler | 12 | — | — | — |
| gbImagem | TGroupBox | contêiner | Carregar Imagem | 1 | — | — | — |
| Image1 | TImage | outro | — | — | — | — | — |
| lbNomeImg | TLabel | rótulo | Nome Imagem Memória | — | — | — | — |
| edNomeImg | TEdit | campo de texto/data | — | 0 | — | — | Text=ACESSUS |
| bCarregarImg | TButton | ação | Carregar Imagem | 1 | — | — | — |
| tabVisitante | TTabSheet | contêiner | Visitante | — | — | — | — |
| GroupBox1 | TGroupBox | contêiner | Imagem | 0 | — | — | — |
| Label1 | TLabel | rótulo | Mutiplicador | — | — | — | — |
| Label2 | TLabel | rótulo | Coluna | — | — | — | — |
| Label3 | TLabel | rótulo | Linha | — | — | — | — |
| EdImagemVisitanteMutiplicador | TEdit | campo de texto/data | — | 0 | — | — | Text=0 |
| EdImagemVisitanteColuna | TEdit | campo de texto/data | — | 1 | — | — | Text=4 |
| edtImagemVisitanteLinha | TEdit | campo de texto/data | — | 2 | — | — | Text=2 |
| GroupBox2 | TGroupBox | contêiner | Texto Visitante | 1 | — | — | — |
| Label4 | TLabel | rótulo | Mutiplicador Linha | — | — | — | — |
| Label6 | TLabel | rótulo | Posição Coluna | — | — | — | — |
| Label7 | TLabel | rótulo | Posição Linha | — | — | — | — |
| Label8 | TLabel | rótulo | Orientação | — | — | — | — |
| Label9 | TLabel | rótulo | Fonte | — | — | — | — |
| Label10 | TLabel | rótulo | Mutiplicador Coluna | — | — | — | — |
| Label11 | TLabel | rótulo | Sub. Fonte | — | — | — | — |
| Label12 | TLabel | rótulo | Texto | — | — | — | — |
| EdVisitanteMultipicadorLinha | TEdit | campo de texto/data | — | 0 | — | — | Text=21 |
| EdVisitantePosicaoColuna | TEdit | campo de texto/data | — | 1 | — | — | Text=10 |
| EdVisitantePosicaoLinha | TEdit | campo de texto/data | — | 2 | — | — | Text=50 |
| cbxVisitanteOrientacao | TComboBox | seleção | — | 3 | — | — | Text=Normal, ItemIndex=0 |
| cbxVisitanteFonte | TComboBox | seleção | — | 4 | — | — | Text=A, ItemIndex=0 |
| EdVisitanteMultipicadorColuna | TEdit | campo de texto/data | — | 5 | — | — | Text=21 |
| EdVisitanteSubFonte | TEdit | campo de texto/data | — | 6 | — | — | Text=0 |
| EdVisitanteTexto | TEdit | campo de texto/data | — | 7 | — | — | Text=VISITANTE |
| GroupBox4 | TGroupBox | contêiner | Nome do Visitante | 2 | — | — | — |
| Label21 | TLabel | rótulo | Mutiplicador Linha | — | — | — | — |
| Label22 | TLabel | rótulo | Posição Coluna | — | — | — | — |
| Label23 | TLabel | rótulo | Posição Linha | — | — | — | — |
| Label24 | TLabel | rótulo | Orientação | — | — | — | — |
| Label25 | TLabel | rótulo | Fonte | — | — | — | — |
| Label26 | TLabel | rótulo | Mutiplicador Coluna | — | — | — | — |
| Label27 | TLabel | rótulo | Sub. Fonte | — | — | — | — |
| Label28 | TLabel | rótulo | Texto | — | — | — | — |
| EdNomeVisitanteMultipicadorLinha | TEdit | campo de texto/data | — | 0 | — | — | Text=20 |
| EdNomeVisitantePosicaoColuna | TEdit | campo de texto/data | — | 1 | — | — | Text=18 |
| EdNomeVisitantePosicaoLinha | TEdit | campo de texto/data | — | 2 | — | — | Text=2 |
| cbxNomeVisitanteOrientacao | TComboBox | seleção | — | 3 | — | — | Text=Normal, ItemIndex=0 |
| cbxNomeVisitanteFonte | TComboBox | seleção | — | 4 | — | — | Text=D, ItemIndex=3 |
| EdNomeVisitanteMultipicadorColuna | TEdit | campo de texto/data | — | 5 | — | — | Text=20 |
| EdNomeVisitanteSubFonte | TEdit | campo de texto/data | — | 6 | — | — | Text=0 |
| EdNomeVisitanteTexto | TEdit | campo de texto/data | — | 7 | — | — | Text=NOME DO VISITANTE |
| GroupBox3 | TGroupBox | contêiner | Nome da Empresa do Visitante | 3 | — | — | — |
| Label13 | TLabel | rótulo | Mutiplicador Linha | — | — | — | — |
| Label14 | TLabel | rótulo | Posição Coluna | — | — | — | — |
| Label15 | TLabel | rótulo | Posição Linha | — | — | — | — |
| Label16 | TLabel | rótulo | Orientação | — | — | — | — |
| Label17 | TLabel | rótulo | Fonte | — | — | — | — |
| Label18 | TLabel | rótulo | Mutiplicador Coluna | — | — | — | — |
| Label19 | TLabel | rótulo | Sub. Fonte | — | — | — | — |
| Label20 | TLabel | rótulo | Texto | — | — | — | — |
| EdEmpresaVisitanteMultipicadorLinha | TEdit | campo de texto/data | — | 0 | — | — | Text=12 |
| EdEmpresaVisitantePosicaoColuna | TEdit | campo de texto/data | — | 1 | — | — | Text=22 |
| EdEmpresaVisitantePosicaoLinha | TEdit | campo de texto/data | — | 2 | — | — | Text=2 |
| cbxEmpresaVisitanteOrientacao | TComboBox | seleção | — | 3 | — | — | Text=Normal, ItemIndex=0 |
| cbxEmpresaVisitanteFonte | TComboBox | seleção | — | 4 | — | — | Text=C, ItemIndex=2 |
| EdEmpresaVisitanteMultipicadorColuna | TEdit | campo de texto/data | — | 5 | — | — | Text=12 |
| EdEmpresaVisitanteSubFonte | TEdit | campo de texto/data | — | 6 | — | — | Text=0 |
| EdEmpresaVisitanteTexto | TEdit | campo de texto/data | — | 7 | — | — | Text=Nome da Empresa |
| GroupBox5 | TGroupBox | contêiner | Nome do Responsável | 4 | — | — | — |
| Label29 | TLabel | rótulo | Mutiplicador Linha | — | — | — | — |
| Label30 | TLabel | rótulo | Posição Coluna | — | — | — | — |
| Label31 | TLabel | rótulo | Posição Linha | — | — | — | — |
| Label32 | TLabel | rótulo | Orientação | — | — | — | — |
| Label33 | TLabel | rótulo | Fonte | — | — | — | — |
| Label34 | TLabel | rótulo | Mutiplicador Coluna | — | — | — | — |
| Label35 | TLabel | rótulo | Sub. Fonte | — | — | — | — |
| Label36 | TLabel | rótulo | Texto | — | — | — | — |
| EdNomeResponsavelVisitanteMultipicadorLinha | TEdit | campo de texto/data | — | 0 | — | — | Text=12 |
| EdNomeResponsavelVisitantePosicaoColuna | TEdit | campo de texto/data | — | 1 | — | — | Text=27 |
| EdNomeResponsavelVisitantePosicaoLinha | TEdit | campo de texto/data | — | 2 | — | — | Text=2 |
| cbxNomeResponsavelVisitanteOrientacao | TComboBox | seleção | — | 3 | — | — | Text=Normal, ItemIndex=0 |
| cbxNomeResponsavelVisitanteFonte | TComboBox | seleção | — | 4 | — | — | Text=C, ItemIndex=2 |
| EdNomeResponsavelVisitanteMultipicadorColuna | TEdit | campo de texto/data | — | 5 | — | — | Text=12 |
| EdNomeResponsavelVisitanteSubFonte | TEdit | campo de texto/data | — | 6 | — | — | Text=0 |
| EdNomeResponavelVisitanteTexto | TEdit | campo de texto/data | — | 7 | — | — | Text=Responsável: Nome do Responsável |
| GroupBox6 | TGroupBox | contêiner | Caixa Mensagem | 5 | — | — | — |
| Label37 | TLabel | rótulo | Posicao Coluna | — | — | — | — |
| Label38 | TLabel | rótulo | Largura | — | — | — | — |
| Label39 | TLabel | rótulo | Altura | — | — | — | — |
| Label42 | TLabel | rótulo | Posição Linha | — | — | — | — |
| Label43 | TLabel | rótulo | Espessura Coluna | — | — | — | — |
| Label44 | TLabel | rótulo | Espessura Linha | — | — | — | — |
| Label40 | TLabel | rótulo | Arrendondar Canto | — | — | — | — |
| EdCaixaVisitantePosicaoColuna | TEdit | campo de texto/data | — | 0 | — | — | Text=31 |
| EdCaixaVisitanteLargura | TEdit | campo de texto/data | — | 1 | — | — | Text=80 |
| EdCaixaVisitanteAltura | TEdit | campo de texto/data | — | 2 | — | — | Text=6 |
| EdCaixaVisitantePosicaoLinha | TEdit | campo de texto/data | — | 3 | — | — | Text=0 |
| EdCaixaVisitanteEspessuraColuna | TEdit | campo de texto/data | — | 4 | — | — | Text=6 |
| EdCaixaVisitanteEspessuraLinha | TEdit | campo de texto/data | — | 5 | — | — | Text=0 |
| EdCaixaVisitanteArrendondarCanto | TEdit | campo de texto/data | — | 6 | — | — | Text=0 |
| GroupBox7 | TGroupBox | contêiner | Mensagem | 6 | — | — | — |
| Label41 | TLabel | rótulo | Mutiplicador Linha | — | — | — | — |
| Label45 | TLabel | rótulo | Posição Coluna | — | — | — | — |
| Label46 | TLabel | rótulo | Posição Linha | — | — | — | — |
| Label47 | TLabel | rótulo | Orientação | — | — | — | — |
| Label48 | TLabel | rótulo | Fonte | — | — | — | — |
| Label49 | TLabel | rótulo | Mutiplicador Coluna | — | — | — | — |
| Label50 | TLabel | rótulo | Sub. Fonte | — | — | — | — |
| Label51 | TLabel | rótulo | Texto | — | — | — | — |
| EdMensagemVisitanteMultipicadorLinha | TEdit | campo de texto/data | — | 0 | — | — | Text=12 |
| EdMensagemVisitantePosicaoColuna | TEdit | campo de texto/data | — | 1 | — | — | Text=33 |
| EdMensagemVisitantePosicaoLinha | TEdit | campo de texto/data | — | 2 | — | — | Text=2 |
| cbxMensagemVisitanteOrientacao | TComboBox | seleção | — | 3 | — | — | Text=Normal, ItemIndex=0 |
| cbxMensagemVisitanteFonte | TComboBox | seleção | — | 4 | — | — | Text=D, ItemIndex=3 |
| EdMensagemVisitanteMultipicadorColuna | TEdit | campo de texto/data | — | 5 | — | — | Text=12 |
| EdMensagemVisitanteSubFonte | TEdit | campo de texto/data | — | 6 | — | — | Text=0 |
| EdMensagemVisitanteTexto | TEdit | campo de texto/data | — | 7 | — | — | Text=OBRIGATÓRIO APRESENTAR ETIQUETA NA SAÍDA |
| btnImprimirVisitante | TBitBtn | outro | Imprimir | 7 | — | — | — |
| OpenPictureDialog1 | TOpenPictureDialog | outro | — | — | — | — | — |

## Procedures relevantes da unit

A tabela aponta o código que precisa de leitura manual. A presença de uma chamada não confirma seu efeito sem analisar condições, controller e DAO.

| Procedure | Linha | Chamadas identificadas |
|---|---:|---|
| `bConfSalvarClick` | 383 | — |
| `FormCreate` | 489 | `TConfigEtiquetaController.Create`, `FConfigEtiquetaController.AcbrEtiqueta` |
| `GravarParametros` | 583 | — |

## Mensagens literais da unit

Mensagens concatenadas podem conter partes dinâmicas; conferir a procedure antes de criar asserção.

- Linha 215: `Defina um nome para a Imagem`
- Linha 252: `Imagem `

## Pendente

Ler procedures, controllers e DAOs para Salvar, Consultar, Excluir, Cancelar e Relatório; conferir controles no build instalado.
