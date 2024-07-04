def print_action_sequence(stack, stable):
    print(stack, end="\t\t")
    stable.reverse()
    print("[", end=" ")
    for item in stable:
        print(item.state_accept_value, end=" ")
    print("]")
    stable.reverse()

class Lalr_Parser:

    def parse_table(rules, stack, parse_table, stable):
        stable.reverse() # AQUI

        # para guardar lista de tokens da linha:
        current_line_tokens = []

        # para cada elemento da lista 
        FOUND = True

        while len(stable): # AQUI

            table_el  = stable.pop(-1) # ultimo elemento fita 
            stack_el = stack[-1] # ultimo elemento da pilha 


            FOUND = False
            # busca na tabela proxima acao
            for col in parse_table[stack_el]:
                col = col.split() 
                # FOUND = False
                if len(col) == 2: # accept state
                    # filter for tape symbol
                    tab_symb, tab_act = col # symbol, action, transition

                    # tab_next = int(tab_next)

                    if not (table_el.state_accept_value == tab_symb): # AQUI
                        continue

                    # if found symb, make action 
                    FOUND = True

                    # logic for accept
                    print("Sentença Reconhecida!!")
                    stable.append(table_el) # return element to tape # AQUI
                    return True

                elif len(col) == 3: # shift or reduce state
                    # filter for tape symbol
                    tab_symb, tab_act, tab_next = col # symbol, action, transition

                    tab_next = int(tab_next)

                    if not (table_el.state_accept_value == tab_symb):
                        continue

                    # if found symb, make action 
                    FOUND = True

                    if tab_act == 's': # shift 
                        # tape element already removed

                        # atualiza lista de tokens da linha 
                        if len(current_line_tokens):
                            if not (table_el.file_line == current_line_tokens[0][0]):
                                current_line_tokens = []
                            current_line_tokens.append([table_el.file_line, table_el.label ])
                        else:
                            current_line_tokens.append([table_el.file_line, table_el.label])

                        # add to stack: 
                        stack.append(table_el.state_accept_value) # curr tape elem
                        stack.append(tab_next) # next state
                        
                    elif tab_act == 'r': # reduce
                        # append again the removed element
                        stable.append(table_el)

                        # capture rule info
                        rule = rules[tab_next]
                        
                        # find rule size 
                        rule_len = len(rule) - 3

                        # remove from stack 
                        stack = stack[:-(rule_len*2)]

                        # put rule name on stack
                        stack.append(rule[1])

                        # goto next state
                        next_col = stack[-1]
                        next_row = stack[-2]
                        for col in parse_table[next_row]:
                            col = col.split()
                            if col[0] == next_col and col[1] == 'g':
                                stack.append(int(col[2]))
                                break
                else:
                    print("Foi encontrada uma inconsistência sintática na FITA:")
                    print(f'\nNot expected an element of len: {len(col)} in \'table\'')
                    return False
                if FOUND:
                    # print stack and tape:
                    print_action_sequence(stack, stable)
                    # current_line_tokens.append(table_el.file_line, table_el.state_accept_value)
                    # print(current_line_tokens)
                    break

            if not FOUND:
                stable.append(table_el)

                print("Foi encontrada uma inconsistência sintática na FITA:")
                print("\tNão há ação para o elemento na cabeça de leitura da FITA para o estado atual da PILHA!!")
                print("================================================================")
                print("PROGRAM ERROR: line ", table_el.file_line)
                print("\t", end="")
                for line, label in current_line_tokens:
                    print(label, end=" ")
                print("⊙", end=" ")
                print(table_el.label)
                print("================================================================")

                # print("fita:")
                # for el in stable:
                #     print(el.state_accept_value, end=" ")
                # print("---")
                break

        return False