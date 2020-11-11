from flask import Flask
from qiskit import *
from qiskit import Aer
import numpy as np

def get_result(q):
    circ = QuantumCircuit(len(q))

    for qubit in q:
        idx = qubit['idx']
        for g in qubit['gates']:
            if g['name'] == "H":
                circ.h(idx)
            elif g['name'] == "CX":
                circ.cx(idx, g['param'])
            elif g['name'] == "RZ":
                circ.rz(np.pi, idx)
         

    meas = QuantumCircuit(len(q), len(q))
    meas.barrier(range(len(q)))
    # map the quantum measurement to the classical bits
    meas.measure(range(len(q)), range(len(q)))

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

app= Flask(__name__)
@app.route('/')
def index():
  q = [{"idx":0, "gates": [{"name":"CX", "param": 1}]}, {"idx":1, "gates": [{"name":"H", "param":""}]}]
  res = get_result(q)
  # return "<h1>Welcome to CodingX</h1>"
  return res