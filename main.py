rules = []
stack = [0]
table = []
tape = []

def read_tape(rules, stack, table, tape):
    tape.reverse()
    # para cada elemento da lista 
    while len(tape): 
        tape_el  = tape.pop(-1) # ultimo elemento fita 
        stack_el = stack[-1] # ultimo elemento da pilha 

        # busca na tabela proxima acao
        for col in table[stack_el]:
            col = col.split() 
            FOUND = False
            if len(col) == 2: # accept state

                FOUND = True

                # logic for accept
                print("Sentença Reconhecida!!")
                tape.append(tape_el) # return element to tape

                return True

            elif len(col) == 3: # shift or reduce state
                FOUND = True
                tab_symb, tab_act, tab_next = col # symbol, action, transition

                tab_next = int(tab_next)

                # filter for tape symbol
                if not (tape_el == tab_symb):
                    continue

                # if found symb, make action 

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
                print(f'not expected an element of len: {len(col)} in \'table\'')
                exit()
                break

            if FOUND:
                break

if __name__ == "__main__":
    from input_.lalr_scanner import read_lalr_info

    keyw_lalr_point = "LALR States"

    # TABLE AND RULES ::: 

    # table, rules = read_lalr_info("./GLCs/mat_ops.txt")
    # table, rules = read_lalr_info("./GLCs/if_else.txt")
    table, rules = read_lalr_info("./GLCs/log_ops.txt")

    # TAPE ::: 

    #tape = ['a', 'times', 'popen', 'a', 'plus', 'a', 'times', 'popen', 'a', 'pclose', 'pclose', '(EOF)']
    # tape = ['if', 'b', 'then', 'a', 'else', 'a', '(EOF)']
    tape = ['id', 'or', 'id', '(EOF)']

    for row in table:
        print(row)
    print()
    
    for row in rules:
        print(row)
    print()


    read_tape(rules, stack, table, tape)