import random
words = [
		"python",
		"programa",
		"variable",
		"funcion",
		"bucle",
		"cadena",
		"entero",
		"lista",
]
categorias = {"tecno_muy_general":["programa","python"],
				"datos" :["lista","entero","cadena","variable"], # dividí las palabras dadas en categorías porque en teoría dijieron eso
				"logica":["funcion","bucle"]
				}
				
ronda =1

print("¡Bienvenido al Ahorcado!")
print("ESTAS POR COMENZAR LA RONDA:1 (hay un máximo de 4, depende de la categoria que elijas) ")

print ("Las opciones que tienes para elegir son: tecno_muy_general,datos,logica") #Corregí las categorías
word = random.choice(words)
categoria =input("Elige una categoría de palabra: ")#Lo agregue para que el usuario elija cat antes de empezar
intentos=list(categorias[categoria]) #Convierto la categoria elegida en lista para despues ir eliminando palabras y que no se repitan
while ronda<5 and len(intentos)>0:
	palabra=random.sample(intentos,1) [0] #Ultimo punto, hago uso del random.sample. Como devuelve una lista el sample le pomgo los corchetes para que solo agarre la palabra
	#Y Le puse intentos dentro de palabra para que elimine de la lista "intentos" y no del diccionario original
	word = palabra #Aca puse para que elija una palabra de la categoria elegida

	guessed = []
	puntaje=0
	attempts = 6

	print()
	while attempts > 0:
# Mostrar progreso: letras adivinadas y guiones para las que faltan
		progress = ""
		for letter in word:
			if letter in guessed:
				progress += letter + " "
			else:
				progress += "_ "
			
		print(progress)
# Verificar si el jugador ya adivinó la palabra completa
		if "_" not in progress:
			print("¡Ganaste!")
			print("La Ronda: ",ronda)
			puntaje=puntaje + 6 
			print("puntaje=",puntaje)
			intentos.remove(word) #elimino la palabra para que no repita
			ronda=ronda+1 # para que arranque otra vez el juego
			break
		print(f"Intentos restantes: {attempts}")
		print("Ronda: ",ronda)
		print(f"Letras usadas: {', '.join(guessed)}")
		letter = input("Ingresá una letra: ")
		if letter in guessed:
			print("Ya usaste esa letra.")
		elif letter in word:
			guessed.append(letter)
			print("¡Bien! Esa letra está en la palabra.")
			print("puntaje=",puntaje)
		elif len(letter)>1 or not letter.isalpha(): #condicion por si se ingresa algo que no sea 1 sola letra
			print ("Entrada no válida")
			print (" No puedes poner numeros o caracteres que no sean letras (solo 1 letra a la vez)")
			print("puntaje=",puntaje)
			print("Ronda: ",ronda)
			
		else:
			guessed.append(letter)
			attempts -= 1
			puntaje=puntaje-1
			print("Esa letra no está en la palabra.")
			print("puntaje=",puntaje)
			print("Ronda: ",ronda)
		print()
	else:
		print(f"¡Perdiste! La palabra era: {word}")
		puntaje=0 
		print("Ronda: ",ronda)
		print ('tu puntaje fue de: ',puntaje)
		ronda=ronda+1 #Lo mismo que cuando ganas para que arranque otra ronda
		intentos.remove(word) #elimino la palabra para que no repita
