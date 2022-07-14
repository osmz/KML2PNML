import xml.etree.ElementTree as ET

import funtionDrawPlace as DPlace
import funtionDrawTransition as DTransition
import funtionDrawArrowOut as DArrowOut
import funtionDrawArrowInt as DArrowInt

def write_Pnml(list_Goal, auxParaFor, quant_Transition, ToRefineAnd, ToRefineOr):
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
            DArrowOut.draw_Arrow(net, index, list_Goal)
            cadena = ToRefineAnd[index]
            separador = ';'
            separador = cadena.split(separador)
            indice = ToRefineAnd.index(cadena)
            for index in range(len(separador)):
                DArrowInt.draw_Arrow_Int(net, separador, indice, index)

        elif ToRefineAnd[index] != 'NONE' and ToRefineOr[index] != 'NONE':
            if ToRefineAnd[index] != 'NONE':
                DArrowOut.draw_Arrow(net, index, list_Goal)
                cadena = ToRefineAnd[index]
                separador = ';'
                separador = cadena.split(separador)
                indice = ToRefineAnd.index(cadena)
                aux_indice = indice
                for aux_index in range(len(separador)):
                    DArrowInt.draw_Arrow_Int(net, separador, indice, aux_index)
                aux_indice += 1
                            
            if ToRefineOr[index] != 'NONE':
                cadena = ToRefineOr[index]
                separador = ';'
                separador = cadena.split(separador)
                for aux_index in range((index + 1), (index + 1) + len(separador), 1):
                    # Arc 1
                    # Son 1.4
                    arc = ET.SubElement(net, 'arc') 
                    arc.set('id', 'T' + str(aux_index) + ' to ' + list_Goal[index].place_Id())
                    arc.set('source', 'T' + str(aux_index))
                    arc.set('target', list_Goal[index].place_Id())

                    # Son 1.4.1
                    element1 = ET.SubElement(arc, 'graphics')

                    # Son 1.4.2
                    element2 = ET.SubElement(arc, 'inscription')
                    # Son 1.4.2.1
                    sub_element2 = ET.SubElement(element2, 'value') 
                    sub_element2.text = 'Default,' + '1'
                    # Son 1.4.2.2
                    sub_element2 = ET.SubElement(element2, 'graphics')

                    # Son 1.4.3
                    element3 = ET.SubElement(arc, 'tagged')
                    # Son 1.4.3.1 
                    sub_element3 = ET.SubElement(element3, 'value') 
                    sub_element3.text = 'false'

                    # Son 1.4.4
                    element4 = ET.SubElement(arc, 'arcpath')
                    element4.set('id', '000')
                    element4.set('x', '0')
                    element4.set('y', '0')
                    element4.set('curvePoint', 'false')

                    # Son 1.4.5
                    element5 = ET.SubElement(arc, 'arcpath')
                    element5.set('id', '001')
                    element5.set('x', '0')
                    element5.set('y', '0')
                    element5.set('curvePoint', 'false')

                    # Son 1.4.6
                    element6 = ET.SubElement(arc, 'type')
                    element6.set('value', 'normal')
                
                indice = aux_indice
                for aux_index in range(len(separador)):
                    DArrowInt.draw_Arrow_Int(net, separador, indice, aux_index)
                    if len(separador) == 1:
                        indice += 1
            
        elif ToRefineAnd[index] == 'NONE' and ToRefineOr[index] != 'NONE':
            DArrowOut.draw_Arrow(net, index, list_Goal)
            cadena = ToRefineAnd[index]
            separador = ';'
            separador = cadena.split(separador)
            indice = ToRefineAnd.index(cadena)
            for index in range(len(separador)):
                DArrowInt.draw_Arrow_Int(net, separador, indice, index)

    ''' # Arc 1
    # Son 1.4
    arc = ET.SubElement(net, 'arc') 
    arc.set('id', 'T0 to 7')
    arc.set('source', 'T0')
    arc.set('target', '7')

    # Son 1.4.1
    element1 = ET.SubElement(arc, 'graphics')

    # Son 1.4.2
    element2 = ET.SubElement(arc, 'inscription')
    # Son 1.4.2.1
    sub_element2 = ET.SubElement(element2, 'value') 
    sub_element2.text = 'Default,' + '1'
    # Son 1.4.2.2
    sub_element2 = ET.SubElement(element2, 'graphics')

    # Son 1.4.3
    element3 = ET.SubElement(arc, 'tagged')
    # Son 1.4.3.1 
    sub_element3 = ET.SubElement(element3, 'value') 
    sub_element3.text = 'false'

    # Son 1.4.4
    element4 = ET.SubElement(arc, 'arcpath')
    element4.set('id', '000')
    element4.set('x', '0')
    element4.set('y', '0')
    element4.set('curvePoint', 'false')

    # Son 1.4.5
    element5 = ET.SubElement(arc, 'arcpath')
    element5.set('id', '001')
    element5.set('x', '0')
    element5.set('y', '0')
    element5.set('curvePoint', 'false')

    # Son 1.4.6
    element6 = ET.SubElement(arc, 'type')
    element6.set('value', 'normal') '''

    ''' # Arc 2
    # Son 1.5
    arc = ET.SubElement(net, 'arc') 
    arc.set('id', '6 to T0')
    arc.set('source', '6')
    arc.set('target', 'T0')

    # Son 1.5.1
    element1 = ET.SubElement(arc, 'graphics')

    # Son 1.5.2
    element2 = ET.SubElement(arc, 'inscription')
    # Son 1.5.2.1
    sub_element2 = ET.SubElement(element2, 'value') 
    sub_element2.text = 'Default,' + '1'
    # Son 1.5.2.2
    sub_element2 = ET.SubElement(element2, 'graphics')

    # Son 1.5.3
    element3 = ET.SubElement(arc, 'tagged')
    # Son 1.5.3.1 
    sub_element3 = ET.SubElement(element3, 'value') 
    sub_element3.text = 'false'

    # Son 1.5.4
    element4 = ET.SubElement(arc, 'arcpath')
    element4.set('id', '000')
    element4.set('x', '0')
    element4.set('y', '0')
    element4.set('curvePoint', 'false')

    # Son 1.5.5
    element5 = ET.SubElement(arc, 'arcpath')
    element5.set('id', '001')
    element5.set('x', '0')
    element5.set('y', '0')
    element5.set('curvePoint', 'false')

    # Son 1.5.6
    element6 = ET.SubElement(arc, 'type')
    element6.set('value', 'normal') '''

    return pnml