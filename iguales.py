from sys import stdin, argv
from automata.tm.dtm import DTM
from automata.base.exceptions import AutomatonException

"""
L = { w#w / w pertenece Sigma* con Sigma = { a }
"""
las_transiciones={
    'q0': {
        'a': ('q1', 'x', 'R'),  # encuentro un a y la tacho
        '#': ('q6', '#', 'R'),  # no me quedan aes a la izquierda
    },
    'q1': {
        'a': ('q1', 'a', 'R'),  # encuentro una a y sigo buscando el #
        '#': ('q2', '#', 'R'),  # encontro el separador #
    },
    'q2': {
        'x': ('q2', 'x', 'R'),  # si veo una x sigo buscando una a
        'a': ('q3', 'x', 'R')   # si encuentro una a veo que viene despues
    },
    'q3': {
        'a': ('q4', 'a', 'L'), # hora de empezar a volver
        '~': ('q31', '~', 'L') # no queda nada al final, me voy a verificar que quedaron todas tachadas
    },
    'q31': {
        'x': ('q31', 'x', 'L'), # vamo!!
        '#': ('q31', '#', 'L'), # llego el separador
        '~': ('qacc', '~', 'R') # llegamos al pcpio y solo quedaban x y el separador
    },
    'q4': {
        'x': ('q4', 'x', 'L'), # solo quedan
        '#': ('q5', '#', 'L')  # volvimos al separador
    },
    'q5': {
        'a': ('q5', 'a', 'L'), # ahora solo aceptamos aes
        'x': ('q0', 'x', 'R')  # si aparece una x, hay que empezar a buscar de la a en adelante
    },
    'q6': {
        'x': ('q6', 'x', 'R'), # si volvimos al pcpio y encontramos una # solo quedan x a derecha
        '~': ('qacc', '~', 'R') #
    }
}

maquina = DTM(
    states={'q0', 'q1', 'q2', 'q3', 'q31', 'q4', 'q5', 'q6', 'qacc'},
    input_symbols={'a'},
    tape_symbols={'a', '#', 'x', 'y', '~'},
    transitions=las_transiciones,
    initial_state='q0',
    final_states={'qacc'},
    blank_symbol='~'
)

def evaluar(w, debug=False):
    if debug:
        for c in maquina.read_input_stepwise(w):
            c.print()
        return True
    return maquina.accepts_input(w)


if __name__ == '__main__':
    for w in stdin:
        res = False
        try:
            res = evaluar(w.strip(), '--debug' in argv) # strip saca el enter del final
        except AutomatonException as ex:
            print(ex.args)
        if (res):
            print('ACEPTA')
        else:
            print('RECHAZA')
