import xml.etree.ElementTree as ET

def draw_Transition(net, index, input_Vector_List, output_Vector_List, Id, list_Goal, list_Transition):
    # Transition
    # Son 1.3
    transition = ET.SubElement(net, 'transition') 
    transition.set('id', 'T' + str(index))

    print('T' + str(index))
    
    # Operations to calculate the coordinates in X and Y

    indice_Reference = index
    ''' print('indice_Reference')
    print(indice_Reference) '''

    lst_list_Transition = list_Transition
    indice_Reference = lst_list_Transition.index(indice_Reference)
    ''' print('indice_Reference_1')
    print(indice_Reference) '''
    
    indice_Reference_1 = input_Vector_List[indice_Reference]
    ''' print('indice_Reference_1')
    print(indice_Reference_1) '''

    indice_Reference_2 = output_Vector_List[indice_Reference]
    ''' print('indice_Reference_1')
    print(indice_Reference_2) '''
    
    lst_Input_Vector = input_Vector_List
    indice_Reference_Input = lst_Input_Vector.index(indice_Reference_1)
    ''' print('indice_Reference_Input')
    print(indice_Reference_Input) '''

    lst_Output_Vector = output_Vector_List
    indice_Reference_Output = lst_Output_Vector.index(indice_Reference_2)
    ''' print('indice_Reference_Output')
    print(indice_Reference_Output) '''

    input_Position = input_Vector_List[indice_Reference_Input]
    ''' print('input_Position')
    print(input_Position) '''
    output_Position = output_Vector_List[indice_Reference_Output]
    ''' print('output_Position')
    print(output_Position) '''

    lst_Id = Id
    indice_Intput = lst_Id.index(input_Position)
    indice_Output = lst_Id.index(output_Position)

    indice_Intput_X = float(list_Goal[indice_Intput].place_PositionX())
    indice_Intput_Y = float(list_Goal[indice_Intput].place_PositionY())

    ''' print('indice_Intput_X')
    print(indice_Intput_X)
    print('indice_Intput_Y')
    print(indice_Intput_Y) '''

    indice_Output_X = float(list_Goal[indice_Output].place_PositionX())
    indice_Output_Y = float(list_Goal[indice_Output].place_PositionY())

    ''' print('indice_Output_X')
    print(indice_Output_X)
    print('indice_Output_Y')
    print(indice_Output_Y) '''

    indice_Final_X = indice_Intput_X -  indice_Output_X
    indice_Final_Y = indice_Intput_Y -  indice_Output_Y

    if indice_Final_X < 0:
        indice_Final_X = indice_Final_X * (-1)
    
    if indice_Final_Y < 0:
        indice_Final_Y = indice_Final_Y * (-1)
    
    indice_Final_X = indice_Final_X / 2
    indice_Final_Y = indice_Final_Y / 2

    if indice_Intput_X < indice_Output_X:
        indice_Final_X = indice_Intput_X + indice_Final_X
    else:
        indice_Final_X = indice_Output_X + indice_Final_X
    
    if indice_Intput_Y < indice_Output_Y:
        indice_Final_Y = indice_Intput_Y + indice_Final_Y
    else:
        indice_Final_Y = indice_Output_Y + indice_Final_Y
    
    indice_Final_X = str(indice_Final_X)
    indice_Final_Y = str(indice_Final_Y)

    ''' print('indice_Final_X')
    print(indice_Final_X)
    print('indice_Final_Y')
    print(indice_Final_Y) '''

    # Son 1.3.1
    element1 = ET.SubElement(transition, 'graphics')
    # Son 1.3.1.1 
    sub_element1 = ET.SubElement(element1, 'position') 
    sub_element1.set('x', indice_Final_X) 
    sub_element1.set('y', indice_Final_Y) 

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