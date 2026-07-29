import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit
from qiskit_algorithms import EstimationProblem

# -----------------------------
# Same probability as your model
# -----------------------------

crash_probability = 0.60

theta = 2 * np.arcsin(np.sqrt(crash_probability))

# -----------------------------
# State preparation
# -----------------------------

state = QuantumCircuit(1)

state.ry(theta, 0)

# -----------------------------
# Amplitude Estimation Circuit
# -----------------------------

num_eval_qubits = 5

qc = QuantumCircuit(num_eval_qubits + 1)

# Put evaluation qubits into superposition
for i in range(num_eval_qubits):
    qc.h(i)

qc.barrier()

# State preparation on objective qubit
qc.ry(theta, num_eval_qubits)

qc.barrier()

qc.measure_all()

print(qc)

fig = qc.draw(
    output="mpl",
    style="iqp",
    fold=-1
)

fig.savefig(
    "graphs/quantum_circuit.png",
    dpi=600,
    bbox_inches="tight"
)

plt.close(fig)

print("Quantum circuit saved!")