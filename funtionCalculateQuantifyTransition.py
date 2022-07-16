def calculate_Quantify_Transition(ToRefineAnd, ToRefineOr, list_Vector, list_Connection, list_Transition):
    cont_Transition = 0
    for index in range(len(ToRefineAnd)):
        if ToRefineAnd[index] != 'NONE' and ToRefineOr[index] == 'NONE':
            cadena = ToRefineAnd[index]
            separador = ';'
            separador = cadena.split(separador)
            for index_Separador_And in range(len(separador)):
                list_Vector.append(separador[index_Separador_And])
                list_Connection.append('And')
                list_Transition.append(cont_Transition)
            cont_Transition += 1
        
        elif ToRefineOr[index] != 'NONE' and ToRefineAnd[index] == 'NONE':
            cadena = ToRefineOr[index]
            separador = ';'
            separador = cadena.split(separador)
            for index_Separador_Or in range(len(separador)):
                list_Vector.append(separador[index_Separador_Or])
                list_Connection.append('Or')
                list_Transition.append(cont_Transition)
                cont_Transition += 1    

        elif ToRefineAnd[index] != 'NONE' and ToRefineOr[index] != 'NONE':
            if ToRefineAnd[index] != 'NONE':
                cadena = ToRefineAnd[index]
                separador = ';'
                separador = cadena.split(separador)
                for index_Separador_And_1 in range(len(separador)):
                    list_Vector.append(separador[index_Separador_And_1])
                    list_Connection.append('And')
                    list_Transition.append(cont_Transition)
                cont_Transition += 1
            
            if ToRefineOr[index] != 'NONE':
                cadena = ToRefineOr[index]
                separador = ';'
                separador = cadena.split(separador)
                for index_Separador_Or_1 in range(len(separador)):
                    list_Vector.append(separador[index_Separador_Or_1])
                    list_Connection.append('Or')
                    list_Transition.append(cont_Transition)
                    cont_Transition += 1
    
    return cont_Transition
    