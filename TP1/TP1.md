# Trabajo Practico N°1

### Asignatura: Sistemas de Computacion

**Facultad de Ciencias Exactas, Físicas y Naturales (UNC)**

---

* **Grupo:** Sudo Make A Sandwich
* **Profesores:** Miguel Angel Solinas y Javier Alejandro Jorge

---

### Integrantes y Contacto

| Nombre y Apellido | Correo Electrónico |
| :--- | :--- |
| **Sergio Fernandez Segovia** | _sergio.fernandez.segovia@mi.unc.edu.ar_ |
| **Enzo Leonel Laura Surco** | _enzo.laura.surco@mi.unc.edu.ar_ |
| **Saqib D. Mohammad Cabrejos** | _saqib.mohammad@mi.unc.edu.ar_ |


## Introduccion

Este trabajo practico se basa en poner en práctica los conocimientos sobre performance y rendimiento de los computadores. El trabajo consta de dos partes, la primera es utilizar benchmarks de terceros para tomar decisiones de hardware y la segunda consiste en utilizar herramientas para medir la performance de nuestro código y como extra jecutaremos un programa en un ESP32 y observaremos que pasa si variamos su frecuencia.


## Parte 1

Para la evaluacion del rendimiento de hardware se puede realizar pruebas de programa o benchmark lo cual consiste en  medir el tiempo que los diversos computadores tardan en ejecutar los programas que realmente el usuario va a utilizar posteriormente siendo este el mejor rendimiento para este usuario.
Y dependiendo de las tareas diarias podemos usar ciertos benchmarks especificos los cuales serian los mas representativos. 

## Benchmarks para Tareas Diarias:

| Tarea diaria                              | Benchmark recomendado            |
|------------------------------------------|---------------------------------|
| Compilacion de Codigo Fuente              | Phoronix Test Suite: build-linux-kernel              |
| Uso general (navegador, multitarea)      | Geekbench                       |
| Renderizado 3D / diseño                  | Cinebench                       |
| Edición de video / multimedia            | Blender Benchmark               |
| Juegos                                   | 3DMark / benchmarks de GPU      |

## Parte 2

En esta parte del trabajo practico analizaremos el rendimiento de distintos procesadores mas precisamente; Intel Core i5-13600K, AMD Ryzen 9 5900X 12-Core y AMD Ryzen 9 7950X 16-Core. Para ello utilizaremos las metricas proporcionadas por el benchmark:

Phoronix Test Suite: build-linux-kernel / https://openbenchmarking.org/test/pts/build-linux-kernel-1.15.0

|Procesador|Tiempo Promedio(seg)|
|----|----|
|Intel Core i5-13600K|	72 +/- 5|
|AMD Ryzen 9 5900X 12-Core|	76 +/- 8|
|AMD Ryzen 9 7950X 16-Core|50 +/- 6|

### Análisis de Rendimiento

El AMD Ryzen 9 7950X se posiciona como el procesador con rendimiento segun las metricas proporcionadas, eso significa que logran mejor tiempo de compilacion para el kernel de linux, su arquitectura y mayor cantidad de nucleos permiten procesamiento mas eficiente en cargas de trabajo. El Intel Core i5-13600K ofrece tambien un buen rendimiento manteniendose en una posicion intermedia siendo una opcion competitiva con un equilibrio entre costo y rendimiento
El AMD Ryzen 9 7950X se posiciona como el procesador con mejor rendimiento en esta prueba, logrando tiempos de compilación significativamente menores. Su arquitectura y mayor cantidad de núcleos permiten un procesamiento más eficiente en cargas de trabajo altamente paralelizables como la compilación del kernel. Y por ultimo el AMD Ryzen 9 5900X muestra un desempeño inferior para es tarea en comparacion con los otros dos; sigue siendo una opcion viable pero con un tiempo de compilacion mas alto indicando que no aprovecha tan bien sus recursos para esta tarea especifica


### ¿Cual es la aceleración cuando usamos un AMD Ryzen 9 7950X 16-Core?

Cuando hablamos de aceleracion tambien podemos hablar de speedup lo cual viene siendo, cuantas veces mas rapido es un procesador comparado con otro y para ello:


$Speedup = Aceleracion = \frac{EX_{cpu \ original}}{EX_{cpu \ mejorado}} = \frac{76}{50} = 1.52$

Esto significa que el AMD Ryzen 9 7950X 16-Core es $1.52$ veces mas rapido que el AMD Ryzen 9 5900X 12-Core en tareas de compilacion del kernel de Linux. Esta mejora se debe principalmente a la mayor cantidad de nucleos y a la arquitectura mas moderna del procesador.



## Parte 3

