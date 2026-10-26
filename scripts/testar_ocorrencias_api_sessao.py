"""Casos autorizados na sess?o RHFagundes, contrato sint?tico 0004/4.
Handles desta sess?o: interromper se a janela ou o contrato mudar.
"""
import json,time,win32gui
from pathlib import Path
from dataclasses import replace
from pywinauto import Desktop
from pywinauto.controls.win32_controls import ComboBoxWrapper
from automatiza.config import Settings
from automatiza.database import SqlServer
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'reports/integracao-api/20261020'
FIELDS={'codigo':198226,'inicio':329106,'hora_inicio':132700,'termino':132704,'hora_termino':132706,'medicao':5113016}
def edit(key,value):
    e=Desktop(backend='win32').window(handle=FIELDS[key]).wrapper_object()
    if not e.is_visible() or not e.is_enabled():raise RuntimeError('Campo indisponivel: '+key)
    e.type_keys('{HOME}+{END}{DELETE}'+value+'{TAB}',pause=.08)
    time.sleep(.15)
def main():
    root=Desktop(backend='win32').window(class_name='TFrm_RHPA0010').wrapper_object()
    contract=Desktop(backend='win32').window(handle=132708).wrapper_object()
    if contract.window_text()!='4':raise RuntimeError('Contrato mudou')
    src=SqlServer(replace(Settings.load(),sql_database='RHFagundes'))
    cases=[
      {'id':'O03','codigo':'011','medicao':'Dias','inicio':'20102026','termino':'21102026'},
      {'id':'O04','codigo':'011','medicao':'Dias','inicio':'10102026','termino':'11102026'},
      {'id':'O05','codigo':'011','medicao':'Dias','inicio':'30112026','termino':'02122026'},
      {'id':'O06','codigo':'013','medicao':'Faixa Horas','inicio':'04112026','termino':'05112026','hora_inicio':'2330','hora_termino':'0130'},
      {'id':'O07','codigo':'013','medicao':'Horas/Dia','inicio':'06112026','termino':'08112026','duracao':'0430'},
    ]
    for case in cases:
      (OUT/(case['id']+'-planejado.json')).write_text(json.dumps(case,indent=2),encoding='utf-8')
      edit('codigo',case['codigo'])
      combo=Desktop(backend='win32').window(handle=FIELDS['medicao']).wrapper_object()
      if combo.is_enabled():ComboBoxWrapper(combo.element_info).select(case['medicao']);combo.type_keys('{TAB}')
      elif case['medicao']!='Dias':raise RuntimeError('Medicao fixa em Dias')
      edit('inicio',case['inicio'])
      if 'hora_inicio' in case:edit('hora_inicio',case['hora_inicio'])
      edit('termino',case['termino'])
      if 'hora_termino' in case:edit('hora_termino',case['hora_termino'])
      if 'duracao' in case:
        duration=[c for c in root.descendants() if c.class_name()=='TDBEdit' and c.is_visible() and 660<=c.rectangle().left<=675]
        if len(duration)!=1:raise RuntimeError('Duracao ambigua')
        duration[0].type_keys('{HOME}+{END}{DELETE}'+case['duracao']+'{TAB}',pause=.08)
      win32gui.PostMessage(root.handle,0x111,9,0)
      time.sleep(1)
      rows=src.query("SELECT UNIDADE,CONTRATO,OCORRENCIA,DATAINICIOOCORRENCIA,DATATERMINOOCORRENCIA,NROHORASOCORRENCIA FROM RHREGOCORRENCIAS WHERE UNIDADE='0004' AND CONTRATO=4 ORDER BY DATAINICIOOCORRENCIA")
      (OUT/(case['id']+'-origem.json')).write_text(json.dumps(rows,default=str,indent=2),encoding='utf-8')
      target=case['inicio'][4:]+'-'+case['inicio'][2:4]+'-'+case['inicio'][:2]
      matching=[r for r in rows if r['OCORRENCIA']==case['codigo'] and str(r['DATAINICIOOCORRENCIA']).startswith(target)]
      print(json.dumps({'caso':case['id'],'salvo_origem':len(matching)==1},ensure_ascii=True),flush=True)
      if len(matching)!=1:raise RuntimeError('Salvar nao confirmado; interromper')
if __name__=='__main__':main()
