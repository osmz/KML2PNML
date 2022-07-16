from numpy import transpose
import pandas as pd
import xml.etree.ElementTree as ET

import funtionCalculateQuantifyTransition as CQT
import funtionWriteXml as WXml
import funtionWritePnml as WPnml
import funtionWriteFileXml as WFXml

from xml.etree.ElementTree import parse
document = parse('Oscar3.kml') 
''' document = parse('oscar.kml') ''' 
''' document = parse('Monitor_Night_Sleep.kml') ''' 
root = document.getroot()

# Define the classes.

class Place:
    def __init__(self, id, name, off_X, off_Y, mark, capacity):
        self.id = id
        self.name = name
        self.off_X = off_X
        self.off_Y = -off_Y
        self.mark = mark
        self.capacity = capacity
    
    def place_Id(self):
        return self.id
    
    def place_Name(self):
        return self.name

    def place_Off_X(self):
        return self.off_X

    def place_Off_Y(self):
        return self.off_X

    def place_Mark(self):
        return self.mark

    def place_Capacity(self):
        return self.capacity

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

list_Goal              = list()
list_Operation         = list()
list_Object            = list()
list_Responsability    = list()

list_Vector            = []
list_Connection        = []
list_Transition        = []

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
print('')
print('Dados de prueba')
print()

# Created object

df_Goal = df.where(df['Model']=='Goal')
df_Operation = df.where(df['Model']=='Operation')
df_Object = df.where(df['Model']=='Object')
df_Responsability = df.where(df['Model']=='Responsability')

aux_Mark = 'Default, 0'

for index, row in df_Goal.iterrows():
    if df_Goal.loc[index][0] == 'Goal':
        Goal = Place(row['Id'], row['Name'], 30, -10, aux_Mark, 0)
        list_Goal.append(Goal)

auxParaFor = len(list_Goal)

# Calculate the vector for the transitions

cont_Transition = CQT.calculate_Quantify_Transition(ToRefineAnd, ToRefineOr, list_Vector, list_Connection, list_Transition)

df_Transition = pd.DataFrame({'List Vector':list_Vector, 'List Connection':list_Connection, 'List Transition':list_Transition})

print(df_Transition)

# Calculate the number of transitions

quant_Transition = cont_Transition

''' quant_Transition_ToRefineAnd = ToRefineAnd.count('NONE')
quant_Transition_ToRefineOR = 0
for index in range(len(ToRefineOr)):
    if ToRefineOr[index] != 'NONE':
        cadena = ToRefineOr[index]
        separador = ';'
        separador = cadena.split(separador)
        len_separador = len(separador)
        quant_Transition_ToRefineOR += len_separador

quant_Transition = (len(ToRefineAnd) - quant_Transition_ToRefineAnd) + quant_Transition_ToRefineOR
print('quant_Transition')
print(quant_Transition) '''

# Write .xml file

xml_pnml = ET.tostring(WXml.write_Xml()) 
pnml_pnml = ET.tostring(WPnml.write_Pnml(list_Goal, auxParaFor, quant_Transition, ToRefineAnd, ToRefineOr, list_Vector, list_Connection, list_Transition))

with open("Monitor_Night_Sleep.xml", "wb") as f: 
    f.write(xml_pnml)
    f.write(pnml_pnml)
    f.close() 

WFXml.write_File_Xml()

# Space for test codes

''' df = transpose(df)
print(df[4]) '''

print(Id)
print(Name)
print(InRefineAnd)
print(InRefineOr)
print(ToRefineAnd)
print(ToRefineOr)

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