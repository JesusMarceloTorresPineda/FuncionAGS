from random import randint
import random
import math 
import matplotlib.pyplot as plt
import numpy as np

initial_population=[]
all_fitness=[]
mejorfit=[]
mejorfit_gen=[]
peorfit_gen=[]
promfit_gen=[]
prob_wheel_roulette=[]
aux_fitness=[]


def seleccion(initial_population):
   global aux_fitness
   funcion_generacion=[]
   retorno_gen=[]
   evaluate_this=[]
   aux_fitness=[]
   suma_fitness = 0
   prom_fitness= 0
   best_retorno=0
   best2_retorno=0
   retorno_gen=[]
   for x in initial_population:
      print(x)
      var = calcularFitness(x) #CALCULO DE FITNESS INDIVIDUAL
      aux_fitness.append(round(var,4)) #SE GUARDA EN LISTA AUXILIAR
      porsi=round(var,4)
      evaluate_this.append([x, porsi])
   #PROBABILIDAD DE SELECCION
   i=0
   suma_fitness=sum(aux_fitness)
   prom_fitness=suma_fitness/(len(initial_population))
   print("suma fitness " ,suma_fitness)
   print("promedio fitness " , prom_fitness)
   print("maximo fitness " , max(aux_fitness))
   for y in aux_fitness:
      prob_individual = y/suma_fitness
      prob_wheel_roulette.append(prob_individual)

   funcion_generacion.append([aux_fitness, suma_fitness])
   
   maximo_gen=max(aux_fitness)
   minimo_gen=min(aux_fitness)
   mejorfit_gen.append(maximo_gen)
   peorfit_gen.append(minimo_gen)
   promfit_gen.append(prom_fitness)
   #best_generation.extend([maximo_gen, minimo_gen, prom_fitness])
   aux_fitness.sort()
   tamanio_auxfit = len(aux_fitness)
   best_retorno=aux_fitness[tamanio_auxfit-1]
   best2_retorno=aux_fitness[tamanio_auxfit-2]

   for pero in evaluate_this:
      print(pero)
      if pero[1] == best_retorno:
         best_retorno=pero[0]
         retorno_gen.append(best_retorno)
      if pero[1] == best2_retorno:
         best2_retorno=pero[0]
         retorno_gen.append(best2_retorno)
   
   print(best_retorno, " --- ", best2_retorno)
   return retorno_gen

def crossover(datos):
   aux_pares=[]
   aux_impares=[]
   dats=[]
   for b in range(len(datos)):
      if b%2==0:
         corte=randint(1,len(datos[b])-2)
      aux_pares.append(datos[b][0:corte])
      aux_impares.append(datos[b][corte:len(datos[b])])
   for c in range(len(aux_pares)):
      aux=[]
      if c%2 == 0:#0|1
         x=c+1#1| 
      else:
         x=c-1#0
      aux.extend(aux_pares[c])
      aux.extend(aux_impares[x])
      dats.append(aux)#c0a1|c1a0
   for d in dats:
      print("ya los cruce",d)
   return dats

def mutation(datos):
   indice=0
   for a in datos:
      ans = bool(random.getrandbits(1))
      if ans:
         for y in range(len(a)):
            if bool(random.getrandbits(1)):
               if datos[indice][y] == 1:
                  datos[indice][y] = 0
               else:
                  datos[indice][y] = 1
      indice+=1
   for b in datos:
      print("mutaron ",b)
   return datos
      
      
def generate_pulation(maximo, tamaño_poblacion): # Poblacion inicial
   while len(initial_population) < tamaño_poblacion:
      individuo = random.randint(1,maximo)
      print(individuo)
      if len(initial_population) == 0:
         print("arreglo vacio, agrego primer individuo")
         initial_population.extend([individuo])
      else:
         if individuo in initial_population:
            print(individuo ," es numero repetido")
         else:
            print("agregue nuevo numero")
            initial_population.extend([individuo])
   

def contenidopoblacion():
   for n in initial_population:
      print(n)
# f(x)=sen(2x) + x cos(x)
def calcularFitness(num):
   fitness = float( (math.sin(2*num)) + (num*math.cos(num)) )
   all_fitness.append(fitness)
   return fitness

def bin_to_int(num_bin):
   letra=""
   rtrn=0
   for x in num_bin:
      letra+=str(x)
   rtrn=(int(letra,2))
   print(letra, " conviertido a decimal ",rtrn)
   return rtrn

def int_to_bin(value):
   binary="{0:06b}".format(value)
   return [int(x) for x in str(binary)]

def tranform_bin_int(param_j):
   d=[]
   for x in param_j:
      ls=[]
      a = bin_to_int(x[0:6])
      print("esto voy a regresar de binario a entero ",a)
      ls.append(a)
      d.extend(ls)
   return d

def generateGraphic(x,y,z):
   plt.plot(x, label = "Mejor Caso")   # Dibuja el gráfico
   plt.xlabel("abscisa")   # Inserta el título del eje X
   plt.ylabel("ordenada")   # Inserta el título del eje Y
   plt.ioff()   # Desactiva modo interactivo de dibujo
   plt.ion()   # Activa modo interactivo de dibujo
   plt.plot(y, label = "Peor Caso")   # Dibuja datos de lista2 sin borrar datos de lista1
   plt.ioff()   # Desactiva modo interactivo
   plt.ion()   # Activa modo interactivo de dibujo
   plt.plot(z, label = "Caso promedio")   # Dibuja datos de lista2 sin borrar datos de lista1
   plt.ioff()   # Desactiva modo interactivo
   # plt.plot(lista3)   # No dibuja datos de lista3
   plt.legend()
   plt.show()   # Fuerza dibujo de datos de lista3

if __name__ == "__main__":
   maximo = int (input("Valor maximo de x: "))
   tamaño_poblacion = int (input("Tamaño de la poblacion: "))
   generate_pulation(maximo, tamaño_poblacion)
   print("----", initial_population,"----")
   poblation = initial_population
   for i in range(100):
      print("generacion no.",i+1)
      poblation = seleccion(poblation)
      va1=[]
      for primer in poblation:
         va2=[]
         va2.extend(int_to_bin(primer))
         va1.append(va2)
      crossver_data=crossover(va1)
      mutation_data = mutation(crossver_data)
      re_translate = tranform_bin_int(mutation_data)
      print(re_translate)
      if re_translate[0]> maximo:
         re_translate[0]=50
      if re_translate[1]>maximo:
         re_translate[1]=50
      print("converti ", re_translate)
      poblation.extend(re_translate)
   generateGraphic(mejorfit_gen, peorfit_gen, promfit_gen)
   