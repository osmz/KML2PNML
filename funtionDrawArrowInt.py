import xml.etree.ElementTree as ET

def draw_Arrow_Int(list_Type, ToRefineAnd, ToRefineOr, index, list_Vector, net, list_Transition):
    if list_Type == 'ToRefineAnd':
        cadena = ToRefineAnd[index]
        separador = ';'
        separador = cadena.split(separador)

        for aux_Separador in range(len(separador)):
            indice_1 = list_Vector.index(str(separador[aux_Separador]))

            # Arc 2
            # Son 1.5
            arc = ET.SubElement(net, 'arc') 
            arc.set('id', str(list_Vector[indice_1]) + ' to T' + str(list_Transition[indice_1]))
            print('position teste')
            print(str(list_Vector[indice_1]) + ' to T' + str(list_Transition[indice_1]))
            arc.set('source', str(list_Vector[indice_1]))
            arc.set('target', 'T' + str(list_Transition[indice_1]))

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
            element6.set('value', 'normal')
    
    if list_Type == 'ToRefineOr':
        cadena = ToRefineOr[index]
        separador = ';'
        separador = cadena.split(separador)

        for aux_Separador in range(len(separador)):
            indice_1 = list_Vector.index(str(separador[aux_Separador]))

            # Arc 2
            # Son 1.5
            arc = ET.SubElement(net, 'arc') 
            arc.set('id', str(list_Vector[indice_1]) + ' to T' + str(list_Transition[indice_1]))
            print('position teste')
            print(str(list_Vector[indice_1]) + ' to T' + str(list_Transition[indice_1]))
            arc.set('source', str(list_Vector[indice_1]))
            arc.set('target', 'T' + str(list_Transition[indice_1]))

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
            element6.set('value', 'normal')