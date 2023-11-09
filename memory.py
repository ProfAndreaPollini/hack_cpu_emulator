
RAM_SIZE = 32*1024

RAM :[int] = []
ROM : [int] = []
A = 0
D = 0
pc = 0

def reset():
    global A,D
    for _ in range(RAM_SIZE):
        RAM.append(0)
    for _ in range(RAM_SIZE):
        ROM.append(0)
    A = 0
    D = 0


reset()

assert len(RAM) == RAM_SIZE
assert len(ROM) == RAM_SIZE

def get_m() :
    return RAM[A]

def set_m(value:int):
    RAM[A] = value

def get_rom():
    return ROM[A]

def set_rom(value:int):
    ROM[A] = value
