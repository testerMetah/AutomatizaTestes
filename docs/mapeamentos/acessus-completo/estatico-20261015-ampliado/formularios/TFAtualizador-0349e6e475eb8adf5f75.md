# TFAtualizador

Mapa estático, sem validação em execução.

| Caminho Delphi | Classe | Legenda | Campo | Ação/evento |
|---|---|---|---|---|
| /FAtualizador | TFAtualizador | Atualizador do Sistema Accessus |  |  |
| /FAtualizador/lblStatus | TLabel | Iniciando a Instalação... |  |  |
| /FAtualizador/memLista | TMemo |  |  |  |
| /FAtualizador/pbProgresso | TProgressBar |  |  |  |
| /FAtualizador/BtnFechar | TButton | Fechar |  | BtnFecharClick |
| /FAtualizador/Timer1 | TTimer |  |  |  |
| /FAtualizador/CdsRelErros | TClientDataSet |  |  |  |
| /FAtualizador/CdsRelErros/CdsRelErrosID | TIntegerField |  |  |  |
| /FAtualizador/CdsRelErros/CdsRelErrosVERSAO | TStringField |  |  |  |
| /FAtualizador/CdsRelErros/CdsRelErrosSTATUS | TStringField |  |  |  |
| /FAtualizador/CdsRelErros/CdsRelErrosDATAHORA | TSQLTimeStampField |  |  |  |
| /FAtualizador/CdsRelErros/CdsRelErrosEXECUTADOCOMERROS | TBooleanField |  |  |  |
| /FAtualizador/frxRelInfoScripts | TfrxReport |  |  |  |
| /FAtualizador/frxRelInfoScripts/Data | TfrxDataPage |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1 | TfrxReportPage |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1/ReportTitle1 | TfrxReportTitle |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1/ReportTitle1/Memo2 | TfrxMemoView |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1/MasterData1 | TfrxMasterData |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1/MasterData1/frxDBInfoScriptsID | TfrxMemoView |  | ID |  |
| /FAtualizador/frxRelInfoScripts/Page1/MasterData1/frxDBInfoScriptsDATAHORA | TfrxMemoView |  | DATAHORA |  |
| /FAtualizador/frxRelInfoScripts/Page1/MasterData1/frxDBInfoScriptsVERSAO | TfrxMemoView |  | VERSAO |  |
| /FAtualizador/frxRelInfoScripts/Page1/MasterData1/frxDBInfoScriptsSTATUS | TfrxMemoView |  | STATUS |  |
| /FAtualizador/frxRelInfoScripts/Page1/PageHeader1 | TfrxPageHeader |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1/PageHeader1/Memo1 | TfrxMemoView |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1/PageHeader1/Memo4 | TfrxMemoView |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1/PageHeader1/Memo5 | TfrxMemoView |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1/PageHeader1/Memo6 | TfrxMemoView |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1/Footer1 | TfrxFooter |  |  |  |
| /FAtualizador/frxRelInfoScripts/Page1/Footer1/Memo7 | TfrxMemoView |  |  |  |
| /FAtualizador/frxDBInfoScripts | TfrxDBDataset |  |  |  |
| /FAtualizador/QryParametros | TFDQuery |  |  |  |
| /FAtualizador/CON_FireDac | TFDConnection |  |  |  |
