import pandas as pd

from xml.etree.ElementTree import parse
from numpy import transpose
document = parse('Monitor_Night_Sleep.kml') 
root = document.getroot()

# Define the classes.

class Test_class:
    def __init__(self):
        pass

    def sumandoValores(a,b):
        resultado =  a + b
        return resultado

class Place:
    def __init__(self, id, name):
        self.id = id
        self.name = name


# Initialize the empty lists of each tag.

Model                  = []
Id                     = []
Name                   = []
Type                   = []
Pattern                = []
Class                  = []

ToRefineAnd            = []  
InRefineAnd            = []
ToRefineOr             = []
InRefineOr             = []
ConflictTo             = [] 
Resolution             = [] 
Obstrution             = [] 
ExpectationOf          = [] 
ConcernsTo             = [] 
AssociateTo            = [] 
IsA                    = [] 
AssignedTo             = [] 
ResponsabilityOf       = [] 
CauseTo                = [] 
InputTo                = [] 
OutputTo               = [] 
PerformanceOf          = [] 
OperationalizationOf   = [] 

Height                 = []
Widtht                 = []
PositionX              = []
PositionY              = []

# FOR to iterate through each element, find the first children and take their values. For those who are children of children add an empty space, because you can not access them.

for item in document.iterfind('Element'):
    Model.append(item.findtext('Model'))
    Id.append(item.findtext('Id'))
    Name.append(item.findtext('Name'))
    Type.append(item.findtext('Type'))
    Pattern.append(item.findtext('Pattern'))
    Class.append(item.findtext('Class'))

    ToRefineAnd.append([])           
    InRefineAnd.append([])         
    ToRefineOr.append([])          
    InRefineOr.append([])          
    ConflictTo.append([])           
    Resolution.append([])           
    Obstrution.append([])           
    ExpectationOf.append([])        
    ConcernsTo.append([])           
    AssociateTo.append([])          
    IsA.append([])                  
    AssignedTo.append([])           
    ResponsabilityOf.append([])     
    CauseTo.append([])              
    InputTo.append([])              
    OutputTo.append([])             
    PerformanceOf.append([])        
    OperationalizationOf.append([]) 

    Height.append([])              
    Widtht.append([])              
    PositionX.append([])           
    PositionY.append([])           

# Create an auxiliary variable that allows us to store the value of the tag in the appropriate position.

aux_Len = 0
for nodo in root.iter('Refinements'):
    for elemento in nodo.iter():
        if elemento.tag == 'ToRefineAnd':
            ToRefineAnd[aux_Len] = elemento.text
        if elemento.tag == 'InRefineAnd':
            InRefineAnd[aux_Len] = elemento.text
        if elemento.tag == 'ToRefineOr':
            ToRefineOr[aux_Len] = elemento.text
        if elemento.tag == 'InRefineOr':
            InRefineOr[aux_Len] = elemento.text
        if elemento.tag == 'ConflictTo':
            ConflictTo[aux_Len] = elemento.text
        if elemento.tag == 'Resolution':
            Resolution[aux_Len] = elemento.text
        if elemento.tag == 'Obstrution':
            Obstrution[aux_Len] = elemento.text
        if elemento.tag == 'ExpectationOf':
            ExpectationOf[aux_Len] = elemento.text
        if elemento.tag == 'ConcernsTo':
            ConcernsTo[aux_Len] = elemento.text
        if elemento.tag == 'AssociateTo':
            AssociateTo[aux_Len] = elemento.text
        if elemento.tag == 'IsA':
            IsA[aux_Len] = elemento.text
        if elemento.tag == 'AssignedTo':
            AssignedTo[aux_Len] = elemento.text
        if elemento.tag == 'ResponsabilityOf':
            ResponsabilityOf[aux_Len] = elemento.text
        if elemento.tag == 'CauseTo':
            CauseTo[aux_Len] = elemento.text
        if elemento.tag == 'InputTo':
            InputTo[aux_Len] = elemento.text
        if elemento.tag == 'OutputTo':
            OutputTo[aux_Len] = elemento.text
        if elemento.tag == 'PerformanceOf':
            PerformanceOf[aux_Len] = elemento.text
        if elemento.tag == 'OperationalizationOf':
            OperationalizationOf[aux_Len] = elemento.text
    aux_Len = aux_Len + 1

