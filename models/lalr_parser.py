def print_action_sequence(stack, tape):
    print(stack, end="\t\t")
    tape.reverse()
    print(tape)
    tape.reverse()

class Lalr_Parser:
    def parse_tape(rules, stack, table, tape):
        tape.reverse()
        # para cada elemento da lista 
        FOUND = True
        while len(tape): 

            if not FOUND:
                print("Foi encontrada uma inconsistência sintática na FITA:")
                print("\tNão há ação para o elemento na cabeça de leitura da FITA para o estado atual da PILHA!!")
                break

            tape_el  = tape.pop(-1) # ultimo elemento fita 
            stack_el = stack[-1] # ultimo elemento da pilha 

            # busca na tabela proxima acao
            for col in table[stack_el]:
                col = col.split() 
                FOUND = False
                if len(col) == 2: # accept state
                    # filter for tape symbol
                    tab_symb, tab_act = col # symbol, action, transition

                    # tab_next = int(tab_next)

                    if not (tape_el == tab_symb):
                        continue

                    # if found symb, make action 
                    FOUND = True

                    # logic for accept
                    print("Sentença Reconhecida!!")
                    tape.append(tape_el) # return element to tape
                    return True

                elif len(col) == 3: # shift or reduce state
                    # filter for tape symbol
                    tab_symb, tab_act, tab_next = col # symbol, action, transition

                    tab_next = int(tab_next)

                    if not (tape_el == tab_symb):
                        continue

                    # if found symb, make action 
                    FOUND = True

                    if tab_act == 's': # shift 
                        # tape element already removed

                        # add to stack: 
                        stack.append(tape_el) # curr tape elem
                        stack.append(tab_next) # next state
                        
                    elif tab_act == 'r': # reduce
                        # append again the removed element
                        tape.append(tape_el)

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
                        for col in table[next_row]:
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
                    print_action_sequence(stack, tape)
                    break
        return False