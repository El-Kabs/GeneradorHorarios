import json
import itertools, operator

data = ''

with open('./courses.json', 'r', encoding="utf8") as f:
    data = json.load(f)
    data = data['records']

for x in data:
    x['curso'] = x['class']+x['course']

cursos = input('Nombre curso: ')

arr = cursos.split(',')

arrMaterias = []

for x in arr:
    aux = []
    for b in data:
        if(x==b['curso']):
            aux.append(b)
    arrMaterias.append(aux)
    aux = []

nArr = list(itertools.product(*arrMaterias))

def conflictosHorario(combinaciones):
    print(len(combinaciones))

conflictosHorario(nArr)

