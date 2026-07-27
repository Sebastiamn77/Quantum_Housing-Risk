import numpy as np

from qiskit import QuantumCircuit
from qiskit_algorithms import AmplitudeEstimation
from qiskit_algorithms import EstimationProblem
from qiskit.primitives import StatevectorSampler


print("Quantum Housing Risk Model")


# Classical probability from your data
crash_probability = 17 / 447

print("Classical probability:")
print(crash_probability)


theta = 2 * np.arcsin(np.sqrt(crash_probability))


# Quantum state preparation
qc = QuantumCircuit(1)

qc.ry(theta, 0)


# Define estimation problem
problem = EstimationProblem(
    state_preparation=qc,
    objective_qubits=[0]
)


print("Running Quantum Amplitude Estimation...")


# Create estimator
ae = AmplitudeEstimation(
    num_eval_qubits=3
)


result = ae.estimate(problem)


print("\nQuantum estimate:")
print(result.estimation)


print("\nClassical:")
print(crash_probability)


print("\nDifference:")
print(abs(result.estimation - crash_probability))