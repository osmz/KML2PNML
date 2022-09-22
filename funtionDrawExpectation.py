import funtionDrawArrowInt as DArrowInt
import funtionDrawArrowIntInhibitor as DArrowIntInhibitor

def draw_Expectation(input_Vector_List, ToRefineAnd, ToRefineOr, ExpectationOf, list_Transition, net):
    lst = input_Vector_List
    for index in range(len(ToRefineAnd)):
        if ToRefineAnd[index] != 'NONE' and ToRefineOr[index] == 'NONE' and ExpectationOf[index] != 'NONE':
            cadena = ToRefineAnd[index]
            separador = ';'
            separador = cadena.split(separador)
            indice = lst.index(separador[0])

            A_name_id = ExpectationOf
            A_cont_name_id = index
            A_name_T = list_Transition
            A_cont_name_T = indice

            DArrowIntInhibitor.draw_Arrow_Int_Inhibitor(net, A_name_id, A_cont_name_id, A_name_T, A_cont_name_T)

            # Draw normal arcs that reach the expectation transition
            for index_Separador_And in range(len(separador)):
                indice_Expectation = lst.index(ExpectationOf[index])

                A_name_id = separador
                A_cont_name_id = index_Separador_And
                A_name_T = list_Transition
                A_cont_name_T = indice_Expectation
                
                DArrowInt.draw_Arrow_Int(net, A_name_id, A_cont_name_id, A_name_T, A_cont_name_T)
        
        elif ToRefineAnd[index] == 'NONE' and ToRefineOr[index] != 'NONE' and ExpectationOf[index] != 'NONE':
            cadena = ToRefineOr[index]
            separador = ';'
            separador = cadena.split(separador)
            for index_Separador_Or in range(len(separador)):
                indice = lst.index(separador[index_Separador_Or])

                A_name_id = ExpectationOf
                A_cont_name_id = index
                A_name_T = list_Transition
                A_cont_name_T = indice

                DArrowIntInhibitor.draw_Arrow_Int_Inhibitor(net, A_name_id, A_cont_name_id, A_name_T, A_cont_name_T)

                # Draw normal arcs that reach the expectation transition
                indice_Expectation = lst.index(ExpectationOf[index])

                A_name_id = separador
                A_cont_name_id = index_Separador_Or
                A_name_T = list_Transition
                A_cont_name_T = indice_Expectation
                
                DArrowInt.draw_Arrow_Int(net, A_name_id, A_cont_name_id, A_name_T, A_cont_name_T)

        elif ToRefineAnd[index] != 'NONE' and ToRefineOr[index] != 'NONE' and ExpectationOf[index] != 'NONE':
            if ToRefineAnd[index] != 'NONE':
                cadena = ToRefineAnd[index]
                separador = ';'
                separador = cadena.split(separador)
                indice = lst.index(separador[0])

                A_name_id = ExpectationOf
                A_cont_name_id = index
                A_name_T = list_Transition
                A_cont_name_T = indice

                DArrowIntInhibitor.draw_Arrow_Int_Inhibitor(net, A_name_id, A_cont_name_id, A_name_T, A_cont_name_T)
                
                # Draw normal arcs that reach the expectation transition
                for index_Separador_And in range(len(separador)):
                    indice_Expectation = lst.index(ExpectationOf[index])

                    A_name_id = separador
                    A_cont_name_id = index_Separador_And
                    A_name_T = list_Transition
                    A_cont_name_T = indice_Expectation
                    
                    DArrowInt.draw_Arrow_Int(net, A_name_id, A_cont_name_id, A_name_T, A_cont_name_T)
        
            if ToRefineOr[index] != 'NONE':
                cadena = ToRefineOr[index]
                separador = ';'
                separador = cadena.split(separador)
                for index_Separador_Or in range(len(separador)):
                    indice = lst.index(separador[index_Separador_Or])

                    A_name_id = ExpectationOf
                    A_cont_name_id = index
                    A_name_T = list_Transition
                    A_cont_name_T = indice

                    DArrowIntInhibitor.draw_Arrow_Int_Inhibitor(net, A_name_id, A_cont_name_id, A_name_T, A_cont_name_T)

                    # Draw normal arcs that reach the expectation transition
                    indice_Expectation = lst.index(ExpectationOf[index])

                    A_name_id = separador
                    A_cont_name_id = index_Separador_Or
                    A_name_T = list_Transition
                    A_cont_name_T = indice_Expectation
                    
                    DArrowInt.draw_Arrow_Int(net, A_name_id, A_cont_name_id, A_name_T, A_cont_name_T)