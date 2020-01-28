"""
Esta libreria se requiere para las operaciones básicas de números complejos que ayudara a determinar la suma, resta, producto, división
a demás de esto también sera posible calcular el conjugado y el modulo de números complejos. Ests funciones realizará la conversión
de números polares a cartesianas y calcular la fase para poder ubicar de una manera mas facil los angulos o radianes 
en un plano cartesiano.
"""

# ## Reprecentacion de un numero complejo 
# El numero complejo $a+ib$ lo representaremos mediante la lista: \[a,b\]

# A continuación definiremos una funcion para la suma de 2 numeros complejos:

def suma(c_1,c_2):
    """
    La función recibe dos números complejos c_1 y c_2 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion c_1 + c_2.
    """
    return [c_1[0]+c_2[0],c_1[1]+c_2[1]]


# Probemos la función suma
c_1 = [3,2]
c_2 = [7,5]
suma(c_1 , c_2)

# Justificación de la prueba :
# (3+2i) + (7+5i) = (3+7) + (2+5)i = 10 + 7i

# A continuación definiremos una funcion para la resta de 2 numeros complejos:

def resta(c_1,c_2):
    """
    La función recibe dos números complejos c_1 y c_2 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion c_1 - c_2.
    """
    return [c_1[0]-c_2[0],c_1[1]-c_2[1]]

c_1 = [5,2]
c_2 = [7,1]
resta(c_1 , c_2)

# Justificación de la prueba :
# (5-2i) - (7-1i) = (5-7) - (2-1)i = -2 - 1i

# A continuación definiremos una funcion para la resta de 2 numeros complejos:

def producto(c_1,c_2):
    """
    La función recibe dos números complejos c_1 y c_2 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion c_1 x c_2.
    """
    return [c_1[0]*c_2[0]-c_1[1]*c_2[1]],[c_1[0]*c_2[1]+c_1[1]*c_2[0]]

c_1 = [3,2]
c_2 = [2,1]
producto(c_1 , c_2)

# Justificación de la prueba :
# (3+2i) *(2+1i) = (3*2) - (2*1) + (3*1 + 2*2)i= 4+7i

# A continuación definiremos una funcion para la modulo de 1 numeros complejos:

def conjugado(c_1):
    """
    La función recibe un número complejo c_1 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion conjugado c_1.
    """
    return (c_1[0],(c_1[1]*(-1)))

c_1 = [-3,7]
conjugado(c_1 )

# Justificación de la prueba :
# ((-3) + (7i)) = ((-3) + (7i)(-1)) = (-3 - 7i) 

# A continuación definiremos una funcion para la division de 2 numeros complejos:

def division(c_1,c_2):
    """
    La función recibe dos números complejos c_1 y c_2 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion c_1 / c_2.
    """
    conjugado = [c_2[0],(c_2[1]*(-1))]
    divisor=producto(c_1,conjugado)
    dividendo= producto(c_2,conjugado)
    if c_2[0] != 0 :
        return [int(divisor[0][0])/int(dividendo[0][0]),int(divisor[1][0])/int(dividendo[0][0])]
    else:
        print("error no se puede divisir por 0")
    
division([3,-2],[5,4])

# Justificación de la prueba :
# (3-2i) / (5+4i) = ((3-2i) / (5+4i))*((5-4i) / (5-4i)) = (7/40)-(22i/40)

# A continuación definiremos una funcion para la modulo de 1 numeros complejos:

def modulo(c_1):
    """
    La función recibe un número complejo c_1 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion ||c_1||.
    """
    return (((c_1[0])**(2))+((c_1[1])**(2)))**(1/2)

c_1 = [-3,7]
modulo(c_1 )

# Justificación de la prueba :
# ((-3)**(2) + (7)**(2))**(1/2) = 7.615 

# A continuación definiremos una funcion para pasar de numero de binomial a polar un numero complejo:

def Bin_polar(c_1):
    '''Esta funcion recibe un arreglo calcula su fase y la retorna'''
    mod=modulo(c_1)
    direc=math.atan(c_1[1]/c_1[0])
    return [mod[0],round(math.degrees(direc),2)]

def polar_Bin(c_1):
    '''Esta funcion recibe un arreglo de la forma [r,el angulo en°]
    y retorna el valor del numero complejo de forma Binomial'''
    a=c_1[0]*math.cos(math.radians(c_1[1]))
    b=c_1[0]*math.sin(math.radians(c_1[1]))
    imprime([round(a,2),round(b,2)])
def ele_n(c_1,n):
    '''Esta funcion recibe un arreglo de la forma[a+bi,"n" el numero del exponente]
    y retorna el valor de elevar un numero complejo a la n'''
    polar=Bin_polar(c_1)
    polar_Bin([round(polar[0]**n,2),round(polar[1]*n,2)])
def imprime(arreglo):
    print("El numero es:",arreglo[0],"+",str(arreglo[1])+"i")

# A continuación definiremos una funcion para retornar la fase de numeros complejos:

def fase(c_1):
    import math 
    """
    La función recibe un número complejo c_1 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion fase de c_1.
    """
    return math.atan((c_1[1]/c_1[0]))*(180/math.pi)

c_1 = [4, 6.92]
fase(c_1 )


# Justificación de la prueba :
# $$ arctan(6.92 / 4)= 59.9 $$ 
