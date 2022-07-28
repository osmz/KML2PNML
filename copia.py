for index in range(len(ToRefineAnd)):
        if ToRefineAnd[index] != 'NONE' and ToRefineOr[index] == 'NONE':
            ''' print('Posicion 1') '''
            list_Type = 'ToRefineAnd'
            DArrowOut.draw_Arrow_Out(list_Type, ToRefineAnd , ToRefineOr, index, net, list_Vector, list_Transition, list_Goal, list_Out)
            ''' print('index teste')
            print(index) '''
            DArrowInt.draw_Arrow_Int(list_Type, ToRefineAnd, ToRefineOr, index, list_Vector, net, list_Transition)
        
        elif ToRefineAnd[index] != 'NONE' and ToRefineOr[index] != 'NONE':
            if ToRefineAnd[index] != 'NONE':
                ''' print('Posicion 2')  '''     
                list_Type = 'ToRefineAnd'          
                DArrowOut.draw_Arrow_Out(list_Type, ToRefineAnd, ToRefineOr, index, net, list_Vector, list_Transition, list_Goal, list_Out)
                ''' print('index teste 2')
                print(index) '''
                DArrowInt.draw_Arrow_Int(list_Type, ToRefineAnd, ToRefineOr, index, list_Vector, net, list_Transition)
            
            if ToRefineOr[index] != 'NONE':
                ''' print('Posicion 3')  '''   
                list_Type = 'ToRefineOr'            
                DArrowOut.draw_Arrow_Out(list_Type, ToRefineAnd, ToRefineOr, index, net, list_Vector, list_Transition, list_Goal, list_Out)
                ''' print('index teste 3')
                print(index) '''
                DArrowInt.draw_Arrow_Int(list_Type, ToRefineAnd, ToRefineOr, index, list_Vector, net, list_Transition)
        
        elif ToRefineAnd[index] == 'NONE' and ToRefineOr[index] != 'NONE':
            ''' print('Posicion 4') '''
            list_Type = 'ToRefineOr'            
            DArrowOut.draw_Arrow_Out(list_Type, ToRefineAnd, ToRefineOr, index, net, list_Vector, list_Transition, list_Goal, list_Out)
            ''' print('index teste 4')
            print(index) '''
            DArrowInt.draw_Arrow_Int(list_Type, ToRefineAnd, ToRefineOr, index, list_Vector, net, list_Transition) 






print(input_Vector_List[0])
lst = Id
print(lst)

for index in range(0, 1, 1):
    ''' print('index')
    print(index) '''
    input_Position = input_Vector_List[index]
    ''' print('input_Position')
    print(input_Position) '''
    output_Position = output_Vector_List[index]

    lst = Id
    indice_Intput = lst.index(input_Position)
    indice_Output = lst.index(output_Position)

    ''' print('indice')
    print(indice) '''

    indice_Intput_X = float(list_Goal[indice_Intput].place_PositionX())
    indice_Intput_Y = float(list_Goal[indice_Intput].place_PositionY())

    indice_Output_X = float(list_Goal[indice_Output].place_PositionX())
    indice_Output_Y = float(list_Goal[indice_Output].place_PositionY())

    indice_Final_X = indice_Intput_X -  indice_Output_X
    indice_Final_Y = indice_Intput_Y -  indice_Output_Y

    if indice_Final_X < 0:
        indice_Final_X = indice_Final_X * (-1)
    
    if indice_Final_Y < 0:
        indice_Final_Y = indice_Final_Y * (-1)

    print(indice_Final_X)
    print(indice_Final_Y)














indice_Reference = list_Transition[index]
    print('indice_Reference')
    print(indice_Reference)
    
    indice_Reference_1 = input_Vector_List[indice_Reference]
    print('indice_Reference_1')
    print(indice_Reference_1)

    indice_Reference_2 = output_Vector_List[indice_Reference]
    print('indice_Reference_1')
    print(indice_Reference_2)
    
    lst_Input_Vector = input_Vector_List
    indice_Reference_Input = lst_Input_Vector.index(indice_Reference_1)
    print('indice_Reference_Input')
    print(indice_Reference_Input)

    lst_Output_Vector = output_Vector_List
    indice_Reference_Output = lst_Output_Vector.index(indice_Reference_2)
    print('indice_Reference_Output')
    print(indice_Reference_Output)

    input_Position = input_Vector_List[indice_Reference_Input]
    print('input_Position')
    print(input_Position)
    output_Position = output_Vector_List[indice_Reference_Output]
    print('output_Position')
    print(output_Position)