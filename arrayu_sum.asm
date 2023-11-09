


@sum
M=0

(FOR_LOOP)
@R1
D=M

@END
D;JEQ

@R1
M=M-1


@sum
D=M

@R0
A=M
D=D+M
@sum
M=D

@R0
M=M+1

@FOR_LOOP
0;JMP

(END)
@END
0;JMP