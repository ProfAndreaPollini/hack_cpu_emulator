print("ok")

A=5
set_m(10)
assert get_m() == 10

set_rom(20)
assert get_rom() == 20

def a_instr(v:int):
    assert v <= 32767
    binary_string = f"0{v:>015b}"
    return int(binary_string,base=2)


COMP = {
    "D&A":"000000",
    "1": "01111",
    "0": "010101"
}

DEST = {
    None : (0,0,0),
    "D": (0,1,0),
}

def c_instr(comp:str, dest:str=None, jmp:str = None):
    assert comp in COMP.keys()
    assert dest in DEST.keys()

    return int(1,base=2)


PROGRAM = [
c_instr("1",dest="D"),
c_instr("1",dest="D")
]

def load_program():
    for i in range(RAM_SIZE):
        ROM[i] = 0

    for i in range(len(PROGRAM)):
        ROM[i] = PROGRAM[i]

load_program()
print(ROM[:10])

def run():
    while True:
        instruction = ROM[pc]# fetch()
        decode_execute(instruction)

run()