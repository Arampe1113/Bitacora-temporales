import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta

def capturar_nombre_del_rol():
  nombre_del_rol = input("Por favor, introduce el nombre del rol: ")
  return nombre_del_rol

def capturar_fechadecreacion():
  fecha_de_creacion = input("Indique la fecha de creación del requerimiento (formato YYYY-MM-DD): ")
  try:
    fecha_de_creacion = datetime.strptime(fecha_de_creacion, "%Y-%m-%d")
  except ValueError:
    print("La fecha de creación no es válida. Por favor, introduce una fecha en formato YYYY-MM-DD.")
    fecha_de_creacion = capturar_fechadecreacion()
  return fecha_de_creacion

def capturar_numerodeposicion():
  numero_de_posicion = input("Indique el número del rol: ")
  return numero_de_posicion

def capturar_fechadeincio():
  fecha_iniciodelrol = input("Indique la fecha en la que debe iniciar esta persona: ")
  return fecha_iniciodelrol

def capturar_solicitante():
  solicitante = input("Indique el nombre de la persona que solicita el cargo: ")
  return solicitante

def capturar_pais():
  pais = input("Indique el país: ")
  return pais

def capturar_compania():
  compania = input("Indique la compañía: ")
  return compania

def capturar_sede():
  sede = input("Indique la sede: ")
  return sede

def capturar_vinculacion():
  vinculacion = input("Indique el tipo de vinculación: ")
  return vinculacion

def capturar_numeroposiciones():
    numeroposiciones = input ("Cuantas posiciones tenemos: ")

def agregar_un_dia_habil(fecha_de_creacion):
  """
  Agrega un día hábil a una fecha dada.

  Args:
    fecha_de_creacion: La fecha de creación del rol (formato YYYY-MM-DD).

  Returns:
    La nueva fecha con un día hábil agregado.
  """
  # Convertimos la cadena de fecha a un objeto datetime
#   fecha_de_creacion = datetime.strptime(fecha_de_creacion, "%Y-%m-%d")

  # Verificamos si el día de la semana es laborable (lunes a viernes)
  if fecha_de_creacion.weekday() < 5:
    return fecha_de_creacion + timedelta(days=1)
  else:
    # Si no es laborable, pasamos al siguiente lunes
    return fecha_de_creacion + timedelta(days=(7 - fecha_de_creacion.weekday()))

def calcular_dias_transcurridos(fecha_de_creacion, fecha_actual):
  """
  Calcula la cantidad de días transcurridos entre dos fechas usando Pandas.

  Args:
    fecha_de_creacion: La fecha de creación del rol (formato YYYY-MM-DD).
    fecha_actual: La fecha actual (formato YYYY-MM-DD).

  Returns:
    La cantidad de días transcurridos entre las dos fechas.
  """

  # Convertir las fechas a objetos datetime
  fecha_de_creacion = pd.to_datetime(fecha_de_creacion)
  fecha_actual = pd.to_datetime(fecha_actual)

  # Restar las dos fechas
  diferencia = fecha_actual - fecha_de_creacion

  # Obtener la cantidad de días
  dias_transcurridos = diferencia.days

  return dias_transcurridos



# Calculo de fecha intento 1

# def calcular_dias_habiles(fecha_de_creacion, fecha_actual):
#   """
#   Calcula la cantidad de días hábiles entre dos fechas.

#   Args:
#     fecha_de_creacion: La fecha de creación del rol (formato YYYY-MM-DD).
#     fecha_actual: La fecha actual (formato YYYY-MM-DD).

#   Returns:
#     La cantidad de días hábiles entre las dos fechas.
#   """
  
#   dias_habiles = 0
#   while fecha_de_creacion <= fecha_actual:
#     fecha_de_creacion = agregar_un_dia_habil(fecha_de_creacion)
#     dias_habiles += 1
#   return dias_habiles

# Ejemplo de uso
nombre_del_rol = capturar_nombre_del_rol()
fecha_de_creacion = capturar_fechadecreacion()
numero_de_posicion = capturar_numerodeposicion()
fecha_iniciodelrol = capturar_fechadeincio()
solicitante = capturar_solicitante()
pais = capturar_pais()
compania = capturar_compania()
sede = capturar_sede()
vinculacion = capturar_vinculacion()
numeroposiciones = capturar_numeroposiciones()

# if fecha_de_creacion.strftime("%Y-%m-%d") != fecha_de_creacion:
#   print("La fecha de creación no tiene el formato correcto.")

if type(fecha_de_creacion) == str:
    fecha_de_creacion = datetime.strptime(fecha_de_creacion, "%Y-%m-%d")
else:
    print("La fecha de creación ya es un objeto datetime. No es necesario convertirla.")

  
  
# fecha_de_creacion = datetime.strptime(fecha_de_creacion, "%Y-%m-%d")  # Convertimos a datetime
fecha_actual = datetime.today()  # Obtenemos la fecha actual como datetime



# Calculamos la cantidad de días hábiles
dias_habiles = calcular_dias_habiles(fecha_de_creacion, fecha_actual)

# Imprimimos la información capturada
print(f"Nombre del rol: {nombre_del_rol}")
print(f"Fecha de creación: {fecha_de_creacion}")
print(f"Número de posición: {numero_de_posicion}")
print(f"Fecha de inicio: {fecha_iniciodelrol}")
print(f"Solicitante: {solicitante}")
print(f"País: {pais}")
print(f"Compañía: {compania}")
print(f"Sede: {sede}")
print(f"Vinculación: {vinculacion}")
print(f"Fecha de creación: {fecha_de_creacion}")
print(f"Fecha actual: {fecha_actual}")
print(f"Días hábiles transcurridos: {dias_habiles}")
print(f"Fecha de creación: {fecha_de_creacion.strftime('%Y-%m-%d')}")  # Formateamos la fecha para imprimirla
print(f"Fecha actual: {fecha_actual.strftime('%Y-%m-%d')}")
print(f"Días hábiles transcurridos: {dias_habiles}")
