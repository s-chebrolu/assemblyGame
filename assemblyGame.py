import random

# Function to generate random 16-bit hexadecimal values (smaller range)
def generate_hex():
    return random.randint(0x0, 0xFFFF)  # 16-bit range from 0x0000 to 0xFFFF

# Function to ask a question and check the user's answer
def ask_question():
    rax = generate_hex()
    rbx = generate_hex()
    rcx = generate_hex()

    # Randomly select an operation to ask about
    operations = [
        'addq %rbx, %rax', 
        'addq %rcx, %rax', 
        'subq %rbx, %rax', 
        'subq %rcx, %rax',
        'leaq %rbx, %rax', 
        'movq %rbx, %rax',
        'sarq $1, %rax', 
        'andq %rbx, %rax', 
        'salq $1, %rax'
    ]
    operation = random.choice(operations)

    # Show the user the initial values of the registers
    print(f"Initial values:")
    print(f"%rax = {hex(rax)}")
    print(f"%rbx = {hex(rbx)}")
    print(f"%rcx = {hex(rcx)}")
    print(f"\nOperation: {operation}\n")

    # Calculate the correct answer based on the operation
    if operation == 'addq %rbx, %rax':
        correct_answer = rax + rbx
    elif operation == 'addq %rcx, %rax':
        correct_answer = rax + rcx
    elif operation == 'subq %rbx, %rax':
        correct_answer = rax - rbx
    elif operation == 'subq %rcx, %rax':
        correct_answer = rax - rcx
    elif operation == 'leaq %rbx, %rax':
        correct_answer = rax + rbx  # For simplicity, treat as addition
    elif operation == 'movq %rbx, %rax':
        correct_answer = rbx  # Just copy the value of %rbx into %rax
    elif operation == 'sarq $1, %rax':
        correct_answer = rax >> 1  # Arithmetic right shift by 1
    elif operation == 'andq %rbx, %rax':
        correct_answer = rax & rbx  # Bitwise AND
    elif operation == 'salq $1, %rax':
        correct_answer = rax << 1  # Arithmetic left shift by 1

    # Limit the result to 16 bits (since we're using smaller values)
    correct_answer &= 0xFFFF

    # Ask the player to enter their answer
    player_answer = input(f"What is the new value of %rax after the operation? (Enter in hexadecimal, e.g., 0x1a2b): ")

    # Check if the player's answer is correct
    if player_answer.lower() == hex(correct_answer).lower():
        print("Correct!\n")
    else:
        print(f"Incorrect! The correct answer was {hex(correct_answer)}.\n")

# Main game loop
def start_game():
    print("Welcome to the Assembly Arithmetic Practice Game (Smaller Values)!")
    while True:
        ask_question()
        play_again = input("Do you want to practice another problem? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

# Start the game
if __name__ == "__main__":
    start_game()

