import json
import itertools, operator

data = ''

#Abrir el archivo de cursos y asignarlo a la variable data
with open('./courses.json', 'r', encoding="utf8") as f:
    data = json.load(f)
    data = data['records']

#Agregar una llave a cada objeto para buscar más facil
#La llave es el departamento+el curso
#Ej: ADMI1101
for x in data:
    x['curso'] = x['class']+x['course']

#Input del usuario
#Cada curso debe estar seguido por coma sin espacios
#ISIS1001,ISIS1104,ISIS1105
cursos = input('Nombre curso: ')

#Split del input
arr = cursos.split(',')

arrMaterias = []

#Recorrido de los cursos para agregar todas las secciones de cada materia en ArrMaterias
for x in arr:
    aux = []
    for b in data:
        if(x==b['curso']):
            aux.append(b)
    arrMaterias.append(aux)
    aux = []

#Combinatoria de n cursos que esten en arrMaterias
nArr = list(itertools.product(*arrMaterias))

#Aun no hace nada este metodo xd
def conflictosHorario(combinaciones):
    print(len(combinaciones))

conflictosHorario(nArr)

