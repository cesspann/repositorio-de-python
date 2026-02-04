entrada = input("Ingrese cualquier valor: ")

try:
  valor_entero = int(entrada)
  print(valor_entero)
except ValueError:
  # No se imprime nada si no es un entero, según la solicitud.
  pass
finally:
  print("Fin de la ejecución")