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
from qiskit import *
from qiskit.circuit import QuantumCircuit

# Define the qubits and classical registers
qubits = QuantumRegister(6, 'q')
output = ClassicalRegister(2, 'out')

# Create the circuit
circuit = QuantumCircuit(qubits, output)

# Define the input values for the multiplexer
mux_input = QuantumRegister(2, 'mux_in')
circuit.add_register(mux_input)

# Define the input and output values for the adders
adder_input = QuantumRegister(2, 'add_in')
adder_output = QuantumRegister(1, 'add_out')
circuit.add_register(adder_input, adder_output)

# Create the 4:1 multiplexer
circuit.cx(qubits[0], mux_input[0])
circuit.cx(qubits[1], mux_input[1])
circuit.ccx(qubits[2], mux_input[0], mux_input[1])
circuit.cx(mux_input[1], qubits[3])

# Create the full adder
circuit.cx(qubits[4], adder_input[0])
circuit.cx(qubits[5], adder_input[1])
circuit.ccx(qubits[4], qubits[5], adder_output)
circuit.cx(qubits[4], qubits[5])

# Create the half adder
circuit.cx(qubits[3], adder_input[0])
circuit.cx(adder_output, adder_input[1])
circuit.cx(qubits[3], adder_output)

# Measure the output qubits and store in the classical register
circuit.measure(adder_output, output)

# Draw the circuit
circuit.draw()
