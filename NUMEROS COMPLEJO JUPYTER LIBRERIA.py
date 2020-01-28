#!/usr/bin/env python
# coding: utf-8
"""
Esta libreria se requiere para las operaciones básicas de números complejos que ayudara a determinar la suma, resta, producto, división
a demás de esto también sera posible calcular el conjugado y el modulo de números complejos. Ests funciones realizará la conversión
de números polares a cartesianas y calcular la fase para poder ubicar de una manera mas facil los angulos o radianes 
en un plano cartesiano.
"""

# ## Reprecentacion de un numero complejo 
# El numero complejo $a+ib$ lpo representaremos mediante la lista: \[a,b\]
# 

# A continuación definiremos una funcion para la suma de 2 numeros complejos:

# In[3]:


def suma(c_1,c_2):
    """
    La función recibe dos números complejos c_1 y c_2 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion c_1 + c_2.
    """
    return [c_1[0]+c_2[0],c_1[1]+c_2[1]]


# Probemos la función ```suma```

# In[7]:


c_1 = [3,2]
c_2 = [7,5]
suma(c_1 , c_2)


# In[ ]:





# 

# Justificación de la prueba :
# $$ (3+2i) + (7+5i) = (3+7) + (2+5)i = 10 + 7i$$ 

# A continuación definiremos una funcion para la resta de 2 numeros complejos:

# In[8]:


def resta(c_1,c_2):
    """
    La función recibe dos números complejos c_1 y c_2 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion c_1 - c_2.
    """
    return [c_1[0]-c_2[0],c_1[1]-c_2[1]]


# In[9]:


c_1 = [5,2]
c_2 = [7,1]
resta(c_1 , c_2)


# Justificación de la prueba :
# $$ (5-2i) - (7-1i) = (5-7) - (2-1)i = -2 - 1i$$ 

# A continuación definiremos una funcion para la resta de 2 numeros complejos:

# In[98]:


def producto(c_1,c_2):
    """
    La función recibe dos números complejos c_1 y c_2 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion c_1 x c_2.
    """
    return [int(c_1[0])*int(c_2[0]) - int(c_1[1])*int(c_2[1]),int(c_1[0])*int(c_2[1])+int(c_1[1])*int(c_2[0])]


# In[99]:


c_1 = [3,2]
c_2 = [2,1]
print(producto(c_1 , c_2))


# Justificación de la prueba :
# $$ (3+2i) *(2+1i) = (3*2) - (2*1) + (3*1 + 2*2)i= 4+7i$$ 

# A continuación definiremos una funcion para la division de 2 numeros complejos:

# In[49]:


'''def division(c_1,c_2):
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
    


# In[50]:


division([3,-2],[5,4])'''


# Justificación de la prueba :
# $$ (3-2i) / (5+4i) = ((3-2i) / (5+4i))*((5-4i) / (5-4i)) = (7/40)-(22i/40)$$ 

# A continuación definiremos una funcion para la modulo de 1 numeros complejos:

# In[59]:


def modulo(c_1):
    """
    La función recibe un número complejo c_1 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion ||c_1||.
    """
    return (((c_1[0])**(2))+((c_1[1])**(2)))**(1/2)


# In[61]:


c_1 = [-3,7]
modulo(c_1 )


# Justificación de la prueba :
# $$ ((-3)**(2) + (7)**(2))**(1/2) = 7.615 $$ 

# A continuación definiremos una funcion para la modulo de 1 numeros complejos:

# In[70]:


def conjugado(c_1):
    """
    La función recibe un número complejo c_1 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion conjugado c_1.
    """
    return (c_1[0],(c_1[1]*(-1)))


# In[71]:


c_1 = [-3,7]
conjugado(c_1 )


# Justificación de la prueba :
# $$ ((-3) + (7i)) = ((-3) + (7i)(-1)) = (-3 - 7i) $$ 

# A continuación definiremos una funcion para pasar de numero polar a cartesiano un numero complejo:

# In[104]:


def depolarcartesiano(c_1):
    import math
    """
    La función recibe un número complejo c_1, de lo que se compone c_1 es de un radio y un angulo en ese orden correspondidnte 
    (que deben ser lista de longuitud 2) y retornar un complejo (lista de longitud 2) 
    correspondinte a la operacion de polar a cartesiano de números complejos  c_1.
    """
    grados = (c_1[1]*math.pi)/180
    
    return (c_1[0] * math.cos(grados) , (c_1[0] * math.sin(grados)))


# In[105]:


c_1 = [5 , 45]
depolarcartesiano(c_1 )


# Justificación de la prueba :
# $$ (5) * cos(45) + (i)(5) * sen(45) = 3,53 + 3,53i $$ 

# A continuación definiremos una funcion para retornar la fase de numeros complejos:

# In[114]:


def fase(c_1):
    import math 
    """
    La función recibe un número complejo c_1 (que deben ser lista de longuitud 2) y retornar un complejo 
    (lista de longitud 2) correspondinte a la operacion fase de c_1.
    """
    return math.atan((c_1[1]/c_1[0]))*(180/math.pi)


# In[115]:


c_1 = [4, 6.92]
fase(c_1 )


# Justificación de la prueba :
# $$ arctan(6.92 / 4)= 59.9 $$ 

# In[ ]:




