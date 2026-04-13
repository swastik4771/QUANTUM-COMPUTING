# ============================================================
# TASK 2: Grover's Algorithm — 3-qubit implementation
# Target state: |101⟩
# ============================================================

from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# ============================================================
# FUNCTION 1: ORACLE
# Marks the target state by flipping its phase
# ============================================================
def build_oracle(n_qubits, target_state):
    oracle = QuantumCircuit(n_qubits)

    # Flip qubits where target has 0
    for i, bit in enumerate(reversed(target_state)):
        if bit == '0':
            oracle.x(i)

    # Apply CCZ using H + CCX + H
    oracle.h(n_qubits - 1)
    oracle.ccx(0, 1, 2)
    oracle.h(n_qubits - 1)

    # Undo X gates
    for i, bit in enumerate(reversed(target_state)):
        if bit == '0':
            oracle.x(i)

    return oracle


# ============================================================
# FUNCTION 2: DIFFUSION OPERATOR
# Performs amplitude amplification
# ============================================================
def build_diffusion(n_qubits):
    diffusion = QuantumCircuit(n_qubits)

    diffusion.h(range(n_qubits))
    diffusion.x(range(n_qubits))

    diffusion.h(n_qubits - 1)
    diffusion.ccx(0, 1, 2)
    diffusion.h(n_qubits - 1)

    diffusion.x(range(n_qubits))
    diffusion.h(range(n_qubits))

    return diffusion


# ============================================================
# MAIN PROGRAM
# ============================================================

n_qubits = 3
target = '101'
n_iterations = 2  # ≈ (π/4)*√8

# Build components
oracle = build_oracle(n_qubits, target)
diffusion = build_diffusion(n_qubits)

# Create circuit
qc = QuantumCircuit(n_qubits, n_qubits)

# Step 1: Create superposition
qc.h(range(n_qubits))

# Step 2: Apply Grover iterations
for _ in range(n_iterations):
    qc.compose(oracle, inplace=True)
    qc.compose(diffusion, inplace=True)

# Step 3: Measurement
qc.measure(range(n_qubits), range(n_qubits))

# ============================================================
# SIMULATION
# ============================================================

simulator = AerSimulator()

# 🔴 Important: Transpile before running
qc = transpile(qc, simulator)

result = simulator.run(qc, shots=1000).result()
counts = result.get_counts()

# ============================================================
# OUTPUT
# ============================================================

print("Measurement Results:", counts)
print("Most Likely State:", max(counts, key=counts.get))
print("Circuit Depth:", qc.depth())

print("\nCircuit Diagram:\n")
print(qc.draw())

# ============================================================
# VISUALIZATION
# ============================================================

plot_histogram(counts)
plt.show()
