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

# Create a quantum circuit with 8 qubits and 2 classical bits
qr = QuantumRegister(8)
cr = ClassicalRegister(2)
qc = QuantumCircuit(qr, cr)

# Define the input qubits
a = qr[0]
b = qr[1]
c = qr[2]

# Define the output qubits
s = qr[3]
f = qr[4]
o = qr[5]
a_out = qr[6]
h = qr[7]

# 4x1 MUX
qc.cx(a, s)
qc.cx(b, s)
qc.cx(c, f)
qc.cx(b, f)
qc.ccx(a, b, s)
qc.ccx(a, c, f)
qc.barrier()

# Full Adder
qc.cx(s, o)
qc.cx(c, o)
qc.ccx(s, c, f)
qc.barrier()

# OR logical block
qc.cx(s, o)
qc.cx(f, o)
qc.barrier()

# AND logical block
qc.ccx(s, f, a_out)
qc.barrier()

# XOR logical block
qc.cx(s, h)
qc.cx(f, h)
qc.barrier()

# XNOR logical block
qc.cx(h, a_out)
qc.barrier()

# 2x1 MUX
qc.cx(s, a_out)
qc.cx(h, a_out)
qc.barrier()

# Half Adder
qc.cx(s, h)
qc.cx(f, h)
qc.barrier()

# 3 input AND gate
qc.ccx(s, f, h)
qc.ccx(h, c, a_out)

# Measure the output qubits
qc.measure(a_out, cr[0])
qc.measure(o, cr[1])

# Draw the circuit
qc.draw()
