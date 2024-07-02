from enum import Enum

keyw_lalr_point = "LALR States"
keyw_state_point = "State"
keyw_prior_states_point = "Prior States:"
keyw_rule_point = "<"
keyw_rules_point = "Rules"
keyw_end_read = "===="
lalr_flag = False
prior_states_flag = False
state_flag = False

STATE = Enum('STATE', ['LALR', 'PIOR', 'STATE', 'RULE_T', 'TABLE_INFO', 'END', 'RULES'])

def read_lalr_info(lalr_filename):
    file = open(lalr_filename, "r") 
    line = file.readline()
    state = 0

    lines = []
    table_info = []
    while line:
        line = line.strip()
        if line == keyw_lalr_point:
            state = 1
        elif keyw_prior_states_point in line:
            state = 2
        elif keyw_state_point in line:
            state = 3
            if (lines):
                table_info.append(lines)
            lines = []
        elif keyw_rule_point in line and (state == 3 or state == 2):
            state = 4
        elif keyw_end_read in line:
            state = 6
        elif keyw_rules_point in line:
            state = 7

            line = file.readline() # skip === line
            line = file.readline() # skip '  ' line

            rules_ids = []

            while state == 7:
                line = file.readline()
                line = line.strip()
                line = line.split()

                if (len(line) > 1):
                    rules_ids.append(line)
                else:
                    state = 2 # arbitrary state "prior"

        if (state == 4 and line == ''):
            state = 5

        if state == 5 and line != '': 
            # print(STATE(state)); print(line)
            lines.append(line)

        line = file.readline()

    return table_info, rules_ids