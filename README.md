# MCOC2020-P0
# Entrega 1: Mi computador

* Marca/modelo: Lenovo ideapad 330S-14IKB

* Tipo: Notebook

* Año Adquisición: 2019

* Procesador:
  * Marca/Modelo: Intel Core i5-8250U CPU
  * Velocidad Base: 1.6 GHz
  * Velocidad Máxima: 3.40 GHz
  * Numero de núcleos: 4 
  * Humero de hilos: 2
  * Arquitectura: x64
  * Set de instrucciones: Intel® SSE4.1, Intel® SSE4.2, Intel® AVX2
  
* Tamaño de las cachés del procesador
  * L1: 256 KB
  * L2: 1 MB
  * L3: 6 MB
  
* Memoria 
  * Total: 4 GB
  * Tipo de memoria:DDR4-2400
  * Velocidad: 2400 MHz
  * Numero de (SO)DIMM: 2
  
* Tarjeta Gráfica
  * Marca / Modelo: Intel (R) UHD Graphics 620
  * Memoria dedicada: 1 GB
  * Resolución: 1920 x 1080 x 60 hercios
  
* Disco 1: 
  * Marca: Intel Optane
  * Tipo: HDD
  * Tamaño: 932GB
  * Particiones: 3
  * Sistema de archivos: NTFS

  
* Dirección MAC de la tarjeta wifi: F8:A2:D6:E2:A9:41 
* Dirección IP (Interna, del router): 192.168.0.9
* Dirección IP (Externa, del ISP): 190.160.0.13
* Proveedor internet: VTR Banda Ancha S.A.


