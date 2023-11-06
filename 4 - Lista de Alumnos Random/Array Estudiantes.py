import random
alumnos = ["Anubis","Dust","Inferno","Mirage","Nuke","Overpass","Vertigo","Aztec","Ancient","Italy","Office"]
print("[A continuacion se muestra una lista de nombres en default]")
print(alumnos)
print("#######################################################################")

print("[A continuación se muestra la lista con un nuevo orden randomizado]")
random.shuffle(alumnos)
print(alumnos)
print("#######################################################################")

print("[Ahora se mostrara la lista ordenada alfabeticamente]")
alumnos.sort()
print(alumnos)
print("#######################################################################")