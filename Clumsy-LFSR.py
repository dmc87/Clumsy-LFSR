import random

def generate_random_seed():
    return format(random.randint(0, 255), '08b') # Makes a random 8 bit binary number

def lfsr(seed, clock):
    feedback_mask = int('10010011', 2)  # Feedback mask for a basic LFSR
    output = []

    for _ in range(clock):
        output.append(seed[-1])
        feedback = bin(int(seed, 2) & feedback_mask).count('1') % 2
        seed = str(feedback) + seed[:-1]

    return seed

def simple_lfsr():
    initial_seed = generate_random_seed()
    clock_input = random.randint(1, 100)  # Choose a random number of clock cycles
    session_key_decimal = int(lfsr(initial_seed, clock_input), 2)

    print(f"Original value: {int(initial_seed, 2)}")
    print(f"Resulting session key: {session_key_decimal}")

# Execute the program
simple_lfsr()
