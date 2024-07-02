def read_tape(tape, program_output_tape_filename ):
    with open(program_output_tape_filename , 'r') as file:
        data = file.read().split('\n')

    dictionary = dict()
    tape, new_tape = [], []
    # for each line of the file 
    for line in data: 
        # translate old symbs to new symbs
        if '¨' in line:
            line = line.split()
            if len(line) < 3:
                continue
            esp, prefix, new_value = line
            dictionary[prefix] = new_value
        elif len(line) <= 1:
            continue
        else: 
            # found tape line, save tape on list() 
            line = line.strip()
            tape = line.split()
            for tape_el in tape:
                if tape_el in dictionary:
                    new_tape.append(dictionary[tape_el])
                else:
                    new_tape.append(tape_el)
    
    return new_tape 