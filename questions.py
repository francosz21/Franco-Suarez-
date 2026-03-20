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
				
print("¡Bienvenido al Ahorcado!")
print ("Las opciones que tienes para elegir son: tecno_muy_general,datos,logica") #Corregí las categorías
word = random.choice(words)
categoria =input("Elige una categoría de palabra: ")#Lo agregue para que el usuario elija cat antes de empezar
word = random.choice(categorias[categoria]) #Aca puse para que elija una palabra de la categoria elegida
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
		puntaje=puntaje + 6 
		print("puntaje=",puntaje)
		break
	print(f"Intentos restantes: {attempts}")
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
	else:
		guessed.append(letter)
		attempts -= 1
		puntaje=puntaje-1
		print("Esa letra no está en la palabra.")
		print("puntaje=",puntaje)
	print()
else:
	print(f"¡Perdiste! La palabra era: {word}")
	puntaje=0 
	print ('tu puntaje fue de: ',puntaje)
