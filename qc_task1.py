from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# A quantum circuit with 2 qubits and 2 classical bits
# Classical bits store the final measurement result
qc = QuantumCircuit(2, 2)

# Both qubits start at |0⟩ automatically

# Step 1: Hadamard on qubit 0 → puts it in superposition
qc.h(0)

# Step 2: CNOT → qubit 0 is control, qubit 1 is target
# This entangles them
qc.cx(0, 1)

# Step 3: Measure both → collapse superposition to classical 0 or 1
qc.measure([0, 1], [0, 1])

# Simulate running this circuit 1000 times
simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()
print(result.get_counts())

# You will ALWAYS see only '00' and '11', never '01' or '10'
