Desarrollo
En primer lugar, debemos tener claro que vamos a desarrollar un ensamblador en un lenguaje de alto nivel (en nuestro caso Python) que nos permitirá traducir comandos como @128, D=M, D;JMP, a unos y ceros. Pero al ver en los códigos pong.asm, max.asm, etc vemos, que hay un montón de nombres como "temp" o "WHILELOOP" entre otros, por lo que necesitaremos preprocesar el archivo antes de comenzar a traducir. Necesitamos guardar el número de línea de (WHILELOOP) en algún arreglo, y también tendremos que devolverlo cuando se llame en @WHILELOOP.

También, es necesario asignar ubicaciones de memoria para "value" y "temp". Podemos usar las ubicaciones desde R16 en adelante para almacenar esas variables. Entonces, cuando se revise el código, la primera vez que nos encontremos con "value" sabemos que debemos darle una ranura en la memoria para un futuro uso, y la próxima vez que veamos este "valor", solo devolveremos la ubicación de memoria que le asignamos.

Pero esto no lo podemos hacer simplemente revisando el archivo, debemos revisar el archivo dos veces. La primera vez limpiamos los comentarios y también limpiamos las etiquetas, pero cuando limpiamos las etiquetas como (WHILELOOP.), hacemos un seguimiento de su número de línea y lo guardamos en un arreglo. Después de este proceso, sabemos exactamente qué devolver en la segunda ronda de lectura del archivo cuando se llama a @WHILELOOP.


De este modo, para resolver este problema se tuvo que separar en tres partes el desarrollo:

Parser. Se usa para leer en el archivo, guardar los comandos, guardar el número de línea, eliminar comentarios, después de adquirir todos los comandos, parser puede usar una variable @index para controlar el proceso de decodificación (commands[@index] será el comando actual).

Code. Después de obtener una línea del analizador, la evaluamos y la comparamos con nuestro Regex para ver qué tipo de instrucción es: Instrucción A o Instrucción C. Luego escriba los códigos binarios correspondientes en el archivo de pirateo.

Assembler. Crea un code y un parser, para luego utilizarlos y finalizar todo el proceso.

Para que logre funcionar escribir:  python3 Assembler.py archivo_de_entrada.asm
ejemplo: 
python3 Assembler.py Add.asm
