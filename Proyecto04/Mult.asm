// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)
//
// This program only needs to handle arguments that satisfy
// R0 >= 0, R1 >= 0, and R0*R1 < 32768.

// Put your code here.
@sum
M=0 //inicializa la suma

@R1
D=M
@count
M=D   //Inicializa el conteo al valor de Ram[1]
(LOOP)
    @count
    D=M
    @END
    D;JEQ  //verifica si el conteo es 0, si es asi, vaya a terminar (va a END)
    @R0
    D=M
    @sum
    M=M+D //agrega RAM[0] a la suma
    @count
    M=M-1 //resta de conteo 1
    @LOOP
    0;JMP //Realiza el bucle nuevo
(END)
    @sum
    D=M
    @R2
    M=D //Escribe sum en RAM[2]
