import xml.etree.ElementTree as ET

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
        # Convert the positions to string
        starting_Position_X_Place = str(starting_Position_X_Place)
        starting_Position_Y_Place = str(starting_Position_Y_Place)

        # Place
        # Son 1.2
        place = ET.SubElement(net, 'place') 
        place.set('id', list_Goal[index].place_Id())

        # Son 1.2.1
        element1 = ET.SubElement(place, 'graphics')
        # Son 1.2.1.1 
        sub_element1 = ET.SubElement(element1, 'position') 
        sub_element1.set('x', starting_Position_X_Place) 
        sub_element1.set('y', starting_Position_Y_Place) 

        # Son 1.2.2
        element2 = ET.SubElement(place, 'name')
        # Son 1.2.2.1 
        sub_element2 = ET.SubElement(element2, 'value') 
        sub_element2.text = list_Goal[index].place_Id()
        # Son 1.2.2.2
        sub_element2 = ET.SubElement(element2, 'graphics')
        # Son 1.2.2.2.1
        sub_sub_element2 = ET.SubElement(sub_element2, 'offset')
        sub_sub_element2.set('x', '0.0') 
        sub_sub_element2.set('y', '0.0') 

        # Son 1.2.3
        element3 = ET.SubElement(place, 'initialMarking')
        # Son 1.2.3.1
        sub_element3 = ET.SubElement(element3, 'value')
        sub_element3.text = 'Default,' + '0'
        # Son 1.2.3.2
        sub_element3 = ET.SubElement(element3, 'graphics')
        # Son 1.2.3.2.1
        sub_sub_element3 = ET.SubElement(sub_element3, 'offset')
        sub_sub_element3.set('x', '0.0') 
        sub_sub_element3.set('y', '0.0')

        # Son 1.2.4
        element4 = ET.SubElement(place, 'capacity')
        # Son 1.2.4.1
        sub_element4 = ET.SubElement(element4, 'value')
        sub_element4.text = '0'

        # Convert the positions to float
        starting_Position_X_Place = float(starting_Position_X_Place)
        starting_Position_Y_Place = float(starting_Position_Y_Place)

        # Increase the positions
        starting_Position_X_Place += 50.0
        starting_Position_Y_Place += 50.0
    
    # Initialize the position variables of the places
    starting_Position_X_Transition = 400.0
    starting_Position_Y_Transition = 200.0 

    # For to create all elements Transition
    for index in range(quant_Transition):
        # Convert the positions to string
        starting_Position_X_Transition = str(starting_Position_X_Transition)
        starting_Position_Y_Transition = str(starting_Position_Y_Transition)

        # Transition
        # Son 1.3
        transition = ET.SubElement(net, 'transition') 
        transition.set('id', 'T' + str(index))

        # Son 1.3.1
        element1 = ET.SubElement(transition, 'graphics')
        # Son 1.3.1.1 
        sub_element1 = ET.SubElement(element1, 'position') 
        sub_element1.set('x', starting_Position_X_Transition) 
        sub_element1.set('y', starting_Position_Y_Transition) 

        # Son 1.3.2
        element2 = ET.SubElement(transition, 'name')
        # Son 1.3.2.1 
        sub_element2 = ET.SubElement(element2, 'value') 
        sub_element2.text = 'T' + str(index)
        # Son 1.3.2.2
        sub_element2 = ET.SubElement(element2, 'graphics')
        # Son 1.3.2.2.1
        sub_sub_element2 = ET.SubElement(sub_element2, 'offset')
        sub_sub_element2.set('x', '11.0') 
        sub_sub_element2.set('y', '43.0')

        # Son 1.3.3
        element3 = ET.SubElement(transition, 'orientation')
        # Son 1.3.3.1 
        sub_element3 = ET.SubElement(element3, 'value') 
        sub_element3.text = '0'

        # Son 1.3.4
        element4 = ET.SubElement(transition, 'rate')
        # Son 1.3.4.1 
        sub_element4 = ET.SubElement(element4, 'value') 
        sub_element4.text = '1.0'

        # Son 1.3.5
        element5 = ET.SubElement(transition, 'timed')
        # Son 1.3.5.1 
        sub_element5 = ET.SubElement(element5, 'value') 
        sub_element5.text = 'false'

        # Son 1.3.6
        element6 = ET.SubElement(transition, 'infiniteServer')
        # Son 1.3.6.1 
        sub_element6 = ET.SubElement(element6, 'value') 
        sub_element6.text = 'false'

        # Son 1.3.7
        element7 = ET.SubElement(transition, 'priority')
        # Son 1.3.7.1 
        sub_element7 = ET.SubElement(element7, 'value') 
        sub_element7.text = '1'

        # Convert the positions to float
        starting_Position_X_Transition = float(starting_Position_X_Transition)
        starting_Position_Y_Transition = float(starting_Position_Y_Transition)

        # Increase the positions
        starting_Position_X_Transition += 100.0
        starting_Position_Y_Transition += 100.0    

    # For to create all elements Arc
    for index in range(len(ToRefineAnd)):
        if ToRefineAnd[index] != 'NONE' and ToRefineOr[index] == 'NONE':
            # Arc 1
            # Son 1.4
            arc = ET.SubElement(net, 'arc') 
            arc.set('id', 'T' + str(index) + ' to ' + list_Goal[index].place_Id())
            arc.set('source', 'T' + str(index))
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

        elif ToRefineAnd[index] != 'NONE' and ToRefineOr[index] != 'NONE':
            if ToRefineAnd[index] != 'NONE':
                # Arc 1
                # Son 1.4
                arc = ET.SubElement(net, 'arc') 
                arc.set('id', 'T' + str(index) + ' to ' + list_Goal[index].place_Id())
                arc.set('source', 'T' + str(index))
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
            
            if ToRefineOr[index] != 'NONE':
                cadena = ToRefineOr[index]
                separador = ';'
                separador = cadena.split(separador)
                for aux_teste in range((index + 1), (index + 1) + len(separador), 1):
                    # Arc 1
                    # Son 1.4
                    arc = ET.SubElement(net, 'arc') 
                    arc.set('id', 'T' + str(aux_teste) + ' to ' + list_Goal[index].place_Id())
                    arc.set('source', 'T' + str(aux_teste))
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
            
        elif ToRefineAnd[index] == 'NONE' and ToRefineOr[index] != 'NONE':
            # Arc 1
            # Son 1.4
            arc = ET.SubElement(net, 'arc') 
            arc.set('id', 'T' + str(index) + ' to ' + list_Goal[index].place_Id())
            arc.set('source', 'T' + str(index))
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