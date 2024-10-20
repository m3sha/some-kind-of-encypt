from qiskit import QuantumCircuit, Aer, execute
import random

def get_data_from_user():
    """Get data from the user for accidents, births, and deaths."""
    accidents = int(input("Enter the number of accidents (previous day): "))
    births = int(input("Enter the number of births (on that day): "))
    deaths = int(input("Enter the number of deaths (previous year, on that day): "))
    return accidents, births, deaths

def simulate_chess_game():
    """Simulate a chess game and return a random number of moves."""
    total_moves = random.randint(20, 100)  # Random moves for simulation
    return total_moves

def qubit_encrypt(hex_key):
    """Encrypt data using a simple Qubit-based method."""
    num_bits = len(hex_key) * 4  # Each hex digit represents 4 bits
    qc = QuantumCircuit(num_bits)  # Create quantum circuit with required qubits

    # Convert hex to binary and set qubits
    binary_key = bin(int(hex_key, 16))[2:].zfill(num_bits)  # Binary representation of hex
    for i, bit in enumerate(binary_key):
        if bit == '1':
            qc.x(i)  # Apply X gate to set qubit to |1>

    # Apply Hadamard to put qubits in superposition
    for i in range(num_bits):
        qc.h(i)

    # Measure the qubits
    qc.measure_all()

    # Simulate the circuit
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc, backend, shots=1024)
    result = job.result().get_counts()
    return result

def qubit_decrypt(hex_key):
    """Decrypt data using a simple reversible method."""
    # Convert hex back to decimal
    combined_value = int(hex_key, 16)
    
    # Perform a simple reverse operation
    # In a real scenario, you'd have the exact gates used and reverse them
    # For this simulation, we return the original combined value for demonstration
    return combined_value

# Main execution flow
def main():
    # User choice for encryption or decryption
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").strip().lower()

    if choice == 'e':
        # Step 1: Get data from the user
        accidents, births, deaths = get_data_from_user()

        # Step 2: Perform mathematical operations
        result1 = accidents * births
        result2 = result1 - deaths
        final_result = result2 + 1

        # Step 3: Simulate a chess game
        total_moves = simulate_chess_game()
        move_number = total_moves % 10

        # Step 4: Combine Values
        combined_value = final_result + move_number

        # Step 5: Convert to Hexadecimal
        hex_key = hex(combined_value)[2:]  # Get hex string without '0x'

        # Step 6: Get text input from the user for encryption
        text_to_encrypt = input("Enter the text to encrypt: ")

        # Step 7: Encrypt using Qubits
        encrypted_result = qubit_encrypt(hex_key)

        # Output results
        print(f"\nData Summary:")
        print(f"Accidents: {accidents}, Births: {births}, Deaths: {deaths}")
        print(f"Final Result: {final_result}, Total Moves: {total_moves}, Move Number: {move_number}")
        print(f"Combined Value: {combined_value}, Hex Key: {hex_key}")
        print(f"Encrypted Result: {encrypted_result}")

    elif choice == 'd':
        # Step 1: Get the hex key from the user for decryption
        hex_key = input("Enter the hex key used for encryption: ")

        # Step 2: Decrypt the result
        decrypted_result = qubit_decrypt(hex_key)
        print(f"Decrypted Result (Combined Value): {decrypted_result}")

    else:
        print("Invalid choice. Please choose 'e' to encrypt or 'd' to decrypt.")

# Run the program
if __name__ == "__main__":
    main()
