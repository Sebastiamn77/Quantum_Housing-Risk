import numpy as np

from qiskit import QuantumCircuit
from qiskit_algorithms import AmplitudeEstimation
from qiskit_algorithms import EstimationProblem
import time


def quantum_risk_estimate(crash_probability):
    start_time = time.time()
    print("\nRunning Quantum Amplitude Estimation...")


    theta = 2 * np.arcsin(
        np.sqrt(crash_probability)
    )


    # Create quantum state
    qc = QuantumCircuit(1)

    qc.ry(theta, 0)


    # Define problem
    problem = EstimationProblem(
        state_preparation=qc,
        objective_qubits=[0]
    )


    # Quantum estimator
    ae = AmplitudeEstimation(
        num_eval_qubits=5
    )


    result = ae.estimate(problem)


    quantum_probability = result.estimation


    difference = abs(
        quantum_probability - crash_probability
    )


    quantum_time = time.time() - start_time

    return quantum_probability, difference, quantum_time