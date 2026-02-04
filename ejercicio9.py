entrada = input("Ingrese cualquier valor: ")

try:
  entero = int(entrada)
  print("El valor entero es: ",entero)
except ValueError:
  pass
finally:
  print("Fin de la ejecución")