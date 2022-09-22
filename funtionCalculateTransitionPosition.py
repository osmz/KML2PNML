def calculate_Transition_Position(index, list_Transition, input_Vector_List, output_Vector_List, lst_Id_Goal, list_Goal):
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

    lst_Id = lst_Id_Goal
    indice_Intput = lst_Id.index(input_Position)
    indice_Output = lst_Id.index(output_Position)

    indice_Intput_X = float(list_Goal[indice_Intput].goal_PositionX())
    indice_Intput_Y = float(list_Goal[indice_Intput].goal_PositionY())

    ''' print('indice_Intput_X')
    print(indice_Intput_X)
    print('indice_Intput_Y')
    print(indice_Intput_Y) '''

    indice_Output_X = float(list_Goal[indice_Output].goal_PositionX())
    indice_Output_Y = float(list_Goal[indice_Output].goal_PositionY())

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

    return indice_Final_X, indice_Final_Y