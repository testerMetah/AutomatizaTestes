"""Casos reais autorizados em RHFagundes; handles da sess?o atual."""
import json,time,win32gui
from pathlib import Path
from dataclasses import replace
from pywinauto import Desktop,mouse
from pywinauto.controls.win32_controls import ComboBoxWrapper
from automatiza.config import Settings
from automatiza.database import SqlServer
OUT=Path(__file__).resolve().parents[1]/'reports/integracao-api/20261020'
def main():
 root=Desktop(backend='win32').window(class_name='TFrm_RHPA0010').wrapper_object()
 if Desktop(backend='win32').window(handle=2229512).window_text()!='4':raise RuntimeError('Contrato mudou')
 db=SqlServer(replace(Settings.load(),sql_database='RHFagundes'))
 cases=[('R02','19102026','19102026','0066','Reserva'),('R03','21102026','21102026','0055','Reserva'),('R04','23102026','25102026','0077','Reserva'),('R05','30112026','02122026','0066','Reserva'),('R06','31122026','02012027','0055','Reserva'),('R07','20102026','20102026','0077','Consumo')]
 for key,start,end,meal,kind in cases:
  (OUT/(key+'-planejado.json')).write_text(json.dumps({'id':key,'inicio_digitos':start,'termino_digitos':end,'refeicao':meal,'tipo':kind,'refeitorio':'666','cardapio':'456','expectativa':'Conferir origem/API/destino com datas exatas; consumo nao deve virar reserva'},indent=2),encoding='utf-8')
  mouse.click(coords=(22,611));time.sleep(.2)
  for h,v in [(394608,start),(394610,end)]:Desktop(backend='win32').window(handle=h).type_keys('{HOME}+{END}{DELETE}'+v+'{TAB}',pause=.07)
  c=Desktop(backend='win32').window(handle=4130022).wrapper_object();ComboBoxWrapper(c.element_info).select(kind);c.type_keys('{TAB}')
  for h,v in [(394612,'666'),(394614,meal),(329124,'456')]:Desktop(backend='win32').window(handle=h).type_keys('{HOME}+{END}{DELETE}'+v+'{TAB}',pause=.07)
  if kind=='Consumo':Desktop(backend='win32').window(handle=329126).type_keys('{HOME}+{END}{DELETE}2{TAB}',pause=.08)
  win32gui.PostMessage(root.handle,0x111,9,0);time.sleep(1)
  modals=[w for w in Desktop(backend='win32').windows() if w.is_visible() and w.class_name() in ['TMessageForm','TFrm_Erro']]
  if modals:raise RuntimeError('Dialogo requer inspecao: '+str([(w.handle,w.window_text()) for w in modals]))
  rows=db.query("SELECT UNIDADE,CONTRATO,NROORDEM,DATAINICIO,DATATERMINO,REFEICAO,CARDAPIO,TIPOREFEICAO,QUANTIDADECONSUMIDA,REFEITORIO FROM RHPROGRESERVACONSUMO WHERE UNIDADE='0004' AND CONTRATO=4 ORDER BY NROORDEM")
  (OUT/(key+'-origem.json')).write_text(json.dumps(rows,default=str,indent=2),encoding='utf-8');print(key,len(rows),flush=True)
if __name__=='__main__':main()