aux_Len = 0
for nodo in root.iter('Graphics'):
    for elemento in nodo.iter():
        if elemento.tag == 'Height':
            Height[aux_Len] = elemento.text
        if elemento.tag == 'Widtht':
            Widtht[aux_Len] = elemento.text
    aux_Len = aux_Len + 1 

aux_Len = 0
for nodo in root.iter('Position'):
    for elemento in nodo.iter():
        if elemento.tag == 'x':
            PositionX[aux_Len] = elemento.text
        if elemento.tag == 'y':
            PositionY[aux_Len] = elemento.text 
    aux_Len = aux_Len + 1 

# FOR to replace empty spaces ([]) with the value of 'NONE'.

for i, value in enumerate(ToRefineAnd):
    if value == []:
        ToRefineAnd[i] = 'NONE'
for i, value in enumerate(InRefineAnd):
    if value == []:
        InRefineAnd[i] = 'NONE'
for i, value in enumerate(ToRefineOr):
    if value == []:
        ToRefineOr[i] = 'NONE'
for i, value in enumerate(InRefineOr):
    if value == []:
        InRefineOr[i] = 'NONE'
for i, value in enumerate(ConflictTo):
    if value == []:
        ConflictTo[i] = 'NONE'
for i, value in enumerate(Resolution):
    if value == []:
        Resolution[i] = 'NONE'
for i, value in enumerate(Obstrution):
    if value == []:
        Obstrution[i] = 'NONE'
for i, value in enumerate(ExpectationOf):
    if value == []:
        ExpectationOf[i] = 'NONE'
for i, value in enumerate(ConcernsTo):
    if value == []:
        ConcernsTo[i] = 'NONE'
for i, value in enumerate(AssociateTo):
    if value == []:
        AssociateTo[i] = 'NONE'
for i, value in enumerate(IsA):
    if value == []:
        IsA[i] = 'NONE'
for i, value in enumerate(AssignedTo):
    if value == []:
        AssignedTo[i] = 'NONE'
for i, value in enumerate(ResponsabilityOf):
    if value == []:
        ResponsabilityOf[i] = 'NONE'
for i, value in enumerate(CauseTo):
    if value == []:
        CauseTo[i] = 'NONE'
for i, value in enumerate(InputTo):
    if value == []:
        InputTo[i] = 'NONE'
for i, value in enumerate(OutputTo):
    if value == []:
        OutputTo[i] = 'NONE'
for i, value in enumerate(PerformanceOf):
    if value == []:
        PerformanceOf[i] = 'NONE'
for i, value in enumerate(OperationalizationOf):
    if value == []:
        OperationalizationOf[i] = 'NONE'

# Create the table.

df = pd.DataFrame({'Model':Model, 'Id':Id, 'Name':Name, 'Type':Type, 'Pattern':Pattern, 'Class':Class,'ToRefineAnd':ToRefineAnd, 'InRefineAnd':InRefineAnd, 'ToRefineOr':ToRefineOr, 'InRefineOr':InRefineOr, 'ConflictTo':ConflictTo, 'Resolution':Resolution, 'Obstrution':Obstrution, 'ExpectationOf':ExpectationOf, 'ConcernsTo':ConcernsTo, 'AssociateTo':AssociateTo, 'IsA':IsA, 'AssignedTo':AssignedTo, 'ResponsabilityOf':ResponsabilityOf, 'CauseTo':CauseTo, 'InputTo':InputTo, 'OutputTo':OutputTo, 'OutputTo':OutputTo, 'PerformanceOf':PerformanceOf, 'OperationalizationOf':OperationalizationOf, 'Height':Height, 'Widtht':Widtht, 'PositionX':PositionX, 'PositionY':PositionY}) 

df = transpose(df)

print(df)

# Trabalhando

Valor1=5
Valor2=10

if df[0][0] == 'Goal':
    Test_class()
    pedro = Test_class.sumandoValores(Valor1,Valor2)
    print(pedro)



