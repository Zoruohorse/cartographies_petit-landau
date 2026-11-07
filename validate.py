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
