
from hack import cycle
from instructions import a_instr, c_instr
from memory import get_d, init_memory,get_m,get_rom, load_program, set_a,set_m,set_rom


def test_memory_access():
    init_memory()
    set_a(5)

    set_m(10)
    assert get_m() == 10

    set_rom(20)
    assert get_rom() == 20


def test_instructions():
    v = 27
    assert a_instr(v) == 27

def test_d_comp():
    comp_instructions_data = [
        ("D","E300"),
        ("0","EA80"),
        ("1","EFC0")
    ]
    for instruction_in, instruction_out in comp_instructions_data:
        i = c_instr(instruction_in)
        assert i == int(instruction_out,base=16)
    

def test_cpu_run():
    init_memory()
    instructions = [
        c_instr("1","D"),
        c_instr("D+1","D"),
        c_instr("0",jmp="JMP")
    ]    
    load_program(instructions)
    cycle()

    print(f"{get_d()=}")

    assert get_d() == 1
    cycle()
    assert get_d() == 2
    cycle()
    cycle()
    assert get_d() == 1

if __name__ == '__main__':
    test_memory_access()
    test_instructions()
    test_d_comp()
    test_cpu_run()