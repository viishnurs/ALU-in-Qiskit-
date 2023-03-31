# Importing standard Qiskit libraries
from qiskit import QuantumCircuit, transpile
from qiskit.tools.jupyter import *
from qiskit.visualization import *
from ibm_quantum_widgets import *
from qiskit_aer import AerSimulator

# qiskit-ibmq-provider has been deprecated.
# Please see the Migration Guides in https://ibm.biz/provider_migration_guide for more detail.
from qiskit_ibm_runtime import QiskitRuntimeService, Sampler, Estimator, Session, Options

# Loading your IBM Quantum account(s)
service = QiskitRuntimeService(channel="ibm_quantum")

# Invoke a primitive inside a session. For more details see https://qiskit.org/documentation/partners/qiskit_ibm_runtime/tutorials.html
# with Session(backend=service.backend("ibmq_qasm_simulator")):
#     result = Sampler().run(circuits).result()



from qiskit import QuantumCircuit, execute, Aer

# Define the circuit
circuit = QuantumCircuit(14, 5)

# Define the input qubits
a = 0
b = 1
c = 2

# Define the output qubits
out1 = 3
out2 = 4

# Define the gates
# OR gate
circuit.cx(a, out1)
circuit.cx(b, out1)
circuit.barrier()
# XOR gate
circuit.cx(a, out2)
circuit.cx(b, out2)
circuit.cx(out1, out2)
circuit.barrier()

# XNOR gate
circuit.cx(a, out1)
circuit.cx(b, out1)
circuit.x(out1)
circuit.cx(a, out2)
circuit.cx(b, out2)
circuit.x(out2)
circuit.cx(out1, out2)
circuit.barrier()

# AND gate
circuit.ccx(a, b, out1)
circuit.barrier()

# 3-input AND gate
circuit.ccx(a, b, 5)
circuit.ccx(5, c, out1)
circuit.barrier()

# 4:1 MUX
circuit.cx(c, 6)
circuit.cx(a, 7)
circuit.cx(b, 8)
circuit.ccx(c, 7, 9)
circuit.ccx(c, 8, 10)
circuit.ccx(6, 9, out1)
circuit.ccx(6, 10, out2)
circuit.barrier()

# 2:1 MUX
circuit.cx(b, 11)
circuit.cx(a, 12)
circuit.ccx(c, 12, 13)
circuit.ccx(11, 13, out1)
circuit.ccx(a, b, out2)
circuit.barrier()

# Full adder
circuit.cx(a, 7)
circuit.cx(b, 7)
circuit.cx(c, 8)
circuit.ccx(a, b, 9)
circuit.ccx(b, c, 10)
circuit.ccx(a, c, 11)
circuit.cx(9, 12)
circuit.cx(10, 12)
circuit.cx(11, 12)
circuit.ccx(9, 10, out1)
circuit.ccx(9, 11, out2)
circuit.barrier()

# Half adder
circuit.cx(a, 7)
circuit.cx(b, 7)
circuit.cx(a, 8)
circuit.cx(b, 8)
circuit.ccx(a, b, out1)

# Measure the output qubits
circuit.measure(out1, 0)
circuit.measure(out2, 1)


circuit.draw()