# DESEMPEÑO MATMUL:
   * ![rendimiento matmul](https://user-images.githubusercontent.com/69210578/89847750-be04ac80-db52-11ea-949c-1719dc1c13c1.png)


   * ¿Como difiere del gráfico del profesor?  -    Difiere bastante en el tiempo de ejecución de cada corrida, se observa que el el gráfico del profesor que para las matrices mas grandes se demora menos de 1 min, mientras que en mi gráfico se observa que se demora 1 minuno y en algunos casos mas de esto. Con respecto a las matrices mas pequeñas se nota una clara diferencia, donde la del profesor tiene una máxima duración de 0,1 ms mientras que mi gráfico demora entre 0,1 ms y 1 s para estos casos. Con respecto a la memoria, los graficos son similares.
   
   * ¿ A que se pueden deber estas diferencias?   -  A que cada procesador tiene un distinto intervalo de tiempo en el que un programa se ejecuta en el sistema opertivo. El procesador utilizado por el procesador es muy bueno, además de tener 32 GM de memoria RAM. Los rendimientos difieren y por ende mi computador tardará mas tiempo en ejecutar el código. 
   
   
   * El gráfico de memoria es lineal, pero el del tiempo transcurrido no ¿porque?    -   De forma automática cada vez que se ejecuta el código se vuelve a realizar todo nuevamente, desde el inicio, tardando una cantidad de tiempo diferente en cada iteración variando en en pocos segundos producto de los diversos programas que se utilicen en el mismo periodo de tiempo de ejecución del código. Mientras que el gráfico de memoria es lineal, mientras mas grande sea la matris mas bytes usará en la ejecución del programa, son directamente proporcionales. 
   * Nympy: 1.18.5
   * Versión Python: 3.8
   * Se utiliza solo un procesador.  
![Captura de pantalla (584)](https://user-images.githubusercontent.com/69210578/89850744-ed1e1c80-db58-11ea-916e-0aac0007c080.png)




# DESEMPEÑO MIMATMUL: 
(Solo se realizó hasta 500 por que tardó mucho tiempo: 1 hora y media aprox)

   * ![rendimiento mimatmul](https://user-images.githubusercontent.com/69210578/89849014-9cf18b00-db55-11ea-8e90-c4f5cc27750b.png)

   * ¿Como difiere del gráfico del profesor?  -    En este caso las diferencias no son tan grandes. Con respecto a la memoria utilizada es similar, y para el caso del tiempo transcurrido para matrices de 500x500 mi gráfico muestra un tiempo de casi 10 minutos por matriz, algo muy diferente al gráfico del ayudante, el que muestra que se demoró un poco mas de 1 min, tardándose 10 minutos para las matrices de 1.000x1.000. La clara diferencia en el tiempo tiene una respuesta similar a la anterior, los procesadores y memoria que cada computador son diferentes, resultando mas eficiente el del ayudante.
   

   * Imagen procesador: ![Captura de pantalla (582)](https://user-images.githubusercontent.com/69210578/89848029-80545380-db53-11ea-9195-f58466b05d5c.png)


# DESEMPEÑO DE INVERSA:
   * Tomando en cuenta que para los tres casos generales, evaluando de igual forma que las entregas anteriores, se llegó hasta la matriz 10.000X10.000 considerando la inversa de solo una matriz "A", pero para los gráficos específicos de cada tipo se corrió el programa hasta la matriz de  5.000X5.000, considerando dos matrices "A" y "B".
   * La información obtenida de cada tipo de dato se encuentra a continuación, donde para "np.double" y "np.longdouble" se considera la misma cantidad de memoria, ambos de tipo float64
   *
   ![Captura de pantalla (586)](https://user-images.githubusercontent.com/69210578/90087984-fab7db80-dceb-11ea-962d-ff5c83c2d131.png)
   ![Captura de pantalla (587)](https://user-images.githubusercontent.com/69210578/90087988-fc819f00-dceb-11ea-8e40-1196144ccf94.png)

   
  # Caso 1: Numpy.Linalg.inv
   
   
   * Gráfico desempeño para caso 1, utilizando las matrices random:
   *
   ![desempeño general caso 1](https://user-images.githubusercontent.com/69210578/90087455-cd1e6280-dcea-11ea-9226-d5a0dac57296.png)
   
   * Para este caso, no se logró ejecutar "np.half" ni "np.longdouble". El procesador trabajó a un 50% aprox, el nivel de uso de la CPU fue 59% aprox, El gráfico se presenta a continuación:
   * ![caso 1](https://user-images.githubusercontent.com/69210578/90088562-38693400-dced-11ea-98b8-3123bac08366.png)
   
   
   * Para las matrices mas pequeñas el tipo de dato "np.double" tardó mas, y ambos con un tiempo de 10 segundos para las matrices de 5.000x5.000, usando 1GB de memoria. "np.single" tiene dos peaks de tiempo para las matrices de 10x10 y 20x20
   
   ![desempeño caso 1- single](https://user-images.githubusercontent.com/69210578/90073961-317bfa80-dcc8-11ea-9d6b-0380ae62115b.png)
   ![desempeño caso 1-double](https://user-images.githubusercontent.com/69210578/90073968-350f8180-dcc8-11ea-9116-8e4d789ea70f.png)

   
   
   
  # Caso 2: Scipy.linalg.inv 
   * Gráfico desempeño para caso 3, utilizando las matrices random:
   
   ![desempeño general caso 2](https://user-images.githubusercontent.com/69210578/90087451-c8f24500-dcea-11ea-9f3b-f71273108f89.png)
   
   * Este resultó mas rápido que el caso 1. El prosesador trabajó a un 74% aproximadamente, el nivel de uso de la CPU fue de 50% aprox. El gráfico se presenta a continuación:
   * ![caso 2](https://user-images.githubusercontent.com/69210578/90088567-3b642480-dced-11ea-931a-d68348ba3be1.png)
   
   *  Con respecto a cada tipo de dato, el que demoró mas tiempo fue "np.longdouble" para matrices mas grandes de 5.000x5.000, "np.single" presenta una corrida que llama la atencion provocada posiblemente por los programas que corrian de forma paralela a python. "np.half" presenta menor tiempo para todas los tamaños de matrices.
   *
   ![desempeño caso 2-single](https://user-images.githubusercontent.com/69210578/90074163-a0595380-dcc8-11ea-9579-c7ae655576ea.png)
   ![desempeño caso2-double](https://user-images.githubusercontent.com/69210578/90074166-a3ecda80-dcc8-11ea-8ac4-9373405a07d3.png)
   ![desempeño caso2-half](https://user-images.githubusercontent.com/69210578/90074173-a64f3480-dcc8-11ea-927e-4ca46b001ba5.png)
   ![desempeño caso 2- longdouble](https://user-images.githubusercontent.com/69210578/90074228-c252d600-dcc8-11ea-8e37-3ddebbc342cd.png)

  # Caso 3: Scipy.linalg.inv usando overwrite=True
   
    
   * Gráfico desempeño para caso 3, utilizando las matrices random:
   
   ![desempeño general caso 3](https://user-images.githubusercontent.com/69210578/90087453-cabc0880-dcea-11ea-9e49-fc29dc2cee8b.png)
   
   * Para este caso, overwrite=True demostró resultar una ganancia en cuanto a desempeño, superior a los dos casos anteriores. La carga del Disco osciló entre 80% y 90% llegando al peak de 100% por un tiempo prolongado. El nivel de uso de la CPU fue de aproximadamente 30%. El gráfico se presenta a continuación:
   
   * ![caso 3](https://user-images.githubusercontent.com/69210578/90088573-3ef7ab80-dced-11ea-9caa-5d24bba7b12d.png)
   
   * Ahora con respecto a cada tipo de dato, el que demoró mas tiempo fue "np.longdouble" con 10 segundos para las matrices de 5.000x5.0000, seguido del tipo "np.double" . El tipo "np.half" fue el tipo de xxxx que mas demoró en el inicio, tardando casi 0.1 s para matrices mas pequeñas de 2x2.
   En el caso de "np.longdouble", se ve un peak que llama la atención en las matrices de 40x40, esto se puede deber a los programas que estaban corriendo simultaneamente a pyhton.
   
   *![desempeño caso 3- half](https://user-images.githubusercontent.com/69210578/90074293-e31b2b80-dcc8-11ea-84f1-f60c1e834f1a.png)
   ![desempeño caso 3- longdouble](https://user-images.githubusercontent.com/69210578/90074300-e7474900-dcc8-11ea-8092-fffb55c34215.png)
   ![desempeño caso 3-double](https://user-images.githubusercontent.com/69210578/90074314-ea423980-dcc8-11ea-9ebf-5c1468cb402f.png)
   ![desempeño caso 3-single](https://user-images.githubusercontent.com/69210578/90074319-ed3d2a00-dcc8-11ea-8b8f-091dd2c438a8.png)

   
   * ¿Qué algoritmo de inversión cree que utiliza cada método? - Se utiliza el algoritmo de Laplacian Matrix, este es un algoritmo con complejidad factorial, lo cual hace que resolver el sistema mediante este método no sea la mejor opción, debido a su demora. Matriz donde las columnas representan a las aristas del grafo y las filas a los vértices. El elemento (i,j) representa que la arista i incide en el vértice j. La diagonal esta compuesta por 2, y las diagonales adyacentes superior e inferior a la central estan compuestas por -1.
   * Además se utiliza la Invertible Matrix, para el caso 1 se utiliza la libreria de Numpy y en el caso 2 y 3 se utiliza la libreria Scipy. En ambos casos se resuelve un sistema lineal de ecuaciones.    
   
   * ¿Cómo incide el paralelismo y la estructura de caché de su procesador en el desempeño de cada caso?- El paralelismo es una función que realiza el procesador para ejecutar varias tareas al mismo tiempo, realizando varios cálculos simultáneamente (paralelismo de datos). Los sistemas informáticos suelen hacer uso de cachés,  ubicados cerca del procesador que almacenan las copias temporales de los valores de la memoria. Como se mencionó anteriormente el caso que presentó menos desempeño utilizando otras aplicaciones o programas mientras se corria el código fue el caso 1. 
   
 # Desempeño Ax=b(parte 1):
 ![desempeño Ax=B](https://user-images.githubusercontent.com/69210578/90299817-8ef97e00-de65-11ea-8952-477145346436.png)

 * Se logra apreciar un incremento exponencial del tiempo a medida que aumenta el tamaño de matrices. Pero desde el inico al fin, se demuestra que A_inv_npSolve tiene un mejor rendimiento. Para las matrices de 10.000x10.000 se demoró aproximadamente 20 segundos, mientras que A_invB_inv estuvo cercano a 1 minuto.
 
 
 
# Entrega 6
# Desempeño Ax=b (Parte 2)
![PAULINA GUERRA_Gráfico Ax=b(parte 2)](https://user-images.githubusercontent.com/69210578/90343112-9c387900-dfdb-11ea-9d73-6d0a08aa321f.png)
* Mejor desempeño:
  * Según lo mostrado en el gráfico, se pueden analizar distintas aristas. En primer lugar se ve como en un comienzo, para las matrices mas pequeñas hasta las matrices de 50x50 el que muestra un mejor desempeño es "A_invB_npSolve" de Numpy, superando por poco 0.1 ms. Pero desde las matrices de 50x50 hasta las matrices mas grandes es "A_invB_spSolve_pos_overwrite", solver de scipy que resuelve de forma mas rápida Ax=b,demorándose 8seg aprox. para las matrices de 10.000x10.000.  Esto demuestra que cuando se sabe que la matriz es definida positiva, el algoritmo es mas eficiente, para esto se escribe: "assume_a='pos'". 
  * Quedó demostrado que mayor es la eficiencia cuando se agrega "overwrite_a" donde permite sobre escribir los datos. Eficiencia ya demostrada previamente en la entrega anterior.
  
* Peor desempeño:
  * Con respecto a las funciones mas lentas o menos eficientes, destaca "A_invB_inv", donde se invierte la matriz A y luego se multiplica por el vector B de unos. Es una función claramente menos eficiente en comparación a las demas, ya que es mas larga, tediosa y no inmediatamente directa. Esta función es la que presenta mas tiempo en todos los casos, para matrices de 10.000x10.000 se demora casi 1 min. 
  * Pero en solo algunas partes la función "A_invB_spSolve_symmetric" supera en tiempo de demora a la función previamente comentada. Esto ocurre para las matrices mas pequeñas que se demora 80ms aproximadamente mientras que las demás funciones no superan los 3 ms. Luego tiene otro aumento para las matrices de 100x100 explicandose por un posible uso de otro programa de forma paralela a la ejecución del código. Para esta función el programa asume que la matriz es simétrica, lo que implica que los valores sobre y bajo la diagonal son los mismos. La función solve permite establecer el argumento "assume_a='sym'".
  * La segunda función mas lenta es  "A_invB_spSolve" durante casi todo el gráfico.
    
* Conclusión desempeño, orden de mejor a peor rendimiento:
  * 1º spSolve_pos_overwrite
  * 2º spSolve_pos
  * 3º npSolve
  * 4º spSolve_symetric
  * 5º spSolve
  * 6º Invertir y multiplicar
 
* El orden de rendimiento por función coincide con el del gráfico del profesor, pero ese muestra menos tiempo en la ejecución. Para la función "A_invB_inv" se demoró 20 seg. aproximadamente para las matrices de 10.000x10.000 mientras que en mi computador esta misma función demoró casi un minuto para el mismo tamaño de matrices. Lo que previamente se ha explicado por la diferencia de procesadores, memoria RAM y paralelismo en cada ordenador, siendo el computador del profesor mas eficiente que el mio.
* Ambos gráficos muestran que cuando se asume que la matriz es simétrica, esta función demora mas de lo habitual justo al comenzar para las matrices mas pequeñas de 2x2 o 4x4 (función representada en rojo)



