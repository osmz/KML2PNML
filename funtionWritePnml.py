import xml.etree.ElementTree as ET

def write_Pnml(list_Goal):
    pnml = ET.Element('pnml')

    net = ET.SubElement(pnml, 'net')
    net.set('id', 'Net-One')
    net.set('type', 'P/T net')

    token = ET.SubElement(net, 'token')
    token.set('id', 'Net-One')
    token.set('enabled', 'true')
    token.set('red', '0')
    token.set('green', '0')
    token.set('blue', '0')

    place = ET.SubElement(net, 'place') 
    place.set('id', list_Goal[0].place_Id())
    element1 = ET.SubElement(place, 'graphics') 
    sub_element1 = ET.SubElement(element1, 'position') 
    sub_element1.set('x', '210.0') 
    sub_element1.set('y', '255.0') 

    element2 = ET.SubElement(place, 'name') 
    sub_element2 = ET.SubElement(element2, 'value') 
    sub_element2.text = list_Goal[0].place_Id()
    sub_element2 = ET.SubElement(element2, 'graphics')
    sub_sub_element2 = ET.SubElement(sub_element2, 'offset')
    sub_sub_element2.set('x', '210.0') 
    sub_sub_element2.set('y', '255.0') 

    element3 = ET.SubElement(place, 'initialMarking')
    sub_element3 = ET.SubElement(element3, 'value')
    sub_element3.text = 'Default, 0'
    sub_element3 = ET.SubElement(element3, 'graphics')
    sub_sub_element3 = ET.SubElement(sub_element3, 'offset')
    sub_sub_element3.set('x', '0.0') 
    sub_sub_element3.set('y', '0.0')

    element4 = ET.SubElement(place, 'capacity')
    sub_element4 = ET.SubElement(element4, 'value')
    sub_element4.text = '0'

    return pnml