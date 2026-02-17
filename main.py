import time

tape = list("_0000_")
head = 1
blank = ""
state = "q0"

def check_bounds():
    global head, tape
    if head < 0:
        tape.insert(0, blank)
        head = 0
    elif head >= len(tape):
        tape.append(blank)

def run_tm(table, tape, head, blank, state):
    while state not in ("q_accept", "q_reject"):
         check_bounds()
         
         symbol = tape[head]
         if (state, symbol) not in table:
             print("HALT")
             break
         
         next_state, write, move = table[(state, symbol)]
         
         tape[head] = write
         if move == "R":
             head += 1
         elif move == "L":
             head -= 1
         elif move == "N":
             pass
         
         state = next_state
         print(tape)

transitions = {
    ("q0", "0"): ("q0", "0", "R"),
    ("q0", "1"): ("q0", "1", "R"),
    ("q0", "_"): ("q1", "_", "L"),

    ("q1", "0"): ("q_accept", "1", "N"),
    ("q1", "1"): ("q1", "0", "L"),
}

tape = list("_0000_")
head = 1
blank = "_"
state = "q0"
run_tm(transitions, tape, head, blank, state)
