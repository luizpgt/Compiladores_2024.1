import copy

from input_.lalr_scanner import read_lalr_info
from input_.stable_scanner import read_stable
from Lexical_analysis.Deterministic_finite_automaton.main import (
    generate_deterministic_state_transition_table,
    markdown_print,
)
# from Lexical_analysis.input_.lexical_scanner import read_input_sentences
# from Lexical_analysis.models.lexical_analyzer import Lexical_Analyzer
from Lexical_analysis.main import generate_lexical_analyzer, print_stable_to_file
from models.lalr_parser import Lalr_Parser

import sys
if __name__ == "__main__":

    RUN_MODE = sys.argv[1]

    finite_automata_input_filename = "finite_automata_input.txt"
    program_filename = "example_program_file.txt"
    program_output_stable_filename = "program_output_table.txt"
    glc_filename = "./GLCs/mat_ops.txt"

    print("DETERMINISTIC STATE TRANSITION TABLE")
    print("------------------------------------")
    deterministic_state_transition_table = generate_deterministic_state_transition_table(finite_automata_input_filename)
    markdown_print(deterministic_state_transition_table)

    print("LEXIC ANALYSIS")
    print("--------------")
    lexical_analyzer = generate_lexical_analyzer(deterministic_state_transition_table, program_filename)
    print(lexical_analyzer)
        
    if RUN_MODE == "lex":
        print_stable_to_file(lexical_analyzer, program_output_stable_filename)
        print("================================================================================")
        print("AGORA é preciso conferir o arquivo de FITA de saída para os ajustes necessários!")
        print("================================================================================")

    if RUN_MODE == "parse": 
        print("LALR PARSER")
        print("-----------")
        rules, stack, parse_table, stable = [], [0], [], []

        parse_table, rules = read_lalr_info(glc_filename)

        stable  = read_stable(program_output_stable_filename)
        print("st")
        print(stable)

        for row in parse_table:
            print(row)
        print()
        
        for row in rules:
            print(row)
        print()

        # for ac in lexical_analyzer.det_state_transition_table.accept_states:
        #     print(ac)
        print("stable:")
        for el in stable:
            print(el)
        print("stable: fim ---")

        parsed = Lalr_Parser.parse_table(copy.deepcopy(rules), copy.deepcopy(stack), copy.deepcopy(parse_table), copy.deepcopy(stable))

        if parsed:
            print("FIM: 0 (sentença reconhecida)")
        else:
            print("FIM: 1 (erro sintático)")