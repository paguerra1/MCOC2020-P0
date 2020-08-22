# Entrega 7: Matrices Dispersas y Complejidad Computacional
* Tomar en cuenta que se realizaron 4 corridas para tamaños de matrices crecientes hasta 8.192 por tiempo de ejecución
# Complejidad Algoritmica de MATMUL
![Complejidad MATMUL_Llena](https://user-images.githubusercontent.com/69210578/90947875-50d10100-e407-11ea-88f8-4718148f71b3.png)  ![Complejidad MATMUL_Dispersa](https://user-images.githubusercontent.com/69210578/90947882-54fd1e80-e407-11ea-8a11-9a77d72f3437.png)



* COMENTAR DIFERENCIAS ENTRE LOS ALGORITMOS DE MATRICES LLENAS Y DISPERSAS
  * Se observa como el tiempo de ensamblado es similar (max 1 min aprox), mientras se muestran claras diferencias en el tiempo de solución del algoritmo MATMUL. Para las matrices mas grandes la dispersa se demora menos de 0.1 s y las matrices llenas casi un minuto.
  * El tiempo de solucion y de ensamblado de las matrices dispersas muestra una uniformidad. Para matrices llenas se observan discontinuidades tamaños de N= 8 y 30 en el tiempo de solución.
  * Tiempo de solución de matriz dispersa se muestra aparentemente constante, variando entre [0.1ms,0.1s] y para matriz llena se observa una variación entre [menos de 0.1ms,casi 1 min].
  
* COMPLEJIDAD ASINTÓTICA ENSAMBLADO/SOLUCIÓN EN AMBOS CASOS
  * Para el caso de tiempo de solución de matrices llenas el comportamiento de complejidad asintotico es  O(N³), con esto e a medida que N aumenta, el tiempo de solución crecera, y con esto tambien el tiempo que tarda el software en resolver la operacion. Esto es esperable ya que son matrices laplacianas llenas se ceros. Para el caso de matrices dispersas es O(N²)
  * En cuanto al ensamblaje, ambas presentan una complejidad asinttica O(N²) 
  * La complejidad asintótica que se observó en mejor estado fuela complejidad algorítmica de MATMUL con la matriz Laplaciana disperspersa.


* COMO AFECTA EL TAMAÑO DE LAS MATRICES AL COMPORTAMIENTO APARENTE
   * El tamaño de ejecución es directamente proporcional al tamaño de matriz, por lo que mientras mas grande sea N, mas tiempo tardará en ejecutarse. Para matrices N<1000 se obsrva mayor uniformidad mientras que para matrices N<100 no se muestra constancia en ninguno de los casos.
   
* QUE TAN ESTABLES SON LAS CORRIDAS
   * Se observa una estabilidad a partir de las matrices 100 en adelante, donde el algoritmo se muestra de forma mas eficiente repitiendo el codigo. Las corridas de la complejidad algoritmica para matrices dispersas muestran mas estabilidad, mientras que para las matrices llenas muestran mayores diferencias.

# Complejidad Algoritmica de SOLVE

![Complejidad SOLVE_Dispersa](https://user-images.githubusercontent.com/69210578/90947877-529ac480-e407-11ea-9ee2-b588b531961e.png)
![Complejidad SOLVE_Llena](https://user-images.githubusercontent.com/69210578/90947878-53335b00-e407-11ea-842d-e604e11976b0.png)

* COMENTAR DIFERENCIAS ENTRE LOS ALGORITMOS DE MATRICES LLENAS Y DISPERSAS
   * Se observa que el tiempo de solucion para la matriz dispersa se muestra relativamente constante en el tiempo entre [0.1ms, 10ms] a excepcion de una de las corridas que presentó una leve discontinuidad para la matriz 500, debido posiblemente a programas que se abrieron de forma paralela. La matriz llena presenta discontinuidades al comienzo hasta la matriz N=50 aprox. En general el tiempo esta dentro del rango de [0.1ms,10ses]
   * Tiempo se ensamblado se muestra similar en ambos casos, menos de 1 min en cada caso. 
   
* COMPLEJIDAD ASINTÓTICA ENSAMBLADO/SOLUCIÓN EN AMBOS CASOS
   * Para ambos casos el tiempo de ensamblado de matrices presenta un comportamiento de complejidad asintotico O(N²).
   * En cueanto al tiempo de solucion: matrices dispersas presentan un comportamiento O(N) y matrices llenas  O(N²).
   
* COMO AFECTA EL TAMAÑO DE LAS MATRICES AL COMPORTAMIENTO APARENTE
   * Cuando se tiene un N pequeño el tiempo de ensamblado y de solución es muy elevado,producto del paraelismo, el computador esta realizando diversas acciones en un inicio
   * Tiempo de solución para las matrices dispersas se muestra relativamente constante con relacion al aumento de tamaño de matriz.
   
* QUE TAN ESTABLES SON LAS CORRIDAS
   * Para el tiempo de ensamblado se observan corridas mas estables para ambos casos
   * En cuanto al tiempo de solucion las matrices dispersas muestran menos estabilidad. y las matrices llenas muestra una completa estabilidad a partir de la matriz N=500
   

# Complejidad Algoritmica de INV

![Complejidad INV_Dispersa](https://user-images.githubusercontent.com/69210578/90947880-54648800-e407-11ea-823b-886404e5b91f.png)
![Complejidad INV_Llena](https://user-images.githubusercontent.com/69210578/90947881-54648800-e407-11ea-9e72-876b7f084f5b.png)

* COMENTAR DIFERENCIAS ENTRE LOS ALGORITMOS DE MATRICES LLENAS Y DISPERSAS
   * Tiempo de ensamblado es similar en ambos casos (max 1 min aprox), aunque la matriz dispersa tarde un poco mas en un comienzo.
   * Tiempo de solucion: Para la matriz llena se observa que las matrices mas pequeñas demoran mucho mas de lo habitual casi 1 seg mientras que en matrices dispersas el tiempo es de 10 ms.
   * El tiempo máximo de solución es similar cercano al minuto, pero demora un poco menos para el caso de las matrices llenas.
* COMPLEJIDAD ASINTÓTICA ENSAMBLADO/SOLUCIÓN EN AMBOS CASOS
   * Para ambos casos el tiempo de ensamblado de matrices presenta un comportamiento de complejidad asintotico O(N²).
   *  En cueanto al tiempo de solucion: matrices dispersas presentan un comportamiento O(N) y matrices llenas O(N³).
   
* COMO AFECTA EL TAMAÑO DE LAS MATRICES AL COMPORTAMIENTO APARENTE
   * Para el caso de tiempo de ensamblado es similar
   * Tiempo de solucion se muestra levemente mas constante en las matrices dispersas, analisis que coincide con la complejidad algorítmica de los otros dos casos de SOLVE y MATMUL

* QUE TAN ESTABLES SON LAS CORRIDAS
   * Para el tiempo de ensamblado se observan corridas mas estables para ambos casos
   * En cuanto al tiempo de solucion las matrices llenas muestran menos estabilidad. y las matrices dispersas muestra una completa estabilidad a partir de la matriz N=1000
   

# Código de Ensamblaje de Matrices Laplacianas

* Código para matrices llenas:

```ruby
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import spsolve, inv
import numpy as np

 def laplaciana_llena(N,t=np.double):
    A=np.identity(N,t)*2
    for i in range(N):
        for j in range (N):
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return A 
```              
   


* Código para matrices dispersas:
```ruby
def laplaciana_dispersa(N,t=np.double):
    A=lil_matrix((N,N))
    for i in range(N):
        for j in range (N):
            if i==j:
                A[i,j]=2
            if i+1==j:
                A[i,j]=-1
            if i-1==j:
                A[i,j]=-1
    return csc_matrix(A) 
 ```
* En el primer código aprovecha una estructura por el uso de las librerias respectivas, de numpy y scipy. Su comodidad para trabajar presenta meyores beneficios que el código de matrices dispersas.
* En ambos casos se recorre una lista de tamaño N y luego de revisar se asigna el valor correspondiente.
* El segundo código si bien es mas extenso, no muestra grandes diferencias. El ```csr_matrix``` demostró menor tiempo pero no necesariamente fue mas optimo al momento de ensamblar la matriz.
