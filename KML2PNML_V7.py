from tkinter import END
from turtle import end_fill
from numpy import transpose
import pandas as pd
import xml.etree.ElementTree as ET

import funtionCalculateQuantifyTransition as CQT
import funtionWriteXml as WXml
import funtionWritePnml as WPnml
import funtionWriteFileXml as WFXml

from xml.etree.ElementTree import parse
''' document = parse('Oscar5.kml') '''
document = parse('test.kml')
''' document = parse('Monitor_Night_Sleep.kml') ''' 
root = document.getroot()

# Define the classes.

class GOAL:
    def __init__(self, id, name,  type, positionX, positionY):
        self.id = id
        self.name = name
        self.type = type
        self.positionX = positionX
        self.positionY = positionY
    
    def goal_Id(self):
        return self.id
    
    def goal_Name(self):
        return self.name

    def goal_Type(self):
        return self.type
    
    def goal_PositionX(self):
        return self.positionX

    def goal_PositionY(self):
        return self.positionY

class OPERATION:
    def __init__(self, id, precondition, postcondition, type, positionX, positionY):
        self.id = id
        self.precondition = precondition
        self.postcondition = postcondition
        self.type = type
        self.positionX = positionX
        self.positionY = positionY
    
    def operation_Id(self):
        return self.id
    
    def operation_Precondition(self):
        return self.precondition
    
    def operation_Postcondition(self):
        return self.postcondition
    
    def operation_Type(self):
        return self.type
    
    def operation_PositionX(self):
        return self.positionX

    def operation_PositionY(self):
        return self.positionY

# Initialize the empty lists of each tag.

Model                  = []
Id                     = []
Name                   = []
Type                   = []
Pattern                = []
Class                  = []
Precondition           = [] 
Postcondition          = [] 

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

list_Goal              = list()
list_Operation         = list()
list_Object            = list()
list_Responsability    = list()

input_Vector_List      = []
list_Connection        = []
list_Type              = []
list_Transition        = []
output_Vector_List     = []

# FOR to iterate through each element, find the first children and take their values. For those who are children of children add an empty space, because you can not access them.

for item in document.iterfind('Element'):
    Model.append(item.findtext('Model'))
    Id.append(item.findtext('Id'))
    Name.append(item.findtext('Name'))
    Type.append(item.findtext('Type'))
    Pattern.append(item.findtext('Pattern'))
    Class.append(item.findtext('Class'))
    Precondition.append(item.findtext('Precondition'))
    Postcondition.append(item.findtext('Postcondition'))

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
        if elemento.tag == 'Operationalizationof':
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

df = pd.DataFrame({'Model':Model, 'Id':Id, 'Name':Name, 'Type':Type, 'Pattern':Pattern, 'Class':Class, 'Precondition':Precondition, 'Postcondition':Postcondition,'ToRefineAnd':ToRefineAnd, 'InRefineAnd':InRefineAnd, 'ToRefineOr':ToRefineOr, 'InRefineOr':InRefineOr, 'ConflictTo':ConflictTo, 'Resolution':Resolution, 'Obstrution':Obstrution, 'ExpectationOf':ExpectationOf, 'ConcernsTo':ConcernsTo, 'AssociateTo':AssociateTo, 'IsA':IsA, 'AssignedTo':AssignedTo, 'ResponsabilityOf':ResponsabilityOf, 'CauseTo':CauseTo, 'InputTo':InputTo, 'OutputTo':OutputTo, 'OutputTo':OutputTo, 'PerformanceOf':PerformanceOf, 'OperationalizationOf':OperationalizationOf, 'Height':Height, 'Widtht':Widtht, 'PositionX':PositionX, 'PositionY':PositionY}) 

''' df = transpose(df) '''

print(df)
print('')
print('Dados de prueba')
print()

# Created object

df_Goal = df.where(df['Model']=='Goal')
df_Operation = df.where(df['Model']=='Operation')
df_Object = df.where(df['Model']=='Object')
df_Responsability = df.where(df['Model']=='Responsability')

for index, row in df_Goal.iterrows():
    if df_Goal.loc[index][0] == 'Goal':
        Goal = GOAL(row['Id'], row['Name'], row['Type'], row['PositionX'], row['PositionY'])
        list_Goal.append(Goal)

helper_For_Goal_Size = len(list_Goal)

for index, row in df_Operation.iterrows():
    if df_Operation.loc[index][0] == 'Operation':
        Operation = OPERATION(row['Id'], row['Precondition'], row['Postcondition'], row['Type'], row['PositionX'], row['PositionY'])
        list_Operation.append(Operation)

# Calculate the vector for the transitions

cont_Transition = CQT.calculate_Quantify_Transition(Id, ToRefineAnd, ToRefineOr, input_Vector_List, list_Connection, list_Type, list_Transition, list_Goal, output_Vector_List, ExpectationOf)

df_Transition = pd.DataFrame({'Input Vector List':input_Vector_List, 'List Connection':list_Connection, 'List Type':list_Type, 'List Transition':list_Transition, 'Output Vector List':output_Vector_List})

print(df_Transition)

# Calculate the number of transitions

quant_Transition = cont_Transition
''' print('quant_Transition')
print(quant_Transition) '''

# Write .xml file

xml_pnml = ET.tostring(WXml.write_Xml()) 
pnml_pnml = ET.tostring(WPnml.write_Pnml(helper_For_Goal_Size, list_Goal, quant_Transition, input_Vector_List, output_Vector_List, Id, list_Transition, ToRefineAnd, ToRefineOr, ExpectationOf, OperationalizationOf, list_Operation))

with open("Monitor_Night_Sleep.xml", "wb") as f: 
    f.write(xml_pnml)
    f.write(pnml_pnml)
    f.close() 

WFXml.write_File_Xml()

# Space for test codes

''' df = transpose(df)
print(df[6:8]) '''

print('Id')
print(Id)
print('ToRefineAnd')
print(ToRefineAnd)
print('ToRefineOr')
print(ToRefineOr)
print('ExpectationOf')
print(ExpectationOf)
print('OperationalizationOf')
print(OperationalizationOf)

print(list_Goal[3].goal_Id())

''' df = transpose(df)

print(ToRefineAnd)
print(df[0])
print(ToRefineOr[0])
cadena = ToRefineOr[0]
separador = ';'
separador = cadena.split(separador)
print(separador)
print(separador[0])
print(Id) '''

''' cadena = ToRefineAnd[1]
separador = ';'
separador = cadena.split(separador)
print(separador[1]) '''

''' indice_test = ToRefineOr.index('21')
ToRefineOr[indice_test] = '21' + '-Ok'
print('indice_test')
print(ToRefineOr) '''

''' df_Transition = pd.DataFrame({'Input Vector List':input_Vector_List, 'List Connection':list_Connection, 'List Transition':list_Transition, 'Output Vector List':output_Vector_List})

print(df_Transition) '''

''' print(list_Goal[0].goal_Id())
print(list_Goal[0].goal_PositionX())
print(list_Goal[0].goal_PositionY()) '''

''' print(ToRefineAnd[13])
print(ToRefineOr[13])
print(ExpectationOf[13]) '''

''' print(len(ToRefineAnd))
print(len(Precondition))
print(Postcondition)
print(OperationalizationOf)
print(len(OperationalizationOf)) '''

''' lst = Id
indice = lst.index('258191')
print(indice)
print(list_Transition.pop()) '''

''' print(df_Transition[0:60])
 '''
