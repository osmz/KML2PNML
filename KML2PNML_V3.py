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
    
    def place_Id(self):
        return self.id
    
    def place_Name(self):
        return self.name

class Transition:
    def __init__(self, name):
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

list_obj               = []

# FOR to iterate through each element, find the first children and take their values. For those who are children of children add an empty space, because you can not access them.

for item in document.iterfind('Element'):
    Model.append(item.findtext('Model'))
    Id.append(item.findtext('Id'))
    Name.append(item.findtext('Name'))
    Type.append(item.findtext('Type'))
    Pattern.append(item.findtext('Pattern'))
    Class.append(item.findtext('Class'))

    ToRefineAnd.append('NONE')           
    InRefineAnd.append('NONE')         
    ToRefineOr.append('NONE')          
    InRefineOr.append('NONE')          
    ConflictTo.append('NONE')           
    Resolution.append('NONE')           
    Obstrution.append('NONE')           
    ExpectationOf.append('NONE')        
    ConcernsTo.append('NONE')           
    AssociateTo.append('NONE')          
    IsA.append('NONE')                  
    AssignedTo.append('NONE')           
    ResponsabilityOf.append('NONE')     
    CauseTo.append('NONE')              
    InputTo.append('NONE')              
    OutputTo.append('NONE')             
    PerformanceOf.append('NONE')        
    OperationalizationOf.append('NONE') 

    Height.append('NONE')              
    Widtht.append('NONE')              
    PositionX.append('NONE')           
    PositionY.append('NONE')           

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

# Create the table.

df = pd.DataFrame({'Model':Model, 'Id':Id, 'Name':Name, 'Type':Type, 'Pattern':Pattern, 'Class':Class,'ToRefineAnd':ToRefineAnd, 'InRefineAnd':InRefineAnd, 'ToRefineOr':ToRefineOr, 'InRefineOr':InRefineOr, 'ConflictTo':ConflictTo, 'Resolution':Resolution, 'Obstrution':Obstrution, 'ExpectationOf':ExpectationOf, 'ConcernsTo':ConcernsTo, 'AssociateTo':AssociateTo, 'IsA':IsA, 'AssignedTo':AssignedTo, 'ResponsabilityOf':ResponsabilityOf, 'CauseTo':CauseTo, 'InputTo':InputTo, 'OutputTo':OutputTo, 'OutputTo':OutputTo, 'PerformanceOf':PerformanceOf, 'OperationalizationOf':OperationalizationOf, 'Height':Height, 'Widtht':Widtht, 'PositionX':PositionX, 'PositionY':PositionY}) 

''' df = transpose(df) '''

print(df)

# Trabalhando

Valor1=5
Valor2=10

if df.loc[0][0] == 'Goal':
    Test_class()
    pedro = Test_class.sumandoValores(Valor1,Valor2)
    print(pedro)

# Created object

print(' ')
print(df.loc[0][1])
print(df.loc[0][2])

numberOfElements = len(Model)
print(' ')
print(numberOfElements)

for i in range(numberOfElements):
    if df.loc[i][0] == 'Goal':
        obj_Place = Place(df.loc[i][1], df.loc[i][2])
        list_obj.append(obj_Place)

''' print(obj_Place) '''
print(len(list_obj))
print(list_obj)
''' print()
print(list_obj[6].place_Name())
print(list_obj[6].place_Id()) ''' 

''' for i in range(numberOfElements):
    print(df.loc[i][0]) '''
