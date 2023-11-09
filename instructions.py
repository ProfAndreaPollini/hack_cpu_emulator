
def a_instr(v:int):
    assert v <= 32767
    binary_string = f"0{v:>015b}"
    return int(binary_string,base=2)


COMP = {
    "D&A"   : "0000000",
    "D"     : "0001100",
    "1"     : "0111111",
    "0"     : "0101010",
    "D+1"   : "0011111"
}

DEST = {
    None : "000",
    "D": "010",
}

JMP = {
    None : "000",
    "JMP": "111"
   
}

def c_instr(comp:str, dest:str=None, jmp:str = None):
    assert comp in COMP.keys()
    assert dest in DEST.keys()
    assert jmp in JMP.keys()

    v_comp = COMP[comp]
    v_dest = DEST[dest]
    v_jmp = JMP[jmp]

    instruction = "111" + v_comp + v_dest + v_jmp

    print(instruction)
    return int(instruction ,base=2)