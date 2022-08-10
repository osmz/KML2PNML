import xml.etree.ElementTree as ET

def draw_Expectation(ToRefineAnd, ToRefineOr, ExpectationOf, input_Vector_List, net, list_Transition):
    lst = input_Vector_List
    for index in range(len(ToRefineAnd)):
        if ToRefineAnd[index] != 'NONE' and ToRefineOr[index] == 'NONE' and ExpectationOf[index] != 'NONE':
            cadena = ToRefineAnd[index]
            separador = ';'
            separador = cadena.split(separador)
            indice = lst.index(separador[0])
            
            # Arc 2
            # Son 1.5
            arc = ET.SubElement(net, 'arc') 
            arc.set('id', str(ExpectationOf[index]) + ' to T' + str(list_Transition[indice]))
            ''' print('position teste and')
            print(str(input_Vector_List[index]) + ' to T' + str(list_Transition[index])) '''
            arc.set('source', str(ExpectationOf[index]))
            arc.set('target', 'T' + str(list_Transition[indice]))

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
            element6.set('value', 'inhibitor')
        
        elif ToRefineAnd[index] == 'NONE' and ToRefineOr[index] != 'NONE' and ExpectationOf[index] != 'NONE':
            cadena = ToRefineOr[index]
            separador = ';'
            separador = cadena.split(separador)
            for index_Separador_Or in range(len(separador)):
                indice = lst.index(separador[index_Separador_Or])
                # Arc 2
                # Son 1.5
                arc = ET.SubElement(net, 'arc') 
                arc.set('id', str(ExpectationOf[index]) + ' to T' + str(list_Transition[indice]))
                ''' print('position teste and')
                print(str(input_Vector_List[index]) + ' to T' + str(list_Transition[index])) '''
                arc.set('source', str(ExpectationOf[index]))
                arc.set('target', 'T' + str(list_Transition[indice]))

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
                element6.set('value', 'inhibitor')

        elif ToRefineAnd[index] != 'NONE' and ToRefineOr[index] != 'NONE' and ExpectationOf[index] != 'NONE':
            if ToRefineAnd[index] != 'NONE':
                cadena = ToRefineAnd[index]
                separador = ';'
                separador = cadena.split(separador)
                indice = lst.index(separador[0])
                
                # Arc 2
                # Son 1.5
                arc = ET.SubElement(net, 'arc') 
                arc.set('id', str(ExpectationOf[index]) + ' to T' + str(list_Transition[indice]))
                ''' print('position teste and')
                print(str(input_Vector_List[index]) + ' to T' + str(list_Transition[index])) '''
                arc.set('source', str(ExpectationOf[index]))
                arc.set('target', 'T' + str(list_Transition[indice]))

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
                element6.set('value', 'inhibitor')
        
            if ToRefineOr[index] != 'NONE':
                cadena = ToRefineOr[index]
                separador = ';'
                separador = cadena.split(separador)
                for index_Separador_Or in range(len(separador)):
                    indice = lst.index(separador[index_Separador_Or])
                    # Arc 2
                    # Son 1.5
                    arc = ET.SubElement(net, 'arc') 
                    arc.set('id', str(ExpectationOf[index]) + ' to T' + str(list_Transition[indice]))
                    ''' print('position teste and')
                    print(str(input_Vector_List[index]) + ' to T' + str(list_Transition[index])) '''
                    arc.set('source', str(ExpectationOf[index]))
                    arc.set('target', 'T' + str(list_Transition[indice]))

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
                    element6.set('value', 'inhibitor')