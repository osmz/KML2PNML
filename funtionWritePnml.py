import xml.etree.ElementTree as ET

import funtionDrawPlace as DPlace
import funtionDrawTransition as DTransition
import funtionDrawArrowOut as DArrowOut
import funtionDrawArrowInt as DArrowInt

def write_Pnml(list_Goal, auxParaFor, quant_Transition, ToRefineAnd, ToRefineOr, list_Vector, list_Connection, list_Transition):
    # Father of the network - has children
    pnml = ET.Element('pnml')

    # Son 1
    net = ET.SubElement(pnml, 'net')
    net.set('id', 'Net-One')
    net.set('type', 'P/T net')

    # Son 1.1
    token = ET.SubElement(net, 'token')
    token.set('id', 'Default')
    token.set('enabled', 'true')
    token.set('red', '0')
    token.set('green', '0')
    token.set('blue', '0')

    # Initialize the position variables of the places
    starting_Position_X_Place = 200.0
    starting_Position_Y_Place = 200.0  

    # For to create all elements Place
    for index in range(auxParaFor - 1, -1, -1):
        DPlace.draw_Place(net, list_Goal, index, starting_Position_X_Place, starting_Position_Y_Place)

        # Increase the positions
        starting_Position_X_Place += 50.0
        starting_Position_Y_Place += 50.0
    
    # Initialize the position variables of the Transition
    starting_Position_X_Transition = 400.0
    starting_Position_Y_Transition = 200.0 

    # For to create all elements Transition
    for index in range(quant_Transition):
        DTransition.draw_Transition(net, index, starting_Position_X_Transition, starting_Position_Y_Transition)

        # Increase the positions
        starting_Position_X_Transition += 100.0
        starting_Position_Y_Transition += 100.0
    
    # For to create all elements Arc
    for index in range(len(ToRefineAnd)):
        if ToRefineAnd[index] != 'NONE' and ToRefineOr[index] == 'NONE':
            print('Posicion 1')
            list_Type = 'ToRefineAnd'
            DArrowOut.draw_Arrow_Out(list_Type, ToRefineAnd , ToRefineOr, index, net, list_Vector, list_Transition, list_Goal)
            print('index teste')
            print(index)
            DArrowInt.draw_Arrow_Int(list_Type, ToRefineAnd, ToRefineOr, index, list_Vector, net, list_Transition)
        
        elif ToRefineAnd[index] != 'NONE' and ToRefineOr[index] != 'NONE':
            if ToRefineAnd[index] != 'NONE':
                print('Posicion 2')      
                list_Type = 'ToRefineAnd'          
                DArrowOut.draw_Arrow_Out(list_Type, ToRefineAnd, ToRefineOr, index, net, list_Vector, list_Transition, list_Goal)
                print('index teste 2')
                print(index)
                DArrowInt.draw_Arrow_Int(list_Type, ToRefineAnd, ToRefineOr, index, list_Vector, net, list_Transition)
            
            if ToRefineOr[index] != 'NONE':
                print('Posicion 3')    
                list_Type = 'ToRefineOr'            
                DArrowOut.draw_Arrow_Out(list_Type, ToRefineAnd, ToRefineOr, index, net, list_Vector, list_Transition, list_Goal)
                print('index teste 3')
                print(index)
                DArrowInt.draw_Arrow_Int(list_Type, ToRefineAnd, ToRefineOr, index, list_Vector, net, list_Transition)
        
        elif ToRefineAnd[index] == 'NONE' and ToRefineOr[index] != 'NONE':
            print('Posicion 4')
            list_Type = 'ToRefineOr'            
            DArrowOut.draw_Arrow_Out(list_Type, ToRefineAnd, ToRefineOr, index, net, list_Vector, list_Transition, list_Goal)
            print('index teste 4')
            print(index)
            DArrowInt.draw_Arrow_Int(list_Type, ToRefineAnd, ToRefineOr, index, list_Vector, net, list_Transition)  

    return pnml