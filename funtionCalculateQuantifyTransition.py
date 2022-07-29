def calculate_Quantify_Transition(Id, ToRefineAnd, ToRefineOr, input_Vector_List, list_Connection, list_Type, list_Transition, list_Goal, output_Vector_List, ExpectationOf):
    cont_Transition = 0
    lst = Id
    for index in range(len(ToRefineAnd)):
        if ToRefineAnd[index] != 'NONE' and ToRefineOr[index] == 'NONE':
            cadena = ToRefineAnd[index]
            separador = ';'
            separador = cadena.split(separador)
            for index_Separador_And in range(len(separador)):
                input_Vector_List.append(separador[index_Separador_And])
                list_Connection.append('And')
                indice = lst.index(separador[index_Separador_And])
                list_Type.append(list_Goal[indice].place_Type())
                list_Transition.append(cont_Transition)
                output_Vector_List.append(list_Goal[index].place_Id())
            cont_Transition += 1
        
        elif ToRefineAnd[index] == 'NONE' and ToRefineOr[index] != 'NONE':
            cadena = ToRefineOr[index]
            separador = ';'
            separador = cadena.split(separador)
            for index_Separador_Or in range(len(separador)):
                input_Vector_List.append(separador[index_Separador_Or])
                list_Connection.append('Or')
                indice = lst.index(separador[index_Separador_Or])
                list_Type.append(list_Goal[indice].place_Type())
                list_Transition.append(cont_Transition)
                output_Vector_List.append(list_Goal[index].place_Id())
                cont_Transition += 1    

        elif ToRefineAnd[index] != 'NONE' and ToRefineOr[index] != 'NONE':
            if ToRefineAnd[index] != 'NONE':
                cadena = ToRefineAnd[index]
                separador = ';'
                separador = cadena.split(separador)
                for index_Separador_And_1 in range(len(separador)):
                    input_Vector_List.append(separador[index_Separador_And_1])
                    list_Connection.append('And')
                    indice = lst.index(separador[index_Separador_And_1])
                    list_Type.append(list_Goal[indice].place_Type())
                    list_Transition.append(cont_Transition)
                    output_Vector_List.append(list_Goal[index].place_Id())
                cont_Transition += 1
            
            if ToRefineOr[index] != 'NONE':
                cadena = ToRefineOr[index]
                separador = ';'
                separador = cadena.split(separador)
                for index_Separador_Or_1 in range(len(separador)):
                    input_Vector_List.append(separador[index_Separador_Or_1])
                    list_Connection.append('Or')
                    indice = lst.index(separador[index_Separador_Or_1])
                    list_Type.append(list_Goal[indice].place_Type())
                    list_Transition.append(cont_Transition)
                    output_Vector_List.append(list_Goal[index].place_Id())
                    cont_Transition += 1  
        
        if ExpectationOf[index] !=  'NONE':
            cadena = ExpectationOf[index]
            separador = ';'
            separador = cadena.split(separador)
            for index_Separador_ExpectationOf in range(len(separador)):
                input_Vector_List.append(separador[index_Separador_ExpectationOf])
                list_Connection.append('Or')
                indice = lst.index(separador[index_Separador_ExpectationOf])
                list_Type.append(list_Goal[indice].place_Type())
                list_Transition.append(cont_Transition)
                output_Vector_List.append(list_Goal[index].place_Id())
            cont_Transition += 1
    
    return cont_Transition
    