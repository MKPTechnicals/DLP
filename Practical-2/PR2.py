no_input_symbols = int(input("Enter number of Input Symbols: "))
input_symbols = input("Enter Input Symbols: ").split(" ")
no_states = int(input("Enter number of states: "))
in_state = int(input("Enter Initial state: "))
fin_state = input("Enter Final states: ").split(" ")
fin_state = [int(x) for x in fin_state]
transitions = {}

for state in range(no_states):
    transitions[state + 1] = {}
    for symbol in input_symbols:
        next_state = int(input(f"{state + 1}, '{symbol}' -> "))
        transitions[state + 1][symbol] = next_state

input_string = input("Enter the input string: ")

current_state = in_state

for symbol in input_string:
    if symbol not in input_symbols:
        print(f"Symbol '{symbol}' not in the input alphabet.")
        break
    if current_state not in transitions or symbol not in transitions[current_state]:
        print(f"No transition for state {current_state} on symbol '{symbol}'.")
        break
    current_state = transitions[current_state][symbol]

if current_state in fin_state:
    print("String accepted!")
else:
    print("String rejected.")
