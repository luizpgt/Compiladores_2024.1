import copy

from input_.lalr_scanner import read_lalr_info
from Lexical_analysis.Deterministic_finite_automaton.main import (
    generate_deterministic_state_transition_table,
    markdown_print,
)
# from Lexical_analysis.input_.lexical_scanner import read_input_sentences
# from Lexical_analysis.models.lexical_analyzer import Lexical_Analyzer
from Lexical_analysis.main import generate_lexical_analyzer
from models.lalr_parser import Lalr_Parser

if __name__ == "__main__":
    finite_automata_input_filename = "finite_automata_input.txt"
    program_filename = "example_program_file.txt"
    program_output_tape_filename = "program_output_tape.txt"

    print("DETERMINISTIC STATE TRANSITION TABLE")
    print("------------------------------------")
    deterministic_state_transition_table = generate_deterministic_state_transition_table(finite_automata_input_filename)
    markdown_print(deterministic_state_transition_table)

    print("LEXIC ANALYSIS")
    print("--------------")
    lexical_analyzer = generate_lexical_analyzer(deterministic_state_transition_table, program_filename)
    print(lexical_analyzer)

    print("LALR PARSER")
    print("-----------")
    rules, stack, table, tape = [], [0], [], []

    table, rules = read_lalr_info("./GLCs/mat_ops.txt")
    with open(program_output_tape_filename , 'r') as file:
        data = file.read().rstrip()
    tape = data.split()

    for row in table:
        print(row)
    print()
    
    for row in rules:
        print(row)
    print()

    for ac in lexical_analyzer.det_state_transition_table.accept_states:
        print(ac)

    parsed = Lalr_Parser.parse_tape(copy.deepcopy(rules), copy.deepcopy(stack), copy.deepcopy(table), copy.deepcopy(tape))

    if parsed:
        print("FIM: 0")
    else:
        print("FIM: 1")