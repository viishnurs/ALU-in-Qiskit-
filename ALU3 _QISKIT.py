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
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister

# Define Quantum Registers
qreg = QuantumRegister(7, 'q')

# Define Classical Registers
creg = ClassicalRegister(2, 'c')

# Create Quantum Circuit
qc = QuantumCircuit(qreg, creg)

# 4x1 MUX
qc.cx(qreg[0], qreg[3])
qc.cx(qreg[1], qreg[3])
qc.ccx(qreg[2], qreg[0], qreg[3])
qc.ccx(qreg[2], qreg[1], qreg[3])
qc.barrier()


# Full Adder
qc.ccx(qreg[0], qreg[1], qreg[4])
qc.cx(qreg[0], qreg[1])
qc.ccx(qreg[2], qreg[1], qreg[4])
qc.cx(qreg[2], qreg[1])
qc.cx(qreg[0], qreg[2])
qc.ccx(qreg[0], qreg[1], qreg[4])
qc.barrier()

# OR Logical Block
qc.cx(qreg[0], qreg[5])
qc.cx(qreg[1], qreg[5])
qc.cx(qreg[2], qreg[5])
qc.barrier()

# AND Logical Block
qc.ccx(qreg[0], qreg[1], qreg[6])
qc.ccx(qreg[6], qreg[2], qreg[5])
qc.barrier()

# XOR Logical Block
qc.cx(qreg[0], qreg[6])
qc.cx(qreg[1], qreg[6])
qc.cx(qreg[2], qreg[6])
qc.barrier()

# XNOR Logical Block
qc.cx(qreg[0], qreg[5])
qc.cx(qreg[1], qreg[5])
qc.cx(qreg[2], qreg[5])
qc.x(qreg[5])
qc.barrier()

# 2x1 MUX
qc.cx(qreg[0], qreg[3])
qc.cx(qreg[1], qreg[3])
qc.cx(qreg[2], qreg[4])
qc.ccx(qreg[0], qreg[1], qreg[3])
qc.ccx(qreg[0], qreg[2], qreg[4])
qc.ccx(qreg[1], qreg[2], qreg[5])
qc.barrier()


# Half Adder
qc.cx(qreg[0], qreg[1])
qc.cx(qreg[2], qreg[1])
qc.barrier()

# 3-input AND Gate
qc.ccx(qreg[0], qreg[1], qreg[4])
qc.ccx(qreg[4], qreg[2], qreg[5])

# Measure qubits
qc.measure(qreg[3], creg[0])
qc.measure(qreg[4], creg[1])

# Draw circuit
qc.draw()
