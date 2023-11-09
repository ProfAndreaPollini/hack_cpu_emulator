
RAM_SIZE = 32*1024

RAM :[int] = []
ROM : [int] = []
A = 0
D = 0
pc = 0

def reset():
    """
    Resets the memory by initializing all the values in RAM and ROM to 0.
    """
    global A,D
    for _ in range(RAM_SIZE):
        RAM.append(0)
    for _ in range(RAM_SIZE):
        ROM.append(0)
    A = 0
    D = 0


def init_memory():
    """
    Initializes the memory by calling the reset function.
    """
    reset()

reset()

assert len(RAM) == RAM_SIZE
assert len(ROM) == RAM_SIZE

def update_pc(v:int = 1):
    global pc
    pc = pc + v

def set_pc(v:int):
    global pc
    pc = v

def get_d()-> int:
    global D
    return D

def set_d(v:int):
    global D
    D = v



def set_a(a: int):
    global A
    A = a

def get_a() -> int:
    global A
    return A

def get_m() :
    """
    Returns the value stored in the memory at the address pointed by the A register.
    """
    return RAM[A]

def set_m(value:int):
    """
    Sets the value of the memory at the address pointed by the A register to the given value.
    """
    RAM[A] = value

def get_rom():
    """
    Returns the value stored in the ROM at the address pointed by the A register.
    """
    return ROM[A]

def set_rom(value:int):
    """
    Sets the value of the ROM at the address pointed by the A register to the given value.
    """
    ROM[A] = value


def load_program(program: [int]):
    for i in range(RAM_SIZE):
        ROM[i] = 0

    for i in range(len(program)):
        ROM[i] = program[i]


def fetch():
    global pc
    return ROM[pc]