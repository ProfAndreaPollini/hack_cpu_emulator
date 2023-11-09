
from instructions import c_instr, a_instr
from memory import fetch, get_a, get_d, init_memory, set_a, set_d, set_m, set_pc, update_pc


init_memory()




PROGRAM = [
c_instr("1",dest="D"),
c_instr("1",dest="D")
]


def decode_execute_a_instruction(instruction:int):
    set_a(instruction)
    update_pc()

def assign(v:int ,dest:int):
    dest_a = dest >> 2 & 0x1 == 1
    dest_d = dest >> 1 & 0x1 == 1
    dest_m = dest & 0x1 == 1

    print(f"assign {dest_a} {dest_d} {dest_m}    ")

    if dest_a:
        set_a(v)
    if dest_d:
        set_d(v)
    if dest_m:
        set_m(v)



def decode_execute_c_instruction(instruction:int):
    j = instruction & 0x7
    d = instruction >> 3 & 0x7
    c = instruction >> 6 & 0x7F

    print(f"dest = {d}")

    if d != 0:
        
        # dest = comp
        match f"{c:>07b}":
            case "0001100": 
                value = get_d()
                assign(value,d)
                update_pc()
            case "0011111":
                value = get_d() +1
                assign(value,d)
                update_pc()
            case "0111111":
                assign(1,d)
                update_pc()
    
    elif j !=0:
        match f"{c:>07b}":
            case "0101010": # unconditional jump
                set_pc(get_a())

def decode_execute(instruction:int):
    is_a_instruction  = instruction >> 15 & 0x1 == 0
    print(f"is a instruction? {is_a_instruction}")
    if is_a_instruction:
        decode_execute_a_instruction(instruction)
    else:
        decode_execute_c_instruction(instruction)

def cycle():
    instruction = fetch()# ROM[pc]# fetch()
    print(f"instruction = {instruction:>016b}")
    decode_execute(instruction)

