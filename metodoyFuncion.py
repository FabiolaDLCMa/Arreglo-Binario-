import random
def main():
  arregloBinario1, arregloBinario2, arregloBinario3 = [], [], []
  arregloBinario1 = funcionArregloBinario(0, 1)
  arregloBinario2 = funcionArregloBinario(0, 1)
  arregloBinario3 =   sumaDeArreglos(arregloBinario1, arregloBinario2)
  mostrarArregloBinario(arregloBinario1)
  mostrarArregloBinario(arregloBinario2)
  mostrarArregloBinario(arregloBinario3)


def funcionArregloBinario(inferior, superior):
	arreglo = []
	for i in range(100):
		arreglo.append(random.randint(inferior, superior))
	return arreglo
def sumaDeArreglos(arregloBinario1, arregloBinario2):
	arregloBinario = []
	for i in range(100):
		suma = arregloBinario1[i] + arregloBinario2[i]
		arregloBinario.append(suma) 
	return arregloBinario
def mostrarArregloBinario(arreglo):
	contador = 0
	for i in arreglo:
		contador = contador + 1
		print("casilla " + str(contador) + " : " + str (i))

main()