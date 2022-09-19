import funtionDrawArrowInt as DArrowIntCopy
import funtionDrawArrowIntInhibitor as DArrowIntInhibitor

def draw_Expectation(ToRefineAnd, ToRefineOr, ExpectationOf, input_Vector_List, net, list_Transition):
    lst = input_Vector_List
    for index in range(len(ToRefineAnd)):
        if ToRefineAnd[index] != 'NONE' and ToRefineOr[index] == 'NONE' and ExpectationOf[index] != 'NONE':
            cadena = ToRefineAnd[index]
            separador = ';'
            separador = cadena.split(separador)
            indice = lst.index(separador[0])

            A_inhibitor = ExpectationOf
            cont_1_inhibitor = index
            B_inhibitor = list_Transition
            cont_2_inhibitor = indice

            DArrowIntInhibitor.draw_Arrow_Int_Inhibitor(net, A_inhibitor, cont_1_inhibitor, B_inhibitor, cont_2_inhibitor)

            # Draw normal arcs that reach the expectation transition

            for index_Separador_And in range(len(separador)):
                indice_Expectation = lst.index(ExpectationOf[index])

                A_normal = separador
                cont_1_normal = index_Separador_And
                B_normal = list_Transition
                cont_2_normal = indice_Expectation
                
                DArrowIntCopy.draw_Arrow_Int(net, A_normal, cont_1_normal, B_normal, cont_2_normal)
        
        elif ToRefineAnd[index] == 'NONE' and ToRefineOr[index] != 'NONE' and ExpectationOf[index] != 'NONE':
            cadena = ToRefineOr[index]
            separador = ';'
            separador = cadena.split(separador)
            print('separador')
            print(separador)
            for index_Separador_Or in range(len(separador)):
                indice = lst.index(separador[index_Separador_Or])

                A_inhibitor = ExpectationOf
                cont_1_inhibitor = index
                B_inhibitor = list_Transition
                cont_2_inhibitor = indice

                DArrowIntInhibitor.draw_Arrow_Int_Inhibitor(net, A_inhibitor, cont_1_inhibitor, B_inhibitor, cont_2_inhibitor)

                # Draw normal arcs that reach the expectation transition

                indice_Expectation = lst.index(ExpectationOf[index])

                A_normal = separador
                cont_1_normal = index_Separador_Or
                B_normal = list_Transition
                cont_2_normal = indice_Expectation
                
                DArrowIntCopy.draw_Arrow_Int(net, A_normal, cont_1_normal, B_normal, cont_2_normal)

        elif ToRefineAnd[index] != 'NONE' and ToRefineOr[index] != 'NONE' and ExpectationOf[index] != 'NONE':
            if ToRefineAnd[index] != 'NONE':
                cadena = ToRefineAnd[index]
                separador = ';'
                separador = cadena.split(separador)
                indice = lst.index(separador[0])

                A_inhibitor = ExpectationOf
                cont_1_inhibitor = index
                B_inhibitor = list_Transition
                cont_2_inhibitor = indice

                DArrowIntInhibitor.draw_Arrow_Int_Inhibitor(net, A_inhibitor, cont_1_inhibitor, B_inhibitor, cont_2_inhibitor)
                
                # Draw normal arcs that reach the expectation transition

                for index_Separador_And in range(len(separador)):
                    indice_Expectation = lst.index(ExpectationOf[index])

                    A_normal = separador
                    cont_1_normal = index_Separador_And
                    B_normal = list_Transition
                    cont_2_normal = indice_Expectation
                    
                    DArrowIntCopy.draw_Arrow_Int(net, A_normal, cont_1_normal, B_normal, cont_2_normal)
        
            if ToRefineOr[index] != 'NONE':
                cadena = ToRefineOr[index]
                separador = ';'
                separador = cadena.split(separador)
                for index_Separador_Or in range(len(separador)):
                    indice = lst.index(separador[index_Separador_Or])

                    A_inhibitor = ExpectationOf
                    cont_1_inhibitor = index
                    B_inhibitor = list_Transition
                    cont_2_inhibitor = indice

                    DArrowIntInhibitor.draw_Arrow_Int_Inhibitor(net, A_inhibitor, cont_1_inhibitor, B_inhibitor, cont_2_inhibitor)

                    # Draw normal arcs that reach the expectation transition

                    indice_Expectation = lst.index(ExpectationOf[index])

                    A_normal = separador
                    cont_1_normal = index_Separador_Or
                    B_normal = list_Transition
                    cont_2_normal = indice_Expectation
                    
                    DArrowIntCopy.draw_Arrow_Int(net, A_normal, cont_1_normal, B_normal, cont_2_normal)