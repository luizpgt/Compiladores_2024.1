from Lexical_analysis.models.table_element import Table_Element

def read_stable(program_output_stable_filename):
    with open(program_output_stable_filename , 'r') as file:
        data = file.read().split('\n')

    dictionary = dict()
    tape = []
    # for each line of the file 
    for line in data: 
        line = line.strip()
        line = line.split()

        # translate old symbs to new symbs
        if '¨' in line:
            if len(line) < 3:
                continue
            esp, prefix, new_value = line
            dictionary[prefix] = new_value

        # eof 
        elif len(line) == 1:
            fstate = line[0]
            if not (fstate in dictionary):
                print("erro, foi encontrado um estado inconsistente!")
                exit()
            glc_symb = dictionary[fstate]
            tape.append(Table_Element(fstate, glc_symb, -1, ""))
            continue

        # found table-info line, save on table on list() 
        elif len(line) == 3: 
            fstate, nline, label = line
            if fstate in dictionary:
                glc_symb = dictionary[fstate]
            else:
                glc_symb = fstate
            tape.append(Table_Element(fstate, glc_symb, nline, label))
    
    return tape 