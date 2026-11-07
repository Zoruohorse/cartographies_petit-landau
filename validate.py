#!/usr/bin/env python3
import json
from pathlib import Path
r=Path(__file__).resolve().parent
j=lambda p:json.loads((r/p).read_text(encoding='utf-8'))
a,c,x,e,s=[j('data/'+k+'.json') for k in ('actors','claims','relations','evidence','sources')]
syn=j('data/synthesis.json');cont=j('data/content.json');tax=j('config/taxonomy.json')
ids=lambda seq:{v['id']:v for v in seq}
A,C,X,E,S=[ids(v) for v in (a,c,x,e,s)]
assert all(len(v)==len(ids(v)) for v in (a,c,x,e,s))
def prove(items):
 assert items
 for i in items:
  assert i in E and E[i]['source_id'] in S and S[E[i]['source_id']]['url'].startswith('https://')
for z in c:
 assert z['subject_id'] in A and z['value'] in tax['stances']
 prove(z['evidence_ids'])
for z in x:
 assert z['source_id'] in A and z['target_id'] in A and z['type'] in tax['relation_types']
 prove(z['evidence_ids'])
for t in ('griefs','vigilance'):
 for z in syn[t]:prove(z['evidence_ids'])
for t in ('milestones','fact_sheet'):
 for z in cont[t]:prove(z['evidence_ids'])
assert len(c)==len([v for v in a if v.get('display_in_cards')])
print('VALIDÉ',len(a),len(c),len(x),len(e),len(s))

# Vérification de la chronologie utilisée dans l'onglet « Évolution des acteurs ».
from datetime import date as _date
timeline = j('data/timeline.json')
config = tax['timeline']
assert len(timeline)==len(c), 'Un premier jalon par fiche visible est attendu'
assert len({t['actor_id'] for t in timeline})==len(timeline),'Doublon chronologique'
allowed={x['id'] for x in config['categories']}
for t in timeline:
 assert t['actor_id'] in A and t['actor_id']!=j('data/meta.json')['id']
 assert t['event_type']==config['event_type']
 assert t['date_precision']=='day'
 dt=_date.fromisoformat(t['date'])
 assert dt<=_date(2026,11,7),'Date future'
 assert t['source_ids'],'Jalon sans source'
 for sid in t['source_ids']:
  assert sid in S and S[sid]['url'].startswith('https://'),'Source manquante'
 assert A[t['actor_id']]['timeline_category'] in allowed,'Typologie invalide'
print('Évolution validée :',len(timeline),'acteurs datés')
