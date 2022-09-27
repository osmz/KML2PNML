import xml.etree.ElementTree as ET

import funtionDrawPlace as DPlace
import funtionCalculateTransitionPosition as CTransitionPosition
import funtionDrawTransition as DTransiton
import funtionDrawArrowOut as DArrowOut
import funtionDrawArrowInt as DArrowInt
import funtionDrawExpectation as DrawExpectation
import funtionDrawOperationalization as DrawOperationalization

def write_Pnml(helper_For_Goal_Size, list_Goal, cont_Transition, input_Vector_List, output_Vector_List, list_Transition, lst_Id_Goal, ToRefineAnd, ToRefineOr, ExpectationOf, OperationalizationOf, list_Operation, list_Connection, list_Type, Id, lst_Id_Operation):
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

    # For to create all elements Place
    for index in range(helper_For_Goal_Size - 1, -1, -1):
        P_name = list_Goal[index].goal_Id()
        P_position_X = list_Goal[index].goal_PositionX()
        P_position_Y = list_Goal[index].goal_PositionY()
        DPlace.draw_Place(net, P_name, P_position_X, P_position_Y)

    # For to create all elements Transition
    for index in range(cont_Transition):
        (indice_Final_X, indice_Final_Y) = CTransitionPosition.calculate_Transition_Position(index, list_Transition, input_Vector_List, output_Vector_List, lst_Id_Goal, list_Goal)
        T_name = index
        T_position_X = indice_Final_X
        T_position_Y = indice_Final_Y
        DTransiton.draw_Transition(net, T_name, T_position_X, T_position_Y)
        
    # Create all Expectation
    DrawExpectation.draw_Expectation(input_Vector_List, ToRefineAnd, ToRefineOr, ExpectationOf, list_Transition, net)
    
    # Create all Operationalization
    DrawOperationalization.draw_Operationalization(cont_Transition, OperationalizationOf, lst_Id_Operation, list_Operation, net, input_Vector_List, list_Connection, list_Type, list_Transition, output_Vector_List, Id)
    
    # For to create all elements Arc
    for index in range(len(input_Vector_List)): 
        A_name_T = list_Transition
        A_cont_name_T = index
        A_name_id = output_Vector_List

        if len(list_Transition) == 1:
            DArrowOut.draw_Arrow_Out(net, A_name_T, A_cont_name_T, A_name_id)
        elif len(list_Transition) > 1:
            if list_Transition[index - 1 ] != list_Transition[index]:
                DArrowOut.draw_Arrow_Out(net, A_name_T, A_cont_name_T, A_name_id)

        A_name_id = input_Vector_List
        A_cont_name_id = index
        A_name_T = list_Transition
        A_cont_name_T = index
        
        DArrowInt.draw_Arrow_Int(net, A_name_id, A_cont_name_id, A_name_T, A_cont_name_T) 
    
    return pnml