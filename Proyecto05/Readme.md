<b>Computer.hdl</b>: Este archivo define el chip Computer, que consta de una CPU, un ROM y una RAM. La CPU es responsable de buscar y ejecutar las instrucciones almacenadas en el ROM. La RAM se utiliza para almacenar los datos que la CPU necesita acceder durante la ejecución del programa.
<br><b>Memory.hdl</b>: Este archivo define el chip Memory, que proporciona acceso a la RAM y a los dispositivos de E/S mapeados en memoria del ordenador. El chip se puede leer o escribir, y se puede utilizar para acceder a la pantalla, al teclado y a otros dispositivos.
<br><b>CPU.hdl</b>: Este archivo define el chip CPU, que es el corazón del ordenador. La CPU es responsable de buscar y ejecutar instrucciones, realizar operaciones aritméticas y lógicas, y controlar el flujo de ejecución del programa.
Cómo funcionan los tres archivos juntos.

El chip Computer es el chip de nivel superior del sistema. Conecta los chips de la CPU, el ROM y la RAM. La CPU busca instrucciones del ROM y las ejecuta. La CPU también puede necesitar acceder a datos de la RAM durante la ejecución del programa.

El chip Memory se utiliza para almacenar datos y dispositivos de E/S mapeados en memoria. La CPU puede acceder a la RAM para leer y escribir datos, y puede acceder a los dispositivos de E/S mapeados en memoria para controlar la pantalla, el teclado y otros dispositivos.

El chip CPU es responsable de buscar y ejecutar instrucciones. La CPU también realiza operaciones aritméticas y lógicas, y controla el flujo de ejecución del programa.

<h5>Ejemplo de cómo funcionan los tres archivos juntos</h5>


Para ejecutar un programa, la CPU primero busca la instrucción del ROM en la dirección especificada por el contador de programa (PC). La CPU luego descodifica la instrucción y la ejecuta. Si la instrucción requiere que la CPU acceda a datos de la RAM, la CPU cargará los datos en sus registros. Si la instrucción requiere que la CPU escriba datos en la RAM, la CPU almacenará los datos en sus registros y luego los escribirá en la RAM.

Si la instrucción requiere que la CPU acceda a un dispositivo de E/S mapeado en memoria, la CPU emitirá la señal adecuada al dispositivo de E/S mapeado en memoria. Por ejemplo, si la instrucción requiere que la CPU muestre un carácter en la pantalla, la CPU emitirá una señal al dispositivo de E/S mapeado en memoria de la pantalla.

La CPU continúa buscando e ejecutando instrucciones hasta que encuentra una instrucción de parada. Cuando la CPU encuentra una instrucción de parada, deja de ejecutar el programa.

<h5>Explicación adicional</h5>

El chip Computer es el componente principal del sistema. Se encarga de conectar los otros chips y de coordinar su funcionamiento.

El chip Memory es responsable de almacenar los datos que necesita la CPU para ejecutar los programas. También proporciona acceso a los dispositivos de E/S mapeados en memoria.

El chip CPU es responsable de ejecutar las instrucciones del programa. También realiza operaciones aritméticas y lógicas, y controla el flujo de ejecución del programa.

Los tres chips funcionan juntos para crear un sistema informático que puede ejecutar programas.
