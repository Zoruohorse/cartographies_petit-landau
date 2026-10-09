import json
from pathlib import Path
root=Path(__file__).resolve().parent
load=lambda p:json.loads((root/p).read_text(encoding='utf-8'))
a=load('data/actors.json');c=load('data/claims.json');e=load('data/evidence.json');r=load('data/relations.json');s=load('data/sources.json');syn=load('data/synthesis.json');t=load('config/taxonomy.json');m=load('data/meta.json')
assert m['id']=='project_petit_landau'
A={x['id'] for x in a};E={x['id'] for x in e};S={x['id'] for x in s}
for ds in (a,c,e,r,s):assert len({x['id'] for x in ds})==len(ds),'Identifiant dupliqué'
assert m['id'] in A
assert len(a)==31 and len(r)==31 and len(c)==28 and len(e)==25 and len(s)==7
assert sum(x.get('display_in_cards',True) for x in a)==28
assert len([x for x in r if x['status']=='reported_in_provided_network'])==24
assert len([x for x in r if x['status']=='contextual_from_provided_actor_cards'])==7
assert len(syn['griefs'])==11 and len(syn['vigilance'])==16 and len(syn['sources'])==7
for x in a:assert all(cat in t['categories'] for cat in x['categories'])
for x in c:assert x['subject_id'] in A and set(x['evidence_ids'])<=E and x['value'] in t['stances'] and x['certainty'] in t['certainty_levels']
for x in e:assert x['source_id'] is None or x['source_id'] in S
for x in r:assert x['source_id'] in A and x['target_id'] in A and x['type'] in t['relation_types'] and set(x['evidence_ids'])<=E
assert sum(not x['evidence_ids'] for x in c)==3
print(f'VALIDATION OK: {len(a)} nœuds, {len(r)} relations, {len(c)} fiches, {len(e)} preuves, {len(s)} sources, 3 onglets')
