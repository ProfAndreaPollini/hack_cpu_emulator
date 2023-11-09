print(int("111",base=2))

v = 15
print(f"0{v:>015b}")

v = 8
first_bit = v >> 3 & 0x1
print(first_bit)