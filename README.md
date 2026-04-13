# Quantum Computing Assignment – Task 1 & Task 2

## Overview

This repository contains implementations of two fundamental quantum computing tasks using **Qiskit**:

* **Task 1:** Construction and analysis of a 2-qubit quantum circuit demonstrating entanglement
* **Task 2:** Implementation of Grover’s Algorithm for a 3-qubit search problem

The goal of this project is to build both **conceptual understanding** and **practical intuition** for quantum circuits and quantum search algorithms.

---

## Task 1 – 2-Qubit Quantum Circuit

### Objective

To create a quantum circuit that demonstrates **superposition** and **entanglement**, and observe its measurement outcomes.

---

### Circuit Steps

1. Initialize both qubits in the default **|0⟩ state**
2. Apply a **Hadamard gate (H)** on qubit 0
3. Apply a **CNOT gate (CX)**:

   * Qubit 0 → control
   * Qubit 1 → target
4. Measure both qubits

---

### State Evolution

* **Initial State:**
  [
  |00⟩
  ]

* **After Hadamard:**
  [
  \frac{1}{\sqrt{2}}(|00⟩ + |10⟩)
  ]

* **After CNOT:**
  [
  \frac{1}{\sqrt{2}}(|00⟩ + |11⟩)
  ]

---

### Key Insight

This final state is a **Bell State**, which is an example of **quantum entanglement**:

* The qubits are no longer independent
* Measuring one qubit determines the other

---

### Output Observation

When the circuit is executed:

* Only **'00'** and **'11'** appear in results
* States **'01'** and **'10'** never occur

This confirms successful entanglement.

---

## Task 2 – Grover’s Algorithm (3 Qubits)

### Objective

To implement Grover’s Algorithm to search for a specific target state in an unsorted search space.

---

### Problem Setup

* **Number of qubits:** 3
* **Search space size:** 8 states (|000⟩ to |111⟩)
* **Target state:** `|101⟩`

---

### Why Grover’s Algorithm?

* Classical search requires checking each state → **O(N)**
* Grover’s Algorithm reduces complexity to → **O(√N)**

---

### Algorithm Components

#### 1. Oracle

* Identifies the target state (`101`)
* Flips its phase (marks it)

#### 2. Diffusion Operator

* Amplifies the probability of the marked state
* Suppresses all other states

---

### Implementation Details

#### Oracle Logic

* Applies X gates based on target bits
* Uses **CCX (Toffoli gate)** to create phase inversion
* Reverses X gates after marking

#### Diffusion Operator

* Applies:

  * Hadamard → X → CCX → X → Hadamard
* Reflects amplitudes about the average

---

### Grover Iterations

* Number of iterations used:
  [
  \approx \frac{\pi}{4} \sqrt{8} \approx 2
  ]

* The algorithm is repeated **2 times** for optimal amplification

---

### Output Observation

After simulation:

* The target state **'101'** appears with the **highest probability**
* Other states appear with significantly lower frequency

---

### Additional Outputs

* Measurement counts
* Most likely state
* Circuit depth
* Circuit diagram
* Histogram visualization

---

## Technologies Used

* Python
* Qiskit
* Qiskit Aer Simulator
* Matplotlib

---

## How to Run

### 1. Install Dependencies

```bash
pip install qiskit qiskit-aer matplotlib
```

### 2. Execute the Code

```bash
python task1.py
python task2.py
```

---

## File Structure

```
├── task1.py        # 2-qubit entanglement circuit
├── task2.py        # Grover’s algorithm implementation
├── README.md       # Project documentation
```

---

## Learning Outcomes

* Understanding **quantum superposition**
* Understanding **quantum entanglement**
* Implementation of **basic quantum circuits**
* Working of **Grover’s search algorithm**
* Insight into **quantum computational advantage**

---

## Notes

* Simulation is performed using **AerSimulator**
* Transpilation is applied in Task 2 for proper backend execution
* Histogram visualization helps in interpreting probability distributions

---

## Author

**Swastik Garg**

---

## Conclusion

This project demonstrates the transition from basic quantum circuit design to implementing a non-trivial quantum algorithm. It highlights how quantum mechanics enables computational advantages over classical methods in specific problem domains.

---
