from qiskit.quantum_info import Statevector
from qiskit import transpile, assemble, Aer
import numpy as np

def grade_ex_1(state):
    v = np.array([1, -1j] / np.sqrt(2))
    if Statevector(v) == state:
        print('Congratulations! You passed question 1')
    else:
        print('Hmm... not quite right, keep tyring!')
    return

def grade_ex_2(qc):
    state = Statevector.from_instruction(qc)
    v = np.array([1, 1j] / np.sqrt(2))
    if Statevector(v) == state:
        print('Congratulations! You passed question 2')
    else:
        print('Hmm... not quite right, keep tyring!')
    return

def grade_ex_3(state):
    v = np.array([1, 1] / np.sqrt(2))
    if Statevector(v) == state:
        print('Congratulations! You passed question 3')
    else:
        print('Hmm... not quite right, keep tyring!')
    return

def grade_ex_5_1(state):
    v = np.array([1,0,0, -1] / np.sqrt(2))
    if Statevector(v) == state:
        print('Congratulations! You passed question 5.1')
    else:
        print('Hmm... not quite right, keep tyring!')
    return

def grade_ex_5_2(state):
    v = np.array([0,1,1,0] / np.sqrt(2))
    if Statevector(v) == state:
        print('Congratulations! You passed question 5.2')
    else:
        print('Hmm... not quite right, keep tyring!')
    return

def grade_ex_5_3(state):
    v = np.array([0,-1,1,0] / np.sqrt(2))
    if Statevector(v) == state:
        print('Congratulations! You passed question 5.3')
    else:
        print('Hmm... not quite right, keep tyring!')
    return

def grade_ex_6(min_q, max_q):
    if min_q == 2 and max_q == 9:
        print('Congratulations! You passed question 6')
    else:
        print('Hmm... not quite right, keep tyring!')

def grade_ex_7(min_q, max_q):
    min_ans = [2]*5
    max_ans = [5, 65, 5444517870735015415413993718908291383297, 16777217, 1125899906842625]
    
    for idx, n in enumerate([3, 7, 133, 25, 51]):
        if min_ans[idx] != min_q(n):
            print('Hmm... not quite right, keep tyring!')
            return
        if max_ans[idx] != max_q(n):
            print('Hmm... not quite right, keep tyring!')
            return
    print('Congratulations! You passed question 7')
    return

def grade_ex_8(qc):
    ans = {'00000': (0.707106), '10000': (-0.707106)}
    try:
        state_dict = Statevector.from_instruction(qc).to_dict()
        is_valid = any([abs(v - ans[k]) > 0.0005 for k, v in state_dict.items()]) == False
    except Exception as e:
        is_valid = False

    if is_valid:
        print('Congratulations! You passed question 8')
    else:
        print('Hmm... not quite right, keep tyring!')
    return

def grade_ex_9(qc):
    ans = {'00000': (0.1767766952966368+0j), '00001': (0.1767766952966368+0j), '00010': (0.1767766952966368+0j), '00011': (0.1767766952966368+0j), '00100': (0.1767766952966368+0j), '00101': (0.1767766952966368+0j), '00110': (0.1767766952966368+0j), '00111': (0.1767766952966368+0j), '01000': (0.1767766952966368+0j), '01001': (0.1767766952966368+0j), '01010': (0.1767766952966368+0j), '01011': (0.1767766952966368+0j), '01100': (0.1767766952966368+0j), '01101': (0.1767766952966368+0j), '01110': (0.1767766952966368+0j), '01111': (0.1767766952966368+0j), '10000': (-0.1767766952966368+0j), '10001': (-0.1767766952966368+0j), '10010': (-0.1767766952966368+0j), '10011': (-0.1767766952966368+0j), '10100': (-0.1767766952966368+0j), '10101': (-0.1767766952966368+0j), '10110': (-0.1767766952966368+0j), '10111': (-0.1767766952966368+0j), '11000': (-0.1767766952966368+0j), '11001': (-0.1767766952966368+0j), '11010': (-0.1767766952966368+0j), '11011': (-0.1767766952966368+0j), '11100': (-0.1767766952966368+0j), '11101': (-0.1767766952966368+0j), '11110': (-0.1767766952966368+0j), '11111': (-0.1767766952966368+0j)}
    try:
        state_dict = Statevector.from_instruction(qc).to_dict()
        is_valid = any([abs(v - ans[k]) > 0.0005 for k, v in state_dict.items()]) == False
    except Exception as e:
        is_valid = False

    if is_valid:
        print('Congratulations! You passed question 9')
    else:
        print('Hmm... not quite right, keep tyring!')
    return

def grade_ex_10(dj_circuit):
    qasm_sim = Aer.get_backend('qasm_simulator')
    transpiled_dj_circuit = transpile(dj_circuit, qasm_sim)
    qobj = assemble(transpiled_dj_circuit)
    results = qasm_sim.run(qobj).result()
    answer = results.get_counts()
    if len(answer) != 1 or '0000' in answer:
        print('Hmm... not quite right, keep tyring!')
    else:
        print('Congratulations! You passed question 10')

def grade_ex_11(test):
    ans = [0,1,0,0,1]
    for i in ans:
        if test[i] != ans[i]:
            print('Hmm... not quite right, keep tyring!')
            return
    print('Congratulations! You passed question 10')
    return
