from flask import Flask, request, jsonify
from flask_cors import CORS
from qiskit import *
from qiskit import Aer
import numpy as np

app = Flask(__name__)

CORS(app)

@app.route('/', methods=["GET", "POST"])
def index():
    req = request.get_json(force=True)
    res = get_result(req['data'])
    return {'finalResult': res}

def get_result(q):
    # Create a Quantum Circuit acting on a quantum register of len(q) qubits
    circ = QuantumCircuit(len(q))

    # find max number of gates in qubit objects list
    gatesList = []
    for qubitObject in q:
        gatesList.append(qubitObject['gates'])
    maxLength = max([len(i) for i in gatesList])

    # add gates on the correct qubits in the correct order
    # going from top to bottom in the qubit matrix
    for i in range(0,maxLength):
        for qubit in q:
            try:
                print(qubit['gates'][i]['name'])
                if qubit['gates'][i]['name'] == "H":
                    circ.h(qubit['idx'])
                elif qubit['gates'][i]['name'] == "I":
                    circ.i(qubit['idx'])
                elif qubit['gates'][i]['name'] == "X":
                    circ.x(qubit['idx'])
                elif qubit['gates'][i]['name'] == "Y":
                    circ.y(qubit['idx'])
                elif qubit['gates'][i]['name'] == "Z":
                    circ.z(qubit['idx'])
                elif qubit['gates'][i]['name'] == "S":
                    circ.s(qubit['idx'])
                elif qubit['gates'][i]['name'] == "T":
                    circ.t(qubit['idx'])
                elif  qubit['gates'][i]['name'] == "CNOT":
                    circ.cx(qubit['idx'], qubit['gates'][i]['param'])
                elif qubit['gates'][i]['name'] == "CNOTtarget":
                    print()
                elif qubit['gates'][i]['name'] == "Rz":
                    circ.rz(np.pi, qubit['idx'])
                elif qubit['gates'][i]['name'] == "Rx":
                    circ.rz(np.pi, qubit['idx'])
                elif qubit['gates'][i]['name']== "Ry":
                    circ.rz(np.pi, qubit['idx'])
            except Exception as e:
                print(e)
            
    meas = QuantumCircuit(len(q), len(q))
    meas.barrier(range(len(q)))
    # map the quantum measurement to the classical bits
    meas.measure(range(len(q)), range(len(q)))

    # To simulate a circuit that includes measurement, 
    # we need to add measurements to the original circuit above.
    # The Qiskit circuit object supports composition using
    # the addition operator.
    qc = circ + meas
    print(circ)

    # Use Aer's qasm_simulator
    backend_sim = Aer.get_backend('qasm_simulator')

    # Execute the circuit on the qasm simulator.
    # We've set the number of repeats of the circuit
    # to be 1024, which is the default.
    job_sim = execute(qc, backend_sim, shots=1024)

    # Grab the results from the job.
    result_sim = job_sim.result()

    counts = result_sim.get_counts(qc)
    
    return counts

if __name__ == "__main__":
  app.run()