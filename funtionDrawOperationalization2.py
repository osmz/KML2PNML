import funtionDrawTransition as DTransition
import funtionDrawPlace as DPlace

def draw_Operationalization(cont_Transition, OperationalizationOf, lst_Id_Operation, list_Operation, net, input_Vector_List, list_Connection, list_Type, list_Transition, output_Vector_List, Id):
    T_name = cont_Transition
    increment_X = 0
    for index in range(len(OperationalizationOf)):
        if OperationalizationOf[index] != 'NONE':
            if OperationalizationOf[index] != OperationalizationOf[index + 1] and OperationalizationOf[index] != OperationalizationOf[index - 1]:
                indice = lst_Id_Operation.index(OperationalizationOf[index])

                T_name = T_name
                T_position_X = list_Operation[indice].operation_PositionX()
                T_position_Y = list_Operation[indice].operation_PositionY()

                DTransition.draw_Transition(net, T_name, T_position_X, T_position_Y)

                P_name = list_Operation[indice].operation_Postcondition()
                P_position_X = T_position_X
                P_position_Y = str(float(T_position_Y) + 100)

                DPlace.draw_Place(net, P_name, P_position_X, P_position_Y)
                
                input_Vector_List.append(list_Operation[indice].operation_Postcondition())
                list_Connection.append('Or')
                list_Type.append(list_Operation[indice].operation_Type())
                list_Transition.append(T_name)
                output_Vector_List.append(Id[index])

                T_name = T_name + 1
                T_position_X = T_position_X
                T_position_Y = str(float(P_position_Y) + 100)

                DTransition.draw_Transition(net, T_name, T_position_X, T_position_Y)

                P_name = list_Operation[indice].operation_Precondition()
                P_position_X = T_position_X
                P_position_Y = str(float(T_position_Y) + 100)

                DPlace.draw_Place(net, P_name, P_position_X, P_position_Y)
                
                input_Vector_List.append(list_Operation[indice].operation_Precondition())
                list_Connection.append('Or')
                list_Type.append(list_Operation[indice].operation_Type())
                list_Transition.append(T_name)
                output_Vector_List.append(list_Operation[indice].operation_Postcondition())

                T_name = T_name + 1  
            else:                
                indice = lst_Id_Operation.index(OperationalizationOf[index])

                T_name = T_name
                T_position_X = str(float(list_Operation[indice].operation_PositionX()) + float(increment_X)) 
                T_position_Y = list_Operation[indice].operation_PositionY()

                DTransition.draw_Transition(net, T_name, T_position_X, T_position_Y)

                P_name = list_Operation[indice].operation_Postcondition() + '.' + str(index)
                P_position_X = T_position_X
                P_position_Y = str(float(T_position_Y) + 100)

                DPlace.draw_Place(net, P_name, P_position_X, P_position_Y)
                
                input_Vector_List.append(list_Operation[indice].operation_Postcondition() + '.' + str(index))
                list_Connection.append('Or')
                list_Type.append(list_Operation[indice].operation_Type())
                list_Transition.append(T_name)
                output_Vector_List.append(Id[index])

                T_name = T_name + 1
                T_position_X = T_position_X
                T_position_Y = str(float(P_position_Y) + 100)

                DTransition.draw_Transition(net, T_name, T_position_X, T_position_Y)

                P_name = list_Operation[indice].operation_Precondition() + '.' + str(index)
                P_position_X = T_position_X
                P_position_Y = str(float(T_position_Y) + 100)

                DPlace.draw_Place(net, P_name, P_position_X, P_position_Y)
                
                input_Vector_List.append(list_Operation[indice].operation_Precondition() + '.' + str(index))
                list_Connection.append('Or')
                list_Type.append(list_Operation[indice].operation_Type())
                list_Transition.append(T_name)
                output_Vector_List.append(list_Operation[indice].operation_Postcondition() + '.' + str(index))

                T_name = T_name + 1 
                increment_X += 100


''' def draw_Operationalization(cont_Transition, OperationalizationOf, lst_Id_Operation, list_Operation, net, input_Vector_List, list_Connection, list_Type, list_Transition, output_Vector_List, Id):
    T_name = cont_Transition
    for index in range(len(OperationalizationOf)):
        if OperationalizationOf[index] != 'NONE':
            indice = lst_Id_Operation.index(OperationalizationOf[index])

            T_name = T_name
            T_position_X = list_Operation[indice].operation_PositionX()
            T_position_Y = list_Operation[indice].operation_PositionY()

            DTransition.draw_Transition(net, T_name, T_position_X, T_position_Y)

            P_name = list_Operation[indice].operation_Postcondition()
            P_position_X = T_position_X
            P_position_Y = str(float(T_position_Y) + 100)

            DPlace.draw_Place(net, P_name, P_position_X, P_position_Y)
             
            input_Vector_List.append(list_Operation[indice].operation_Postcondition())
            list_Connection.append('Or')
            list_Type.append(list_Operation[indice].operation_Type())
            list_Transition.append(T_name)
            output_Vector_List.append(Id[index])

            T_name = T_name + 1
            T_position_X = T_position_X
            T_position_Y = str(float(P_position_Y) + 100)

            DTransition.draw_Transition(net, T_name, T_position_X, T_position_Y)

            P_name = list_Operation[indice].operation_Precondition()
            P_position_X = T_position_X
            P_position_Y = str(float(T_position_Y) + 100)

            DPlace.draw_Place(net, P_name, P_position_X, P_position_Y)
             
            input_Vector_List.append(list_Operation[indice].operation_Precondition())
            list_Connection.append('Or')
            list_Type.append(list_Operation[indice].operation_Type())
            list_Transition.append(T_name)
            output_Vector_List.append(list_Operation[indice].operation_Postcondition())

            T_name = T_name + 1  '''     