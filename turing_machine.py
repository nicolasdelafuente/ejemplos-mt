from automata.tm.dtm import DTM

transitions  = {
    'q0': {
        'a': ('q1', 'x', 'R'),
        'b': ('q5', 'x', 'R'),
        'x': ('q4', 'x', 'R')
    },
    'q1': {
        'a': ('q1', 'a', 'R'),
        'b': ('q1', 'b', 'R'),
        'c': ('q2', 'x', 'L'),
        'x': ('q3', 'x', 'R')
    },
    'q2': {
        'a': ('q2', 'a', 'L'),
        'b': ('q2', 'b', 'L'),
        'x': ('q2', 'x', 'L'),
        '~': ('q0', '~', 'R')
    },
    'q3': {
        'x': ('q3', 'x', 'R'),
        'c': ('q2', 'x', 'L')
    },
    'q4': {
        'x': ('q4', 'x', 'R'),
        'a': ('q1', 'x', 'R'),
        'b': ('q5', 'x', 'R'),
        '~': ('qaccept', '~', 'R')
    },
    'q5': {
        'b': ('q5', 'b', 'R'),
        'x': ('q3', 'x', 'R'),
        'c': ('q2', 'x', 'L')
    }
}

turing_machine = DTM(
    states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'qaccept'},
    input_symbols={'a', 'b', 'c'},
    tape_symbols={'a', 'b', 'c', 'x', '~'},
    transitions=transitions ,
    initial_state='q0',
    blank_symbol='~',
    final_states={'qaccept'}
)
