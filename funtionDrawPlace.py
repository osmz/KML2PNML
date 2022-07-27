import xml.etree.ElementTree as ET

def draw_Place(net, list_Goal, index):

    # Place
    # Son 1.2
    place = ET.SubElement(net, 'place') 
    place.set('id', list_Goal[index].place_Id())

    # Son 1.2.1
    element1 = ET.SubElement(place, 'graphics')
    # Son 1.2.1.1 
    sub_element1 = ET.SubElement(element1, 'position')
    sub_element1.set('x', list_Goal[index].place_PositionX()) 
    sub_element1.set('y', list_Goal[index].place_PositionY()) 

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

    