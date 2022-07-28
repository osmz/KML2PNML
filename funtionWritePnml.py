import xml.etree.ElementTree as ET

import funtionDrawPlace as DPlace
import funtionDrawTransition as DTransition
import funtionDrawArrowOut as DArrowOut
import funtionDrawArrowInt as DArrowInt

def write_Pnml(helper_For_Goal_Size, list_Goal, quant_Transition, input_Vector_List, list_Transition, output_Vector_List, Id):
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

    # For to create all elements Place
    for index in range(helper_For_Goal_Size - 1, -1, -1):
        DPlace.draw_Place(net, list_Goal, index)

    # For to create all elements Transition
    for index in range(quant_Transition):
        DTransition.draw_Transition(net, index, input_Vector_List, output_Vector_List, Id, list_Goal, list_Transition)
    
    # For to create all elements Arc
    for index in range(len(input_Vector_List)): 
        DArrowOut.draw_Arrow_Out(list_Transition, index, net, output_Vector_List)
        DArrowInt.draw_Arrow_Int(net, input_Vector_List, index, list_Transition)

    return pnml