"""Cobre tipos ativos em contrato sint?tico pela interface; sem inser??o SQL."""
import json,time
from pathlib import Path
from datetime import datetime,timedelta
from dataclasses import replace
from pywinauto import Desktop,keyboard,mouse
from automatiza.config import Settings
from automatiza.database import SqlServer
OUT=Path(__file__).resolve().parents[1]/'reports/integracao-api/20261020'
def field(f,cls,left):
 values=[c for c in f.descendants() if c.is_visible() and c.class_name()==cls and c.rectangle().left==left]
 if len(values)!=1:raise RuntimeError('Campo ambiguo '+cls+str(left))
 return values[0]
def fill(c,value):
 c.click_input();keyboard.send_keys('{HOME}+{END}{DELETE}'+value+'{TAB}',pause=.07);time.sleep(.2)
def main():
 db=SqlServer(replace(Settings.load(),sql_database='RHFagundes'))
 root=Desktop(backend='win32').window(class_name='TFrm_RHPA0010').wrapper_object();f=[c for c in root.descendants() if c.class_name()=='TFrm_RHPA5020' and c.is_visible()][0]
 if field(f,'TEdit',65).window_text()!='4':raise RuntimeError('Contrato mudou')
 types=db.query("SELECT OCORRENCIA,DESCRICAO40,GERAAFASTAMENTO,GERAAFASTAMENTOPONTO FROM RHOCORRENCIAS WHERE ATIVADESATIVADA='1' AND (GERAAFASTAMENTO='S' OR GERAAFASTAMENTOPONTO='S') AND OCORRENCIA NOT IN ('011','013') ORDER BY OCORRENCIA")
 for i,kind in enumerate(types):
  if kind['OCORRENCIA']<'017':continue
  date=datetime(2027,4,1)+timedelta(days=i*7);key='OT-'+kind['OCORRENCIA'];case={**kind,'id':key,'inicio':date.isoformat(),'termino':date.isoformat(),'expectativa':'Caso de limite de um dia; registrar aceitacao/rejeicao do RH. Se salvo, conferir API e filtro de vigencia no destino.'}
  (OUT/(key+'-planejado.json')).write_text(json.dumps(case,ensure_ascii=False,indent=2),encoding='utf-8')
  fill(field(f,'TEdit',16),kind['OCORRENCIA']);fill(field(f,'TMaskEdit',519),date.strftime('%d%m%Y'));fill(field(f,'TDBEdit',731),date.strftime('%d%m%Y'))
  inss=[c for c in f.descendants() if c.is_visible() and c.class_name()=='TDBComboMeta' and c.rectangle().left==174]
  if inss:
   inss[0].click_input();keyboard.send_keys('{HOME}{TAB}',pause=.1)
  mouse.click(coords=(10,55));time.sleep(.6)
  modals=[w for w in Desktop(backend='win32').windows() if w.is_visible() and w.class_name() in ['TMessageForm','TFrm_Erro']]
  if modals:
   for j,w in enumerate(modals):w.capture_as_image().save(str(OUT/(key+'-aviso-'+str(j)+'.png')))
   print(json.dumps({'caso':key,'estado':'DIALOGO_REQUER_INSPECAO','handles':[w.handle for w in modals]}),flush=True);return
  rows=db.query("SELECT OCORRENCIA,DATAINICIOOCORRENCIA,DATATERMINOOCORRENCIA,NROHORASOCORRENCIA FROM RHREGOCORRENCIAS WHERE UNIDADE='0004' AND CONTRATO=4 AND OCORRENCIA=? AND DATAINICIOOCORRENCIA=?",(kind['OCORRENCIA'],date))
  (OUT/(key+'-origem.json')).write_text(json.dumps(rows,default=str,indent=2),encoding='utf-8');print(json.dumps({'caso':key,'salvo':len(rows)==1}),flush=True)
  if len(rows)!=1:raise RuntimeError('Persistencia nao confirmada; interrompido sem avancar')
if __name__=='__main__':main()
