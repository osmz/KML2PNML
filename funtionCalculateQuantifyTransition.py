def calculate_Quantify_Transition(lst_Id_Goal, ToRefineAnd, ToRefineOr, input_Vector_List, list_Connection, list_Type, list_Goal, list_Transition, output_Vector_List, Id, ExpectationOf):
    cont_Transition = 0
    lst = lst_Id_Goal
    # Loop through the ToRefineAnd vector, all vectors have the same size.
    for index in range(len(ToRefineAnd)):
        if ToRefineAnd[index] != 'NONE' and ToRefineOr[index] == 'NONE':
            cadena = ToRefineAnd[index]
            separador = '@'
            separador = cadena.split(separador)
            for index_Separador_And_Arroa in range(len(separador)):
                cadena = separador[index_Separador_And_Arroa]
                separador2 = ';'
                separador2 = cadena.split(separador2)
                for index_Separador_And_PuntoYComa in range(len(separador2)):
                    input_Vector_List.append(separador2[index_Separador_And_PuntoYComa])
                    list_Connection.append('And')
                    indice = lst.index(separador2[index_Separador_And_PuntoYComa])
                    list_Type.append(list_Goal[indice].goal_Type())
                    list_Transition.append(cont_Transition)
                    output_Vector_List.append(Id[index])
                cont_Transition += 1
        
        elif ToRefineAnd[index] == 'NONE' and ToRefineOr[index] != 'NONE':
            cadena = ToRefineOr[index]
            separador = ';'
            separador = cadena.split(separador)
            for index_Separador_Or in range(len(separador)):
                input_Vector_List.append(separador[index_Separador_Or])
                list_Connection.append('Or')
                indice = lst.index(separador[index_Separador_Or])
                list_Type.append(list_Goal[indice].goal_Type())
                list_Transition.append(cont_Transition)
                output_Vector_List.append(Id[index])
                cont_Transition += 1    

        elif ToRefineAnd[index] != 'NONE' and ToRefineOr[index] != 'NONE':
            if ToRefineAnd[index] != 'NONE':
                cadena = ToRefineAnd[index]
                separador = '@'
                separador = cadena.split(separador)
                for index_Separador_And_Arroa in range(len(separador)):
                    cadena = separador[index_Separador_And_Arroa]
                    separador2 = ';'
                    separador2 = cadena.split(separador2)
                    for index_Separador_And_PuntoYComa in range(len(separador2)):
                        input_Vector_List.append(separador2[index_Separador_And_PuntoYComa])
                        list_Connection.append('And')
                        indice = lst.index(separador2[index_Separador_And_PuntoYComa])
                        list_Type.append(list_Goal[indice].goal_Type())
                        list_Transition.append(cont_Transition)
                        output_Vector_List.append(Id[index])
                    cont_Transition += 1
            
            if ToRefineOr[index] != 'NONE':
                cadena = ToRefineOr[index]
                separador = ';'
                separador = cadena.split(separador)
                for index_Separador_Or_1 in range(len(separador)):
                    input_Vector_List.append(separador[index_Separador_Or_1])
                    list_Connection.append('Or')
                    indice = lst.index(separador[index_Separador_Or_1])
                    list_Type.append(list_Goal[indice].goal_Type())
                    list_Transition.append(cont_Transition)
                    output_Vector_List.append(Id[index])
                    cont_Transition += 1  
        
        # Loop through the ExpectationOf vector to add to the list.
        if ExpectationOf[index] !=  'NONE':
            cadena = ExpectationOf[index]
            separador = ';'
            separador = cadena.split(separador)
            for index_Separador_ExpectationOf in range(len(separador)):
                input_Vector_List.append(separador[index_Separador_ExpectationOf])
                list_Connection.append('Or')
                indice = lst.index(separador[index_Separador_ExpectationOf])
                list_Type.append(list_Goal[indice].goal_Type())
                list_Transition.append(cont_Transition)
                output_Vector_List.append(Id[index])
            cont_Transition += 1
    
    return cont_Transition    