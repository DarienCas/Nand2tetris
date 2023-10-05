![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/61f5eb0b-4d6e-4215-b0b3-e738f19b4822)
<br><p>Idealmente, todos los cálculos y comparaciones en la computadora se realizan inmediatamente, sin demora alguna, pero esa no es la realidad. En realidad, la razón radica en el nivel de hardware: tenemos que saber algo sobre el silicio y la electricidad. A nivel de hardware, ¿cómo representamos 1 y 0? No existe ninguna lógica binaria o decimal en la electricidad. Pero hay alto voltaje y bajo voltaje. Entonces el máximo podría ser 1 y el mínimo podría ser cero. En dispositivos como raspberry pi y Arduino, 3.3v-5v se considera alto, que es 1, bueno, si es inferior a ese rango se considerará bajo, que es 0. Este proceso de carga no ocurre instantáneamente, tomará En algún momento, no importa que sea un milisegundo o un nanosegundo, lleva algo de tiempo. Por tanto, debemos tener en cuenta el concepto de tiempo. En el área gris de la imagen 1, el sistema aún no está estabilizado, y si verificamos la producción en ese período de tiempo, es posible que no obtengamos la respuesta que esperábamos. Entonces podemos importar el concepto de reloj y solo vemos la salida fuera del área gris cuando el polvo se asienta.
<br>
Con la introducción del concepto de reloj, ahora tenemos dos formas diferentes de abordar los cálculos.</p>

<h2> Combinacional: </h2> <br>

![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/b625f241-723e-4e83-b624-b446294d6757)

<br><h2>Secuencial: </h2><br>

 ![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/4065c69c-0f99-4bcd-9a02-a66e88f3c391) 

<p> <br> En los últimos proyectos, cuando hablábamos de compuertas o cálculos de ALU, todos son combinatorios: salida[t] = función(in[t]), lo que significa que si le damos una entrada a la computadora, la computadora dará algo instantáneamente. Nuestro sistema no memorizará nada, solo está computando.

<br> Pero en la lógica secuencial de la imagen 3, en realidad estamos memorizando algo. Nuestra producción actual en realidad se basa en la entrada anterior. Este es un pequeño salto, pero significa que podemos recordar, ¡y que haya MEMORIA!

<br> Necesitamos algún tipo de puerta que pueda recordar cosas, ¿verdad? ¿Cómo pueden recordar las siliconas? Los científicos son realmente geniales, usan este bucle de puerta NAND para crear una unidad de memoria.

<br> En el estado inicial, aún no conocemos el resultado. </p><br>
![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/c47c40bc-232c-4a1c-8e3e-b139d4f138c2)
<br> Guardar un estado:
<br>
![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/cf678c30-553f-4800-a05a-814eb8da1a49)
<br>
Parece que acabamos de hacer un cambio en la entrada y no es gran cosa, pero lo interesante es que el estado ha sido memorizado. ingrese 0, 1, generará 1, 0.

Incluso si cambiamos la entrada nuevamente a 1, 1, la salida seguirá siendo 1, 0. (La situación x=1, y=1 puede verse como la situación estándar, lo que significa que la computadora no está guardando nada y el el valor guardado anteriormente no se puede modificar)

Y este estado será el mismo hasta que cambiemos la entrada para que sea x = 1, y = 0, ahora se han realizado cambios y la salida se cambiará a salida x = 0, salida y = 1.<br>
![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/2a3c0b77-4be5-4dcb-ad67-e5bb15d34809)
<br>Después de volver al estado estándar x = 1, y = 1, esta puerta flip-flop recordará el estado anterior para siempre hasta que realicemos cambios en la entrada. Sí, recordamos 1 bit de datos. Y este CHIP se llama chanclas.

