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