(LOOP)

@R1 
D=M

@END
D;JEQ 


D = D-1
@R1
M=D 

@R0
A=M 
M=-1

@R0
M=M+1

@LOOP
0;JMP

(END)

@END
0;JMP