Pero este flip-flop evita estrictamente la situación x = 0, y = 0, ya que esto generará resultados confusos. Si alimentamos 0 0 al sistema, es como si empezáramos una carrera, la salida de x corre hacia la entrada y, y la salida de y también corre hacia la entrada x. Quien llegue primero alterará la salida de esa puerta Nand a cero. Al hacerlo, la otra puerta permanecerá como 1, pero la salida nunca será ambas 1. Y en este caso la salida no está determinada por la lógica sino por la calidad de los cables en estas dos puertas nand, que no es lo que queremos.

Después de crear este FlipFlop, lo llamamos DFF y lo usamos como base de todos los cálculos posteriores, tal como usamos nand como base de todos los cálculos combinatorios. <br>
![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/4f476fb2-df8c-4ecc-97d5-641f925570a1)
<br>La implementación de DFF no es tan simple como describí anteriormente. La verdadera puerta DFF será algo así como en la imagen DFF GATE.

El DFF es bueno, pero todavía hay un problema más. El DFF solo puede recordar los datos en un ciclo de reloj, por ejemplo, si alimentamos 1 0, la salida será 01, y luego ingresamos 0 1, la salida será 10, ¿qué pasa si queremos guardar este estado 01? para siempre, sin importar que la entrada cambie o no?

Tendremos que usar algo llamado Bit. Descubramos cómo utilizar el DFF para memorizar datos en múltiples ciclos.<br>
![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/7aeaf14b-3ae0-4f6e-b93a-ac4646483774) <br>
![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/10514b55-025f-4ab9-85cc-f72c367051e4)<br>
Dff_input es Mux_output, si la carga es siempre 0, el resultado de Mux_output siempre será el dff_output anterior, y dff_input siempre será su entrada anterior, y nunca cambiará. Pero si la carga se cambia a 1, Mux_output se ingresará en este ciclo de reloj, pero la salida de DFF seguirá siendo la salida anterior, que no se puede cambiar en este ciclo, pero en el siguiente ciclo, se cambiará la salida. en la entrada actual.

Ahora tenemos un poco. El componente básico de la MEMORIA.
RAM es también un tipo de Memoria. Es volátil, lo que significa que si apagamos la computadora, todo lo que hay en la memoria RAM desaparece. Pero nuestro disco duro o unidad flash son memorias no volátiles, pueden almacenar estados y mantenerlos allí para siempre.

La RAM está compuesta por registros, los registros son una combinación de bits. Si tenemos Bits, lo tenemos todo. La imagen de abajo es un carnero. Ram tiene registros, puede tomar entradas, también tiene que tomar un dato muy importante, que es la dirección. El sistema tiene que saber en qué dirección queremos operar. En un solo ciclo de reloj, sólo se puede acceder y manipular una dirección de RAM, y esta es la regla.

Necesitaremos log 2 de n dígitos para representar la dirección, y esto es matemática.

"en" son los datos de entrada

“cargar” es decidir si lo guardamos

La “dirección” le dice a la RAM dónde guardar los datos o qué ranura queremos ver en este momento.
![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/52752a16-71e3-4d8c-8591-7b29d9d03745)<br>
La dirección es importada, al igual que el CONTADOR. Counter CHIP es algo que recuerda en qué línea de palabra/comando está trabajando la ROM.

Digamos que si comenzamos desde la línea 0 de la ROM (ubicación de memoria que guarda las instrucciones), en la mayoría de las situaciones nos gustaría ir a la línea 1 en el siguiente círculo, así podremos incrementar el contador cuando sea necesario. . También tenemos que crear algo que pueda obligar al contador a ir a una determinada línea, digamos 101, cuando el usuario así lo desee. entonces tenemos que obtener un bit de carga para indicarle al contador cuándo guardar datos y cambiar la salida de la siguiente ronda. Bueno, también tenemos que conseguir un bit de reinicio, que ponga el contador en 0 y permita que el sistema se reinicie. Ahora tenemos esta estructura:
![image](https://github.com/DarienCas/Nand2tetris/assets/144241018/c6621270-2b67-4397-ad9c-5ca673eebf5e)


