import xml.etree.ElementTree as ET

def draw_Operationalization(OperationalizationOf, list_Transition, Id, list_Operation, net):
    for index in range(len(OperationalizationOf)):
        if OperationalizationOf[index] != 'NONE':
            cadena = OperationalizationOf[index]
            separador = ';'
            separador = cadena.split(separador)
            indice_Transition = list_Transition[-1] + 1
            indice_Place = list_Transition[-1]
            increment_X = 0
            increment_Y = 200
            aux_Complement_Out = 0

            for index_1 in range(len(list_Operation)):
                for index_2 in range(len(Id)):
                    if list_Operation[index_1].operation_Id() == Id[index_2]:
                        for index_Separador_OperationalizationOf in range(len(separador)*2):
                            if indice_Transition % 2 != 0:
                                new_Position_Transition_X = float(list_Operation[index_1].operation_PositionX())
                                new_Position_Transition_X = str(new_Position_Transition_X + increment_X)
                                new_Position_Transition_Y = list_Operation[index_1].operation_PositionY()
                                new_Position_Place_X = float(list_Operation[index_1].operation_PositionX())
                                new_Position_Place_X = str(new_Position_Place_X + increment_X)
                                new_Position_Place_Y = float(list_Operation[index_1].operation_PositionY())
                                new_Position_Place_Y = str(new_Position_Place_Y + (increment_Y/2))
                                complement_Out = separador[aux_Complement_Out]
                                print('complement_Out')
                                print(complement_Out)
                                complement = '- Post'
                                aux_Complement_Out += 1
                            else:
                                new_Position_Transition_X = float(list_Operation[index_1].operation_PositionX())
                                new_Position_Transition_X = str(new_Position_Transition_X + increment_X)
                                new_Position_Transition_Y = float(list_Operation[index_1].operation_PositionY())
                                new_Position_Transition_Y = str(new_Position_Transition_Y + increment_Y)
                                new_Position_Place_X = float(list_Operation[index_1].operation_PositionX())
                                new_Position_Place_X = str(new_Position_Place_X + increment_X)
                                new_Position_Place_Y = float(list_Operation[index_1].operation_PositionY())
                                new_Position_Place_Y = str(new_Position_Place_Y + increment_Y + (increment_Y/2))
                                complement_Out = str(indice_Transition - 2) + '- Post'
                                print('complement_Out')
                                print(complement_Out)
                                complement = '- Pre'
                                increment_X += 100  
                            
                            # Transition
                            # Son 1.3
                            transition = ET.SubElement(net, 'transition') 
                            transition.set('id', 'T' + str(indice_Transition))

                            # Son 1.3.1
                            element1 = ET.SubElement(transition, 'graphics')
                            # Son 1.3.1.1 
                            sub_element1 = ET.SubElement(element1, 'position') 
                            sub_element1.set('x', new_Position_Transition_X) 
                            sub_element1.set('y', new_Position_Transition_Y) 

                            # Son 1.3.2
                            element2 = ET.SubElement(transition, 'name')
                            # Son 1.3.2.1 
                            sub_element2 = ET.SubElement(element2, 'value') 
                            sub_element2.text = 'T' + str(indice_Transition)
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



                            # Place
                            # Son 1.2
                            place = ET.SubElement(net, 'place') 
                            place.set('id', str(indice_Place) + complement)

                            # Son 1.2.1
                            element1 = ET.SubElement(place, 'graphics')
                            # Son 1.2.1.1 
                            sub_element1 = ET.SubElement(element1, 'position')
                            sub_element1.set('x', new_Position_Place_X) 
                            sub_element1.set('y', new_Position_Place_Y) 

                            # Son 1.2.2
                            element2 = ET.SubElement(place, 'name')
                            # Son 1.2.2.1 
                            sub_element2 = ET.SubElement(element2, 'value') 
                            sub_element2.text = str(indice_Place) + complement
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

                            

                            # Arc 2
                            # Son 1.5
                            arc = ET.SubElement(net, 'arc') 
                            arc.set('id', str(indice_Place) + complement + ' to T' + str(indice_Transition))
                            print('position teste and')
                            print(str(indice_Place) + complement + ' to T' + str(indice_Transition))
                            arc.set('source', str(indice_Place) + complement)
                            arc.set('target', 'T' + str(indice_Transition))

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


                            # Arc 1
                            # Son 1.4
                            arc = ET.SubElement(net, 'arc') 
                            arc.set('id', 'T' + str(indice_Transition) + ' to ' + complement_Out)
                            ''' print('position teste and out')
                            print('T' + str(list_Transition[indice_1]) + ' to ' + list_Goal[indice_2].place_Id()) '''
                            arc.set('source', 'T' + str(indice_Transition))
                            arc.set('target', complement_Out)

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

                            indice_Transition += 1    
                            indice_Place += 1  
                            