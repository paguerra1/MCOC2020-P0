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

   # Caso 1: Numpy.Linalg.inv
   
   ![desempeño caso 1- single](https://user-images.githubusercontent.com/69210578/90073961-317bfa80-dcc8-11ea-9d6b-0380ae62115b.png)
   ![desempeño caso 1-double](https://user-images.githubusercontent.com/69210578/90073968-350f8180-dcc8-11ea-9116-8e4d789ea70f.png)

   
   
   
   # Caso 2: Scipy.linalg.inv 
   ![desempeño caso 2-single](https://user-images.githubusercontent.com/69210578/90074163-a0595380-dcc8-11ea-9579-c7ae655576ea.png)
   ![desempeño caso2-double](https://user-images.githubusercontent.com/69210578/90074166-a3ecda80-dcc8-11ea-8ac4-9373405a07d3.png)
   ![desempeño caso2-half](https://user-images.githubusercontent.com/69210578/90074173-a64f3480-dcc8-11ea-927e-4ca46b001ba5.png)
   ![desempeño caso 2- longdouble](https://user-images.githubusercontent.com/69210578/90074228-c252d600-dcc8-11ea-8e37-3ddebbc342cd.png)

   # Caso 3: Scipy.linalg.inv usando overwrite=True
   
   
   * ¿Qué algoritmo de inversión cree que utiliza cada método? - Se utiliza el algoritmo de Matriz Laplaciana, este es un algotires un algoritmo con complejidad factorial, lo cual hace que resolver el sistema mediante este método no sea la mejor opción, debido a su demora.
   
   * ¿Cómo incide el paralelismo y la estructura de caché de su procesador en el desempeño de cada caso?
