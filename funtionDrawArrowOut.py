import xml.etree.ElementTree as ET

def draw_Arrow_Out(net, A_name_T, A_cont_name_T, A_name_id):
    # Arc 1
    # Son 1.4
    arc = ET.SubElement(net, 'arc') 
    arc.set('id', 'T' + str(A_name_T[A_cont_name_T]) + ' to ' + A_name_id[A_cont_name_T])
    ''' print('position teste and out')
    print('T' + str(A_name_T[A_cont_name_T]) + ' to ' + A_name_id[A_cont_name_T]) '''
    arc.set('source', 'T' + str(A_name_T[A_cont_name_T]))
    arc.set('target', A_name_id[A_cont_name_T])

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