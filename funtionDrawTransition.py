import xml.etree.ElementTree as ET

def draw_Transition(net, index, starting_Position_X_Transition, starting_Position_Y_Transition):
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