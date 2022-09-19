import xml.etree.ElementTree as ET

def draw_Arrow_Int(net, A_normal, cont_1_normal, B_normal, cont_2_normal):
    # Arc 2
    # Son 1.5
    arc = ET.SubElement(net, 'arc') 
    arc.set('id', str(A_normal[cont_1_normal]) + ' to T' + str(B_normal[cont_2_normal]))
    ''' print('position teste and')
    print(str(A_normal[cont_1_normal]) + ' to T' + str(B[cont_2])) '''
    arc.set('source', str(A_normal[cont_1_normal]))
    arc.set('target', 'T' + str(B_normal[cont_2_normal]))

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