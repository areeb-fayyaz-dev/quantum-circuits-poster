from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Circuit 1: Bell State (Entanglement)
def create_bell_circuit():
    qr = QuantumRegister(2, 'q')
    cr = ClassicalRegister(2, 'c')
    qc = QuantumCircuit(qr, cr, name='Bell State')
    
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    qc.measure(qr, cr)
    
    return qc

# Circuit 2: Superposition
def create_superposition_circuit():
    qr = QuantumRegister(1, 'q')
    cr = ClassicalRegister(1, 'c')
    qc = QuantumCircuit(qr, cr, name='Superposition')
    
    qc.h(qr[0])
    qc.measure(qr, cr)
    
    return qc

# Circuit 3: Three-Qubit GHZ State
def create_ghz_circuit():
    qr = QuantumRegister(3, 'q')
    cr = ClassicalRegister(3, 'c')
    qc = QuantumCircuit(qr, cr, name='GHZ State')
    
    qc.h(qr[0])
    qc.cx(qr[0], qr[1])
    qc.cx(qr[1], qr[2])
    qc.measure(qr, cr)
    
    return qc

# Simulate and get results
def simulate_circuit(qc, shots=1000):
    simulator = AerSimulator()
    job = simulator.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts()
    return counts

# Main execution
if __name__ == "__main__":
    circuits = {
        'Bell State': create_bell_circuit(),
        'Superposition': create_superposition_circuit(),
        'GHZ State': create_ghz_circuit()
    }
    
    for name, circuit in circuits.items():
        print(f"\n{'='*50}")
        print(f"Circuit: {name}")
        print(f"{'='*50}")
        
        # Draw circuit
        circuit.draw(output='mpl', scale=2, filename=f'circuit_{name.replace(" ", "_").lower()}.png')
        
        # Simulate
        counts = simulate_circuit(circuit)
        print(f"Results: {counts}")
        
        # Plot results
        plot_histogram(counts)
        plt.savefig(f'histogram_{name.replace(" ", "_").lower()}.png', dpi=150, bbox_inches='tight')
        plt.close()
        
        print(f"✓ Saved circuit_{name.replace(' ', '_').lower()}.png")
        print(f"✓ Saved histogram_{name.replace(' ', '_').lower()}.png")
    
    print("\n" + "="*50)
    print("✅ ALL CIRCUITS CREATED SUCCESSFULLY!")
    print("="*50)
