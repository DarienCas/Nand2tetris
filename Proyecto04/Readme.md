<p> En este proyecto se quiere ecribir y ejecutar algunos programas en lenguaje de máquina de bajo nivel.
  En particular, se planea escribir programas en el lenguaje ensamblador Hack, usare un ensamblador para traducir 
  Convertirlos en código binario y probar el código resultante.</p>
  <h2>FILL</h2>
  <p>Este programa ejecuta un bucle infinito que escucha el teclado. Cuando se presiona una tecla (cualquier tecla),
    el programa oscurece toda la pantalla escribiendo -1 en los registros que conforman cada píxel. Cuando no se presiona
    ninguna tecla, el programa borra la pantalla escribiendo 0 en esos mismos registros.

Para este programa usamos un bucle infinito que escuchara los cambios en el teclado, y otro ciclo para recorrer todos 
los registros que conforman los pixeles y cambiar su valor deacuerdo a la tecla presionada.</p>

<h2>MULT</h2>
<p>Las entradas de este programa son los valores almacenados en R0 y R1 (RAM[0] y RAM[1]). El programa calcula el producto
  R0 * R1 y almacena el resultado en R2 (RAM[2]). Se asume que R0 ≥ 0, R1 ≥ 0 y R0 * R1 < 32768 (el programa no necesita comprobar
    estas condiciones).

Para este programa usamos un bucle que va sumando en un acumulador el valor de R0, que se va sumando R1 veces. </p>
